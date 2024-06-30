class Animation:
    def __init__(self, entity_to_animate,
                 entity_to_animate_direction,
                 start_rect, end_rect,
                 current_frame, total_frames,
                 animation_to_apply,
                 is_done
                 ):
        self.entity_to_animate = entity_to_animate
        self.entity_to_animate_direction = entity_to_animate_direction
        self.start_rect = start_rect
        self.end_rect = end_rect
        self.current_frame = current_frame
        self.total_frames = total_frames
        self.animation_to_apply = animation_to_apply
        self.is_done = is_done

    def update(self):
        if self.entity_to_animate.name == 'force bolt':
            directions = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
            for direction in directions:
                if self.entity_to_animate_direction == direction:
                    self.entity_to_animate.glyph_rotation = 45 * directions.index(direction)
        if self.animation_to_apply == 'move':
            x_diff = self.end_rect.centerx - self.start_rect.centerx
            y_diff = self.end_rect.centery - self.start_rect.centery

            x_move = x_diff / self.total_frames
            y_move = y_diff / self.total_frames

            if self.current_frame <= self.total_frames:
                self.entity_to_animate.rect.centerx = self.entity_to_animate.rect.centerx + x_move
                self.entity_to_animate.rect.centery = self.entity_to_animate.rect.centery + y_move

        elif self.animation_to_apply == 'shake':
            if self.current_frame % 2 == 0:
                self.entity_to_animate.rect.centerx += 5
            elif self.current_frame % 2 == 1:
                self.entity_to_animate.rect.centerx -= 5

        if self.current_frame == self.total_frames:
            self.is_done = True
            # self.entity_to_animate.rect.center = self.end_rect.center
        else:
            self.current_frame += 1
