import asyncio
import pygame
from client.state import State
from client.renderer import render
import time
import pickle

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
        valid_inputs={'g': 'generate_map'},
        py_game=pygame
    )

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
            if event.unicode in state.valid_inputs:
                message = {'action': state.valid_inputs[event.unicode]}
                new_state = await ping_host(message)
                print(new_state)
                state.world_map = new_state.world_map
                state.player_location = new_state.player_location
                state.valid_inputs = new_state.valid_inputs

            # TODO: Better way of handling input depending on screen in view
            # state = MapScreen.process_input(event, state)
        else:
            print("event", event)
    asyncio.get_event_loop().stop()


async def ping_host(message):
    payload = bytes(pickle.dumps(message))
    reader, writer = await asyncio.open_connection('127.0.0.1', 8888)

    print(f'Send: {message!r}')
    writer.write(payload)

    data = await reader.read()
    print("has read data back...")
    payload = pickle.loads(data)
    print(f'Received: {payload!r}')

    print('Close the connection')
    await asyncio.sleep(1)
    writer.close()

    return payload

if __name__ == '__main__':
    main()
