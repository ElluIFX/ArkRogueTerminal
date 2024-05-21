import os
import time
from queue import Empty as QueueEmptyError
from queue import Queue
from typing import Literal

import obsws_python as obs
from loguru import logger
from PySide6.QtCore import QObject, QThread


class ReqClientEx(obs.ReqClient):
    __find_source_cache = None

    @property
    def current_scene(self) -> str:
        return self.get_current_program_scene().current_program_scene_name

    def get_sources(self, scene_name: str) -> dict:
        items = self.get_scene_item_list(scene_name).scene_items
        return {item["sourceName"]: item for item in items}

    def find_source(
        self,
        scene_name: str,
        item_name: str,
        cache: bool = True,
        cache_time: float = 5,
    ) -> dict:
        if cache:
            if self.__find_source_cache is None:
                self.__find_source_cache = {}
            if scene_name not in self.__find_source_cache:
                self.__find_source_cache[scene_name] = ({}, -1)
            if time.time() - self.__find_source_cache[scene_name][1] > cache_time:
                self.__find_source_cache[scene_name] = (
                    self.get_sources(scene_name),
                    time.time(),
                )
            return self.__find_source_cache[scene_name][0][item_name]
        else:
            return self.get_sources(scene_name)[item_name]

    def set_source_enabled(self, scene_name: str, item_name: str, enabled: bool):
        self.set_scene_item_enabled(
            scene_name, self.find_source(scene_name, item_name)["sceneItemId"], enabled
        )

    # https://obs.infor-r.com/lower?id=3&line1=OBS&color1=ffffff&line2=Studio&color2=cf4c4e
    def display_web_lower_thirds(
        self,
        scene_name: str,
        web_item_name: str,
        line1: str,
        line2: str,
        color1: str = "ffffff",
        color2: str = "ffffff",
        style: Literal[1, 2, 3, 4, 5] = 1,
    ):
        addr = f"https://obs.infor-r.com/lower?id={style}&line1={line1}&color1={color1}&line2={line2}&color2={color2}"
        self.set_scene_item_enabled(
            scene_name,
            self.find_source(scene_name, web_item_name)["sceneItemId"],
            False,
        )
        # time.sleep(0.1)
        self.set_input_settings(web_item_name, {"url": addr}, True)
        # time.sleep(0.2)
        self.set_scene_item_enabled(
            scene_name,
            self.find_source(scene_name, web_item_name)["sceneItemId"],
            True,
        )

    def display_lower(
        self,
        line1: str,
        line2: str,
        num: int,
        duration: float = 3,
        animation: float = 1,
    ):
        GROUP_NAME = "lower_group"
        LINE1_NAME = "lower_text_a"
        LINE2_NAME = "lower_text_b"
        TWO_DIGIT_NAME = "lower_text_c"
        THREE_DIGIT_NAME = "lower_text_d"
        BK_NAME = "lower_bk"
        PLUS_BK = "resource/toast.png"
        PLUS_COLOR = 0xFFFFF5C9
        MINUS_BK = "resource/toast2.png"
        MINUS_COLOR = 0xFF5C59FF

        if abs(num) < 100:
            name = TWO_DIGIT_NAME
            name_o = THREE_DIGIT_NAME
        else:
            name = THREE_DIGIT_NAME
            name_o = TWO_DIGIT_NAME
        if num >= 0:
            path = os.path.join(os.path.dirname(__file__), PLUS_BK)
            color = PLUS_COLOR
        else:
            path = os.path.join(os.path.dirname(__file__), MINUS_BK)
            color = MINUS_COLOR
        self.set_input_settings(LINE1_NAME, {"text": line1, "color": color}, True)
        self.set_input_settings(LINE2_NAME, {"text": line2, "color": color}, True)
        if num == 0:
            self.set_input_settings(name, {"text": " +", "color": color}, True)
        else:
            self.set_input_settings(
                name, {"text": f"{abs(num):d}", "color": color}, True
            )
        self.set_input_settings(name_o, {"text": " "}, True)
        path = os.path.abspath(path)
        self.set_input_settings(BK_NAME, {"file": path}, True)
        self.set_source_enabled("main", GROUP_NAME, True)
        time.sleep(animation)
        time.sleep(duration)
        self.set_source_enabled("main", GROUP_NAME, False)
        time.sleep(animation)

    def set_score(self, score: int):
        self.set_input_settings("text_score", {"text": str(round(score))}, True)


class Worker(QObject):
    # Pyside 6 multi-threading wrapper of ReqClientEx
    def __init__(self, client: ReqClientEx):
        super().__init__()
        self.client = client
        self.action_queue = Queue()
        self.running = True

    def action(self, action: str, args: tuple, kwargs: dict):
        self.action_queue.put((action, args, kwargs))
        logger.debug(f"OBS Client received action: {action}")

    def stop(self):
        self.running = False
        while not self.action_queue.empty():
            self.action_queue.get()
        self.client.disconnect()
        logger.info("OBS Client worker requested to stop")

    def clear(self):
        while not self.action_queue.empty():
            self.action_queue.get()
        logger.info("OBS Client queue cleared")

    def run(self):
        logger.success("OBS Client worker started")
        while self.running:
            try:
                action, args, kwargs = self.action_queue.get(timeout=1)
                logger.debug(f"OBS Client worker running: {action}")
                getattr(self.client, action)(*args, **kwargs)
            except (TimeoutError, QueueEmptyError):
                pass
            except Exception:
                logger.exception("Error in worker")
        logger.info("OBS Client worker exited")


class ReqClientExQThread(QThread):
    def __init__(self, host: str, port: int, password: str, timeout: float):
        self.inited = False
        super().__init__()
        self.client = ReqClientEx(
            host=host, port=port, password=password, timeout=timeout
        )
        self.worker = Worker(self.client)
        self.worker_thread = QThread()
        self.worker.moveToThread(self.worker_thread)
        self.worker_thread.started.connect(self.worker.run)
        self.worker_thread.start()
        self.inited = True
        logger.success("OBS Client prepared")

    def __del__(self):
        if self.inited:
            self.stop()

    def stop(self):
        self.worker.stop()
        self.worker_thread.quit()
        self.worker_thread.wait()

    def clear(self):
        self.worker.clear()

    @property
    def fake(self) -> ReqClientEx:
        return self

    def run_action(self, action: str, *args, **kwargs):
        self.worker.action(action, args, kwargs)

    def __getattr__(self, item):
        if item in dir(self.client):
            logger.debug(f"OBS Try request: {item}")
            return lambda *args, **kwargs: self.run_action(item, *args, **kwargs)
        else:
            return super().__getattr__(item)
