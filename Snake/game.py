import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
import pygame as pg
import snake
import fruit


def gameManager():

	apple = fruit.Fruit()
	python = snake.Snake(apple)
	end = False

	while not end:

		python.updatePosition()
		python.checkCollision(apple)
		python.eat(apple)
		pg.display.update()
		clock.tick(python.speed)


		
		
if __name__ == "__main__":

	pg.init()
	pg.display.set_caption("Snake")
	clock = pg.time.Clock()
	gameManager()
