animation_events = []


def animate(level):
    for animation_event in animation_events:
        if animation_event.is_done is False:
            animation_event.update()
        else:
            pass
