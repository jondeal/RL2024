import random
import pygame
import constants
import Tile
import Actor
import actor_templates
import tile_templates


class Level:
    def __init__(self, tiles, actors):
        self.tiles = tiles
        self.actors = actors

    def get_random_open_tile(self):
        open_tiles = []
        for tile in self.tiles:
            if tile.is_blocked is not True:
                open_tiles.append(tile)
            for actor in self.actors:
                if (actor.x, actor.y) == (tile.x, tile.y):
                    open_tiles.remove(tile)
        random_open_tile = random.choice(open_tiles)
        return random_open_tile

    def generate_tiles(self):
        # generates a grid of floor tiles
        for i in range(constants.X_RANGE):
            x = i
            for i_2 in range(constants.Y_RANGE):
                y = i_2
                # assigns rect vertices to each tile during creation
                x_1 = x * constants.TILE_WIDTH
                y_1 = y * constants.TILE_HEIGHT
                tile_rect = pygame.Rect((x_1, y_1), (constants.TILE_WIDTH, constants.TILE_HEIGHT))

                new_tile = Tile.Tile('floor', x, y, tile_rect,
                                     None, 0, constants.FONT_SIZE, None,
                                     None, None)

                self.tiles.append(new_tile)
        # this makes border walls
        for tile in self.tiles:
            if tile.x == 0 or tile.x == constants.X_RANGE - 1 or tile.y == 0 or tile.y == constants.Y_RANGE - 1:
                tile.name = 'wall'

    def generate_terrain(self):
        for tile in self.tiles:
            for template in tile_templates.tile_templates:
                if template['name'] == tile.name:
                    tile.glyph = template['glyph']
                    tile.glyph_color = template['glyph_color']
                    tile.bg_color = (
                        template['bg_base_rgba'][0] + random.randrange(template['bg_rgb_range'][0][0], template['bg_rgb_range'][0][1]),
                        template['bg_base_rgba'][1] + random.randrange(template['bg_rgb_range'][1][0], template['bg_rgb_range'][1][1]),
                        template['bg_base_rgba'][2] + random.randrange(template['bg_rgb_range'][2][0], template['bg_rgb_range'][2][1]),
                        template['bg_base_rgba'][3]
                    )
                    tile.is_blocked = template['is_blocked']

    def spawn_actor(self, actor_type, location):
        for template in actor_templates.actor_templates:
            if template['name'] == actor_type:
                new_actor = Actor.Actor(template['name'], location.x, location.y, location.rect,
                                        template['glyph'], 0, constants.FONT_SIZE,
                                        template['glyph_color'], None,
                                        0, 0)
                self.actors.append(new_actor)
