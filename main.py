import pygame

from drawing_utils import DrawingUtilities
from map_generator import generate_map
from state import State


def move(current_event: pygame.event, current_state: State):
    if current_event.key == pygame.K_ESCAPE:
        # Quit
        exit(0)

    movements = {pygame.K_LEFT: (-1, 0), pygame.K_RIGHT: (1, 0), pygame.K_UP: (0, -1), pygame.K_DOWN: (0, 1)}

    if current_event.key in movements:
        potential_pos = tuple(sum(x) for x in zip(current_state.player_location, movements[current_event.key]))
        potential_tile = current_state.get_tile(*potential_pos)
        if potential_tile.can_travel:
            current_state.player_location = potential_pos
            print(current_state.player_location)
    return current_state


state = State(
    map=generate_map(1000, 1000),
    player_location=(50, 50))
print("finished generating map")

pygame.init()
draw_utils = DrawingUtilities(grid_size=20, display_height=1000, display_width=1400, py_game=pygame)

key_is_down = False

clock = pygame.time.Clock()

while not False:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and not key_is_down:
            key_is_down = True
            state = move(event, state)
        elif event.type == pygame.KEYUP:
            key_is_down = False

    draw_utils.draw_grid(pygame, state)
    draw_utils.draw_hud(pygame, f"Now walking on {state.get_tile(*state.player_location).type}")
    draw_utils.game_draw_player(pygame, state, (0, 128, 255))

    pygame.display.flip()
    clock.tick(60)
