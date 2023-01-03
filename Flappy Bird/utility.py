import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
import pygame as pg
from constants import *
import random
import pipe


def placePipes(pipes):

    if not hasattr(placePipes, "time_previous"): 

        placePipes.time_previous = pg.time.get_ticks() - random.randint(PIPE_INTERVAL[0], PIPE_INTERVAL[1])

    time_now = pg.time.get_ticks()

    if ((time_now - placePipes.time_previous) > random.randint(PIPE_INTERVAL[0], PIPE_INTERVAL[1])):

        pipe_height = random.randint(PIPE_LENGTH[0], PIPE_LENGTH[1])
        pipe_bottom = pipe.Pipe(SCREEN_WIDTH, SCREEN_HEIGHT // 2 + pipe_height)
        pipe_top = pipe.Pipe(SCREEN_WIDTH, SCREEN_HEIGHT // 2 + pipe_height, -1)
        pipes.add(pipe_bottom), pipes.add(pipe_top)
        placePipes.time_previous = time_now

    pipes.update()


def scrollWindow(screen):

    if not all(hasattr(scrollWindow, item) for item in ["ground_scroll", "ground"]):

        scrollWindow.ground_scroll = 0
        scrollWindow.ground = pg.image.load("assets/ground.png")

    scrollWindow.ground_scroll -= SCROLL_SPEED
    if (abs(scrollWindow.ground_scroll) > SCROLL_THRESHOLD): scrollWindow.ground_scroll = 0
    screen.blit(scrollWindow.ground, (scrollWindow.ground_scroll, GROUND_HEIGHT))
