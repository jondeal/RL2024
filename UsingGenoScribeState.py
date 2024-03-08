import render_ui
import Message
import constants
from State import State


class UsingGenoScribeState(State):
    def __init__(self, game, player):
        super().__init__(game, player)

    def enter(self):
        render_ui.prompt_to_render = Message.Message(constants.PROMPT_RECT,
                                                     'Select a gene to transfer.',
                                                     [255, 255, 255, 255])

    def exit(self):
        pass

    def update(self, events):
        for event in events:
            pass