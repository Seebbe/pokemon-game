import pygame

pika = pygame.image.load('img/pika.png')
magi = pygame.image.load('img/magi.png')
snor = pygame.image.load('img/snorlax.png')
blasttoise = pygame.image.load('img/blasttoise.png')


###TILES IMPORT
GRASS1 = pygame.image.load('img/tiles/grass1.png')
TALL_GRASS = pygame.image.load('img/tiles/tall_grass.png')
TALL_GRASS1 = pygame.image.load('img/tiles/tall_grass1.png')
TALL_GRASS2 = pygame.image.load('img/tiles/tall_grass2.png')

WALL_BOT = pygame.image.load('img/tiles/wall_bot.png')
WALL_BOT_LEFT = pygame.image.load('img/tiles/wall_bot_left.png')
WALL_TOP_LEFT = pygame.image.load('img/tiles/wall_top_left.png')
WALL_RIGHT = pygame.image.load('img/tiles/wall_right.png')
WALL_MID = pygame.image.load('img/tiles/wall_mid.png')
WALL_MID_BOT_RIGHT = pygame.image.load('img/tiles/wall_mid_bot_right.png')
WALL_MID_BOT_LEFT = pygame.image.load('img/tiles/wall_mid_bot_left.png')
WALL_BOT_RIGHT = pygame.image.load('img/tiles/wall_bot_right.png')

WALL_LEFT = pygame.image.load('img/tiles/wall_left.png')

WALL_TOP_RIGHT = pygame.image.load('img/tiles/wall_top_right.png')
WALL_TOP = pygame.image.load('img/tiles/wall_top.png')

def getTile(val):
    if val == 0:
        return GRASS1
    elif val == 1:
        return TALL_GRASS1
    elif val == 2:
        return WALL_RIGHT
    elif val == 3:
        return WALL_BOT
    elif val == 4:
        return WALL_BOT_RIGHT
    elif val == 5:
        return WALL_BOT_LEFT
    elif val == 6:
        return WALL_LEFT
    elif val == 7:
        return WALL_TOP_LEFT
    elif val == 8:
        return WALL_TOP
    elif val == 9:
        return WALL_TOP_RIGHT
    elif val == 10:
        return WALL_MID
    elif val == 11:
        return WALL_MID_BOT_RIGHT
    elif val == 12:
        return WALL_MID_BOT_LEFT

    return GRASS1
