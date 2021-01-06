from abc import ABC, abstractmethod


class FrameSimulation(ABC):

    @abstractmethod
    def _next_frame(self) -> None:
        pass

    @abstractmethod
    def step(self, size: int) -> None:
        for i in range(size):
            self._next_frame()

    @abstractmethod
    def display(self) -> None:
        pass


class GameOfLife(FrameSimulation):

    __slots__ = 'world', 'dead_cell_character', 'alive_cell_character', 'frame_sleep', 'skip_frames'

    def _next_frame(self) -> None:
        pass

    def step(self, size: int) -> None:
        pass

    def display(self) -> None:
        pass

