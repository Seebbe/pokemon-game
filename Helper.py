import pygame
import tiles as assets

"""
    Method that contains helper functions
"""

# Returns the distance between two points
def distance(x1, x2, y1, y2):
    return (((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** 0.5


# Check if x, y is within map
def inbounds(x, y, entities, map_width, map_height, map):
    return 0 <= x < map_width and 0 <= y < map_height


# Check if x,y is within map, and not on solid tile
def inboundSolid(x, y, entities, map_width, map_height, map):
    if inbounds(x, y, entities, map_width, map_height, map):
        return map[y][x] <= 1
    return False


# Check if x,y is within map, not on solid tile, and not on entity
def inboundSolidEntity(x, y, entities, map_width, map_height, map):
    noEntity = True
    if inboundSolid(x, y, entities, map_width, map_height, map):
        for e in entities:
            if e.x == x and e.y == y:
                noEntity = False
                break
    else:
        noEntity = False
    return noEntity

# Method that pre-renders map and foreground
def generateBackgroundForeground(map, map_width, map_height, tile_width, tile_height, width, height):

    background = pygame.Surface([width, height], pygame.SRCALPHA, 32)
    foreground = pygame.Surface([width, height], pygame.SRCALPHA, 32)
    foreground.convert_alpha()
    for y in range(0, map_height):
        for x in range(0, map_width):
            val = map[y][x]
            background.blit(assets.getTile(0), (x * tile_width, y * tile_height))
            background.blit(assets.getTile(val), (x * tile_width, y * tile_height))
            if val == 1:
                foreground.blit(assets.TALL_GRASS2, (x * tile_width, y * tile_height))

    return background, foreground

# https://stackoverflow.com/questions/42014195/rendering-text-with-multiple-lines-in-pygame
# Method that draws multi-line text. Based on Stack-overflow comment
def box_text(surface, font, x_start, x_end, y_start, text, colour):
    x = x_start
    y = y_start
    words = text.split(' ')

    space = 5

    for word in words:
        word_t = font.render(word, True, colour)
        if word_t.get_width() + x <= x_end:
            surface.blit(word_t, (x, y))
            x += word_t.get_width() + space
        else:
            y += word_t.get_height() + 4
            x = x_start
            surface.blit(word_t, (x, y))
            x += word_t.get_width() + space

