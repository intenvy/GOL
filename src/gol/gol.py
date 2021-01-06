import os
from abc import ABC, abstractmethod
from time import sleep as time_sleep
from typing import List

import numpy as np

from src.utils.config import GolConfig


class FrameSimulation(ABC):

    @abstractmethod
    def _next_frame(self) -> None:
        pass

    def step(self, size: int) -> None:
        for i in range(size):
            self._next_frame()

    @abstractmethod
    def run(self, frames: int) -> None:
        pass

    @abstractmethod
    def display(self) -> None:
        pass


class GameOfLife(FrameSimulation):
    __slots__ = [
        'world', 'rows', 'cols', 'char_map', 'cast',
        'frame_sleep', 'skip_frames',
    ]

    def __init__(self, world: np.ndarray, config: GolConfig):
        self.world = world
        self.rows = world.shape[0]
        self.cols = world.shape[1]
        self.char_map: List[str] = [config.display_dead_cell, config.display_alive_cell]
        self.cast = np.vectorize(lambda cell: self.char_map[cell])
        self.frame_sleep = config.frame_sleep
        self.skip_frames = config.skip_frames

    def _compute_neighbours(self) -> np.ndarray:
        N = np.zeros(np.shape(self.world))
        N = np.roll(self.world, 1, axis=1) + \
            np.roll(self.world, -1, axis=1) + \
            np.roll(self.world, 1, axis=0) + \
            np.roll(self.world, -1, axis=0)
        return N

    def _next_frame(self) -> None:
        N = self._compute_neighbours()
        zeros = (self.world == 1) & ((N < 2) | (N > 3))
        ones = (self.world != 1) & (N == 3)
        self.world[zeros] = 0
        self.world[ones] = 1

    def display(self) -> None:
        _ = os.system('cls') if os.name.startswith('nt') else os.system('clear')
        out = '\n'.join(''.join(self.cast(row)) for row in self.world)
        print(out)

    def run(self, frames: int) -> None:
        for frame in range(frames):
            print('s')
            self.display()
            self.step(self.skip_frames + 1)
            time_sleep(self.frame_sleep)
