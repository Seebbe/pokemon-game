import pygame

"""
    file that imports all the assets for the game
"""


pika = pygame.image.load('img/pika.png')
magi = pygame.image.load('img/magi.png')
snor = pygame.image.load('img/snorlax.png')
blasttoise = pygame.image.load('img/pixel_art/blastoise_pixel.png')
jiggly = pygame.image.load('img/pixel_art/jiggly_pixel.png')
pidgey = pygame.image.load('img/pixel_art/pidgey.png')


#Figting pictures
pikachu_fighting = pygame.image.load('img/fighting_images/back/pikachu.png')
blastoise_fighting = pygame.image.load('img/fighting_images/emerald_sprites/9.png')
jiggly_fighting = pygame.image.load('img/fighting_images/emerald_sprites/39.png')
pidgey_fighting = pygame.image.load('img/fighting_images/emerald_sprites/16.png')

char_splash = pygame.image.load('img/char_splash.png')
blast_splash = pygame.image.load('img/blast_splash.png')
venu_splash = pygame.image.load('img/venu_splash.png')

poke_logo = pygame.image.load('img/pokemon logo.png')
poke_logo = pygame.transform.scale(poke_logo, (512, 188))
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


box1 = pygame.image.load('img/ui/box1.png')
box1_hover = pygame.image.load('img/ui/box1_hover.png')
box2 = pygame.image.load('img/ui/box2.png')
box2_hover = pygame.image.load('img/ui/box2_hover.png')

# Attacks
lightning_attack = pygame.image.load('img/attack/lightning.png')
water_attack = pygame.image.load('img/attack/watter_attack.png')
#battle_scene
battle_scene = pygame.image.load('img/battle_background.png')

#Function that returns asset based on value in 2d-list map
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


# Pokemon Fighting images
battle_snorlax = pygame.image.load('img/fighting_images/emerald_sprites/143.png')
