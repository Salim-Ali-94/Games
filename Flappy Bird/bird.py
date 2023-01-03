import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
import pygame as pg
from constants import *


class Bird(pg.sprite.Sprite):

    def __init__(self, x, y):

        pg.sprite.Sprite.__init__(self)
        self.images = []
        self.index, self.counter = 0, 0
        self.velocity, self.velocity_max = 0, 8
        self.pressed, self.pass_pipe = False, False
        self.flap_cooldown, self.score = 5, 0
        self.ground_height = GROUND_HEIGHT
        for img in range(1, 4): self.images.append(pg.image.load(f"assets/bird{img}.png"))
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)


    def update(self):

        self.counter += 1
        self.velocity += 0.5
        if (self.velocity > self.velocity_max): self.velocity = self.velocity_max
        if (self.rect.bottom < self.ground_height): self.rect.y += int(self.velocity)
        self.eventHandler()
        self.fly()


    def fly(self):

        if ((pg.key.get_pressed()[pg.K_SPACE] == True) and (self.pressed == False)): self.velocity, self.pressed = -10, True
        if (pg.key.get_pressed()[pg.K_SPACE] == False): self.pressed = False

        if (self.counter > self.flap_cooldown): 

            self.counter = 0
            if (self.index < len(self.images) - 1): self.index += 1
            else: self.index = 0

        self.image = self.images[self.index]
        self.image = pg.transform.rotate(self.images[self.index], -1*self.velocity)


    def checkCollision(self, birds, pipes):

        if (pg.sprite.groupcollide(birds, pipes, False, False) or (self.rect.top < 0)): self.restart(pipes)
        if (self.rect.bottom >= self.ground_height): self.restart(pipes)


    def checkPassPipe(self, birds, pipes):

        if (len(pipes) > 0):

            if ((birds.sprites()[0].rect.left > pipes.sprites()[0].rect.left) and 
                (birds.sprites()[0].rect.right < pipes.sprites()[0].rect.right) and 
                (self.pass_pipe == False)): 

                self.pass_pipe = True

            if (self.pass_pipe == True): 

                if (birds.sprites()[0].rect.left > pipes.sprites()[0].rect.right):

                    self.score += 1
                    self.pass_pipe = False


    def eventHandler(self):

        for event in pg.event.get():

            if (event.type == pg.QUIT):

                pg.quit()
                quit()


    def restart(self, pipes):

        pipes.empty()
        self.score = 0
        self.rect.x = 100
        self.rect.y = SCREEN_HEIGHT // 2
        self.image = self.images[0]
