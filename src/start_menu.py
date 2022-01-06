import pygame
import sys
from load_image import load_image

pygame.init()
pygame.display.set_caption('Descent')
mainClock = pygame.time.Clock()
size = screen_width, screen_height = 1024, 768
screen = pygame.display.set_mode(size)
menu_font = pygame.font.Font('../data/fonts/war_priest_condensed.ttf', 15)
title_font = pygame.font.Font('../data/fonts/war_priest.ttf', 60)


def draw_text(text, cur_font, color, surface, x, y):
    text = cur_font.render(text, True, color)
    text_rect = text.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text, text_rect)


def main_menu():
    click = False
    background = pygame.transform.scale(load_image('background_1920_1080.jpg'), (screen_width, screen_height))
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
                start_game()
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


def start_game():
    running = True
    while running:
        screen.fill((0, 0, 0))
        draw_text('Начать игру', menu_font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
        pygame.display.flip()
        mainClock.tick(60)


def options():
    running = True
    while running:
        screen.fill((0, 0, 0))
        draw_text('Настройки', menu_font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
        pygame.display.flip()
        mainClock.tick(60)


def terminate():
    pygame.quit()
    sys.exit()