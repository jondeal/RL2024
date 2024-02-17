def resolve_physics(level):

    def move_check(entity):
        position_to_check = (entity.position[0] + entity.direction[0], entity.position[1] + entity.direction[1])
        destination_tile = None
        collision = False
        for other_actor in level.actors:
            if other_actor.position == position_to_check:
                collision = True
                handle_collision(entity, other_actor)
        for tile in level.tiles:
            if tile.position == position_to_check:
                if tile.is_blocked:
                    collision = True
                    handle_collision(entity, tile)
                else:
                    destination_tile = tile
        if collision is False:
            entity.position = position_to_check
            entity.rect = destination_tile.rect
            entity.impulse -= 1
            entity.direction = (0, 0)

    def handle_collision(initiating_entity, receiving_entity):
        if receiving_entity.name == 'wall':
            # initiating_entity.impulse = 0  # if enabled, will keep entity from bouncing back from wall collision
            initiating_entity.direction = (-initiating_entity.direction[0], -initiating_entity.direction[1])
            print(f'{initiating_entity.name} hits {receiving_entity.name}')

        else:
            receiving_entity.impulse = initiating_entity.impulse
            receiving_entity.direction = initiating_entity.direction
            print(f'{initiating_entity.name} hits {receiving_entity.name}')

            initiating_entity.impulse = 0
            initiating_entity.direction = (0, 0)
            move_check(receiving_entity)

    for actor in level.actors:
        if actor.impulse > 0:
            move_check(actor)
