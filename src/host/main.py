import asyncio
import pickle
from pickle import UnpicklingError

from host.host_state import State
from host.map_generator import generate_map


class GameHost:

    def __init__(self):
        self.game_state = State(world_map=None,
                                player_location=(2, 2),
                                valid_inputs={'g': 'generate_map'})
        asyncio.run(self.main())

    async def handle_request(self, reader, writer):
        data = await reader.read(1024)

        try:
            message = pickle.loads(data)

            addr = writer.get_extra_info('peername')
            print(f"Received {message!r} from {addr!r}")

            if 'action' in message:
                action = message['action']

                if action == 'generate_map':
                    self.game_state = State(world_map=await generate_map(20, 20),
                                            player_location=(10, 10),
                                            valid_inputs={'a': 'a', 'w': 'w', 'd': 'd', 's': 's'})
                else:
                    self.game_state = self.process_input(action)

                print(f"Writing {self.game_state}")
                writer.write(pickle.dumps(self.game_state))

                await writer.drain()

        except UnpicklingError:
            print("Invalid message format!")
            writer.write(pickle.dumps('Invalid message format!'))
        finally:
            print("Close the connection")
            writer.close()

    async def main(self):
        server = await asyncio.start_server(self.handle_request, '127.0.0.1', 8888)

        addr = server.sockets[0].getsockname()
        print(f'Serving on {addr}')

        async with server:
            await server.serve_forever()

    def process_input(self, key: str) -> State:
        movements = {'a': (-1, 0), 'd': (1, 0), 'w': (0, -1), 's': (0, 1)}

        if key in movements:
            # Get the tile that is attempted to be walked on
            potential_pos = tuple(sum(x) for x in zip(self.game_state.player_location, movements[key]))
            potential_tile = self.game_state.get_tile(*potential_pos)
            # Check to see if the move is valid
            if potential_tile.can_travel:
                self.game_state.player_location = potential_pos
                print(self.game_state.player_location)
        return self.game_state


if __name__ == '__main__':
    GameHost()
