from client.tiles import Tile


class State:

    def __init__(self,
                 world_map,
                 player_location: tuple,
                 valid_inputs: dict):
        self.world_map: list = world_map
        self.view: list = world_map
        self.player_location: tuple = player_location
        self.valid_inputs = valid_inputs

    def get_tile(self, x: int, y: int) -> Tile:
        return self.world_map[x][y]
