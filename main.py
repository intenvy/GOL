from src.gol import GameOfLife
from src.io import MapReader
from src.utils import GolConfig

if __name__ == '__main__':
    config = GolConfig('settings.cfg')
    reader = MapReader(config)
    board = reader.read('test.map')
    gol = GameOfLife(board, config)
    gol.run(100)
