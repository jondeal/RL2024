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
                                 '*', 'cyan', None, size=constants.FONT_SIZE * 1.5, rotation=45)

    inventory, inventory_rect = constants.FONT.render('<INVENTORY>', [255, 255, 255, 255], None, size=constants.FONT_SIZE, rotation=0)
    inventory_rect.centerx = ui_rect.centerx
    inventory_rect.top = ui_rect.top + constants.TILE_HEIGHT * 3
    inventory_rect.bottom = ui_rect.top + constants.TILE_HEIGHT * 4
    constants.screen.blit(inventory, inventory_rect)

    if player.inventory:
        for item in player.inventory:
            inventory_item, inventory_item_rect = constants.FONT.render(item.glyph + ' : ' + item.name,
                                                                        [255, 255, 0, 255], None,
                                                                        size=constants.FONT_SIZE, rotation=0)
            constants.screen.blit(inventory_item, (ui_rect.left + constants.TILE_WIDTH, inventory_rect.bottom + constants.TILE_HEIGHT +
                                                   constants.TILE_HEIGHT * player.inventory.index(item)))
