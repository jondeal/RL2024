import bools
import pygame.freetype
import os

import constants

pygame.freetype.init()
pygame.display.init()
pygame.display.set_caption('RL2024')
pygame.mouse.set_visible(False)


screen_info = pygame.display.Info()
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d, %d" % (screen_info.current_w - screen_info.current_h, 0)
# os.environ['SDL_VIDEO_WINDOW_POS'] = "%d, %d" % (screen_info.current_w / 4, 0)  # for being able to see the console; disable render_ui

if bools.is_fullscreen:
    screen = pygame.display.set_mode((screen_info.current_w, screen_info.current_h), pygame.FULLSCREEN)
else:
    screen = pygame.display.set_mode((screen_info.current_h, screen_info.current_h), pygame.NOFRAME)

X_RANGE = 20
Y_RANGE = 20

TILE_HEIGHT = screen_info.current_h // (Y_RANGE + 1)  # int following Y_RANGE is num lines to make the message bar below the level display
TILE_WIDTH = TILE_HEIGHT

LEVEL_RECT = pygame.Rect(0, 0, X_RANGE * TILE_WIDTH, Y_RANGE * TILE_HEIGHT)
UI_RECT = pygame.Rect(screen_info.current_h, 0, screen_info.current_w - screen_info.current_h, screen_info.current_h)
PROMPT_RECT = pygame.Rect(0, screen_info.current_h - constants.TILE_WIDTH, LEVEL_RECT.width, constants.TILE_HEIGHT)

FONT_SIZE = TILE_WIDTH
# FONT = pygame.freetype.SysFont('juliamono', FONT_SIZE)
FONT = pygame.freetype.Font('/usr/share/fonts/truetype/julia/JuliaMono-Light.ttf', FONT_SIZE)

SCREEN_COLOR = (0, 0, 35)
