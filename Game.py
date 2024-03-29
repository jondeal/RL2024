import Level


class Game:

    def __init__(self, levels, current_level, state_manager):
        self.levels = levels
        self.current_level = current_level
        self.state_manager = state_manager

    def generate_new_level(self):
        new_level = Level.Level([], [], [])
        new_level.generate_terrain()
        new_level.spawn_terrain('wall', 10)
        new_level.define_terrain()
        self.levels.append(new_level)
