import pygame
import constants

ui_rect = pygame.Rect(
    (constants.screen_info.current_h, 0),
    (constants.screen_info.current_w - constants.screen_info.current_h, constants.screen_info.current_h)
)

player_GLO = 10


def render_ui():
    constants.screen.fill(constants.SCREEN_COLOR, ui_rect)

    glo_rect = constants.FONT.render_to(constants.screen, (ui_rect.left + constants.TILE_WIDTH, ui_rect.top),
                                        'GLO: ', [255, 255, 255, 255], None, size=constants.FONT_SIZE, rotation=0)

    for i in range(player_GLO):
        constants.FONT.render_to(constants.screen, (glo_rect.right + (constants.TILE_WIDTH * i), glo_rect.top),
                                 '*', 'cyan', None, size=constants.FONT_SIZE * 2, rotation=45)

# §  gene


