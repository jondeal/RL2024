class Actor:
    def __init__(self, name, position, rect,
                 glyph, glyph_rotation, glyph_size, glyph_color,
                 direction, speed, mass,
                 glo_count,
                 inventory,
                 action,
                 can_pickup):
        self.name = name
        self.position = position
        self.rect = rect
        self.glyph = glyph
        self.glyph_rotation = glyph_rotation
        self.glyph_size = glyph_size
        self.glyph_color = glyph_color
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
