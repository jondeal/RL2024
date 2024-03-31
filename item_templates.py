import random

item_templates = [
    {'name': 'GenoScribe',
     'glyph': '⚨',
     'default_glyph_color': [255, 255, 0, 255],
     'glyph_size_modifier': 1,
     'glyph_rotation': random.randrange(8) * 45,
     'mass': 1,
     'inventory': []
     },
    {'name': 'YeetStick',
     'glyph': '⇞',
     'default_glyph_color': [255, 255, 0, 255],
     'glyph_size_modifier': 1,
     'glyph_rotation': random.randrange(8) * 45,
     'mass': 1,
     'inventory': None
     },
    {'name': 'GenoQuery',
     'glyph': '⌂',
     'default_glyph_color': [255, 255, 0, 255],
     'glyph_size_modifier': 1.75,
     'glyph_rotation': 0,
     'mass': 3,
     'inventory': None
     },
    {'name': 'force bolt',
     'glyph': 'ᛵ',
     'default_glyph_color': [255, 255, 255, 255],
     'glyph_size_modifier': 1,
     'glyph_rotation': 0,
     'mass': 1,
     'inventory': None
     }
]
