import pygame
from tiles import Tile
from settings import *
from player import Player
from enemy import Skeleton, RedSkeleton, Boss
from portal import Portal
from time import time


class ForestLevel:
    def __init__(self, level_data, surface):
        self.display_surface = surface
        self.world_shift = 6
        self.current_player_x = 0
        self.enemy_counter = 0
        self.killed_enemy_set = set()
        self.bg_x = 0
        self.big_tiles_list = ['*', '.', '_', 'c', '%']
        self.shift_x_tiles_list = ['6', '7', '8']
        self.setup_level(level_data)

    def get_enemy_list(self):
        self.enemy1 = pygame.sprite.GroupSingle()
        self.enemy2 = pygame.sprite.GroupSingle()
        self.enemy3 = pygame.sprite.GroupSingle()
        self.enemy4 = pygame.sprite.GroupSingle()
        return [self.enemy1, self.enemy2, self.enemy3, self.enemy4]

    def setup_level(self, layout):
        self.tiles = pygame.sprite.Group()

        self.player = pygame.sprite.GroupSingle()

        self.boss = pygame.sprite.GroupSingle()

        self.enemy_list = self.get_enemy_list()
        self.enemy_object_list = []

        self.portal = pygame.sprite.GroupSingle()
        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size
                if cell in self.big_tiles_list:
                    x = col_index * 64
                    y = row_index * 64
                    if cell == '%':
                        tile = Tile((x - 30, y + 150), cell)
                        self.tiles.add(tile)
                    else:
                        tile = Tile((x, y), cell)
                        self.tiles.add(tile)
                    if cell == '_':
                        tile = Tile((x - 300, y), cell)
                        self.tiles.add(tile)
                elif cell in self.shift_x_tiles_list:
                    tile = Tile((x - 750, y), cell)
                    self.tiles.add(tile)
                elif cell == '9':
                    tile = Tile((x - 630, y + 250), cell)
                    self.tiles.add(tile)
                elif cell == 'p':
                    self.player_sprite = Player((x, y))
                    self.player.add(self.player_sprite)
                elif cell == '4':
                    tile = Tile((x, y - 25), cell)
                    self.tiles.add(tile)
                elif cell == '@':
                    tile = Tile((x - 256, y - 256), cell)
                    self.tiles.add(tile)
                elif cell == '+':
                    tile = Tile((x - 768, y), cell)
                    self.tiles.add(tile)
                elif cell == '#':
                    tile = Tile((x - 1000, y - 80), cell)
                    self.tiles.add(tile)
                elif cell == 'e':
                    if self.enemy_counter % 2 == 0:
                        enemy = Skeleton((x, y))
                    else:
                        enemy = RedSkeleton((x, y))
                    self.enemy_list[self.enemy_counter].add(enemy)
                    if self.enemy_counter < 3:
                        self.enemy_object_list.append(enemy)
                        self.enemy_counter += 1
                elif cell == 'b':
                    boss = Boss((x, y))
                    self.boss_object = boss
                    self.boss.add(boss)
                elif cell == '0':
                    portal_sprite = Portal((x, y - 60))
                    self.portal.add(portal_sprite)
                elif cell != '-':
                    tile = Tile((x, y), cell)
                    self.tiles.add(tile)

    def scroll_x(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x

        if player_x < screen_width / 4 and direction_x < 0:
            self.world_shift = 8
            player.speed = 0
        elif player_x > screen_width * 3 / 4 and direction_x > 0:
            self.world_shift = -8
            player.speed = 0
        else:
            self.world_shift = 0
            player.speed = 8

    def player_horizontal_move_collision(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                    player.on_left = True
                    self.current_player_x = player.rect.left
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left
                    player.on_right = True
                    self.current_player_x = player.rect.right

        if player.on_left and (player.rect.left < self.current_player_x or player.direction.x >= 0):
            player.on_left = False
        if player.on_right and (player.rect.right > self.current_player_x or player.direction.x <= 0):
            player.on_right = False

    def player_vertical_move_collision(self):
        player = self.player.sprite
        player.apply_gravity()

        for sprite in self.tiles.sprites():
            self.check_vertical_collide(sprite, player)

        if player.on_ground and player.direction.y < 0 or player.direction.y > 1:
            player.on_ground = False
        if player.on_ceiling and player.direction.y > 0:
            player.on_ceiling = False

    def check_horizontal_collide(self, sprite, object):
        if object:
            if sprite.rect.colliderect(object.rect):
                if object.direction.x < 0:
                    object.rect.left = sprite.rect.right
                    object.on_left = True
                    object.rect.x = object.rect.left
                elif object.direction.x > 0:
                    object.rect.right = sprite.rect.left
                    object.on_right = True
                    object.rect.x = object.rect.right

    def check_vertical_collide(self, sprite, object):
        if object:
            if sprite.rect.colliderect(object.rect):
                if object.direction.y < 0:
                    object.rect.top = sprite.rect.bottom
                    object.direction.y = 0
                    object.on_ceiling = True
                elif object.direction.y > 0:
                    object.rect.bottom = sprite.rect.top
                    object.direction.y = 0
                    object.on_ground = True

    def enemy_vertical_move_collision(self):
        enemy1 = self.enemy_list[0].sprite
        if enemy1:
            enemy1.apply_gravity()

        enemy2 = self.enemy_list[1].sprite
        if enemy2:
            enemy2.apply_gravity()

        enemy3 = self.enemy_list[2].sprite
        if enemy3:
            enemy3.apply_gravity()

        enemy4 = self.enemy_list[3].sprite
        if enemy4:
            enemy4.apply_gravity()

        boss = self.boss.sprite
        if boss:
            boss.apply_gravity()

        for sprite in self.tiles.sprites():
            self.check_vertical_collide(sprite, enemy1)
            self.check_vertical_collide(sprite, enemy2)
            self.check_vertical_collide(sprite, enemy3)
            self.check_vertical_collide(sprite, enemy4)
            self.check_vertical_collide(sprite, boss)

    def enemy_horizontal_move_collision(self):
        enemy1 = self.enemy_list[0].sprite
        enemy2 = self.enemy_list[1].sprite
        enemy3 = self.enemy_list[2].sprite
        enemy4 = self.enemy_list[3].sprite
        for sprite in self.tiles.sprites():
            self.check_horizontal_collide(sprite, enemy1)
            self.check_horizontal_collide(sprite, enemy2)
            self.check_horizontal_collide(sprite, enemy3)
            self.check_horizontal_collide(sprite, enemy4)

    def get_bg_coords(self):
        player = self.player.sprite
        direction_x = player.direction.x
        if direction_x > 0:
            self.bg_x -= self.world_shift
        elif direction_x < 0:
            self.bg_x -= self.world_shift
        return self.bg_x

    def final_score(self, start_time):
        return (len(self.killed_enemy_set) * 1000 + 5000) // (time() - start_time)

    def run(self):
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)
        self.scroll_x()

        for enemy in self.enemy_list:
            enemy.update(self.world_shift, self.player.sprite.rect.centerx,
                         self.player.sprite.rect.y,
                         self.player_sprite.get_player_status(),
                         self.player_sprite.attack_power)
            enemy.draw(self.display_surface)

        for enemy in self.enemy_object_list:
            if enemy.status == 'dead':
                self.killed_enemy_set.add(enemy)

        self.portal.update(self.world_shift)
        self.portal.draw(self.display_surface)

        self.boss.update(self.world_shift, self.player.sprite.rect.centerx,
                         self.player.sprite.rect.y,
                         self.player_sprite.get_player_status(),
                         self.player_sprite.attack_power)
        self.boss.draw(self.display_surface)

        self.player.update()
        self.player_horizontal_move_collision()
        self.player_vertical_move_collision()
        self.enemy_vertical_move_collision()
        self.player.draw(self.display_surface)


class NightLevel(ForestLevel):
    def __init__(self, level_data, surface):
        super().__init__(level_data, surface)
        self.setup_level(level_data)
        self.boss_dead = False

    def run(self):
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)
        self.scroll_x()

        for enemy in self.enemy_list:
            enemy.update(self.world_shift, self.player.sprite.rect.centerx,
                         self.player.sprite.rect.y,
                         self.player_sprite.get_player_status(),
                         self.player_sprite.attack_power)
            enemy.draw(self.display_surface)

        self.portal.update(self.world_shift)
        self.portal.draw(self.display_surface)

        self.boss.update(self.world_shift, self.player.sprite.rect.centerx,
                         self.player.sprite.rect.y,
                         self.player_sprite.get_player_status(),
                         self.player_sprite.attack_power)
        self.boss.draw(self.display_surface)

        self.player.update()
        self.player_horizontal_move_collision()
        self.player_vertical_move_collision()
        self.enemy_vertical_move_collision()
        self.player.draw(self.display_surface)

        if self.boss_object.status == 'dead':
            self.boss_dead = True
