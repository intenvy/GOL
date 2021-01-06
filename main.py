from gol import GolConfig

if __name__ == '__main__':
    c = GolConfig('settings.cfg')
    print(c.reader_alive_cell)
