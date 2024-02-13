class Actor:
    def __init__(self, name, x, y, rect,
                 glyph, glyph_rotation, glyph_size,
                 glyph_color, bg_color,
                 direction, impulse):
        self.name = name
        self.x = x
        self.y = y
        self.rect = rect
        self.glyph = glyph
        self.glyph_rotation = glyph_rotation
        self.glyph_size = glyph_size
        self.glyph_color = glyph_color
        self.bg_color = bg_color
        self.direction = direction
        self.impulse = impulse
