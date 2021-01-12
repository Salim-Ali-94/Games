from constants import *
from pygame import gfxdraw
import pygame as pg


class TicTacToe(object):

	def __init__(self):

		self.square = screen_width // 3
		self.line_colour = line_colour
		self.line_thickness = 4
		self.X_colour = X_colour
		self.O_colour = O_colour
		self.token_thickness = 7
		self.clearance = 20
		self.initialize_board()
		self.initialize_states()
		self.game_conditions()


	def initialize_board(self):

		screen.fill(background_colour)
		horizontal_line1_start = (0, self.square + self.line_thickness / 2)
		horizontal_line1_end = (screen_width, self.square + self.line_thickness / 2)
		horizontal_line2_start = (0, 2*self.square + self.line_thickness)
		horizontal_line2_end = (screen_width, 2*self.square + self.line_thickness)
		vertical_line1_start = (self.square + self.line_thickness / 2, 0)
		vertical_line1_end = (self.square + self.line_thickness / 2, screen_height)
		vertical_line2_start = (2*self.square + self.line_thickness, 0)
		vertical_line2_end = (2*self.square + self.line_thickness, screen_height)
		pg.draw.line(screen, self.line_colour, horizontal_line1_start, horizontal_line1_end, self.line_thickness)
		pg.draw.line(screen, self.line_colour, horizontal_line2_start, horizontal_line2_end, self.line_thickness)
		pg.draw.line(screen, self.line_colour, vertical_line1_start, vertical_line1_end, self.line_thickness)
		pg.draw.line(screen, self.line_colour, vertical_line2_start, vertical_line2_end, self.line_thickness)
		self.positions = [1, 2, 3, 4, 5, 6, 7, 8, 9]
		self.X_board, self.O_board = [], []
		self.token = 0


	def insert(self):

		position = self.keyboard_handler()

		if (position != 0):
			
			if (self.token%2 != 0):
				line1_start = self.X_state[position - 1][0]
				line1_end = self.X_state[position - 1][1]
				line2_start = self.X_state[position - 1][2]
				line2_end = self.X_state[position - 1][3]
				pg.draw.line(screen, self.X_colour, line1_start, line1_end, self.token_thickness)
				pg.draw.line(screen, self.X_colour, line2_start, line2_end, self.token_thickness)
				board = ("X", position)
				self.X_board.append(board)
			elif (self.token%2 == 0):
				diameter = self.square - 2*self.clearance
				radius = int(diameter / 2)
				x = self.O_state[position - 1][0]
				y = self.O_state[position - 1][1]
				gfxdraw.aacircle(screen, x, y, radius, self.O_colour)
				gfxdraw.filled_circle(screen, x, y, radius, self.O_colour)
				gfxdraw.aacircle(screen, x, y, radius - 5, background_colour)
				gfxdraw.filled_circle(screen, x, y, radius - 5, background_colour)
				board = ("O", position)
				self.O_board.append(board)


	def keyboard_handler(self):

		position = 0

		for event in pg.event.get():

			if (event.type == pg.QUIT):
				pg.quit()
				quit()
			elif (event.type == pg.KEYDOWN):
				if (event.key == pg.K_1):
					validity = self.check_available_positions(1)
					if (validity == True):
						position = 1
				elif (event.key == pg.K_2):
					validity = self.check_available_positions(2)
					if (validity == True):
						position = 2
				elif (event.key == pg.K_3):
					validity = self.check_available_positions(3)
					if (validity == True):
						position = 3
				elif (event.key == pg.K_4):
					validity = self.check_available_positions(4)
					if (validity == True):
						position = 4
				elif (event.key == pg.K_5):
					validity = self.check_available_positions(5)
					if (validity == True):
						position = 5
				elif (event.key == pg.K_6):
					validity = self.check_available_positions(6)
					if (validity == True):
						position = 6
				elif (event.key == pg.K_7):
					validity = self.check_available_positions(7)
					if (validity == True):
						position = 7
				elif (event.key == pg.K_8):
					validity = self.check_available_positions(8)
					if (validity == True):
						position = 8
				elif (event.key == pg.K_9):
					validity = self.check_available_positions(9)
					if (validity == True):
						position = 9

		return position


	def check_available_positions(self, position):

		if (position in self.positions):
			self.positions.remove(position)
			validity = True
			self.token += 1
		else:
			validity = False

		return validity


	def check_game_condition(self):

		X_counter = 0
		O_counter = 0

		if (self.token >= 6):			

			for x_win, o_win in zip(self.win_X, self.win_O):

				for index in  range(3):

					if (x_win[index] in self.X_board):
						X_counter += 1
					if (o_win[index] in self.O_board):
						O_counter += 1

				if (X_counter == 3):
					pg.time.delay(1000)
					self.initialize_board()
				if (O_counter == 3):
					pg.time.delay(1000)
					self.initialize_board()

				X_counter, O_counter = 0, 0

		if (self.token >= 9):

			pg.time.delay(1000)
			self.initialize_board()


	def initialize_states(self):

		X1 = [(0 + self.clearance, 0 + self.clearance),
		      (self.square - self.clearance, self.square - self.clearance),
		      (self.square - self.clearance, 0 + self.clearance),
		      (0 + self.clearance, self.square - self.clearance)]

		X2 = [(self.square + self.line_thickness + self.clearance, 0 + self.clearance),
		      (2*self.square + self.line_thickness - self.clearance, self.square - self.clearance),
		      (2*self.square + self.line_thickness - self.clearance, 0 + self.clearance),
		      (self.square + self.line_thickness + self.clearance, self.square - self.clearance)]

		X3 = [(2*self.square + 2*self.line_thickness + self.clearance, 0 + self.clearance),
		      (3*self.square + 2*self.line_thickness - self.clearance, self.square - self.clearance),
		      (3*self.square + 2*self.line_thickness - self.clearance, 0 + self.clearance),
		      (2*self.square + 2*self.line_thickness + self.clearance, self.square - self.clearance)]

		X4 = [(0 + self.clearance, self.square + self.line_thickness + self.clearance),
		      (self.square - self.clearance, 2*self.square + self.line_thickness - self.clearance),
		      (self.square - self.clearance, self.square + self.line_thickness + self.clearance),
		      (0 + self.clearance, 2*self.square + self.line_thickness - self.clearance)]

		X5 = [(self.square + self.line_thickness + self.clearance, self.square + self.line_thickness + self.clearance),
		      (2*self.square + self.line_thickness - self.clearance, 2*self.square + self.line_thickness - self.clearance),
		      (2*self.square + self.line_thickness - self.clearance, self.square + self.line_thickness + self.clearance),
		      (self.square + self.line_thickness + self.clearance, 2*self.square + self.line_thickness - self.clearance)]

		X6 = [(2*self.square + 2*self.line_thickness + self.clearance, self.square + self.line_thickness + self.clearance),
		      (3*self.square + 2*self.line_thickness - self.clearance, 2*self.square + self.line_thickness - self.clearance),
		      (3*self.square + 2*self.line_thickness - self.clearance, self.square + self.line_thickness + self.clearance),
		      (2*self.square + 2*self.line_thickness + self.clearance, 2*self.square + self.line_thickness - self.clearance)]

		X7 = [(0 + self.clearance, 2*self.square + 2*self.line_thickness + self.clearance),
		      (self.square - self.clearance, 3*self.square + 2*self.line_thickness - self.clearance),
		      (self.square - self.clearance, 2*self.square + 2*self.line_thickness + self.clearance),
		      (0 + self.clearance, 3*self.square + 2*self.line_thickness - self.clearance)]

		X8 = [(self.square + self.line_thickness + self.clearance, 2*self.square + 2*self.line_thickness + self.clearance),
		      (2*self.square + self.line_thickness - self.clearance, 3*self.square + 2*self.line_thickness - self.clearance),
		      (2*self.square + self.line_thickness - self.clearance, 2*self.square + 2*self.line_thickness + self.clearance),
		      (self.square + self.line_thickness + self.clearance, 3*self.square + 2*self.line_thickness - self.clearance)]

		X9 = [(2*self.square + 2*self.line_thickness + self.clearance, 2*self.square + 2*self.line_thickness + self.clearance),
		      (3*self.square + 2*self.line_thickness - self.clearance, 3*self.square + 2*self.line_thickness - self.clearance),
		      (3*self.square + 2*self.line_thickness - self.clearance, 2*self.square + 2*self.line_thickness + self.clearance),
		      (2*self.square + 2*self.line_thickness + self.clearance, 3*self.square + 2*self.line_thickness - self.clearance)]

		O1 = [int((0 + self.square) / 2), int((0 + self.square) / 2)]
		O2 = [int(screen_width / 2), int((0 + self.square) / 2)]
		O3 = [int(3*self.square + 2*self.line_thickness - self.square / 2), int((0 + self.square) / 2)]
		O4 = [int((0 + self.square) / 2), int(screen_height / 2)]
		O5 = [int(screen_width / 2), int(screen_height / 2)]
		O6 = [int(3*self.square + 2*self.line_thickness - self.square / 2), int(screen_height / 2)]
		O7 = [int((0 + self.square) / 2), int(3*self.square + 2*self.line_thickness - self.square / 2)]
		O8 = [int(screen_width / 2), int(3*self.square + 2*self.line_thickness - self.square / 2)]
		O9 = [int(3*self.square + 2*self.line_thickness - self.square / 2), int(3*self.square + 2*self.line_thickness - self.square / 2)]

		self.X_state = [X1, X2, X3, X4, X5, X6, X7, X8, X9]
		self.O_state = [O1, O2, O3, O4, O5, O6, O7, O8, O9]


	def game_conditions(self):

		win1_X = [("X", 1), ("X", 2), ("X", 3)]
		win2_X = [("X", 4), ("X", 5), ("X", 6)]
		win3_X = [("X", 7), ("X", 8), ("X", 9)]
		win4_X = [("X", 1), ("X", 4), ("X", 7)]
		win5_X = [("X", 2), ("X", 5), ("X", 8)]
		win6_X = [("X", 3), ("X", 6), ("X", 9)]
		win7_X = [("X", 1), ("X", 5), ("X", 9)]
		win8_X = [("X", 3), ("X", 5), ("X", 7)]
		win1_O = [("O", 1), ("O", 2), ("O", 3)]
		win2_O = [("O", 4), ("O", 5), ("O", 6)]
		win3_O = [("O", 7), ("O", 8), ("O", 9)]
		win4_O = [("O", 1), ("O", 4), ("O", 7)]
		win5_O = [("O", 2), ("O", 5), ("O", 8)]
		win6_O = [("O", 3), ("O", 6), ("O", 9)]
		win7_O = [("O", 1), ("O", 5), ("O", 9)]
		win8_O = [("O", 3), ("O", 5), ("O", 7)]

		self.win_X = [win1_X, win2_X, win3_X, win4_X, win5_X, win6_X, win7_X, win8_X]
		self.win_O = [win1_O, win2_O, win3_O, win4_O, win5_O, win6_O, win7_O, win8_O]
