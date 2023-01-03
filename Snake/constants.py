import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
import pygame as pg


SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600
SIZE = [SCREEN_WIDTH, SCREEN_HEIGHT]
WHITE = (255, 255, 255)
GREY = (50, 50, 50)
BODY_COLOUR = pg.Color("#086623")
HEAD_COLOUR = pg.Color("#4CBB17")
BACKGROUND_COLOUR = GREY
FRAMERATE = 15
screen = pg.display.set_mode(SIZE)
screen.fill(BACKGROUND_COLOUR)
