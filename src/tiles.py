import pygame
from settings import ALL_TILES


class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos):
        super().__init__()
        self.image = ALL_TILES[tile_type]
        self.rect = self.image.get_rect(topleft=pos)