from state import State
from tiles import empty


def draw_grid(state: State):
    center = state.player_location

    x_bounds = int(center[0] - (int(state.display_width / state.grid_size) / 2)), \
               int(center[0] + (int(state.display_width / state.grid_size) / 2))

    y_bounds = int(center[1] - (int(state.display_height / state.grid_size) / 2)), \
               int(center[1] + (int(state.display_height / state.grid_size) / 2))

    # Draw tiles
    for view_x, x in enumerate(range(x_bounds[0], x_bounds[1])):
        for view_y, y in enumerate(range(y_bounds[0], y_bounds[1])):
            tile = state.world_map[x][y] if 0 <= x < len(state.world_map) and 0 <= y < len(
                state.world_map[0]) else empty
            state.py_game.draw.rect(state.screen, tile.color,
                                    state.py_game.Rect(view_x * state.grid_size, view_y * state.grid_size,
                                                       state.grid_size,
                                                       state.grid_size))

    # Draw grid
    grid_color = (135, 20, 255)
    for x_ in range(0, state.display_width, state.grid_size):
        state.py_game.draw.rect(state.screen, grid_color, state.py_game.Rect(x_, 0, 1, state.display_height))

    for y_ in range(0, state.display_height, state.grid_size):
        state.py_game.draw.rect(state.screen, grid_color, state.py_game.Rect(0, y_, state.display_width, 1))


def draw_hud(state: State, message: str):
    state.py_game.draw.rect(state.screen, state.py_game.Color(255, 255, 255),
                            state.py_game.Rect(0, int(state.display_height * 0.8), state.display_width,
                                               int(state.display_height * 0.2)))
    font = state.py_game.font.Font('freesansbold.ttf', 35)
    text_surface = font.render(message, True, (0, 0, 0))
    text_rect = text_surface.get_rect()
    text_rect.center = ((state.display_width / 2), int(state.display_height * 0.9))
    state.screen.blit(text_surface, text_rect)
    state.py_game.display.update()


def game_draw_player(state, color):
    center_width = int(int(state.display_width / state.grid_size) / 2)
    center_height = int(int(state.display_height / state.grid_size) / 2)

    state.py_game.draw.rect(state.screen, color,
                            state.py_game.Rect(center_width * state.grid_size,
                                               center_height * state.grid_size,
                                               state.grid_size,
                                               state.grid_size))


def render(state: State):
    # Startup screen
    if state.world_map is None:
        draw_hud(state, "Map generating...")

    # draw map
    else:
        draw_grid(state)
        draw_hud(state, f"Now walking on {state.get_tile(*state.player_location).type}")
        game_draw_player(state, (0, 128, 255))
    state.py_game.display.flip()
    state.py_game.time.Clock().tick(60)
