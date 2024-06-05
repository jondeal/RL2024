class Item:
    def __init__(self, name, position, rect,
                 glyph, default_glyph_color, current_glyph_color,
                 glyph_size, glyph_size_modifier, glyph_rotation,
                 direction, speed, mass,
                 inventory,
                 is_selected
                 ):
        self.name = name
        self.position = position
        self.rect = rect
        self.glyph = glyph
        self.default_glyph_color = default_glyph_color
        self.current_glyph_color = current_glyph_color
        self.glyph_size = glyph_size
        self.glyph_size_modifier = glyph_size_modifier
        self.glyph_rotation = glyph_rotation
        self.direction = direction
        self.speed = speed
        self.mass = mass
        self.inventory = inventory
        self.is_selected = is_selected
