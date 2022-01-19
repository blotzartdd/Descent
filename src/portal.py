import pygame
from support import load_image, get_portal_assets
from settings import *


class Portal(pygame.sprite.DirtySprite):
    def __init__(self, pos):
        super().__init__()
        portal_image = load_image(FOREST_TILES_CROPS['0'])
        self.image = pygame.transform.scale(portal_image,
                                            (portal_image.get_width() * 1.5,
                                             portal_image.get_height() * 1.5))
        self.rect = self.image.get_rect(topleft=pos)
        self.visible = 1

        # animation
        self.frame_index = 0
        self.animation_speed = 0.1
        self.animation_list = get_portal_assets()

    def animate(self):
        self.frame_index += self.animation_speed
        if self.frame_index >= len(self.animation_list):
            self.frame_index = 0

        image = self.animation_list[int(self.frame_index)]
        self.image = image

    def update(self, x_shift):
        #  self.animate()
        self.rect.x += x_shift