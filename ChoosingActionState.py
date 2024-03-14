import pygame
import controls
import render_ui
from State import State
from DroppingItemState import DroppingItemState
from ApplyingItemState import ApplyingItemState


class ChoosingActionState(State):
    def __init__(self, game, player):
        super().__init__(game, player)

    def enter(self):
        render_ui.prompt_to_render = None

    def exit(self):
        pass

    def update(self, events):
        for event in events:
            if event.type == pygame.KEYUP:
                render_ui.prompt_to_render = None
                if event.key in controls.direction_keys:
                    self.player.direction = controls.direction_keys[event.key][1]
                    self.player.move()
                    if event.mod == controls.keybinds['mod key']:
                        self.player.shove()
                elif event.key == controls.keybinds['pickup']:
                    self.player.pickup(self.game.current_level)
                elif event.key == controls.keybinds['drop']:
                    self.game.state_manager.change_state(DroppingItemState(self.game, self.player))
                elif event.key == controls.keybinds['apply']:
                    self.game.state_manager.change_state(ApplyingItemState(self.game, self.player))
