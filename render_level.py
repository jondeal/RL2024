import constants
import pygame

bg_surface = pygame.Surface((constants.TILE_WIDTH, constants.TILE_HEIGHT))

ui_rect = pygame.Rect((constants.screen_info.current_h, 0), (constants.screen_info.current_w - constants.screen_info.current_h, constants.screen_info.current_h))
constants.screen.fill(constants.SCREEN_COLOR, ui_rect)


def render(level):

    for tile in level.tiles:
        bg_surface.fill(tile.bg_color)
        constants.screen.blit(bg_surface, tile.rect)
        tile.glyph_color[3] = 255
        for actor in level.actors:
            if tile.position == actor.position:
                tile.glyph_color = [tile.glyph_color[0], tile.glyph_color[1], tile.glyph_color[2], 0]

    to_render = [level.tiles, level.actors]

    for entity_list in to_render:
        for entity in entity_list:
            if entity.glyph_size != constants.FONT_SIZE:
                size = entity.glyph_size
            else:
                size = constants.FONT_SIZE

            glyph_image, glyph_rect = constants.FONT.render(entity.glyph, entity.glyph_color, None, size=size,
                                                            rotation=entity.glyph_rotation)

            glyph_rect.center = entity.rect.center

            constants.screen.blit(glyph_image, glyph_rect)
