import pygame
from drawing_utils import DrawingUtilities
from state import State


class MapScreen:

    @staticmethod
    def process_input(current_event: pygame.event, current_state: State) -> State:
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

    @staticmethod
    def draw(draw_utils: DrawingUtilities, current_state: State, _pygame: pygame):
        draw_utils.draw_grid(_pygame, current_state)
        draw_utils.draw_hud(_pygame, f"Now walking on {current_state.get_tile(*current_state.player_location).type}")
        draw_utils.game_draw_player(_pygame, current_state, (0, 128, 255))

        _pygame.display.flip()
