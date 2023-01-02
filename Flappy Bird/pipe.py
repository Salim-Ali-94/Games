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
        if (position == 1): self.rect.topleft = [x, y + int(random.randint(160, 200) / 2)]
        else: self.image, self.rect.bottomleft = pg.transform.flip(self.image, False, True), [x, y - int(random.randint(180, 200) / 2)]


    def update(self):

        self.rect.x -= scroll_speed
        if (self.rect.right < 0): self.kill()
