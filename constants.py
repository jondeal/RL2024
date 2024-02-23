import bools
import pygame.freetype
import os

pygame.freetype.init()
pygame.display.init()
pygame.display.set_caption('RL2024')
pygame.mouse.set_visible(False)


screen_info = pygame.display.Info()
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d, %d" % (screen_info.current_w - screen_info.current_h, 0)


X_RANGE = 20
Y_RANGE = 20

TILE_HEIGHT = screen_info.current_h // Y_RANGE
TILE_WIDTH = TILE_HEIGHT

FONT_SIZE = TILE_WIDTH
FONT = pygame.freetype.SysFont('dejavusans', FONT_SIZE)

SCREEN_COLOR = (0, 0, 35)

if bools.KEYPAD:
    move_keys = {pygame.K_KP7: 'upper left', pygame.K_KP4: 'left', pygame.K_KP1: 'lower left',
                 pygame.K_KP8: 'up', pygame.K_KP2: 'down', pygame.K_KP9: 'upper right', pygame.K_KP6: 'right',
                 pygame.K_KP3: 'lower right'}
else:
    move_keys = {pygame.K_7: (-1, -1), pygame.K_u: (-1, 0), pygame.K_j: (-1, 1), pygame.K_8: (0, -1),
                 pygame.K_k: (0, 1), pygame.K_9: (1, -1), pygame.K_o: (1, 0), pygame.K_l: (1, 1)}

if bools.FULLSCREEN:
    screen = pygame.display.set_mode((screen_info.current_w, screen_info.current_h), pygame.FULLSCREEN)
else:
    screen = pygame.display.set_mode((screen_info.current_h, screen_info.current_h))

# directions order: upper left, left, lower left, up, down, upper right, right, lower right
# directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
