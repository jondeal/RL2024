import pygame
import controls
import constants
import render_ui
import Message
from PlayerState import PlayerState


class PlayerStateChoosingDirection(PlayerState):
    def __init__(self, game, player):
        super().__init__(game, player)

    def enter(self):
        from PlayerStateApplyingItem import PlayerStateApplyingItem

        if isinstance(self.game.player_state_manager.previous_state, PlayerStateApplyingItem):
            render_ui.prompt_to_render = Message.Message(constants.PROMPT_RECT,
                                                         'Apply the ' + self.player.action_item.glyph +
                                                         self.player.action_item.name +
                                                         ' in which direction?',
                                                         [255, 255, 255, 255])
        self.player.direction = None

    def exit(self):
        for tile in self.game.current_level.tiles:
            if tile.is_highlighted:
                tile.is_highlighted = False
        render_ui.prompt_to_render = None

    def update(self, events):
        from PlayerStateApplyingItem import PlayerStateApplyingItem
        for event in events:
            if event.type == pygame.KEYUP:
                if event.key in controls.direction_keys:
                    self.player.direction = controls.direction_keys[event.key][1]
                    if isinstance(self.game.player_state_manager.previous_state, PlayerStateApplyingItem):
                        if self.player.action_item.name == 'GenoScribe':
                            self.player.apply(self.game, self.player.action_item, self.player.direction)
                        elif self.player.action_item.name == 'YeetStick':
                            points = self.game.current_level.get_points(self.player.position,
                                                                        (self.player.position[0] +
                                                                         self.player.direction[0] * 5,
                                                                         self.player.position[1] +
                                                                         self.player.direction[1] * 5))
                            for tile in self.game.current_level.tiles:
                                if tile.position in points[1:]:
                                    tile.is_highlighted = True
                                else:
                                    tile.is_highlighted = False
                elif event.key == controls.keybinds['confirm']:
                    if self.player.action_item.name == 'YeetStick':
                        if self.player.direction is not None:
                            self.player.apply(self.game, self.player.action_item, self.player.direction)
                        else:
                            render_ui.prompt_to_render = Message.Message(constants.PROMPT_RECT,
                                                                         'You must choose a direction first.',
                                                                         [255, 255, 255, 255])
                elif event.key == controls.keybinds['cancel']:
                    self.game.player_state_manager.change_state(self.game.player_state_manager.previous_state)
