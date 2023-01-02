import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
import pygame as pg
import random
from constants import *


class Pipe(pg.sprite.Sprite):

    def __init__(self, x, y, position = 1):

        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(f"assets/pipe.png")
        self.rect = self.image.get_rect()
        self.gap_interval = [180, 200]
        self.length_interval = [160, 200]
        if (position == 1): self.rect.topleft = [x, y + int(random.randint(self.length_interval[0], self.length_interval[1]) / 2)]
        else: self.image, self.rect.bottomleft = pg.transform.flip(self.image, False, True), [x, y - int(random.randint(self.gap_interval[0], self.gap_interval[1]) / 2)]


    def update(self):

        self.rect.x -= scroll_speed
        if (self.rect.right < 0): self.kill()
