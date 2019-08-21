import pygame

from client.tiles import Tile


class State:

    def __init__(self,
                 world_map,
                 player_location: tuple,
                 grid_size: int,
                 display_width: int,
                 display_height: int,
                 valid_inputs: dict,
                 py_game: pygame):
        self.world_map: list = world_map
        self.view: list = world_map
        self.player_location: tuple = player_location
        self.grid_size = grid_size
        self.display_width = display_width
        self.display_height = display_height
        self.py_game = py_game
        self.valid_inputs = valid_inputs
        self.screen = self.py_game.display.set_mode((display_width, display_height))

    def get_tile(self, x: int, y: int) -> Tile:
        return self.world_map[x][y]
