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
            # initiating_entity.impulse -= 1  # if set <= 0, will keep entity from bouncing back from wall collision, if commented out impulse will not be affected
            # might need to adjust this in the future to avoid 'infinite bounce' between parallel walls
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
            receiving_entity.impulse = initiating_entity.impulse
            receiving_entity.direction = initiating_entity.direction

            initiating_entity.impulse = 0
            initiating_entity.direction = (0, 0)
            move_check(receiving_entity)

    for actor in level.actors:
        if actor.impulse > 0:
            move_check(actor)
