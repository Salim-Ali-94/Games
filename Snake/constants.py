import pygame as pg

screen_width = 1200
screen_height = 600
size = [screen_width, screen_height]
white = (255, 255, 255)
grey = (50, 50, 50)
background_colour = grey
framerate = 15
screen = pg.display.set_mode(size)
screen.fill(background_colour)