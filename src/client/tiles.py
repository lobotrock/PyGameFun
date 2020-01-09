import pygame


class Tile:
    def __init__(self, type, color: pygame.Color, can_travel: bool):
        self.type = type
        self.color = color
        self.can_travel = can_travel

    def __str__(self):
        return self.type


grass = Tile("grass", pygame.Color('chartreuse3'), True)
sand = Tile("sand", pygame.Color('darkgoldenrod1'), True)
water = Tile("water", pygame.Color('cyan4'), False)
empty = Tile("empty", pygame.Color('black'), False)
