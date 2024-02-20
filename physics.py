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
            #  right and up
            elif initiating_entity.direction == (1, -1):
                positions_to_check = [
                    (initiating_entity.position[0] + 1, initiating_entity.position[1]),  # tile to the right
                    (initiating_entity.position[0], initiating_entity.position[1] - 1)  # tile up
                ]
                right_tile_blocked = None
                up_tile_blocked = None
                for tile in level.tiles:
                    if tile.position == positions_to_check[0]:
                        if tile.is_blocked:
                            right_tile_blocked = True
                        else:
                            right_tile_blocked = False
                    elif tile.position == positions_to_check[1]:
                        if tile.is_blocked:
                            up_tile_blocked = True
                        else:
                            up_tile_blocked = False
                condition_bools = [right_tile_blocked, up_tile_blocked]
                if condition_bools == [True, True]:
                    initiating_entity.direction = (-initiating_entity.direction[0], -initiating_entity.direction[1])
                elif condition_bools == [False, False]:
                    initiating_entity.direction = (-initiating_entity.direction[0], -initiating_entity.direction[1])
                elif condition_bools == [True, False]:
                    initiating_entity.direction = (-initiating_entity.direction[0], initiating_entity.direction[1])
                elif condition_bools == [False, True]:
                    initiating_entity.direction = (initiating_entity.direction[0], -initiating_entity.direction[1])
            # left and up
            elif initiating_entity.direction == (-1, -1):
                positions_to_check = [
                    (initiating_entity.position[0] - 1, initiating_entity.position[1]),  # tile to the left
                    (initiating_entity.position[0], initiating_entity.position[1] - 1)  # tile up
                ]
                left_tile_blocked = None
                up_tile_blocked = None
                for tile in level.tiles:
                    if tile.position == positions_to_check[0]:
                        if tile.is_blocked:
                            left_tile_blocked = True
                        else:
                            left_tile_blocked = False
                    elif tile.position == positions_to_check[1]:
                        if tile.is_blocked:
                            up_tile_blocked = True
                        else:
                            up_tile_blocked = False
                condition_bools = [left_tile_blocked, up_tile_blocked]
                if condition_bools == [True, True]:
                    initiating_entity.direction = (-initiating_entity.direction[0], -initiating_entity.direction[1])
                elif condition_bools == [False, False]:
                    initiating_entity.direction = (-initiating_entity.direction[0], -initiating_entity.direction[1])
                elif condition_bools == [True, False]:
                    initiating_entity.direction = (-initiating_entity.direction[0], initiating_entity.direction[1])
                elif condition_bools == [False, True]:
                    initiating_entity.direction = (initiating_entity.direction[0], -initiating_entity.direction[1])
            # right and down
            elif initiating_entity.direction == (1, 1):
                positions_to_check = [
                    (initiating_entity.position[0] + 1, initiating_entity.position[1]),  # tile to the right
                    (initiating_entity.position[0], initiating_entity.position[1] + 1)  # tile down
                ]
                right_tile_blocked = None
                down_tile_blocked = None
                for tile in level.tiles:
                    if tile.position == positions_to_check[0]:
                        if tile.is_blocked:
                            right_tile_blocked = True
                        else:
                            right_tile_blocked = False
                    elif tile.position == positions_to_check[1]:
                        if tile.is_blocked:
                            down_tile_blocked = True
                        else:
                            down_tile_blocked = False
                condition_bools = [right_tile_blocked, down_tile_blocked]
                if condition_bools == [True, True]:
                    initiating_entity.direction = (-initiating_entity.direction[0], -initiating_entity.direction[1])
                elif condition_bools == [False, False]:
                    initiating_entity.direction = (-initiating_entity.direction[0], -initiating_entity.direction[1])
                elif condition_bools == [True, False]:
                    initiating_entity.direction = (-initiating_entity.direction[0], initiating_entity.direction[1])
                elif condition_bools == [False, True]:
                    initiating_entity.direction = (initiating_entity.direction[0], -initiating_entity.direction[1])
            # left and down
            elif initiating_entity.direction == (-1, 1):
                positions_to_check = [
                    (initiating_entity.position[0] - 1, initiating_entity.position[1]),  # tile to the left
                    (initiating_entity.position[0], initiating_entity.position[1] + 1)  # tile down
                ]
                left_tile_blocked = None
                down_tile_blocked = None
                for tile in level.tiles:
                    if tile.position == positions_to_check[0]:
                        if tile.is_blocked:
                            left_tile_blocked = True
                        else:
                            left_tile_blocked = False
                    elif tile.position == positions_to_check[1]:
                        if tile.is_blocked:
                            down_tile_blocked = True
                        else:
                            down_tile_blocked = False
                condition_bools = [left_tile_blocked, down_tile_blocked]
                if condition_bools == [True, True]:
                    initiating_entity.direction = (-initiating_entity.direction[0], -initiating_entity.direction[1])
                elif condition_bools == [False, False]:
                    initiating_entity.direction = (-initiating_entity.direction[0], -initiating_entity.direction[1])
                elif condition_bools == [True, False]:
                    initiating_entity.direction = (-initiating_entity.direction[0], initiating_entity.direction[1])
                elif condition_bools == [False, True]:
                    initiating_entity.direction = (initiating_entity.direction[0], -initiating_entity.direction[1])
        else:  # receiving_entity.name != 'wall'
            receiving_entity.impulse = initiating_entity.impulse
            receiving_entity.direction = initiating_entity.direction
            # print(f'{initiating_entity.name} hits {receiving_entity.name} with impulse {initiating_entity.impulse}')  # debug

            initiating_entity.impulse = 0
            initiating_entity.direction = (0, 0)
            move_check(receiving_entity)

    for actor in level.actors:
        if actor.impulse > 0:
            move_check(actor)
