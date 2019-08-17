import asyncio

import pygame

from map_generator import generate_map
from screens.map_screen import MapScreen
from state import State
from renderer import render
import time

FPS = 100


def main():
    loop = asyncio.get_event_loop()
    event_queue = asyncio.Queue()

    pygame.init()

    state = State(
        world_map=None,
        player_location=(50, 50),
        grid_size=20,
        display_height=1000,
        display_width=1400,
        py_game=pygame)

    pygame_task = loop.run_in_executor(None, pygame_event_loop, loop, event_queue, state)
    animation_task = asyncio.ensure_future(render_state(state))
    event_task = asyncio.ensure_future(handle_events(event_queue, state))

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass
    finally:
        pygame_task.cancel()
        animation_task.cancel()
        event_task.cancel()

    pygame.quit()


def pygame_event_loop(loop, event_queue, state):
    while True:
        if state.world_map is None:
            print("generating map ...")
            state.world_map = generate_map(1000, 1000)
        event = pygame.event.wait()
        asyncio.run_coroutine_threadsafe(event_queue.put(event), loop=loop)


async def render_state(state):
    current_time = 0
    while True:
        last_time, current_time = current_time, time.time()
        await asyncio.sleep(1 / FPS - (current_time - last_time))  # tick
        render(state)


async def handle_events(event_queue, state):
    while True:
        event = await event_queue.get()
        if event.type == pygame.QUIT:
            break
        elif event.type == pygame.KEYDOWN:
            # TODO: Better way of handling input depending on screen in view
            state = MapScreen.process_input(event, state)
        else:
            print("event", event)
    asyncio.get_event_loop().stop()


if __name__ == '__main__':
    main()
