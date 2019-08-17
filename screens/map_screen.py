import pygame
from state import State


class MapScreen:

    @staticmethod
    def process_input(current_event: pygame.event, current_state: State) -> State:
        movements = {pygame.K_LEFT: (-1, 0), pygame.K_RIGHT: (1, 0), pygame.K_UP: (0, -1), pygame.K_DOWN: (0, 1)}

        if current_event.key in movements:
            # Get the tile that is attempted to be walked on
            potential_pos = tuple(sum(x) for x in zip(current_state.player_location, movements[current_event.key]))
            potential_tile = current_state.get_tile(*potential_pos)
            # Check to see if the move is valid
            if potential_tile.can_travel:
                current_state.player_location = potential_pos
                print(current_state.player_location)
        return current_state
