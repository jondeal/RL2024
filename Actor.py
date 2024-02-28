class Actor:
    def __init__(self, name, position, rect,
                 glyph, glyph_color, glyph_size, glyph_size_modifier, glyph_rotation,
                 direction, speed, mass,
                 glo_count,
                 inventory,
                 action,
                 can_pickup):
        self.name = name
        self.position = position
        self.rect = rect
        self.glyph = glyph
        self.glyph_color = glyph_color
        self.glyph_size = glyph_size
        self.glyph_size_modifier = glyph_size_modifier
        self.glyph_rotation = glyph_rotation
        self.direction = direction
        self.speed = speed
        self.mass = mass
        self.glo_count = glo_count
        self.inventory = inventory
        self.action = action
        self.can_pickup = can_pickup

    def move(self):
        self.speed = 1
        self.action = 'push'

    def shove(self):
        self.speed = 1
        self.action = 'shove'

    def pickup(self, current_level):
        for item in current_level.items:
            if item.position == self.position:
                self.inventory.append(item)
                current_level.items.remove(item)
