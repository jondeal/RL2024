import pygame
import constants

prompt_to_render = None


def render_ui(player):
    constants.screen.fill(constants.SCREEN_COLOR)

    glo_rect = constants.FONT.render_to(constants.screen, (constants.UI_RECT.left + constants.TILE_WIDTH,
                                                           constants.UI_RECT.top),
                                        '﹝GLO﹞', [255, 255, 255, 255], None, size=constants.FONT_SIZE, rotation=0)

    constants.FONT.render_to(constants.screen, (glo_rect.right, constants.UI_RECT.top),
                             ' ✻' + str(player.glo_count), 'cyan', None, size=constants.FONT_SIZE * 1.25, rotation=0)

    inventory_rect = constants.FONT.render_to(constants.screen,
                                              (glo_rect.left, glo_rect.bottom + constants.TILE_HEIGHT),
                                              '﹝INVENTORY﹞', [255, 255, 255, 255], None,
                                              size=constants.FONT_SIZE, rotation=0)

    if player.inventory:
        for item in player.inventory:
            inventory_item, inventory_item_rect = constants.FONT.render(item.inventory_slot[1] + ': ' + item.glyph + ' ' + item.name,
                                                                        [255, 255, 0, 255], None,
                                                                        size=constants.FONT_SIZE * 0.75, rotation=0)
            constants.screen.blit(inventory_item, (constants.UI_RECT.left + constants.TILE_WIDTH,
                                                   inventory_rect.bottom + constants.TILE_HEIGHT // 2 +
                                                   constants.TILE_HEIGHT * player.inventory.index(item)))

    if prompt_to_render is not None:
        constants.FONT.render_to(constants.screen, prompt_to_render.position,
                                 prompt_to_render.text, prompt_to_render.color, None,
                                 size=constants.FONT_SIZE, rotation=0)
