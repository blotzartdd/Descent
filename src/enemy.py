import pygame
from support import load_image, get_enemy_assets_dict
from settings import *


class Skeleton(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = load_image(ENEMY_MELEE_SKELETON['idle'], crop_coords=(0, 0, 24, 32))
        self.rect = self.image.get_rect(topleft=pos)

        # animation
        self.frame_index = 0
        self.animation_speed = 0.2
        self.animation_dict = get_enemy_assets_dict(ENEMY_MELEE_SKELETON,
                                                    MELEE_SKELETON_ANIMATIONS_CUT)

        # enemy_status
        self.status = 'idle'
        self.facing = 'right'
        self.on_ground = False
        self.on_ceiling = False
        self.on_left = False
        self.on_right = False
        self.hp = 300
        self.attack_power = 10

        # enemy movement
        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 2
        self.gravity = 0.8

    def get_status(self, player_x, player_y, player_status, player_attack_power):
        if self.direction.x == -1 or self.direction.x == 1:
            self.status = 'walk'
        else:
            self.status = 'idle'

        if abs(player_x - self.rect.centerx) <= 40 and abs(player_y - self.rect.y) <= 80:
            self.status = 'attack'
        if player_status == 'attack' and abs(player_x - self.rect.centerx) <= 40 and abs(player_y - self.rect.y) <= 80:
            self.status = 'hit'
            self.hp -= player_attack_power
        if self.hp < 0:
            self.status = 'dead'

    def get_enemy_status(self):
        return self.status

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def move_enemy(self, player_x):
        if player_x > self.rect.centerx:
            self.direction.x = 1
            self.facing = 'right'
            self.speed = 4
        elif player_x < self.rect.x:
            self.direction.x = -1
            self.facing = 'left'
            self.speed = -4
        else:
            self.speed = 0
            self.direction.x = 0

    def animate(self):
        animation_list = self.animation_dict[self.status]
        if self.status == 'attack':
            self.frame_index += self.animation_speed * 0.65
        elif self.status == 'hit':
            self.frame_index += self.animation_speed * 2
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

    def update(self, x_shift, player_x, player_y, player_status, attack_power):
        if self.status == 'dead':
            self.animate_dead()
            self.rect.x += x_shift
        else:
            self.move_enemy(player_x)
            self.rect.x += x_shift + self.speed
            self.get_status(player_x, player_y, player_status, attack_power)
            self.animate()


class RedSkeleton(Skeleton):
    def __init__(self, pos):
        super().__init__(pos)
        self.image = load_image(ENEMY_RED_SKELETON['idle'], crop_coords=(0, 0, 20, 32))
        self.rect = self.image.get_rect(topleft=pos)
        self.animation_dict = get_enemy_assets_dict(ENEMY_RED_SKELETON,
                                                    RED_SKELETON_ANIMATIONS_CUT)
        self.animation_speed = 0.15

    def move_enemy(self, player_x):
        self.speed = 0
        self.direction.x = 0
        if player_x > self.rect.centerx:
            self.facing = 'right'
        elif player_x < self.rect.x:
            self.facing = 'left'


class Boss(Skeleton):
    def __init__(self, pos):
        super().__init__(pos)
        self.image = load_image(BOSS['idle'], crop_coords=(0, 0, 20, 32))
        self.rect = self.image.get_rect(topleft=pos)
        self.animation_dict = get_enemy_assets_dict(BOSS,
                                                    BOSS_ANIMATIONS_CUT)
        self.animation_speed = 0.15
        self.hp = 2000

    def get_status(self, player_x, player_y, player_status, player_attack_power):
        if self.direction.x == -1 or self.direction.x == 1:
            self.status = 'walk'
        else:
            self.status = 'idle'

        if abs(player_x - self.rect.centerx) <= 100 and abs(player_y - self.rect.y) <= 200:
            self.status = 'attack'
        if player_status == 'attack' and abs(player_x - self.rect.centerx) <= 100 and abs(player_y - self.rect.y) <= 200:
            self.status = 'hit'
            self.hp -= player_attack_power
        if self.hp < 0:
            self.status = 'dead'