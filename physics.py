def resolve_physics(level):

    def move_check(entity):
        position_to_check = (entity.position[0] + entity.direction[0], entity.position[1] + entity.direction[1])
        for other_actor in level.actors:
            if other_actor.position == position_to_check:
                handle_collision(other_actor)
        for tile in level.tiles:
            if tile.position == position_to_check:
                if tile.is_blocked:
                    handle_collision(tile)
                else:
                    entity.position = tile.position
                    entity.rect = tile.rect
                    entity.impulse -= 1
                    entity.direction = (0, 0)

    def handle_collision(other_thing):
        if other_thing.name == 'wall':
            actor.direction = (-actor.direction[0], -actor.direction[1])
        else:
            other_thing.impulse = actor.impulse
            other_thing.direction = actor.direction
            move_check(other_thing)

    for actor in level.actors:
        if actor.impulse > 0:
            move_check(actor)
