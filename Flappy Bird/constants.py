import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
import pygame as pg
import random


screen_width = 864
screen_height = 936
size = [screen_width, screen_height]
white = (255, 255, 255)
scroll_speed = 4
ground_scroll = 0
ground_height = 768
time_previous = pg.time.get_ticks() - random.randint(1500, 100000)
framerate = 60
screen = pg.display.set_mode(size)
