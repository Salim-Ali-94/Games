import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
import pygame as pg


screen_width = 600
screen_height = 600
size = [screen_width, screen_height]
white = (255, 255, 255)
grey = (50, 50, 50)
green = pg.Color("#4CBB17")
orange = pg.Color("#FD6A02")
background_colour = grey
line_colour = white
X_colour = green
O_colour = orange
framerate = 15
screen = pg.display.set_mode(size)
screen.fill(background_colour)
