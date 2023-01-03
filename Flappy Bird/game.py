import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
import pygame as pg
import pipe
import bird, pipe
from constants import *
from utility import *


def gameManager():
    
    bird_group = pg.sprite.Group()
    pipe_group = pg.sprite.Group()
    hawk = bird.Bird(100, int(SCREEN_HEIGHT / 2))
    tunnel = pipe.Pipe()
    bird_group.add(hawk)
    end = False

    while not end:

        screen.blit(background, (0, 0))
        bird_group.draw(screen)
        bird_group.update()
        pipe_group.draw(screen)
        hawk.checkPassPipe(bird_group, pipe_group)
        hawk.checkCollision(bird_group, pipe_group)
        placePipes(pipe_group)
        scrollWindow(screen)
        pg.display.update()
        clock.tick(FRAMERATE)




if __name__ == "__main__":

    pg.init()
    pg.display.set_caption("Flappy Bird")
    background = pg.image.load("assets/bg.png")
    clock = pg.time.Clock()
    gameManager()
