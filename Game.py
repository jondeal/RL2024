import Level


class Game:

    def __init__(self, levels, current_level):
        self.levels = levels
        self.current_level = current_level

    def generate_new_level(self):
        new_level = Level.Level([], [])
        new_level.generate_tiles()
        new_level.generate_terrain()
        self.levels.append(new_level)
