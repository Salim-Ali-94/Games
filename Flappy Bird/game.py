import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
import pygame as pg
import pipe
import bird, pipe
from constants import *


def gameManager():
    
    bird_group = pg.sprite.Group()
    pipe_group = pg.sprite.Group()
    hawk = bird.Bird(100, int(screen_height / 2))
    bird_group.add(hawk)
    end = False

    while not end:

        screen.blit(background, (0, 0))
        bird_group.draw(screen)
        bird_group.update()
        pipe_group.draw(screen)
        screen.blit(ground, (hawk.ground_scroll, 768))
        hawk.checkPassPipe(bird_group, pipe_group)
        hawk.checkCollision(bird_group, pipe_group)
        hawk.placePipes(pipe_group)
        pg.display.update()
        clock.tick(framerate)




if __name__ == "__main__":

    pg.init()
    pg.display.set_caption("Flappy Bird")
    background = pg.image.load("assets/bg.png")
    ground = pg.image.load("assets/ground.png")
    clock = pg.time.Clock()
    gameManager()
