import random
import pygame

import Item
import constants
import Tile
import Actor
import actor_templates
import item_templates
import tile_templates


class Level:
    def __init__(self, tiles, actors, items):
        self.tiles = tiles
        self.actors = actors
        self.items = items

    def get_random_open_tile(self):
        open_tiles = []
        for tile in self.tiles:
            if tile.name != 'wall':
                open_tiles.append(tile)
            for actor in self.actors:
                if actor.position == tile.position:
                    open_tiles.remove(tile)
            for item in self.items:
                if item.position == tile.position:
                    open_tiles.remove(tile)
        random_open_tile = random.choice(open_tiles)
        return random_open_tile

    def generate_terrain(self):
        # generates a grid of floor tiles
        for i in range(constants.X_RANGE):
            x = i
            for i_2 in range(constants.Y_RANGE):
                y = i_2
                # assigns rect vertices to each tile during creation
                # x_1 = x * constants.TILE_WIDTH
                # y_1 = y * constants.TILE_HEIGHT
                # tile_rect = pygame.Rect((x_1, y_1), (constants.TILE_WIDTH, constants.TILE_HEIGHT))
                tile_rect = pygame.Rect(constants.LEVEL_RECT.left + x * constants.TILE_WIDTH,
                                        constants.LEVEL_RECT.top + y * constants.TILE_HEIGHT,
                                        constants.TILE_WIDTH,
                                        constants.TILE_HEIGHT)

                new_tile = Tile.Tile('floor', (x, y), tile_rect,
                                     None, None, constants.FONT_SIZE, None, 0,
                                     None, None)

                self.tiles.append(new_tile)
        # this makes border walls
        for tile in self.tiles:
            if (tile.position[0] == 0 or tile.position[0] == constants.X_RANGE - 1
                    or tile.position[1] == 0 or tile.position[1] == constants.Y_RANGE - 1):
                tile.name = 'wall'

    def define_terrain(self):
        for tile in self.tiles:
            for template in tile_templates.tile_templates:
                if template['name'] == tile.name:
                    tile.glyph = template['glyph']
                    tile.glyph_color = template['glyph_color']
                    tile.glyph_size_modifier = template['glyph_size_modifier']
                    tile.bg_color = (
                        template['bg_base_rgba'][0] + random.randrange(template['bg_rgb_range'][0][0], template['bg_rgb_range'][0][1]),
                        template['bg_base_rgba'][1] + random.randrange(template['bg_rgb_range'][1][0], template['bg_rgb_range'][1][1]),
                        template['bg_base_rgba'][2] + random.randrange(template['bg_rgb_range'][2][0], template['bg_rgb_range'][2][1]),
                        template['bg_base_rgba'][3]
                    )
                    tile.is_blocked = template['is_blocked']

    def spawn_actor(self, actor_type, destination):
        for template in actor_templates.actor_templates:
            if template['name'] == actor_type:
                new_actor = Actor.Actor(template['name'],
                                        destination.position, destination.rect,
                                        template['glyph'], template['glyph_color'],
                                        constants.FONT_SIZE, template['glyph_size_modifier'], 0,
                                        (0, 0), 0, template['mass'],
                                        template['glo_count'],
                                        [],
                                        None,
                                        template['can_pickup'])
                self.actors.append(new_actor)

    def spawn_terrain(self, terrain_name, limit):
        terrain_count = 0

        # turns random unblocked tiles into walls
        while terrain_count < limit:
            random_tile = self.get_random_open_tile()
            for template in tile_templates.tile_templates:
                if template['name'] == terrain_name:
                    random_tile.name = template['name']
            terrain_count += 1

    def spawn_item(self, item_name, destination):
        for template in item_templates.item_templates:
            if template['name'] == item_name:
                new_item = Item.Item(template['name'],
                                     destination.position, destination.rect,
                                     template['glyph'], template['glyph_color'],
                                     constants.FONT_SIZE, template['glyph_size_modifier'], template['glyph_rotation'],
                                     (0, 0), 0, template['mass'],
                                     None)
                self.items.append(new_item)
