def resolve_physics(level):

    def move_check(entity):
        position_to_check = (entity.position[0] + entity.direction[0], entity.position[1] + entity.direction[1])
        destination = None
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
                    destination = tile
        if collision is False:
            entity.position = position_to_check
            entity.rect = destination.rect
            entity.impulse -= 1
            if entity.impulse == 0:
                entity.direction = (0, 0)
            else:
                pass

    def handle_collision(initiating_entity, receiving_entity):
        if receiving_entity.name == 'wall':
            # print(f'{initiating_entity.name} hits {receiving_entity.name} with impulse {initiating_entity.impulse}')  # debug
            # initiating_entity.impulse -= 1  # if set <= 0, will keep entity from bouncing back from wall collision, if commented out impulse will not be affected
            if initiating_entity.direction == (1, 0):  # right
                initiating_entity.direction = (-initiating_entity.direction[0], -initiating_entity.direction[1])
            elif initiating_entity.direction == (-1, 0):  # left
                initiating_entity.direction = (-initiating_entity.direction[0], -initiating_entity.direction[1])
            elif initiating_entity.direction == (0, -1):  # up
                initiating_entity.direction = (-initiating_entity.direction[0], -initiating_entity.direction[1])
            elif initiating_entity.direction == (0, 1):  # down
                initiating_entity.direction = (-initiating_entity.direction[0], -initiating_entity.direction[1])
            elif initiating_entity.direction == (1, -1):  # right and up
                position_to_check = (initiating_entity.position[0], initiating_entity.position[1] + 1)
                for tile in level.tiles:
                    if tile.position == position_to_check:
                        if not tile.is_blocked:
                            initiating_entity.direction = (-initiating_entity.direction[0], -initiating_entity.direction[1])
                        else:
                            initiating_entity.direction = (initiating_entity.direction[0], -initiating_entity.direction[1])
            elif initiating_entity.direction == (-1, -1):  # left and up
                position_to_check = (initiating_entity.position[0], initiating_entity.position[1] + 1)
                for tile in level.tiles:
                    if tile.position == position_to_check:
                        if not tile.is_blocked:
                            initiating_entity.direction = (-initiating_entity.direction[0], -initiating_entity.direction[1])
                        else:
                            initiating_entity.direction = (initiating_entity.direction[0], -initiating_entity.direction[1])
            elif initiating_entity.direction == (1, 1):  # right and down
                position_to_check = (initiating_entity.position[0], initiating_entity.position[1] + 1)
                for tile in level.tiles:
                    if tile.position == position_to_check:
                        if not tile.is_blocked:
                            initiating_entity.direction = (-initiating_entity.direction[0], -initiating_entity.direction[1])
                        else:
                            initiating_entity.direction = (initiating_entity.direction[0], -initiating_entity.direction[1])
            elif initiating_entity.direction == (-1, 1):  # left and down
                position_to_check = (initiating_entity.position[0], initiating_entity.position[1] + 1)
                for tile in level.tiles:
                    if tile.position == position_to_check:
                        if not tile.is_blocked:
                            initiating_entity.direction = (-initiating_entity.direction[0], -initiating_entity.direction[1])
                        else:
                            initiating_entity.direction = (-initiating_entity.direction[0], initiating_entity.direction[1])

        else:
            receiving_entity.impulse = initiating_entity.impulse
            receiving_entity.direction = initiating_entity.direction
            # print(f'{initiating_entity.name} hits {receiving_entity.name} with impulse {initiating_entity.impulse}')  # debug

            initiating_entity.impulse = 0
            initiating_entity.direction = (0, 0)
            move_check(receiving_entity)

    for actor in level.actors:
        if actor.impulse > 0:
            move_check(actor)
