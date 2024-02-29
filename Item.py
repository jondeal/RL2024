class Item:
    def __init__(self, name, position, rect,
                 glyph, glyph_color, glyph_size, glyph_size_modifier, glyph_rotation,
                 direction, speed, mass,
                 inventory_slot):
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
        self.inventory_slot = inventory_slot
