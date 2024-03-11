import pygame
import render_ui
import Message
import constants
import controls
from State import State
from ChoosingDirectionState import ChoosingDirectionState


class ApplyingItemState(State):
    def __init__(self, game, player):
        super().__init__(game, player)

    def enter(self):
        if self.player.inventory:
            render_ui.prompt_to_render = Message.Message(constants.PROMPT_RECT,
                                                         'Select an item to apply.', [255, 255, 255, 255])
            self.player.inventory[0].is_selected = True
        else:
            render_ui.prompt_to_render = Message.Message(constants.PROMPT_RECT,
                                                         'You have nothing to apply.', [255, 255, 255, 255])
            self.game.state_manager.change_state(self.game.state_manager.previous_state)

    def exit(self):
        pass

    def update(self, events):
        from ChoosingActionState import ChoosingActionState
        for event in events:
            if event.type == pygame.KEYUP:
                direction_keys_list = list(controls.direction_keys.keys())
                selected_item_index = 0
                for item in self.player.inventory:
                    if item.is_selected is True:
                        selected_item_index = self.player.inventory.index(item)
                if event.key == direction_keys_list[1]:  # up
                    if selected_item_index == 0:
                        selected_item_index = self.player.inventory.index(self.player.inventory[-1])
                    else:
                        selected_item_index -= 1
                elif event.key == direction_keys_list[7]:  # down
                    if selected_item_index == self.player.inventory.index(self.player.inventory[-1]):
                        selected_item_index = self.player.inventory.index(self.player.inventory[0])
                    else:
                        selected_item_index += 1
                elif event.key == controls.keybinds['confirm']:
                    for item in self.player.inventory:
                        if self.player.inventory.index(item) == selected_item_index:
                            self.player.action_item = item
                    for item in self.player.inventory:
                        item.is_selected = False
                    selected_item_index = None
                    render_ui.prompt_to_render = None
                    self.game.state_manager.change_state(ChoosingDirectionState(self.game, self.player))
                elif event.key == controls.keybinds['escape']:
                    render_ui.prompt_to_render = None
                    selected_item_index = None
                    self.game.state_manager.change_state(ChoosingActionState(self.game, self.player))
                for item in self.player.inventory:
                    if self.player.inventory.index(item) == selected_item_index:
                        item.is_selected = True
                    else:
                        item.is_selected = False
