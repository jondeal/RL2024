import Actor
import Item
import constants


def resolve_physics(level):

    def move_to_position(initiating_entity, receiving_entity):
        initiating_entity.position = receiving_entity.position
        initiating_entity.rect = receiving_entity.rect
        initiating_entity.speed -= 1
        make_still(initiating_entity)

    def apply_force(initiating_entity, receiving_entity):
        initiating_entity_initial_momentum = initiating_entity.mass * initiating_entity.speed

        receiving_entity.speed = initiating_entity_initial_momentum // receiving_entity.mass
        receiving_entity.direction = initiating_entity.direction

        make_still(initiating_entity)

        if receiving_entity.speed > 0:
            collision = collision_check(receiving_entity)
            handle_collision(collision)
        else:  # prevents receiving entity from moving if entity.speed == 0 after collision
            make_still(receiving_entity)

    def diagonal_wall_gap_check(entity_to_check):
        positions_to_check = [
            (entity_to_check.position[0] + entity_to_check.direction[0], entity_to_check.position[1]),
            (entity_to_check.position[0], entity_to_check.position[1] + entity_to_check.direction[1])
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
        if x_tile_blocked is True and y_tile_blocked is True:
            return True
        else:
            return False

    def wall_rebound_direction(entity_to_rebound):
        if abs(entity_to_rebound.direction[0]) + abs(
                entity_to_rebound.direction[1]) == 1:  # direction is non-diagonal
            entity_to_rebound.direction = (
                -entity_to_rebound.direction[0],
                -entity_to_rebound.direction[1]
            )
            return entity_to_rebound.direction
        else:
            positions_to_check = [
                (entity_to_rebound.position[0] + entity_to_rebound.direction[0],
                 entity_to_rebound.position[1]),  # x-axis tile
                (entity_to_rebound.position[0],
                 entity_to_rebound.position[1] + entity_to_rebound.direction[1])  # y-axis tile
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
                entity_to_rebound.direction = (
                    -entity_to_rebound.direction[0],
                    -entity_to_rebound.direction[1]
                )
            elif condition_bools == [True, False]:
                entity_to_rebound.direction = (
                    -entity_to_rebound.direction[0],
                    entity_to_rebound.direction[1]
                )
            elif condition_bools == [False, True]:
                entity_to_rebound.direction = (
                    entity_to_rebound.direction[0],
                    -entity_to_rebound.direction[1]
                )
            return entity_to_rebound.direction

    def make_still(entity_to_still):
        entity_to_still.speed = 0
        entity_to_still.direction = (0, 0)
        if isinstance(entity_to_still, Actor.Actor):
            entity_to_still.action = None
        else:
            pass

    def collision_check(entity_to_check):
        position_to_check = (entity_to_check.position[0] + entity_to_check.direction[0],
                             entity_to_check.position[1] + entity_to_check.direction[1])
        initiating_entity = entity_to_check
        for actor in level.actors:
            if actor.position == position_to_check:
                had_collision = True
                receiving_entity = actor
                return had_collision, initiating_entity, receiving_entity
        for item in level.items:
            if item.position == position_to_check:
                had_collision = True
                receiving_entity = item
                return had_collision, initiating_entity, receiving_entity
        for tile in level.tiles:
            if tile.position == position_to_check:
                if tile.is_blocked:
                    had_collision = True
                    receiving_entity = tile
                    return had_collision, initiating_entity, receiving_entity
                else:
                    had_collision = False
                    receiving_entity = tile
                    return had_collision, initiating_entity, receiving_entity

    def handle_collision(collision):
        had_collision = collision[0]
        initiating_entity = collision[1]
        receiving_entity = collision[2]

        if had_collision:
            if isinstance(initiating_entity, Actor.Actor):
                if initiating_entity.action == 'shove':
                    if receiving_entity.name == 'wall':
                        make_still(initiating_entity)  # shove against wall fails
                    else:  # shove against entity succeeds
                        apply_force(initiating_entity, receiving_entity)
                elif initiating_entity.action == 'push':
                    if receiving_entity.name == 'wall':
                        make_still(initiating_entity)  # push against wall fails
                    elif isinstance(receiving_entity, Item.Item):
                        move_to_position(initiating_entity, receiving_entity)
                    elif isinstance(receiving_entity, Actor.Actor):
                        if receiving_entity.mass > initiating_entity.mass:
                            make_still(initiating_entity)  # push against more massive entity fails
                        else:
                            open_tile_reached = False
                            total_mass = receiving_entity.mass
                            entities_in_row = []
                            current_entity = receiving_entity
                            current_entity.direction = initiating_entity.direction
                            while total_mass <= initiating_entity.mass and open_tile_reached is False:
                                entities_in_row.append(current_entity)
                                collision_check_result = collision_check(current_entity)
                                if collision_check_result[2].name == 'wall':
                                    for row_entity in entities_in_row:
                                        make_still(row_entity)
                                    make_still(initiating_entity)  # push against wall fails, row of entities doesn't move
                                elif isinstance(collision_check_result[2], Item.Item):
                                    entities_in_row.append(initiating_entity)
                                    for row_entity in entities_in_row:
                                        row_entity.speed += 1
                                        row_entity.position = (
                                            row_entity.position[0] + row_entity.direction[0],
                                            row_entity.position[1] + row_entity.direction[1]
                                        )
                                        for tile in level.tiles:
                                            if tile.position == row_entity.position:
                                                row_entity.rect = tile.rect
                                        make_still(row_entity)

                                    open_tile_reached = True
                                elif isinstance(collision_check_result[2], Actor.Actor):
                                    total_mass += collision_check_result[2].mass
                                    entities_in_row.append(collision_check_result[2])
                                    current_entity = collision_check_result[2]
                                    current_entity.direction = initiating_entity.direction
                                    collision_check(current_entity)
                                elif collision_check_result[0] is False:
                                    entities_in_row.append(initiating_entity)
                                    for row_entity in entities_in_row:
                                        row_entity.position = (
                                            row_entity.position[0] + row_entity.direction[0],
                                            row_entity.position[1] + row_entity.direction[1]
                                        )
                                        for tile in level.tiles:
                                            if tile.position == row_entity.position:
                                                row_entity.rect = tile.rect
                                        make_still(row_entity)

                                    open_tile_reached = True
                            else:  # total_mass > initiating_entity.mass
                                make_still(initiating_entity)
                else:  # if initiating_entity.action != 'shove' and != 'push', i.e. passive movement from collision
                    if receiving_entity.name == 'wall':
                        initiating_entity.direction = wall_rebound_direction(initiating_entity)
                    elif isinstance(receiving_entity, Actor.Actor):
                        apply_force(initiating_entity, receiving_entity)
                    elif isinstance(receiving_entity, Item.Item):
                        initiating_entity.position = receiving_entity.position
                        initiating_entity.rect = receiving_entity.rect
            elif isinstance(initiating_entity, Item.Item):
                if receiving_entity.name == 'wall':
                    initiating_entity.direction = wall_rebound_direction(initiating_entity)
                else:  # elif isinstance(receiving_entity, Item.Item):
                    apply_force(initiating_entity, receiving_entity)
        else:  # if not had_collision
            if isinstance(initiating_entity, Actor.Actor):
                if initiating_entity.action == 'shove':
                    make_still(initiating_entity)
                elif initiating_entity.action == 'push':
                    is_gap = diagonal_wall_gap_check(initiating_entity)
                    if is_gap:
                        make_still(initiating_entity)
                    else:
                        move_to_position(initiating_entity, receiving_entity)
                else:  # passive movement
                    if abs(initiating_entity.direction[0]) + abs(initiating_entity.direction[1]) > 1:  # direction is diagonal
                        is_gap = diagonal_wall_gap_check(initiating_entity)
                        if is_gap:
                            initiating_entity.direction = (-initiating_entity.direction[0], -initiating_entity.direction[1])
                        else:
                            move_to_position(initiating_entity, receiving_entity)
                    else:
                        move_to_position(initiating_entity, receiving_entity)
            elif isinstance(initiating_entity, Item.Item):
                move_to_position(initiating_entity, receiving_entity)

    for entity in level.actors + level.items:
        if entity.speed > 0:
            entity.glyph_color = [255, 0, 0, 255]  # DEBUG
            collision_result = collision_check(entity)
            handle_collision(collision_result)
        else:  # DEBUG
            entity.glyph_color = [0, 0, 255, 255]
        # if entity.direction == (0, 0):  # DEBUG
        #     entity.glyph_size = constants.FONT_SIZE
        # else:
        #     entity.glyph_size = constants.FONT_SIZE / 2
