import pygame as pg
import random


class Snake(object):

	erase = lambda self: pg.draw.rect(screen, background_colour, [self.position[0][0], self.position[0][1], self.unit, self.unit])

	def __init__(self):

		self.unit = 10
		self.indicator = 0
		self.reset()
		self.body_colour = pg.Color("#086623")
		self.head_colour = pg.Color("#4f7942")


	def update_position(self):

		for event in pg.event.get():

			if (event.type == pg.QUIT):
				pg.quit()
				quit()
			if (event.type == pg.KEYDOWN):
				if (event.key == pg.K_UP):
					self.x_velocity = 0
					self.y_velocity = -self.unit
				elif (event.key == pg.K_DOWN):
					self.x_velocity = 0
					self.y_velocity = self.unit
				elif (event.key == pg.K_LEFT):
					self.y_velocity = 0
					self.x_velocity = -self.unit
				elif (event.key == pg.K_RIGHT):
					self.y_velocity = 0
					self.x_velocity = self.unit

		self.x_position += self.x_velocity
		self.y_position += self.y_velocity
		location = (self.x_position, self.y_position)
		self.position.append(location)
		self.erase()

		if (len(self.position) > self.length):
			self.position.pop(0)


	def create(self):

		counter = 0
		depth = len(self.position)

		for location in self.position:

			if (counter == depth - 1):
				colour = self.head_colour
			else:
				colour = self.body_colour

			pg.draw.rect(screen, colour, [location[0], location[1], self.unit, self.unit])
			counter += 1


	def check_boundary_collision(self):

		if ((self.x_velocity <= 0) & (self.x_position < 0)): 
			self.x_position = screen_width
		elif ((self.x_velocity >= 0) & (self.x_position > screen_width)): 
			self.x_position = 0 - self.unit
		elif ((self.y_velocity >= 0) & (self.y_position > screen_height)): 
			self.y_position = 0 - self.unit
		elif ((self.y_velocity <= 0) & (self.y_position < 0)): 
			self.y_position = screen_height


	def check_body_collision(self, fruit):

		body = self.position[:-1]
		head = self.position[-1]

		for point in body:

			if (point == head):

				self.indicator = 1
				self.reset(fruit)


	def eat(self, fruit):

		head = self.position[-1]
		x = abs(head[0] - fruit.x_position)
		y = abs(head[1] - fruit.y_position)

		if ((x < self.unit) & (y < self.unit)):

			fruit.erase()
			fruit.update_position(self.position)
			fruit.spawn()
			self.length += 1

			if (self.length > 10):
				self.speed += 1
			elif (self.length > 20):
				self.speed += 1
			elif (self.length > 30):
				self.speed += 1
			elif (self.length > 40):
				self.speed += 1
			elif (self.length > 50):
				self.speed += 1


	def reset(self, fruit = None):

		screen.fill(background_colour)
		self.speed = framerate
		self.x_position = random.randrange(0, screen_width - self.unit, self.unit)
		self.y_position = random.randrange(0, screen_height - self.unit, self.unit)
		direction = random.choice(["up", "down", "left", "right"])

		if (direction == "up"):
			self.x_velocity = 0
			self.y_velocity = -self.unit
			tail = (self.x_position, self.y_position)
			head = (self.x_position, self.y_position + self.unit)
		elif (direction == "down"):
			self.x_velocity = 0
			self.y_velocity = self.unit
			tail = (self.x_position, self.y_position)
			head = (self.x_position, self.y_position - self.unit)
		elif (direction == "left"):
			self.x_velocity = -self.unit
			self.y_velocity = 0
			tail = (self.x_position, self.y_position)
			head = (self.x_position + self.unit, self.y_position)
		elif (direction == "right"):
			self.x_velocity = self.unit
			self.y_velocity = 0
			tail = (self.x_position, self.y_position)
			head = (self.x_position - self.unit, self.y_position)

		self.position = [tail, head]
		self.length = len(self.position)

		if (self.indicator != 0):

			fruit.erase()
			fruit.update_position(self.position)
			fruit.spawn()
			self.indicator = 0


class Fruit(object):

	spawn = lambda self: pg.draw.rect(screen, self.colour, [self.position[0], self.position[1], self.unit, self.unit])
	erase = lambda self: pg.draw.rect(screen, background_colour, [self.x_position, self.y_position, self.unit, self.unit])

	def __init__(self):

		self.unit = 10
		self.colour = white


	def update_position(self, snake):

		self.x_position = random.randrange(0, screen_width - self.unit, self.unit)
		self.y_position = random.randrange(0, screen_height - self.unit, self.unit)
		self.position = (self.x_position, self.y_position)

		if (self.position in snake):
			self.update_position(snake)


def game_manager():

	snake = Snake()
	fruit = Fruit()
	fruit.update_position(snake.position)
	fruit.spawn()
	end = False

	while not end:

		snake.update_position()
		snake.check_body_collision(fruit)
		snake.check_boundary_collision()
		snake.eat(fruit)
		snake.create()
		pg.display.update()
		clock.tick(snake.speed)


if __name__ == "__main__":

	pg.init()
	screen_width = 1200
	screen_height = 600
	size = (screen_width, screen_height)
	white = (255, 255, 255)
	grey = (50, 50, 50)
	background_colour = grey
	framerate = 15
	screen = pg.display.set_mode(size)
	screen.fill(background_colour)
	pg.display.set_caption("Snake")
	clock = pg.time.Clock()

	game_manager()