from typing import List, Dict
from numpy import array
from gol.config import GolConfig


class MapReader:

    __slots__ = 'base_directory', 'dead_cell', 'alive_cell'

    def __init__(self, config: GolConfig) -> None:
        self.base_directory = config.map_directory
        self.dead_cell = config.reader_dead_cell
        self.alive_cell = config.reader_alive_cell

    def read(self, map_file: str) -> array:
        with open(f'{self.base_directory}{map_file}') as file:
            content: List[str] = file.read().strip().split('\n')
            _value_map: Dict[str, int] = {self.dead_cell: 0, self.alive_cell: 1}
            mapped_array = [list(map(lambda char: _value_map[char], list(line))) for line in content]
            return array(mapped_array)
