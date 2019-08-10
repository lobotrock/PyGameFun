import pygame

from drawing_utils import DrawingUtilities
from map_generator import generate_map
from state import State
from screens.map_screen import MapScreen
from screens.open_screen import OpenScreen
import time

# Creating state
state = State(
    map=generate_map(1000, 1000),
    player_location=(50, 50))

# Starting Pygame
pygame.init()

# Creating Drawing utils that store dimensions of display
draw_utils = DrawingUtilities(
    grid_size=20,
    display_height=1000,
    display_width=1400,
    py_game=pygame)

# Start Pygame clock
clock = pygame.time.Clock()

# Draw Intro
t_end = time.time() + 4
while time.time() < t_end:
    OpenScreen.draw(draw_utils, state, pygame)
    clock.tick(60)




# Running Map Screen
while not False:
    key_is_down = False

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and not key_is_down:
            key_is_down = True
            state = MapScreen.process_input(event, state)
        elif event.type == pygame.KEYUP:
            key_is_down = False

    MapScreen.draw(draw_utils, state, pygame)
    clock.tick(60)

