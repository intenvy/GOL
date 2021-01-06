from .config import GolConfig
from numpy import ndarray

class MapReader(object):

    __slots__ = 'base_directory',

    def __int__(self, directory: str, Gol):
        self.base_directory = directory

    def read