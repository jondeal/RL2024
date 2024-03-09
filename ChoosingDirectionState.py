import pygame
import controls
import constants
import render_ui
import Message
from State import State


class ChoosingDirectionState(State):
    def __init__(self, game, player):
        super().__init__(game, player)

    def enter(self):
        from ApplyingItemState import ApplyingItemState

        if isinstance(self.game.state_manager.previous_state, ApplyingItemState):
            render_ui.prompt_to_render = Message.Message(constants.PROMPT_RECT,
                                                         'Apply the ' + self.player.action_item.glyph +
                                                         self.player.action_item.name +
                                                         ' in which direction?',
                                                         [255, 255, 255, 255])

    def exit(self):
        pass

    def update(self, events):
        from ApplyingItemState import ApplyingItemState
        for event in events:
            if event.type == pygame.KEYUP:
                if event.key in controls.direction_keys:
                    self.player.direction = controls.direction_keys[event.key][1]
                    if isinstance(self.game.state_manager.previous_state, ApplyingItemState):
                        self.player.apply(self.game, self.player.action_item, self.player.direction)
