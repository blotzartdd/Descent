from load_image import load_image


ALL_TILES = {
    'forest_tiles': load_image('../data/tiles/forest/forest.png')
}

CHARACTER = {
    'attack1': load_image('../data/character/Attack1.png'),
    'attack2': load_image('../data/character/Attack2.png'),
    'attack3': load_image('../data/character/Attack3.png'),
    'before_jump': load_image('..data/character/beforejumpnew.png'),
    'jump': load_image('..data/character/jump.png'),
    'before_landing': load_image('..data/character/beforelanding.png'),
    'fall': load_image('..data/character/fall.png'),
    'dash': load_image('..data/chracter/dash.png'),
    'dead': load_image('..data/character/Dead.png'),
    'run': load_image('..data/character/Run.png'),
    'hit': load_image('..data/character/Hit.png'),
    'attack_icon': load_image('..data/character/skillicon/attack.png')
}

ENEMY_MELEE_SKELETON = {
    'attack': load_image('../data/enemy/melee_skeleton/SkeletonAttack.png'),
    'dead': load_image('../data/enemy/melee_skeleton/SkeletonDead.png'),
    'hit': load_image('../data/enemy/melee_skeleton/SkeletonHit.png'),
    'walk': load_image('../data/enemy/melee_skeleton/SkeletonWalk.png')
}