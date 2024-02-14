class Tile:
    def __init__(self, name, position, rect, glyph, glyph_rotation, glyph_size, glyph_color, bg_color, is_blocked):
        self.name = name
        self.position = position
        self.rect = rect
        self.glyph = glyph
        self.glyph_rotation = glyph_rotation
        self.glyph_size = glyph_size
        self.glyph_color = glyph_color
        self.bg_color = bg_color
        self.is_blocked = is_blocked
