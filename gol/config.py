from abc import ABC
from configparser import ConfigParser
from json import dumps
from typing import Dict


class Config(ABC):
    __slots__ = 'parser', 'directory'

    def __init__(self, directory: str) -> None:
        self.directory: str = directory
        self.parser: ConfigParser = ConfigParser()
        self.parser.read(directory)

    def save(self) -> None:
        with open(self.directory, 'w', encoding='utf8') as configfile:
            self.parser.write(configfile)

    def _get_dict(self) -> Dict[str, Dict[str, str]]:
        out: Dict[str, Dict[str, str]] = {}
        for section in self.parser.sections():
            out[section] = {}
            for key in self.parser[section]:
                out[section][key] = self.parser[section][key]
        return out

    def __str__(self) -> str:
        return dumps(self._get_dict())

    def __repr__(self) -> str:
        return dumps(self._get_dict(), indent=4)


class GolConfig(Config):

    def __init__(self, directory: str) -> None:
        super().__init__(directory)

    @property
    def display_dead_cell(self) -> str:
        return self.parser['DISPLAY']['dead_cell'][1:-1]

    @property
    def display_alive_cell(self) -> str:
        return self.parser['DISPLAY']['alive_cell'][1:-1]

    @property
    def reader_dead_cell(self) -> str:
        return self.parser['DISPLAY']['dead_cell'][1:-1]

    @property
    def reader_alive_cell(self) -> str:
        return self.parser['DISPLAY']['alive_cell'][1:-1]

    @property
    def frame_sleep(self) -> float:
        return float(self.parser['PERFORMANCE']['frame_sleep'])

    @property
    def skip_frames(self) -> int:
        return int(self.parser['PERFORMANCE']['skip_frames'])

    @property
    def map_directory(self) -> str:
        return self.parser['RESOURCES']['maps']
