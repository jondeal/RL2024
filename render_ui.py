import pygame
import constants

prompt_to_render = None


def render_ui(player):
    constants.screen.fill(constants.SCREEN_COLOR)

    glo_surface, glo_surface_rect = constants.FONT.render('﹝GLO﹞',
                                                  [255, 255, 255, 255],
                                                  None,
                                                  size=constants.FONT_SIZE,
                                                  rotation=0)
    glo_surface_rect.topleft = constants.UI_RECT.topleft

    glo_count_surface, glo_count_surface_rect = constants.FONT.render('✻' + str(player.glo_count),
                                                                      'cyan',
                                                                      None,
                                                                      size=constants.FONT_SIZE,
                                                                      rotation=0)
    glo_count_surface_rect = (glo_surface_rect.right + constants.TILE_WIDTH // 2,
                              glo_surface_rect.height // 4 - glo_count_surface_rect.height // 4)

    inventory_surface, inventory_surface_rect = constants.FONT.render('﹝INVENTORY﹞',
                                                                      [255, 255, 255, 255],
                                                                      None,
                                                                      size=constants.FONT_SIZE,
                                                                      rotation=0)
    inventory_surface_rect.topleft = glo_surface_rect.bottomleft

    ui_elements_to_render = [(glo_surface, glo_surface_rect),
                             (glo_count_surface, glo_count_surface_rect),
                             (inventory_surface, inventory_surface_rect)]

    if player.inventory:
        for item in player.inventory:
            inventory_item_glyph_surface, inventory_item_glyph_rect = constants.FONT.render(
                item.inventory_slot[1] + ': ' + item.glyph + ' ' + item.name,
                [255, 255, 0, 255],
                None,
                size=constants.FONT_SIZE * 0.75,
                rotation=0)
            inventory_item_glyph_rect = (inventory_surface_rect.left,
                                         inventory_surface_rect.bottom +
                                         constants.TILE_HEIGHT * player.inventory.index(item))
            ui_elements_to_render.append((inventory_item_glyph_surface, inventory_item_glyph_rect))

    if prompt_to_render is not None:
        prompt_surface, prompt_surface_rect = constants.FONT.render(prompt_to_render.text,
                                                                    prompt_to_render.color,
                                                                    None,
                                                                    size=constants.FONT_SIZE,
                                                                    rotation=0)
        prompt_surface_rect = (constants.LEVEL_RECT.centerx - prompt_surface_rect.width // 2,
                               constants.LEVEL_RECT.bottom)
        ui_elements_to_render.append((prompt_surface, prompt_surface_rect))

    for ui_element in ui_elements_to_render:
        constants.screen.blit(ui_element[0], ui_element[1])
