import pygame
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

        x_bounds = int(center[0] - (int(self.display_width / self.grid_size) / 2)), \
                   int(center[0] + (int(self.display_width / self.grid_size) / 2))

        y_bounds = int(center[1] - (int(self.display_height / self.grid_size) / 2)), \
                   int(center[1] + (int(self.display_height / self.grid_size) / 2))

        # Draw tiles
        for view_x, x in enumerate(range(x_bounds[0], x_bounds[1])):
            for view_y, y in enumerate(range(y_bounds[0], y_bounds[1])):
                tile = current_state.map[x][y] if 0 <= x < len(current_state.map) and 0 <= y < len(current_state.map[0]) else empty
                py_game.draw.rect(self.screen,  tile.color,
                                  py_game.Rect(view_x * self.grid_size, view_y * self.grid_size, self.grid_size, self.grid_size))

        # Draw grid
        grid_color = (135, 20, 255)
        for x_ in range(0, self.display_width, self.grid_size):
            py_game.draw.rect(self.screen, grid_color, py_game.Rect(x_, 0, 1, self.display_height))

        for y_ in range(0, self.display_height, self.grid_size):
            py_game.draw.rect(self.screen, grid_color, py_game.Rect(0, y_, self.display_width, 1))

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
