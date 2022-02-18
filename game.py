# Import and initialize the pygame library
import pygame
import Entities as ent
import tiles as assets
import Helper
import math





pygame.init()

# Set up the drawing window
height = 32 * 26
width = 32 * 26

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
tickrate = 100

pygame.font.init()
font = pygame.font.Font('img/pokemon_fire_red.ttf', 16)

# Initialize hero and entities

hero = ent.Hero(assets.pika)
magicarp = ent.Pokemon(10, 10, assets.magi)
magicarp2 = ent.Pokemon(3, 3, assets.magi)
magicarp3 = ent.Pokemon(6, 3, assets.magi)

pidgey = ent.Pidgey(10,20, assets.blasttoise)

snorlax = ent.Pokemon(4, 7, assets.snor)

entities = [magicarp, magicarp2, magicarp3, snorlax, pidgey]




# Helper functions


# Updates every tick
def update():
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
                if e is pidgey:
                    pidgey.start()
                print("INTERACT with ", e)
                e.talk()

    for e in entities:
        e.update()


# Draw calls
def draw():
    screen.fill((255, 255, 255))

    # Draw tiles of map
    for y in range(0, map_height):
        for x in range(0, map_width):
            val = map1[y][x]
            screen.blit(assets.getTile(0), (x * tile_width, y * tile_height))
            screen.blit(assets.getTile(val), (x * tile_width, y * tile_height))

    # Loop all pokemons and draw
    for e in entities:
        screen.blit(e.asset, (e.x * tile_width, e.y * tile_height))

    # Draw hero
    screen.blit(hero.getAsset(), hero.realpositiontuple(tick, tickrate, tile_width, tile_height))

    # Draw Tiles ontop of everything
    for y in range(0, map_height):
        for x in range(0, map_width):
            val = map1[y][x]
            if val == 1:
                screen.blit(assets.TALL_GRASS2, (x * tile_width, y * tile_height))

    # Draw entity text
    for e in entities:
        if (e.displaymessage):
            textsurface = font.render(e.message, False, (0, 0, 0))

            tx = e.x * tile_width - textsurface.get_width() / 4
            ty = e.y * tile_height - 20

            pygame.draw.rect(screen, (255, 255, 255, 100),
                             (tx - 4, ty - 4, textsurface.get_width() + 8, textsurface.get_height() + 8))
            screen.blit(textsurface, (tx, ty))

    # Flip the display
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

# Done! Time to quit.
pygame.quit()
