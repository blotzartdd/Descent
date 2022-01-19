import pygame
from settings import *
from support import load_image


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, tile_type):
        super().__init__()
        cur_image = load_image(FOREST_TILES_CROPS[tile_type])
        if tile_type != '/':
            self.image = pygame.transform.scale(cur_image,
                                                (cur_image.get_width() * 2, cur_image.get_height() * 2))
        else:
            self.image = pygame.transform.scale(cur_image,
                                                (cur_image.get_width() * 4, cur_image.get_height() * 2))
        self.rect = self.image.get_rect(topleft=pos)

    def update(self, x_shift):
        self.rect.x += x_shift