import pygame
import constants

prompt_to_render = None
genome_to_render = None

genoscribe_window_left_nub_surface_rect = None
genoscribe_window_right_nub_surface_rect = None


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

    global genoscribe_window_left_nub_surface_rect

    genoscribe_window_left_nub_surface, genoscribe_window_left_nub_surface_rect = constants.FONT.render('╭──╮',
                                                                                                        [255, 255, 255, 255],
                                                                                                        None,
                                                                                                        size=constants.FONT_SIZE,
                                                                                                        rotation=0)

    genoscribe_window_left_nub_surface_rect = pygame.Rect(constants.GENOSCRIBE_WINDOW_RECT.left,
                                                          constants.GENOSCRIBE_WINDOW_RECT.top,
                                                          genoscribe_window_left_nub_surface_rect.width,
                                                          genoscribe_window_left_nub_surface_rect.height)

    global genoscribe_window_right_nub_surface_rect

    genoscribe_window_right_nub_surface, genoscribe_window_right_nub_surface_rect = constants.FONT.render('╭──╮',
                                                                                                          [255, 255, 255, 255],
                                                                                                          None,
                                                                                                          size=constants.FONT_SIZE,
                                                                                                          rotation=0)

    genoscribe_window_right_nub_surface_rect = pygame.Rect(constants.GENOSCRIBE_WINDOW_RECT.right - genoscribe_window_right_nub_surface_rect.width,
                                                           constants.GENOSCRIBE_WINDOW_RECT.top,
                                                           genoscribe_window_right_nub_surface_rect.width,
                                                           genoscribe_window_right_nub_surface_rect.height)

    genoscribe_window_left_middle_1_surface, genoscribe_window_left_middle_1_surface_rect = constants.FONT.render('├──┴─────┬',
                                                                                                                  [255, 255, 255, 255],
                                                                                                                  None,
                                                                                                                  size=constants.FONT_SIZE,
                                                                                                                  rotation=0)

    genoscribe_window_left_middle_1_surface_rect = pygame.Rect(constants.GENOSCRIBE_WINDOW_RECT.left,
                                                               genoscribe_window_left_nub_surface_rect.bottom,
                                                               genoscribe_window_left_middle_1_surface_rect.width,
                                                               genoscribe_window_left_middle_1_surface_rect.height)

    genoscribe_window_right_middle_1_surface, genoscribe_window_right_middle_1_surface_rect = constants.FONT.render('┬─────┴──┤',
                                                                                                                    [255, 255, 255, 255],
                                                                                                                    None,
                                                                                                                    size=constants.FONT_SIZE,
                                                                                                                    rotation=0)

    genoscribe_window_right_middle_1_surface_rect = pygame.Rect(constants.GENOSCRIBE_WINDOW_RECT.right - genoscribe_window_right_middle_1_surface_rect.width,
                                                                genoscribe_window_right_nub_surface_rect.bottom,
                                                                genoscribe_window_right_middle_1_surface_rect.width,
                                                                genoscribe_window_right_middle_1_surface_rect.height)

    genoscribe_window_left_middle_2_surface, genoscribe_window_left_middle_2_surface_rect = constants.FONT.render('│        │',
                                                                                                                  [255, 255, 255, 255],
                                                                                                                  None,
                                                                                                                  size=constants.FONT_SIZE,
                                                                                                                  rotation=0)

    genoscribe_window_left_middle_2_surface_rect = pygame.Rect(constants.GENOSCRIBE_WINDOW_RECT.left,
                                                               genoscribe_window_left_middle_1_surface_rect.bottom,
                                                               genoscribe_window_left_middle_2_surface_rect.width,
                                                               genoscribe_window_left_middle_2_surface_rect.height)

    genoscribe_window_right_middle_2_surface, genoscribe_window_right_middle_2_surface_rect = constants.FONT.render('│        │',
                                                                                                                    [255, 255, 255, 255],
                                                                                                                    None,
                                                                                                                    size=constants.FONT_SIZE,
                                                                                                                    rotation=0)

    genoscribe_window_right_middle_2_surface_rect = pygame.Rect(constants.GENOSCRIBE_WINDOW_RECT.right - genoscribe_window_right_middle_2_surface_rect.width,
                                                                genoscribe_window_right_middle_1_surface_rect.bottom,
                                                                genoscribe_window_left_middle_2_surface_rect.width,
                                                                genoscribe_window_right_middle_2_surface_rect.height)

    genoscribe_window_left_middle_3_surface, genoscribe_window_left_middle_3_surface_rect = constants.FONT.render('│        │',
                                                                                                                  [255, 255, 255, 255],
                                                                                                                  None,
                                                                                                                  size=constants.FONT_SIZE,
                                                                                                                  rotation=0)

    genoscribe_window_left_middle_3_surface_rect = pygame.Rect(constants.GENOSCRIBE_WINDOW_RECT.left,
                                                               genoscribe_window_left_middle_2_surface_rect.bottom,
                                                               genoscribe_window_left_middle_3_surface_rect.width,
                                                               genoscribe_window_left_middle_3_surface_rect.height)

    genoscribe_window_right_middle_3_surface, genoscribe_window_right_middle_3_surface_rect = constants.FONT.render('│        │',
                                                                                                                    [255, 255, 255, 255],
                                                                                                                    None,
                                                                                                                    size=constants.FONT_SIZE,
                                                                                                                    rotation=0)

    genoscribe_window_right_middle_3_surface_rect = pygame.Rect(constants.GENOSCRIBE_WINDOW_RECT.right - genoscribe_window_right_middle_3_surface_rect.width,
                                                                genoscribe_window_right_middle_2_surface_rect.bottom,
                                                                genoscribe_window_right_middle_3_surface_rect.width,
                                                                genoscribe_window_right_middle_3_surface_rect.height)

    genoscribe_window_left_bottom_surface, genoscribe_window_left_bottom_surface_rect = constants.FONT.render('╰────────┴',
                                                                                                              [255, 255, 255, 255],
                                                                                                              None,
                                                                                                              size=constants.FONT_SIZE,
                                                                                                              rotation=0)

    genoscribe_window_left_bottom_surface_rect = pygame.Rect(constants.GENOSCRIBE_WINDOW_RECT.left,
                                                             genoscribe_window_left_middle_3_surface_rect.bottom,
                                                             genoscribe_window_left_bottom_surface_rect.width,
                                                             genoscribe_window_left_bottom_surface_rect.height)

    genoscribe_window_right_bottom_surface, genoscribe_window_right_bottom_surface_rect = constants.FONT.render('┴────────╯',
                                                                                                                [255, 255, 255, 255],
                                                                                                                None,
                                                                                                                size=constants.FONT_SIZE,
                                                                                                                rotation=0)

    genoscribe_window_right_bottom_surface_rect = pygame.Rect(constants.GENOSCRIBE_WINDOW_RECT.right - genoscribe_window_right_bottom_surface_rect.width,
                                                              genoscribe_window_right_middle_3_surface_rect.bottom,
                                                              genoscribe_window_right_bottom_surface_rect.width,
                                                              genoscribe_window_right_bottom_surface_rect.height)

    ui_elements_to_render = [(glo_surface, glo_surface_rect),
                             (glo_count_surface, glo_count_surface_rect),
                             (inventory_surface, inventory_surface_rect),
                             (genoscribe_window_left_nub_surface, genoscribe_window_left_nub_surface_rect),
                             (genoscribe_window_right_nub_surface, genoscribe_window_right_nub_surface_rect),
                             (genoscribe_window_left_middle_1_surface, genoscribe_window_left_middle_1_surface_rect),
                             (genoscribe_window_right_middle_1_surface, genoscribe_window_right_middle_1_surface_rect),
                             (genoscribe_window_left_middle_2_surface, genoscribe_window_left_middle_2_surface_rect),
                             (genoscribe_window_right_middle_2_surface, genoscribe_window_right_middle_2_surface_rect),
                             (genoscribe_window_left_middle_3_surface, genoscribe_window_left_middle_3_surface_rect),
                             (genoscribe_window_right_middle_3_surface, genoscribe_window_right_middle_3_surface_rect),
                             (genoscribe_window_left_bottom_surface, genoscribe_window_left_bottom_surface_rect),
                             (genoscribe_window_right_bottom_surface, genoscribe_window_right_bottom_surface_rect)]

    if player.inventory:
        for item in player.inventory:
            if item.is_selected:
                bg_color = [100, 100, 100, 255]
            else:
                bg_color = None
            inventory_item_glyph_surface, inventory_item_glyph_rect = constants.FONT.render(
                item.glyph + ' ' + item.name,
                [255, 255, 0, 255],
                bg_color,
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

    if genome_to_render is not None:
        render_genes(genome_to_render[0], genome_to_render[1], player)


def render_genes(actor, actor_genome, player):
    genoscribe_glyph_surface, genoscribe_glyph_rect = constants.FONT.render('⚨',
                                                                            [255, 255, 0, 255],
                                                                            None,
                                                                            size=constants.FONT_SIZE * 2,
                                                                            rotation=0)

    genoscribe_glyph_rect.center = (genoscribe_window_left_nub_surface_rect.centerx,
                                    genoscribe_window_left_nub_surface_rect.top +
                                    genoscribe_window_left_nub_surface_rect.height +
                                    genoscribe_window_left_nub_surface_rect.height // 10)

    constants.screen.blit(genoscribe_glyph_surface, genoscribe_glyph_rect)

    glyph = None
    glyph_color = None

    if actor.is_dormant:
        glyph = actor.dormant_glyph
        glyph_color = actor.dormant_glyph_color
    else:
        glyph = actor.glyph
        glyph_color = actor.glyph_color

    genome_actor_surface, genome_actor_surface_rect = constants.FONT.render(glyph,
                                                                            glyph_color,
                                                                            None,
                                                                            size=constants.FONT_SIZE * 2,
                                                                            rotation=0)

    genome_actor_surface_rect.center = (genoscribe_window_right_nub_surface_rect.centerx,
                                        genoscribe_window_right_nub_surface_rect.top +
                                        genoscribe_window_right_nub_surface_rect.height +
                                        genoscribe_window_right_nub_surface_rect.height // 10)

    constants.screen.blit(genome_actor_surface, genome_actor_surface_rect)

    for gene in actor_genome:
        if gene.is_selected is True:
            bg_color = [100, 100, 100, 255]
        else:
            bg_color = None
        gene_surface, gene_rect = constants.FONT.render('§ ' + gene.name,
                                                        [255, 255, 255, 255],
                                                        bg_color,
                                                        size=constants.FONT_SIZE * 0.5,
                                                        rotation=0)

        gene_rect = (constants.GENOSCRIBE_WINDOW_RECT.centerx + constants.FONT_SIZE * 0.5,
                     constants.GENOSCRIBE_WINDOW_RECT.top +
                     actor_genome.index(gene) * constants.TILE_HEIGHT // 2 + constants.TILE_HEIGHT * 2)

        constants.screen.blit(gene_surface, gene_rect)

    if player.action_item and player.action_item.name == 'GenoScribe':
        if player.action_item.inventory:
            for gene in player.action_item.inventory:
                if gene.is_selected is True:
                    bg_color = [100, 100, 100, 255]
                else:
                    bg_color = None
                gene_surface, gene_rect = constants.FONT.render('§ ' + gene.name,
                                                                [255, 255, 255, 255],
                                                                bg_color,
                                                                size=constants.FONT_SIZE * 0.5,
                                                                rotation=0)

                gene_rect = (constants.GENOSCRIBE_WINDOW_RECT.left + constants.FONT_SIZE * 0.5,
                             constants.GENOSCRIBE_WINDOW_RECT.top +
                             player.action_item.inventory.index(gene) * constants.TILE_HEIGHT // 2 +
                             constants.TILE_HEIGHT * 2)

                constants.screen.blit(gene_surface, gene_rect)
