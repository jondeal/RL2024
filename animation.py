def update():
    if entities_to_animate:
        entity = entities_to_animate[0][0]
        rects_traversed = entities_to_animate[0][1]
        if rects_traversed:
            entity.rect = rects_traversed[0]
            rects_traversed.remove(rects_traversed[0])
        else:
            entities_to_animate.remove(entities_to_animate[0])
    else:
        pass


entities_to_animate = []
