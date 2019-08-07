import pygame
import numpy as np
from state import State
from tiles import empty

class DrawingUtilities:

    def __init__(self, grid_size: int, display_width: int, display_height: int, py_game: pygame):
        self.grid_size = grid_size
        self.display_width = display_width
        self.display_height = display_height
        self.screen = py_game.display.set_mode((display_width, display_height))

    def draw_grid(self, py_game, current_state: State):

        center = current_state.player_location

        max_tiles_width = int(self.display_width / self.grid_size)
        max_tiles_height = int(self.display_height / self.grid_size)

        top_ = center[0]-int(max_tiles_width/2)
        bottom_ = center[0]+int(max_tiles_width/2)
        top = center[1]-int(max_tiles_height/2)
        bottom = center[1]+int(max_tiles_height/2)

        np_map = np.array(current_state.map)


        horizontal_view = top_ if top_ > 0 else 0, bottom_ if bottom_ < len(current_state.map) else len(current_state.map)
        vertical_view = top if top > 0 else 0, bottom if bottom < len(current_state.map[0]) else len(current_state.map[0])


        current_view = np_map[horizontal_view[0]:horizontal_view[1], vertical_view[0]:vertical_view[1]]
        if top_ < 0:
            np.pad(np_map, [(2, 0), (0, 0)], mode='constant', constant_values=empty)


        left_adjust = -1 * (center[0] - int(max_tiles_width / 2))
        right_adjust = -1 * (len(current_state.map) - center[0] + int(max_tiles_width/2))
        top_adjust = -1 * (center[1]-int(max_tiles_height/2))
        bottom_adjust = -1 * (len(current_state.map[0]) - center[1]+int(max_tiles_height/2))

        # if top_adjust > 0:
        #     current_view = np.pad(current_view, [(0,0), (top_adjust,0) ], mode='constant', constant_values=empty)
        for x, row in enumerate(current_state.map[horizontal_view[0]:horizontal_view[1]], 0):
            for y, tile in enumerate(row[vertical_view[0]:vertical_view[1]], 0):
                py_game.draw.rect(self.screen, tile.color,
                                  py_game.Rect(y * self.grid_size, x * self.grid_size, self.grid_size,
                                               self.grid_size))


        # for x, row in enumerate(current_view, 0):
        #     for y, tile in enumerate(row, 0):
        #         py_game.draw.rect(self.screen, tile.color,
        #                           py_game.Rect(y * self.grid_size, x * self.grid_size, self.grid_size,
        #                                        self.grid_size))

        grid_color = (135, 20, 255)
        for x in range(0, self.display_width, self.grid_size):
            py_game.draw.rect(self.screen, grid_color, py_game.Rect(x, 0, 1, self.display_height))

        for y in range(0, self.display_height, self.grid_size):
            py_game.draw.rect(self.screen, grid_color, py_game.Rect(0, y, self.display_width, 1))

    def draw_hud(self, py_game, message):
        py_game.draw.rect(self.screen, py_game.Color(255, 255, 255),
                          py_game.Rect(0, int(self.display_height * 0.8), self.display_width,
                                       int(self.display_height * 0.2)))
        font = py_game.font.Font('freesansbold.ttf', 35)
        text_surface = font.render(message, True, (0, 0, 0))
        text_rect = text_surface.get_rect()
        text_rect.center = ((self.display_width / 2), int(self.display_height * 0.9))
        self.screen.blit(text_surface, text_rect)
        py_game.display.update()

    def game_draw_player(self, py_game, state, color):
        center_width = int(int(self.display_width / self.grid_size)/2)
        center_height = int(int(self.display_height / self.grid_size)/2)

        py_game.draw.rect(self.screen, color,
                          py_game.Rect(center_width * self.grid_size,
                                       center_height * self.grid_size,
                                       self.grid_size,
                                       self.grid_size))
