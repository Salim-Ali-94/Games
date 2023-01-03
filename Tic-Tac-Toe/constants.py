import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
import pygame as pg


SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SIZE = [SCREEN_WIDTH, SCREEN_HEIGHT]
LINE_COLOUR = (255, 255, 255)
BACKGROUND_COLOUR = (50, 50, 50)
X_colour = pg.Color("#4CBB17")
O_colour = pg.Color("#FD6A02")
FRAMERATE = 15
screen = pg.display.set_mode(SIZE)
screen.fill(BACKGROUND_COLOUR)
