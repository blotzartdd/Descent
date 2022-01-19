from support import load_image, terminate, draw_text, open_level
import pygame
from settings import *
from level import ForestLevel, NightLevel
from music import Music
from time import time

pygame.init()
pygame.display.set_caption('Descent')
mainClock = pygame.time.Clock()
start_time = time()
screen = window = pygame.display.set_mode(size, pygame.FULLSCREEN)
canvas = pygame.Surface(size)
menu_font = pygame.font.Font('../data/fonts/war_priest_condensed.ttf', 15)
final_menu_font = pygame.font.Font('../data/fonts/war_priest_condensed.ttf', 30)
final_score_font = pygame.font.Font('../data/fonts/war_priest_condensed.ttf', 45)
title_font = pygame.font.Font('../data/fonts/war_priest.ttf', 60)
forest_level_map = open_level('../data/map/forest_level.txt')
night_level_map = open_level('../data/map/night_level.txt')
forest_level = ForestLevel(forest_level_map, screen)
night_level = NightLevel(night_level_map, screen)
music = Music('start_menu')


def main_menu():
    click = False
    music.start_play_music()
    background = pygame.transform.scale(load_image(MENU['menu_background']), (screen_width, screen_height))
    while True:
        screen.blit(background, (0, 0))
        draw_text('Descent', title_font, (255, 255, 255), screen, 30, 20)

        mouse_pos = pygame.mouse.get_pos()

        start_game_btn = pygame.Rect(50, 100, 200, 50)
        options_btn = pygame.Rect(50, 200, 200, 50)
        exit_btn = pygame.Rect(50, 300, 200, 50)

        if start_game_btn.collidepoint(mouse_pos):
            start_game_btn = pygame.Rect(40, 90, 220, 70)
            if click:
                start_forest_level()
        if options_btn.collidepoint(mouse_pos):
            options_btn = pygame.Rect(40, 190, 220, 70)
            if click:
                options()
        if exit_btn.collidepoint(mouse_pos):
            exit_btn = pygame.Rect(40, 290, 220, 70)
            if click:
                terminate()

        pygame.draw.rect(screen, (255, 0, 0), start_game_btn, border_radius=10)
        pygame.draw.rect(screen, (255, 0, 0), options_btn, border_radius=10)
        pygame.draw.rect(screen, (255, 0, 0), exit_btn, border_radius=10)

        draw_text('Start game', menu_font, (255, 255, 255), screen, 105, 115)
        draw_text('Options', menu_font, (255, 255, 255), screen, 115, 215)
        draw_text('Exit', menu_font, (255, 255, 255), screen, 130, 315)

        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        pygame.display.flip()
        mainClock.tick(60)


def options():
    running = True
    while running:
        screen.fill((0, 0, 0))
        draw_text('В разработке', menu_font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
        pygame.display.flip()
        mainClock.tick(60)


def start_forest_level():
    is_change_level = False
    music.change_music('forest_level1')
    running = True
    decro_far = pygame.transform.scale(load_image(FOREST['decro_far']), (screen_width, screen_height))
    sky = pygame.transform.scale(load_image(FOREST['sky']), (screen_width, screen_height))
    static = pygame.transform.scale(load_image(FOREST['static']), (2500, 800))
    while running:
        canvas.blit(sky, (0, 0))
        canvas.blit(decro_far, (0, 0))
        canvas.blit(static, (-forest_level.get_bg_coords(), 0))
        window.blit(canvas, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.K_ESCAPE:
                terminate()
        if is_change_level:
            start_night_level()
        else:
            forest_level.run()
            if forest_level.player.sprite.rect.colliderect(forest_level.portal.sprite.rect):
                is_change_level = True
        pygame.display.flip()
        mainClock.tick(60)


def start_night_level():
    music.change_music('forest_level2')
    running = True
    decro_far = pygame.transform.scale(load_image(NIGHT['decro_far']), (screen_width * 2, screen_height))
    decro_near = pygame.transform.scale(load_image(NIGHT['decro_near']), (screen_width * 2, screen_height))
    night = pygame.transform.scale(load_image(NIGHT['night']), (screen_width * 2, screen_height))
    while running:
        canvas.blit(night, (0, 0))
        canvas.blit(decro_far, (0, 0))
        canvas.blit(decro_near, (0, 0))
        window.blit(canvas, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.K_ESCAPE:
                terminate()
        night_level.run()
        if night_level.boss_dead and night_level.player.sprite.rect.colliderect(night_level.portal.sprite.rect):
            final_menu()

        pygame.display.flip()
        mainClock.tick(60)


def final_menu():
    click = False
    final_score = forest_level.final_score(start_time)
    music.change_music('start_menu')
    background = pygame.transform.scale(load_image(MENU['menu_background']), (screen_width, screen_height))
    while True:
        screen.blit(background, (0, 0))
        draw_text('Descent', title_font, (255, 255, 255), screen, screen_width // 2, 100)

        mouse_pos = pygame.mouse.get_pos()

        exit_btn = pygame.Rect(500, 400, 350, 50)
        if exit_btn.collidepoint(mouse_pos):
            exit_btn = pygame.Rect(490, 390, 370, 70)
            if click:
                main_menu()

        pygame.draw.rect(screen, (255, 0, 0), exit_btn, border_radius=10)

        draw_text('Main menu', final_menu_font, (255, 255, 255), screen, 600, 407)

        draw_text(f'Final score - {final_score}', final_score_font, (255, 255, 255), screen, 600, 700)

        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        pygame.display.flip()
        mainClock.tick(60)


main_menu()