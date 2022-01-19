'''
Знаки для level_map:
1 - grass1
2 - grass2
3 - grass3
4 - grass4
5 - grass5
6 - grass1 - 750(x)
7 - grass2 - 750(x)
8 - grass5 - 750(x)
9 - grass1 - 1000(x) - 500(y)
* - big_stone
% - big_stone - 50(y)
. - big_wood
_ - big_wooden_bridge
0 - portal
| - fortress_bg
/ - small_wooden_bridge
c - wooden_chair
p - player
# - brown_tile
@ - empty_tile
+ - empty_tile + 100(y)
e - enemy
b - boss
'''

tile_size = 128
size = screen_width, screen_height = 1600, 1080

MENU = {
    'menu_background': 'images/background_1920_1080.jpg'
}
FOREST = {
    'forest_tiles': 'tiles/forest/forest.png',
    'decro_far': 'tiles/forest/pratice/decro_far.png',
    'sky': 'tiles/forest/pratice/Sky.png',
    'static': 'tiles/forest/2/decro_static.png'
}

NIGHT = {
    'night': 'tiles/night/1/Background.png',
    'decro_near': 'tiles/night/1/decro_near.png',
    'decro_far': 'tiles/night/1/decro_far.png'
}

FOREST_TILES_CROPS = {
    '1': 'tiles/forest/grass1.png',
    '2': 'tiles/forest/grass2.png',
    '3': 'tiles/forest/grass3.png',
    '4': 'tiles/forest/grass4.png',
    '5': 'tiles/forest/grass5.png',
    '6': 'tiles/forest/grass1.png',
    '7': 'tiles/forest/grass2.png',
    '8': 'tiles/forest/grass5.png',
    '9': 'tiles/forest/grass5.png',
    '*': 'tiles/forest/big_stone.png',
    '%': 'tiles/forest/big_stone.png',
    '.': 'tiles/forest/big_wood.png',
    '_': 'tiles/forest/big_wooden_bridge.png',
    '|': 'tiles/forest/fortress_bg.png',
    '/': 'tiles/forest/small_wooden_bridge.png',
    'c': 'tiles/forest/wooden_Chair.png',
    '#': 'tiles/forest/brown_tile.png',
    '@': 'tiles/forest/empty_tile.png',
    '+': 'tiles/forest/empty_tile.png',
    '0': 'tiles/forest/portal.png'
}

CHARACTER = {
    'attack': 'character/Attack1.png',
    'before_jump': 'character/beforejumpnew.png',
    'jump': 'character/jump.png',
    'before_landing': 'character/beforelanding.png',
    'fall': 'character/fall.png',
    'dash': 'character/dash.png',
    'dead': 'character/Dead.png',
    'run': 'character/Run.png',
    'hit': 'character/Hit.png',
    'idle': 'character/Idle.png',
    'skill': 'character/skill.png'
}

CHARACTER_ANIMATIONS_CUT = {
        #  How much cut
        'attack': [52, 27, 10],
        'before_jump': [23, 28, 6],
        'jump': [13, 25, 4],
        'before_landing': [25, 24, 10],
        'fall': [16, 30, 4],
        'dash': [22, 19, 4],
        'dead': [26, 24, 10],
        'run': [19, 21, 10],
        'hit': [24, 19, 10],
        'idle': [15, 18, 2],
        'skill': [512, 512, 15]
    }

PORTAL_ANIMATIONS_CUT = {
    'portal': [186, 188, 10]
}

ENEMY_MELEE_SKELETON = {
    'attack': 'enemy/melee_skeleton/SkeletonAttack.png',
    'dead': 'enemy/melee_skeleton/SkeletonDead.png',
    'hit': 'enemy/melee_skeleton/SkeletonHit.png',
    'walk': 'enemy/melee_skeleton/SkeletonWalk.png',
    'idle': 'enemy/melee_skeleton/SkeletonIdle.png'
}

ENEMY_RED_SKELETON = {
    'attack': 'enemy/red_skeleton/attack1.png',
    'dead': 'enemy/red_skeleton/dead.png',
    'hit': 'enemy/red_skeleton/hit.png',
    'walk': 'enemy/red_skeleton/walk.png',
    'idle': 'enemy/red_skeleton/idle.png'
}

BOSS = {
    'attack': 'enemy/boss/Attack.png',
    'dead': 'enemy/boss/Dead.png',
    'hit': 'enemy/boss/Hit.png',
    'walk': 'enemy/boss/Walk.png',
    'idle': 'enemy/boss/Idle.png'
}

MELEE_SKELETON_ANIMATIONS_CUT = {
    'attack': [43, 37, 18],
    'dead': [33, 32, 15],
    'hit': [30, 32, 8],
    'walk': [22, 33, 13],
    'idle': [24, 32, 11]
}

RED_SKELETON_ANIMATIONS_CUT = {
    'attack': [49, 31, 6],
    'dead': [48, 33, 6],
    'hit': [22, 31, 3],
    'walk': [18, 33, 6],
    'idle': [20, 32, 3]
}

BOSS_ANIMATIONS_CUT = {
    'attack': [152, 82, 7],
    'dead': [70, 64, 8],
    'hit': [50, 64, 4],
    'walk': [70, 66, 6],
    'idle': [50, 64, 6]
}

MUSIC = {
    'start_menu': '../data/sounds/soundtrack/Heroic_Demise.mp3',
    'forest_level1': '../data/sounds/soundtrack/carnivalrides.mp3',
    'forest_level2': '../data/sounds/soundtrack/The Dark Amulet.mp3'
}