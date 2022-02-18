def distance(x1, x2, y1, y2):
    return (((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** 0.5


# Check if x,y is within map
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