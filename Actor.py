import render_ui
import ui_prompts
from PlayerStateChoosingAction import PlayerStateChoosingAction
from PlayerStateUsingGenoScribe import PlayerStateUsingGenoScribe


class Actor:
    def __init__(self, name, position, rect,
                 glyph, default_glyph_color, current_glyph_color,
                 glyph_size, glyph_size_modifier, glyph_rotation,
                 dormant_glyph, dormant_glyph_color, is_dormant,
                 direction, speed, mass,
                 glo_count,
                 inventory,
                 genome,
                 action, action_item,
                 abilities,
                 turn_complete
                 ):
        self.name = name
        self.position = position
        self.rect = rect
        self.glyph = glyph
        self.default_glyph_color = default_glyph_color
        self.current_glyph_color = current_glyph_color
        self.glyph_size = glyph_size
        self.glyph_size_modifier = glyph_size_modifier
        self.glyph_rotation = glyph_rotation
        self.dormant_glyph = dormant_glyph
        self.dormant_glyph_color = dormant_glyph_color
        self.is_dormant = is_dormant
        self.direction = direction
        self.speed = speed
        self.mass = mass
        self.glo_count = glo_count
        self.inventory = inventory
        self.genome = genome
        self.action = action
        self.action_item = action_item
        self.abilities = abilities
        self.turn_complete = turn_complete

    def move(self, current_level):
        if self.name == 'player':
            for tile in current_level.tiles:
                if tile.position == (self.position[0] + self.direction[0], self.position[1] + self.direction[1]):
                    if tile.name == 'wall':
                        render_ui.prompt_to_render = ui_prompts.wall_prompt
                    else:
                        self.speed = 1
                        self.action = 'push'
                        self.turn_complete = True
        else:
            self.speed = 1
            self.action = 'push'
            self.turn_complete = True

    def shove(self, current_level):
        if self.name == 'player':
            for tile in current_level.tiles:
                if tile.position == (self.position[0] + self.direction[0], self.position[1] + self.direction[1]):
                    if tile.name == 'wall':
                        render_ui.prompt_to_render = ui_prompts.wall_prompt
                    else:
                        self.speed = 1
                        self.action = 'shove'
                        self.turn_complete = True
        else:
            self.speed = 1
            self.action = 'shove'
            self.turn_complete = True

    def pickup(self, current_level):
        for item in current_level.items:
            if item.position == self.position:
                if item.name != 'GenoQuery':
                    self.inventory.append(item)
                    item.position = None
                    current_level.items.remove(item)
        self.turn_complete = True

    def drop(self, game, current_level, item_to_drop):
        item_to_drop.position = self.position
        item_to_drop.rect = self.rect.copy()
        self.inventory.remove(item_to_drop)
        current_level.items.append(item_to_drop)
        if self.name == 'player':
            game.player_state_manager.change_state(PlayerStateChoosingAction(game, self))
        self.turn_complete = True

    def apply(self, game, item_to_apply, direction_to_apply):
        if item_to_apply.name == 'GenoScribe':
            for actor in game.current_level.actors:
                if actor.position == (self.position[0] + direction_to_apply[0],
                                      self.position[1] + direction_to_apply[1]):
                    game.player_state_manager.change_state(PlayerStateUsingGenoScribe(game, self, actor))
        if item_to_apply.name == 'YeetStick':
            for tile in game.current_level.tiles:
                if tile.position == self.position:
                    game.current_level.spawn_item('force bolt', tile)
                    game.current_level.items[-1].direction = self.direction
                    game.current_level.items[-1].speed = 5
                    directions = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
                    for direction in directions:
                        if game.current_level.items[-1].direction == direction:
                            game.current_level.items[-1].glyph_rotation = 45 * directions.index(direction)
            if self.name == 'player':
                game.player_state_manager.change_state(PlayerStateChoosingAction(game, self))
            self.turn_complete = True
