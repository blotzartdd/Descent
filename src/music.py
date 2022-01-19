import pygame
from settings import MUSIC


class Music:
    def __init__(self, game_status):
        self.cur_music = pygame.mixer.Sound(MUSIC[game_status])
        self.cur_music.set_volume(0.2)
        self.game_status = game_status

    def start_play_music(self):
        if self.game_status == 'main_menu':
            self.cur_music.play(-1, 5)
        else:
            self.cur_music.play(-1)

    def change_music(self, game_status):
        self.game_status = game_status
        self.cur_music.stop()
        self.cur_music = pygame.mixer.Sound(MUSIC[game_status])
        self.start_play_music()