import os
import time
from queue import Empty as QueueEmptyError
from queue import Queue
from typing import List, Literal

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

    def set_player(self, name: str, avatar_path: str):
        MID_X = 145  # 文字的对齐中心X
        X_MIN = 35  # 文字的左换行边界
        Y1 = 440  # 第一行文字的Y
        Y2 = 433  # 第二行文字的Y
        Y3 = 463  # 第三行文字的Y
        Y2_ONLY = 446  # 只有第二行文字的Y

        self.set_input_settings("icon_player", {"file": avatar_path}, True)
        self.set_source_enabled("main", "text_player1", False)
        self.set_source_enabled("main", "text_player2", False)
        self.set_source_enabled("main", "text_player3", False)
        self.set_input_settings("text_player1", {"text": name}, True)
        time.sleep(0.15)
        width = self.find_source("main", "text_player1", cache=False)[
            "sceneItemTransform"
        ]["width"]
        x = MID_X - width / 2
        if x >= X_MIN:
            self.set_scene_item_transform(
                "main",
                self.find_source("main", "text_player1")["sceneItemId"],
                {"positionX": x, "positionY": Y1},
            )
            self.set_source_enabled("main", "text_player1", True)
            return
        self.set_input_settings("text_player2", {"text": name}, True)
        time.sleep(0.15)
        width = self.find_source("main", "text_player2", cache=False)[
            "sceneItemTransform"
        ]["width"]
        x = MID_X - width / 2
        if x >= X_MIN:
            self.set_scene_item_transform(
                "main",
                self.find_source("main", "text_player2")["sceneItemId"],
                {"positionX": x, "positionY": Y2_ONLY},
            )
            self.set_source_enabled("main", "text_player2", True)
            return
        text1 = name[: len(name) // 2 + 1]
        text2 = name[len(name) // 2 + 1 :]
        self.set_input_settings("text_player2", {"text": text1}, True)
        self.set_input_settings("text_player3", {"text": text2}, True)
        time.sleep(0.15)
        width1 = self.find_source("main", "text_player2", cache=False)[
            "sceneItemTransform"
        ]["width"]
        width2 = self.find_source("main", "text_player3", cache=False)[
            "sceneItemTransform"
        ]["width"]
        self.set_scene_item_transform(
            "main",
            self.find_source("main", "text_player2")["sceneItemId"],
            {"positionX": MID_X - width1 / 2, "positionY": Y2},
        )
        self.set_scene_item_transform(
            "main",
            self.find_source("main", "text_player3")["sceneItemId"],
            {"positionX": MID_X - width2 / 2, "positionY": Y3},
        )
        self.set_source_enabled("main", "text_player2", True)
        self.set_source_enabled("main", "text_player3", True)

    def set_start(
        self,
        team_path: str,
        operator_path1: str,
        operator_path2: str,
        operator_path3: str,
    ):
        if team_path:
            self.set_input_settings("icon_team", {"file": team_path}, True)
            self.set_source_enabled("main", "icon_team", True)
        else:
            self.set_source_enabled("main", "icon_team", False)
        for i, path in enumerate([operator_path1, operator_path2, operator_path3]):
            if path:
                self.set_input_settings(f"icon_operator{i + 1}", {"file": path}, True)
                self.set_source_enabled("main", f"icon_operator{i + 1}", True)
            else:
                self.set_source_enabled("main", f"icon_operator{i + 1}", False)


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
    def fake(self) -> ReqClientEx:
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
