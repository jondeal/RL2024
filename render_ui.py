import pygame
import constants

ui_rect = pygame.Rect(
    (constants.screen_info.current_h, 0),
    (constants.screen_info.current_w - constants.screen_info.current_h, constants.screen_info.current_h)
)


def render_ui(player):
    constants.screen.fill(constants.SCREEN_COLOR, ui_rect)

    glo_rect = constants.FONT.render_to(constants.screen, (ui_rect.left + constants.TILE_WIDTH,
                                                           ui_rect.top + constants.TILE_HEIGHT),
                                        'GLO: ', [255, 255, 255, 255], None, size=constants.FONT_SIZE, rotation=0)

    for i in range(player.glo_count):
        constants.FONT.render_to(constants.screen, (glo_rect.right + (constants.TILE_WIDTH * i), glo_rect.top),
                                 '*', 'cyan', None, size=constants.FONT_SIZE * 2, rotation=45)
