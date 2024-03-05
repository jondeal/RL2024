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

    genoscribe_window_top_surface, genoscribe_window_top_surface_rect = constants.FONT.render('╭──╮           ╭──╮',
                                                                                              [255, 255, 255, 255],
                                                                                              None,
                                                                                              size=constants.FONT_SIZE,
                                                                                              rotation=0)

    genoscribe_window_top_surface_rect = pygame.Rect(constants.UI_RECT.left, constants.UI_RECT.bottom - constants.TILE_HEIGHT * 8,
                                                     constants.TILE_WIDTH * 19, constants.TILE_HEIGHT)

    genoscribe_window_middle_1_surface, genoscribe_window_middle_1_surface_rect = constants.FONT.render('├──┴─────┬─────┴──┤',
                                                                                                         [255, 255, 255, 255],
                                                                                                         None,
                                                                                                         size=constants.FONT_SIZE,
                                                                                                         rotation=0)

    genoscribe_window_middle_1_surface_rect = pygame.Rect(constants.UI_RECT.left, genoscribe_window_top_surface_rect.bottom - 10,
                                                          constants.TILE_WIDTH * 19, constants.TILE_HEIGHT)

    genoscribe_window_middle_2_surface, genoscribe_window_middle_2_surface_rect = constants.FONT.render('│        │        │',
                                                                                                        [255, 255, 255, 255],
                                                                                                        None,
                                                                                                        size=constants.FONT_SIZE,
                                                                                                        rotation=0)

    genoscribe_window_middle_2_surface_rect = pygame.Rect(constants.UI_RECT.left, genoscribe_window_middle_1_surface_rect.bottom,
                                                          constants.TILE_WIDTH * 19, constants.TILE_HEIGHT)

    genoscribe_window_middle_3_surface, genoscribe_window_middle_3_surface_rect = constants.FONT.render('│        │        │',
                                                                                                        [255, 255, 255, 255],
                                                                                                        None,
                                                                                                        size=constants.FONT_SIZE,
                                                                                                        rotation=0)

    genoscribe_window_middle_3_surface_rect = pygame.Rect(constants.UI_RECT.left, genoscribe_window_middle_2_surface_rect.bottom,
                                                          constants.TILE_WIDTH * 19, constants.TILE_HEIGHT)

    genoscribe_window_middle_4_surface, genoscribe_window_middle_4_surface_rect = constants.FONT.render('│        │        │',
                                                                                                        [255, 255, 255, 255],
                                                                                                        None,
                                                                                                        size=constants.FONT_SIZE,
                                                                                                        rotation=0)

    genoscribe_window_middle_4_surface_rect = pygame.Rect(constants.UI_RECT.left,
                                                          genoscribe_window_middle_3_surface_rect.bottom,
                                                          constants.TILE_WIDTH * 19, constants.TILE_HEIGHT)

    genoscribe_window_bottom_surface, genoscribe_window_bottom_surface_rect = constants.FONT.render('╰────────┴────────╯',
                                                                                                    [255, 255, 255, 255],
                                                                                                    None,
                                                                                                    size=constants.FONT_SIZE,
                                                                                                    rotation=0)

    genoscribe_window_bottom_surface_rect = (constants.UI_RECT.left, genoscribe_window_middle_4_surface_rect.bottom)

    ui_elements_to_render = [(glo_surface, glo_surface_rect),
                             (glo_count_surface, glo_count_surface_rect),
                             (inventory_surface, inventory_surface_rect),
                             (genoscribe_window_top_surface, genoscribe_window_top_surface_rect),
                             (genoscribe_window_middle_1_surface, genoscribe_window_middle_1_surface_rect),
                             (genoscribe_window_middle_2_surface, genoscribe_window_middle_2_surface_rect),
                             (genoscribe_window_middle_3_surface, genoscribe_window_middle_3_surface_rect),
                             (genoscribe_window_middle_4_surface, genoscribe_window_middle_4_surface_rect),
                             (genoscribe_window_bottom_surface, genoscribe_window_bottom_surface_rect)]

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
        prompt_to_render_rect = constants.FONT.get_rect(prompt_to_render.text, rotation=0, size=constants.FONT_SIZE)
        if prompt_to_render_rect.width > constants.PROMPT_RECT.width:
            prompt_to_render_font_size = (constants.PROMPT_RECT.width // len(prompt_to_render.text)) // 0.6
        else:
            prompt_to_render_font_size = constants.FONT_SIZE
        prompt_surface, prompt_surface_rect = constants.FONT.render(prompt_to_render.text,
                                                                    prompt_to_render.color,
                                                                    None,
                                                                    size=prompt_to_render_font_size,
                                                                    rotation=0)
        prompt_surface_rect = (constants.PROMPT_RECT.centerx - prompt_surface_rect.width // 2,
                               constants.PROMPT_RECT.centery - prompt_surface_rect.height // 2)
        ui_elements_to_render.append((prompt_surface, prompt_surface_rect))

    for ui_element in ui_elements_to_render:
        constants.screen.blit(ui_element[0], ui_element[1])
