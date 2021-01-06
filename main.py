from gol.config import GolConfig
from gol.map_reader import MapReader
from gol.gol import GameOfLife

config = GolConfig('settings.cfg')
reader = MapReader(config)
board = reader.read('test.map')
gol = GameOfLife(board, config)
gol.run(50)