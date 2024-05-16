import time
from typing import Literal

import obsws_python as obs


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
