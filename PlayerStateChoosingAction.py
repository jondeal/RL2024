import pygame
import controls
import render_ui
from PlayerState import PlayerState
from PlayerStateApplyingItem import PlayerStateApplyingItem
from PlayerStateDroppingItem import PlayerStateDroppingItem


class PlayerStateChoosingAction(PlayerState):
    def __init__(self, game, player):
        super().__init__(game, player)

    def enter(self):
        pass

    def exit(self):
        pass

    def update(self, events):
        for event in events:
            if event.type == pygame.KEYUP:
                if event.key == controls.keybinds['mod key']:
                    pass
                else:
                    render_ui.prompt_to_render = None
                    if event.key in controls.direction_keys:
                        self.player.direction = controls.direction_keys[event.key][1]
                        keys = pygame.key.get_pressed()
                        if keys[controls.keybinds['mod key']]:
                            self.player.shove(self.game.current_level)
                        else:
                            self.player.move(self.game.current_level)
                    elif event.key == controls.keybinds['pickup']:
                        self.player.pickup(self.game.current_level)
                    elif event.key == controls.keybinds['drop']:
                        self.game.player_state_manager.change_state(PlayerStateDroppingItem(self.game, self.player))
                    elif event.key == controls.keybinds['apply']:
                        self.game.player_state_manager.change_state(PlayerStateApplyingItem(self.game, self.player))
