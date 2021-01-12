import pygame as pg
import snake
import fruit


def game_manager():

	apple = fruit.Fruit()
	python = snake.Snake(apple)
	end = False

	while not end:

		python.update_position()
		python.check_body_collision(apple)
		python.check_boundary_collision()
		python.eat(apple)
		pg.display.update()
		clock.tick(python.speed)


if __name__ == "__main__":

	pg.init()
	pg.display.set_caption("Snake")
	clock = pg.time.Clock()
	game_manager()