import constants
import pygame

bg_surface = pygame.Surface((constants.TILE_WIDTH, constants.TILE_HEIGHT))


def render_level(level):

    for tile in level.tiles:
        if tile.is_highlighted:
            tile.current_bg_color = [100, 100, 0, 255]
        else:
            tile.current_bg_color = tile.default_bg_color
        bg_surface.fill(tile.current_bg_color)
        constants.screen.blit(bg_surface, tile.rect)
        tile.glyph_color[3] = 255
        for actor in level.actors:
            if tile.position == actor.position:
                tile.glyph_color = [tile.glyph_color[0], tile.glyph_color[1], tile.glyph_color[2], 0]
        for item in level.items:
            if tile.position == item.position:
                tile.glyph_color = [tile.glyph_color[0], tile.glyph_color[1], tile.glyph_color[2], 0]

    to_render = [level.tiles, level.actors, level.items]

    for entity_list in to_render:
        for entity in entity_list:
            if entity.glyph_size != constants.FONT_SIZE:
                size = entity.glyph_size
            else:
                size = constants.FONT_SIZE * entity.glyph_size_modifier
            glyph = None
            glyph_color = None
            if entity in level.actors and entity.is_dormant:
                glyph = entity.dormant_glyph
                glyph_color = entity.dormant_glyph_color
            else:
                glyph = entity.glyph
                glyph_color = entity.glyph_color
            if entity in level.items and entity.name == 'force blast':
                directions = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
                for direction in directions:
                    if entity.direction == direction:
                        entity.glyph_rotation = 45 * directions.index(direction)

            glyph_image, glyph_rect = constants.FONT.render(glyph, glyph_color, None, size=size,
                                                            rotation=entity.glyph_rotation)

            glyph_rect.center = entity.rect.center

            constants.screen.blit(glyph_image, glyph_rect)
