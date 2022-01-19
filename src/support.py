import os
import sys
import pygame
from PIL import Image
from settings import CHARACTER, CHARACTER_ANIMATIONS_CUT, ENEMY_MELEE_SKELETON, MELEE_SKELETON_ANIMATIONS_CUT, \
    PORTAL_ANIMATIONS_CUT, FOREST_TILES_CROPS


def load_image(name, colorkey=None, crop_coords=()):
    fullname = os.path.join('../data/', name)
    if not os.path.isfile(fullname):
        sys.exit()
    if crop_coords:
        im = Image.open(fullname)
        im_crop = im.crop(crop_coords)
        fullname = fullname[:-4] + 'crop' + fullname[-4:]
        im_crop.save(fullname)
        image = pygame.image.load(fullname)
    else:
        image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


def terminate():
    pygame.quit()
    sys.exit()


def get_character_assets_dict():
    animations = {
        'attack': [],
        'before_jump': [],
        'jump': [],
        'before_landing': [],
        'fall': [],
        'dash': [],
        'dead': [],
        'run': [],
        'hit': [],
        'idle': [],
        'skill': []
    }

    for animation in animations:
        for i in range(CHARACTER_ANIMATIONS_CUT[animation][2]):
            animations[animation].append(pygame.transform.scale(load_image(CHARACTER[animation],
                                                                           crop_coords=(CHARACTER_ANIMATIONS_CUT
                                                                                        [animation][0] * i,
                                                                                        0,
                                                                                        CHARACTER_ANIMATIONS_CUT
                                                                                        [animation][0] * (i + 1),
                                                                                        CHARACTER_ANIMATIONS_CUT
                                                                                        [animation][1])),
                                                                (CHARACTER_ANIMATIONS_CUT[animation][0] * 2.5,
                                                                 CHARACTER_ANIMATIONS_CUT[animation][1] * 2.5)))
    return animations


def get_enemy_assets_dict(enemy_type, animations_type):
    animations = {
        'attack': [],
        'dead': [],
        'hit': [],
        'walk': [],
        'idle': []
    }

    for animation in animations:
        for i in range(animations_type[animation][2]):
            animations[animation].append(pygame.transform.scale(load_image(enemy_type[animation],
                                                                           crop_coords=(animations_type
                                                                                        [animation][0] * i,
                                                                                        0,
                                                                                        animations_type
                                                                                        [animation][0] * (i + 1),
                                                                                        animations_type
                                                                                        [animation][1])),
                                                                (animations_type[animation][0] * 2.5,
                                                                 animations_type[animation][1] * 2.5)))
    return animations


def get_portal_assets():
    animations = []
    for i in range(PORTAL_ANIMATIONS_CUT['portal'][2]):
        animations.append(pygame.transform.scale(load_image(FOREST_TILES_CROPS['0'],
                                                            crop_coords=(PORTAL_ANIMATIONS_CUT['portal'][0] * i,
                                                                         0,
                                                                         PORTAL_ANIMATIONS_CUT['portal'][0] * (i + 1),
                                                                         PORTAL_ANIMATIONS_CUT['portal'][1])),
                                                 (PORTAL_ANIMATIONS_CUT['portal'][0] * 2,
                                                  PORTAL_ANIMATIONS_CUT['portal'][1] * 2)))
    return animations


def draw_text(text, cur_font, color, surface, x, y):
    text = cur_font.render(text, True, color)
    text_rect = text.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text, text_rect)


def open_level(filepath):
    with open(filepath, 'r') as f:
        map = []
        for line in f.readlines():
            if line != '\n':
                map.append(line.rstrip())
    return map