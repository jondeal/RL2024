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

    def pickup(self, game, current_level):
        for item in current_level.items:
            if item.position == self.position:
                if self.name == 'player':
                    item.inventory_slot = game.inventory_slots[0]
                    game.inventory_slots.remove(item.inventory_slot)
                self.inventory.append(item)
                item.position = None
                current_level.items.remove(item)

    def drop(self, game, current_level, item_to_drop):
        item_to_drop.position = self.position
        item_to_drop.rect = self.rect
        self.inventory.remove(item_to_drop)
        current_level.items.append(item_to_drop)
        if self.name == 'player':
            game.inventory_slots.append(item_to_drop.inventory_slot)
            game.inventory_slots.sort()
            item_to_drop.inventory_slot = None
            game.state = 'choosing action'

