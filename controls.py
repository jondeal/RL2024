import pygame
import bools

keybinds = {'quit': pygame.K_q,
            'mod key': pygame.KMOD_LSHIFT,
            'pickup': pygame.K_g,
            'drop': pygame.K_d}

if bools.has_keypad:
    move_keys = {
        pygame.K_KP7: ('upper left', (-1, -1)), pygame.K_KP8: ('up', (0, -1)), pygame.K_KP9: ('upper right', (1, -1)),
        pygame.K_KP4: ('left', (-1, 0)), pygame.K_KP5: ('in place', (0, 0)), pygame.K_KP6: ('right', (1, 0)),
        pygame.K_KP1: ('lower left', (-1, 1)), pygame.K_KP2: ('down', (0, 1)), pygame.K_KP3: ('lower right', (1, 1))
    }
else:
    move_keys = {
        pygame.K_7: ('upper left', (-1, -1)), pygame.K_8: ('up', (0, -1)), pygame.K_9: ('upper right', (1, -1)),
        pygame.K_u: ('left', (-1, 0)), pygame.K_i: ('in place', (0, 0)), pygame.K_o: ('right', (1, 0)),
        pygame.K_j: ('lower left', (-1, 1)), pygame.K_k: ('down', (0, 1)), pygame.K_l: ('lower right', (1, 1))
    }
