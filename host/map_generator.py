import random

from client.tiles import grass, water, sand, empty


# TODO: make this more interesting and faster
async def generate_map(width: int, height: int):
    return [[rand_tile(x_, y_, width, height) for y_ in range(0, height)] for x_ in range(0, width)]


def rand_tile(x, y, max_x, max_y):
    if x == 0 or y == 0 or x == max_x - 1 or y == max_y - 1:
        return empty
    rng = random.randint(0, 100)
    if rng > 95:
        return water
    elif rng > 75:
        return sand
    else:
        return grass
