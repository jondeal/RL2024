import pygame
import Level


class Game:

    inventory_slots = [(pygame.K_a, 'a'), (pygame.K_b, 'b'), (pygame.K_c, 'c'), (pygame.K_d, 'd'), (pygame.K_e, 'e'),
                       (pygame.K_f, 'f'), (pygame.K_g, 'g'), (pygame.K_h, 'h'), (pygame.K_i, 'i'), (pygame.K_j, 'j'),
                       (pygame.K_k, 'k'), (pygame.K_l, 'l'), (pygame.K_m, 'm'), (pygame.K_n, 'n'), (pygame.K_o, 'o'),
                       (pygame.K_p, 'p'), (pygame.K_q, 'q'), (pygame.K_r, 'r'), (pygame.K_s, 's'), (pygame.K_t, 't'),
                       (pygame.K_u, 'u'), (pygame.K_v, 'v'), (pygame.K_w, 'w'), (pygame.K_x, 'x'), (pygame.K_y, 'y'),
                       (pygame.K_z, 'z')]

    def __init__(self, levels, current_level, state):
        self.levels = levels
        self.current_level = current_level
        self.inventory_slots = Game.inventory_slots
        self.state = state

    def generate_new_level(self):
        new_level = Level.Level([], [], [])
        new_level.generate_terrain()
        new_level.spawn_terrain('wall', 10)
        new_level.define_terrain()
        self.levels.append(new_level)
