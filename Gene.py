class Gene:
    def __init__(self, name, ability, is_selected):
        self.name = name
        self.ability = ability
        self.is_selected = is_selected

    def __lt__(self, other):
        return self.name < other.name
