import random


# def update(level):  # example of how to do animation updates for color-shifting glyphs, etc.
#     for tile in level.tiles:
#         if tile.position == (0, 0):
#             randos = ['a', 'b', 'c']
#             tile.glyph = random.choice(randos)


def animate(level):
    if entities_to_animate:
        entity = entities_to_animate[0][0]
        rects_traversed = entities_to_animate[0][1]
        if rects_traversed:
            entity.rect = rects_traversed[0]
            rects_traversed.remove(rects_traversed[0])
        else:
            entities_to_animate.remove(entities_to_animate[0])
            if entity.name == 'force bolt':
                if entity in level.items:
                    level.items.remove(entity)
                else:
                    pass
    else:
        pass


entities_to_animate = []
