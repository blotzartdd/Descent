import pygame
from support import load_image, get_character_assets_dict
from settings import *


class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = load_image(CHARACTER['idle'], crop_coords=(0, 0, 15, 18))
        self.rect = self.image.get_rect(topleft=pos)

        # animation
        self.frame_index = 0
        self.animation_speed = 0.5
        self.animation_dict = get_character_assets_dict()

        # player_status
        self.status = 'idle'
        self.facing = 'right'
        self.on_ground = False
        self.on_ceiling = False
        self.on_left = False
        self.on_right = False
        self.hp = 1000
        self.attack_power = 10

        # player movement
        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 6
        self.gravity = 0.8
        self.jump_speed = -4

    def move_player(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            self.direction.x = 1
            if keys[pygame.K_LSHIFT]:
                self.direction.x = 2
            self.facing = 'right'
        elif keys[pygame.K_a]:
            self.direction.x = -1
            if keys[pygame.K_LSHIFT]:
                self.direction.x = -2
            self.facing = 'left'
        else:
            self.direction.x = 0

        if keys[pygame.K_SPACE]:
            self.fly()

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def get_status(self):
        keys = pygame.key.get_pressed()
        if self.direction.y < 0:
            self.status = 'jump'
        elif self.direction.y > 1:
            self.status = 'fall'
        else:
            if self.direction.x == -1 or self.direction.x == 1:
                self.status = 'run'
            elif self.direction.x == 2 or self.direction.x == -2:
                self.status = 'dash'
            else:
                self.status = 'idle'

        if keys[pygame.K_z]:
            self.status = 'attack'

    def get_player_x(self):
        return self.rect.centerx

    def get_player_status(self):
        return self.status

    def fly(self):
        self.direction.y = self.jump_speed

    def animate(self):
        animation_list = self.animation_dict[self.status]
        if self.status == 'attack':
            self.frame_index += self.animation_speed * 0.85
        else:
            self.frame_index += self.animation_speed
        if self.frame_index >= len(animation_list):
            self.frame_index = 0

        image = animation_list[int(self.frame_index)]
        if self.facing == 'right':
            self.image = image
        else:
            flipped_image = pygame.transform.flip(image, True, False)
            self.image = flipped_image

        if self.on_ground and self.on_right:
            self.rect = self.image.get_rect(bottomright=self.rect.bottomright)
        elif self.on_ground and self.on_left:
            self.rect = self.image.get_rect(bottomleft=self.rect.bottomleft)
        elif self.on_ground:
            self.rect = self.image.get_rect(midbottom=self.rect.midbottom)
        elif self.on_ceiling and self.on_right:
            self.rect = self.image.get_rect(topright=self.rect.topright)
        elif self.on_ceiling and self.on_left:
            self.rect = self.image.get_rect(topleft=self.rect.topleft)
        elif self.on_ceiling:
            self.rect = self.image.get_rect(midtop=self.rect.midtop)

    def animate_dead(self):
        animation_list = self.animation_dict['dead']
        if self.frame_index < len(animation_list):
            image = animation_list[int(self.frame_index)]
            self.frame_index += self.animation_speed
            if self.facing == 'right':
                self.image = image
            else:
                flipped_image = pygame.transform.flip(image, True, False)
                self.image = flipped_image

    def update(self):
        if self.status == 'dead':
            self.animate_dead()
        else:
            self.move_player()
            self.get_status()
            self.animate()
