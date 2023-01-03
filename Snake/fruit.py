from constants import *
import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
import pygame as pg
import random


class Fruit(object):

	create = lambda self: pg.draw.rect(screen, self.colour, [self.position[0], self.position[1], self.unit, self.unit])
	erase = lambda self: pg.draw.rect(screen, BACKGROUND_COLOUR, [self.x_position, self.y_position, self.unit, self.unit])

	def __init__(self):

		self.colour = WHITE
		self.unit = 10
		self.x_position = 0
		self.y_position = 0
		location = (self.x_position, self.y_position)
		self.position = location


	def updatePosition(self, snake):

		self.x_position = random.randrange(0, SCREEN_WIDTH - self.unit, self.unit)
		self.y_position = random.randrange(0, SCREEN_HEIGHT - self.unit, self.unit)
		self.position = (self.x_position, self.y_position)

		while (self.position in snake): 

			self.x_position = random.randrange(0, SCREEN_WIDTH - self.unit, self.unit)
			self.y_position = random.randrange(0, SCREEN_HEIGHT - self.unit, self.unit)
			self.position = (self.x_position, self.y_position)


	def spawn(self):

		self.erase()
		self.updatePosition(self.position)
		self.create()
