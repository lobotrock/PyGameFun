from tiles import Tile


class State:

    def __init__(self, map: list, player_location: tuple):
        self.map: list = map
        self.view: list = map
        self.player_location: tuple = player_location

    def get_tile(self, x: int, y: int) -> Tile:
        return self.map[x][y]
