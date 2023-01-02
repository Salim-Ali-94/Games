import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
import pygame as pg
from constants import *
import random
import pipe


class Bird(pg.sprite.Sprite):

    def __init__(self, x, y):

        pg.sprite.Sprite.__init__(self)
        self.images = []
        self.index = 0
        self.counter = 0
        for img in range(1, 4): self.images.append(pg.image.load(f"assets/bird{img}.png"))
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.velocity = 0
        self.clicked = False
        self.pressed = False
        self.flap_cooldown = 5
        self.pass_pipe = False
        self.score = 0
        self.time_previous = time_previous
        self.ground_scroll = ground_scroll
        self.ground_height = 768
        self.scroll_threshold = 35
        self.pipe_height = [-180, 180]
        self.pipe_interval = [1500, 100000]
        self.velocity_max = 8


    def update(self):

        self.eventHandler()
        self.fly()


    def eventHandler(self):

        for event in pg.event.get():

            if (event.type == pg.QUIT):

                pg.quit()
                quit()


    def fly(self):

        self.counter += 1
        self.velocity += 0.5
        if (self.velocity > self.velocity_max): self.velocity = self.velocity_max
        if (self.rect.bottom < self.ground_height): self.rect.y += int(self.velocity)
        if ((pg.mouse.get_pressed()[0] == 1) and (self.clicked == False)): self.velocity, self.clicked = -10, True
        if (pg.mouse.get_pressed()[0] == 0): self.clicked = False
        if ((pg.key.get_pressed()[pg.K_SPACE] == True) and (self.pressed == False)): self.velocity, self.pressed = -10, True
        if (pg.key.get_pressed()[pg.K_SPACE] == False): self.pressed = False
        if (self.counter > self.flap_cooldown): self.counter, self.index = 0, self.index + 1 if (self.index < len(self.images) - 1) else 0
        self.image = self.images[self.index]
        self.image = pg.transform.rotate(self.images[self.index], -1*self.velocity)


    def checkCollision(self, birds, pipes):

        if (pg.sprite.groupcollide(birds, pipes, False, False) or (self.rect.top < 0)): self.restart(pipes)
        if (self.rect.bottom >= self.ground_height): self.restart(pipes)


    def restart(self, pipes):

        self.reset = False
        pipes.empty()
        self.rect.x = 100
        self.rect.y = int(screen_height / 2)
        self.score = 0
        self.image = self.images[0]


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


    def placePipes(self, pipes):

        time_now = pg.time.get_ticks()

        if ((time_now - self.time_previous) > random.randint(self.pipe_interval[0], self.pipe_interval[1])):

            pipe_height = random.randint(self.pipe_height[0], self.pipe_height[1])
            pipe_bottom = pipe.Pipe(screen_width, int(screen_height / 2) + pipe_height)
            pipe_top = pipe.Pipe(screen_width, int(screen_height / 2) + pipe_height, -1)
            pipes.add(pipe_bottom), pipes.add(pipe_top)
            self.time_previous = time_now

        self.ground_scroll -= scroll_speed
        if (abs(self.ground_scroll) > self.scroll_threshold): self.ground_scroll = 0
        pipes.update()
