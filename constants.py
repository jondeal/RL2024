import bools
import pygame.freetype
import os

pygame.freetype.init()
pygame.display.init()
pygame.display.set_caption('RL2024')
pygame.mouse.set_visible(False)


screen_info = pygame.display.Info()
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d, %d" % (screen_info.current_w - screen_info.current_h, 0)
# os.environ['SDL_VIDEO_WINDOW_POS'] = "%d, %d" % (screen_info.current_w / 4, 0)  # for being able to see the console; disable render_ui


X_RANGE = 20
Y_RANGE = 20

TILE_HEIGHT = screen_info.current_h // Y_RANGE
TILE_WIDTH = TILE_HEIGHT

FONT_SIZE = TILE_WIDTH
# FONT = pygame.freetype.SysFont('juliamono', FONT_SIZE)
FONT = pygame.freetype.Font('/usr/share/fonts/truetype/julia/JuliaMono-Light.ttf', FONT_SIZE)

SCREEN_COLOR = (0, 0, 35)

if bools.is_fullscreen:
    screen = pygame.display.set_mode((screen_info.current_w, screen_info.current_h), pygame.FULLSCREEN)
else:
    screen = pygame.display.set_mode((screen_info.current_h, screen_info.current_h), pygame.NOFRAME)

# directions order: upper left, left, lower left, up, down, upper right, right, lower right
# directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
