def resolve_physics(level):
    to_resolve = []
    for actor in level.actors:
        if actor.impulse > 0:
            to_resolve.append(actor)
    while to_resolve:
        for actor in to_resolve:
            while actor.impulse > 0:
                test_address = (actor.x + actor.direction[0], actor.y + actor.direction[1])
                for tile in level.tiles:
                    if (tile.x, tile.y) == test_address:
                        if tile.is_blocked:
                            actor.impulse = 0
                            actor.direction = (0, 0)
                        else:
                            actor.x, actor.y = tile.x, tile.y
                            actor.rect = tile.rect
                            actor.impulse -= 1
                            actor.direction = (0, 0)
            else:
                to_resolve.remove(actor)
