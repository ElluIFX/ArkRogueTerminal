import datetime
import os
import time
from queue import Empty as QueueEmptyError
from queue import Queue
from typing import List

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
            try:
                return self.__find_source_cache[scene_name][0][item_name]
            except KeyError:
                return self.find_source(scene_name, item_name, cache=False)
        else:
            return self.get_sources(scene_name)[item_name]

    def set_source_enabled(self, scene_name: str, item_name: str, enabled: bool):
        self.set_scene_item_enabled(
            scene_name, self.find_source(scene_name, item_name)["sceneItemId"], enabled
        )

    def display_score(
        self,
        details: List[str],
        total: float,
    ):
        self.set_input_settings(
            "text_score_details", {"text": "\n".join(details)}, True
        )
        self.set_input_settings(
            "text_score_sum", {"text": f"总分：{total:>6.2f}"}, True
        )

    def align_text(
        self, source_name: str, text: str, mid_x: int, y: int, enable: bool = True
    ):
        self.set_source_enabled("main", source_name, False)
        self.set_input_settings(source_name, {"text": text}, True)
        time.sleep(0.15)
        width = self.find_source("main", source_name, cache=False)[
            "sceneItemTransform"
        ]["width"]
        x = mid_x - width / 2
        self.set_scene_item_transform(
            "main",
            self.find_source("main", source_name)["sceneItemId"],
            {"positionX": x, "positionY": y},
        )
        if enable:
            self.set_source_enabled("main", source_name, True)

    def set_player(self, name: str, avatar_path: str):
        self.set_input_settings("icon_player", {"file": avatar_path}, True)
        self.align_text("text_player", name, 121, 280)
        return

    def set_metadata(
        self,
        team_path: str,
        operator_path: str,
        cup: str,
        team: str,
        select: str,
        speaker: str,
    ):
        if team_path:
            self.set_input_settings("icon_team", {"file": team_path}, True)
            self.align_text(
                "text_team", os.path.basename(team_path).split(".")[0], 141, 672, False
            )
            self.set_source_enabled("main", "icon_team", True)
            self.set_source_enabled("main", "text_team", True)
        else:
            self.set_source_enabled("main", "icon_team", False)
            self.set_source_enabled("main", "text_team", False)
        if operator_path:
            self.set_input_settings("icon_operator", {"file": operator_path}, True)
            self.set_source_enabled("main", "icon_operator", True)
        else:
            self.set_source_enabled("main", "icon_operator", False)
        today = datetime.datetime.now()
        offset = (today - datetime.datetime(2025, 2, 3)).days
        self.set_input_settings("text_day", {"text": f"{offset}"}, True)
        self.align_text("text_cup", cup, 157, 324)
        self.align_text("text_player_team", team, 122, 441)
        self.align_text("text_select", select, 122, 558)
        speaker = speaker.replace("，", ",")
        speakers = [x.strip() for x in speaker.split(",")]
        self.align_text("text_speaker", "  ".join(speakers), 1429, 983)


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
    """
    异步代理 (将操作发送到子线程队列执行)
    """

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
        self.paused = False
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
    def a(self) -> ReqClientEx:
        """
        提供类型提示
        """
        return self

    def set_pause(self, pause: bool):
        self.paused = pause

    def run_action(self, action: str, *args, **kwargs):
        if not self.paused:
            self.worker.action(action, args, kwargs)

    def __getattr__(self, item):
        if item in dir(self.client):
            logger.debug(f"OBS Try request: {item}")
            return lambda *args, **kwargs: self.run_action(item, *args, **kwargs)
        else:
            return super().__getattr__(item)
