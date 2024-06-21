from GameState import GameState
from GameStateResolvingPhysics import GameStateResolvingPhysics


class GameStateWaitingForInput(GameState):
    def __init__(self, game, player):
        super().__init__(game)
        self.player = player

    def enter(self):
        pass

    def exit(self):
        pass

    def update(self, events):
        if self.player.turn_complete is False:
            self.game.player_state_manager.update(events)
        else:
            for actor in self.game.current_level.actors[1:]:
                if 'can_move' in actor.abilities:
                    neighboring_tile = self.game.current_level.get_random_open_neighboring_tile(actor)
                    actor.direction = (neighboring_tile.position[0] - actor.position[0],
                                       neighboring_tile.position[1] - actor.position[1])
                    if actor.direction == (0, 0):  # DEBUG
                        actor.current_glyph_color = [0, 0, 255, 255]
                    else:
                        actor.current_glyph_color = actor.default_glyph_color
                    actor.move(self.game.current_level)
                else:
                    pass
            self.player.turn_complete = False
            self.game.game_state_manager.change_state(GameStateResolvingPhysics(self.game, self.player))
