import pygame
from drawing_utils import DrawingUtilities
from state import State

class OpenScreen:

    @staticmethod
    def process_input(current_event: pygame.event, current_state: State) -> State:
        return current_state

    @staticmethod
    def draw(draw_utils: DrawingUtilities, current_state: State, _pygame: pygame):
        draw_utils.draw_hud(_pygame, "Hello World!")
        _pygame.display.flip()