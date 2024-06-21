from GameState import GameState
import physics


class GameStateResolvingPhysics(GameState):
    def __init__(self, game, player):
        super().__init__(game)
        self.player = player

    def enter(self):
        pass

    def exit(self):
        pass

    def update(self, events):
        from GameStateWaitingForInput import GameStateWaitingForInput
        physics_resolved = False
        while physics_resolved is False:
            if physics.resolve_physics(self.game.current_level) is True:
                physics_resolved = True
                self.game.game_state_manager.change_state(GameStateWaitingForInput(self.game, self.player))
            else:
                continue
        else:
            pass
