def resolve_physics(level):

    def position_check(entity, direction):
        position_to_check = (entity.position[0] + direction[0], entity.position[1] + direction[1])
        for other_actor in level.actors:
            if other_actor.position == position_to_check:
                return other_actor
        for tile in level.tiles:
            if tile.position == position_to_check:
                if tile.is_blocked:
                    return 'wall'
                else:
                    return 'open'

    def collision_check(entity):
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
            entity.speed -= 1
            if entity.speed == 0:
                entity.direction = (0, 0)
            else:
                pass

    def handle_collision(initiating_entity, receiving_entity):
        if initiating_entity.action == 'push':
            if receiving_entity.name == 'wall':
                return
            else:
                if receiving_entity.mass > initiating_entity.mass:
                    return
                else:
                    total_mass = receiving_entity.mass
                    entities_in_row = []
                    current_entity = receiving_entity
                    open_tile_reached = False
                    while total_mass <= initiating_entity.mass and open_tile_reached is False:
                        entities_in_row.append(current_entity)
                        position_check_result = position_check(current_entity, initiating_entity.direction)
                        if position_check_result == 'wall':
                            return
                        elif position_check_result in level.actors:
                            total_mass += position_check_result.mass
                            entities_in_row.append(position_check_result)
                            current_entity = position_check_result
                            position_check(current_entity, initiating_entity.direction)
                        elif position_check_result == 'open':
                            for entity in entities_in_row:
                                entity.speed = 1
                                entity.direction = initiating_entity.direction
                                for tile in level.tiles:
                                    if tile.position == entity.position:
                                        entity.rect = tile.rect
                            open_tile_reached = True

        else:  # initiating_entity.action != 'push'
            if receiving_entity.name == 'wall':
                # initiating_entity.speed -= 1  # if set <= 0, will keep entity from bouncing back from wall collision, if commented out impulse will not be affected
                if abs(initiating_entity.direction[0]) + abs(
                        initiating_entity.direction[1]) == 1:  # direction is non-diagonal
                    initiating_entity.direction = (-initiating_entity.direction[0], -initiating_entity.direction[1])
                else:
                    positions_to_check = [
                        (initiating_entity.position[0] + initiating_entity.direction[0], initiating_entity.position[1]),  # x-axis tile
                        (initiating_entity.position[0], initiating_entity.position[1] + initiating_entity.direction[1])   # y-axis tile
                    ]
                    x_tile_blocked = None
                    y_tile_blocked = None
                    for tile in level.tiles:
                        if tile.position == positions_to_check[0]:
                            if tile.is_blocked:
                                x_tile_blocked = True
                            else:
                                x_tile_blocked = False
                        elif tile.position == positions_to_check[1]:
                            if tile.is_blocked:
                                y_tile_blocked = True
                            else:
                                y_tile_blocked = False
                    condition_bools = [x_tile_blocked, y_tile_blocked]
                    if condition_bools == [True, True] or condition_bools == [False, False]:
                        initiating_entity.direction = (-initiating_entity.direction[0], -initiating_entity.direction[1])
                    elif condition_bools == [True, False]:
                        initiating_entity.direction = (-initiating_entity.direction[0], initiating_entity.direction[1])
                    elif condition_bools == [False, True]:
                        initiating_entity.direction = (initiating_entity.direction[0], -initiating_entity.direction[1])
            else:  # receiving_entity.name != 'wall'
                initiating_entity_initial_momentum = initiating_entity.mass * initiating_entity.speed

                receiving_entity.speed = initiating_entity_initial_momentum // receiving_entity.mass
                receiving_entity.direction = initiating_entity.direction

                initiating_entity.speed = 0
                initiating_entity.direction = (0, 0)
                if receiving_entity.speed > 0:
                    collision_check(receiving_entity)
                else:
                    pass

    for actor in level.actors:
        if actor.speed > 0:
            collision_check(actor)
