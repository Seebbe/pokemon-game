# Import and initialize the pygame library
import pygame
from Pokemons import pidgey
import Entities as ent
import tiles as assets
import Helper

pygame.init()

# Set up the drawing window
height = 32 * 26
width = 32 * 26
a = 5
screen = pygame.display.set_mode([width, height], pygame.DOUBLEBUF, 32)

tile_width = 32
tile_height = 32

map_width = 26
map_height = 26

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

map1 = [[11, 3, 3, 3, 3, 3, 3, 3, 3, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [2, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [2, 1, 1, 7, 9, 1, 1, 1, 0, 0, 0, 0, 0, 0, 7, 8, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [2, 1, 1, 5, 4, 1, 1, 0, 0, 0, 0, 0, 0, 0, 6, 10, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [4, 0, 1, 1, 1, 1, 0, 0, 0, 0, 7, 8, 8, 8, 10, 10, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 6, 10, 10, 10, 10, 10, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 12, 10, 11, 3, 3, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 3, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
        ]

# Game variables
running = True
tick = 0
tickrate = 4

pygame.font.init()
font = pygame.font.Font('img/pokemon_fire_red.ttf', 16)

# Initialize hero and entities

hero = ent.Hero(assets.pika)
magicarp = ent.Pokemon(10, 10, assets.magi)
magicarp2 = ent.Pokemon(3, 3, assets.magi)
magicarp3 = ent.Pokemon(6, 3, assets.magi)

#pidgey = pidgey.Pidgey(10, 20, assets.blasttoise)

snorlax = ent.Pokemon(4, 7, assets.snor)

entities = [magicarp, magicarp2, magicarp3, snorlax, pidgey]

background, foreground = Helper.generateBackgroundForeground(map1, map_width, map_height, tile_width, tile_height, width, height)


# Updates every tick
# TODO: Fix tick rate
clock = pygame.time.Clock()
def update(dt):
    clock.tick(30)

    if tick % tickrate == 0:
        hero.prevposition()

        # Input for keys

        if keys[pygame.K_LEFT]:
            if Helper.inboundSolidEntity(hero.x - 1, hero.y, entities, map_width, map_height, map1):
                hero.move(hero.x - 1, hero.y)
                hero.left()

        if keys[pygame.K_RIGHT]:
            if Helper.inboundSolidEntity(hero.x + 1, hero.y, entities, map_width, map_height, map1):
                hero.move(hero.x + 1, hero.y)
                hero.right()

        if keys[pygame.K_UP]:
            if Helper.inboundSolidEntity(hero.x, hero.y - 1, entities, map_width, map_height, map1):
                hero.move(hero.x, hero.y - 1)

        if keys[pygame.K_DOWN]:
            if Helper.inboundSolidEntity(hero.x, hero.y + 1, entities, map_width, map_height, map1):
                hero.move(hero.x, hero.y + 1)

        if keys[pygame.K_SPACE]:

            e = hero.nearEntity(entities)
            if e:
                print("INTERACT with ", e)
                e.talk()
                if e is pidgey:
                    pidgey.start()
                    print(pidgey.health)
                    pidgey.health -= 11
                    print(pidgey.health)

    for e in entities:
        e.update(dt)


# Draw calls
def draw():
    screen.fill((255, 255, 255))

    # Render pre-rendered background
    screen.blit(background, (0, 0))

    # Loop all pokemons and draw
    for e in entities:
        screen.blit(e.asset, (e.x * tile_width, e.y * tile_height))

    # Draw hero
    screen.blit(hero.getAsset(), hero.realpositiontuple(tick, tickrate, tile_width, tile_height))

    # Foreground on top of everything
    screen.blit(foreground, (0, 0))

    # Draw entity text
    for e in entities:
        if (e.displaymessage):
            textsurface = font.render(e.message, False, (0, 0, 0))

            tx = e.x * tile_width - textsurface.get_width() / 4
            ty = e.y * tile_height - 20

            pygame.draw.rect(screen, (255, 255, 255, 100),
                             (tx - 4, ty - 4, textsurface.get_width() + 8, textsurface.get_height() + 8))
            screen.blit(textsurface, (tx, ty))


    # Flip the display, pygame stuff
    pygame.display.flip()


while running:
    tick += 1
    # Pygame, if quit, exit loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        keys = pygame.key.get_pressed()

    update()
    draw()

    if tick > 1000000:
        tick = 0

pygame.quit()
