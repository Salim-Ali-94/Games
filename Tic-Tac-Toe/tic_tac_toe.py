from constants import *
from pygame import gfxdraw
import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
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
		x0 = (0, self.square + self.line_thickness / 2)
		x1 = (screen_width, self.square + self.line_thickness / 2)
		x2 = (0, 2*self.square + self.line_thickness)
		x3 = (screen_width, 2*self.square + self.line_thickness)
		y0 = (self.square + self.line_thickness / 2, 0)
		y1 = (self.square + self.line_thickness / 2, screen_height)
		y2 = (2*self.square + self.line_thickness, 0)
		y3 = (2*self.square + self.line_thickness, screen_height)
		pg.draw.line(screen, self.line_colour, x0, x1, self.line_thickness)
		pg.draw.line(screen, self.line_colour, x2, x3, self.line_thickness)
		pg.draw.line(screen, self.line_colour, y0, y1, self.line_thickness)
		pg.draw.line(screen, self.line_colour, y2, y3, self.line_thickness)
		self.positions = [1, 2, 3, 4, 5, 6, 7, 8, 9]
		self.X_board, self.O_board = [], []
		self.token = 0


	def insert(self):

		position = self.event_handler()

		if (position != 0):
			
			if (self.token%2 != 0):
				
				x0 = self.X_state[position - 1][0]
				x1 = self.X_state[position - 1][1]
				x2 = self.X_state[position - 1][2]
				x3 = self.X_state[position - 1][3]
				pg.draw.line(screen, self.X_colour, x0, x1, self.token_thickness)
				pg.draw.line(screen, self.X_colour, x2, x3, self.token_thickness)
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


	def event_handler(self):

		position = 0

		for event in pg.event.get():

			if (event.type == pg.QUIT):
				
				pg.quit()
				quit()
				
			elif (event.type == pg.KEYDOWN):
				
				if (event.key == pg.K_1):
					
					validity = self.check_available_positions(1)
					if (validity == True): position = 1
						
				elif (event.key == pg.K_2):
					
					validity = self.check_available_positions(2)
					if (validity == True): position = 2
						
				elif (event.key == pg.K_3):
					
					validity = self.check_available_positions(3)
					if (validity == True): position = 3
						
				elif (event.key == pg.K_4):
					
					validity = self.check_available_positions(4)
					if (validity == True): position = 4
						
				elif (event.key == pg.K_5):
					
					validity = self.check_available_positions(5)
					if (validity == True): position = 5
						
				elif (event.key == pg.K_6):
					
					validity = self.check_available_positions(6)
					if (validity == True): position = 6
						
				elif (event.key == pg.K_7):
					
					validity = self.check_available_positions(7)
					if (validity == True): position = 7
						
				elif (event.key == pg.K_8):
					
					validity = self.check_available_positions(8)
					if (validity == True): position = 8
						
				elif (event.key == pg.K_9):
					
					validity = self.check_available_positions(9)
					if (validity == True): position = 9
						
			elif (event.type == pg.MOUSEBUTTONDOWN):
				
				x, y = pg.mouse.get_pos()
				
				if ((x >= 0) & (x <= self.square + self.line_thickness / 2) & 
			            (y >= 0) & (y <= self.square + self.line_thickness / 2)):
					
					validity = self.check_available_positions(1)
					if (validity == True): position = 1
						
				elif ((x >= self.square + self.line_thickness / 2) & (x <= 2*self.square + 3*self.line_thickness / 2) & 
				      (y >= 0) & (y <= self.square + self.line_thickness / 2)):
					
					validity = self.check_available_positions(2)
					if (validity == True): position = 2
						
				elif ((x >= 2*self.square + 3*self.line_thickness / 2) & (x <= screen_width) & 
				      (y >= 0) & (y <= self.square + self.line_thickness / 2)):
					
					validity = self.check_available_positions(3)
					if (validity == True): position = 3
						
				elif ((x >= 0) & (x <= self.square + self.line_thickness / 2) & 
				      (y >= self.square + self.line_thickness / 2) & (y <= 2*self.square + 3*self.line_thickness / 2)):
					
					validity = self.check_available_positions(4)
					if (validity == True): position = 4
						
				elif ((x >= self.square + self.line_thickness / 2) & (x <= 2*self.square + 3*self.line_thickness / 2) & 
				      (y >= self.square + self.line_thickness / 2) & (y <= 2*self.square + 3*self.line_thickness / 2)):
					
					validity = self.check_available_positions(5)
					if (validity == True): position = 5
						
				elif ((x >= 2*self.square + 3*self.line_thickness / 2) & (x <= screen_width) & 
				      (y >= self.square + self.line_thickness / 2) & (y <= 2*self.square + 3*self.line_thickness / 2)):
					
					validity = self.check_available_positions(6)
					if (validity == True): position = 6
						
				elif ((x >= 0) & (x <= self.square + self.line_thickness / 2) & 
				      (y >= 2*self.square + 3*self.line_thickness / 2) & (y <= screen_height)):
					
					validity = self.check_available_positions(7)
					if (validity == True): position = 7
						
				elif ((x >= self.square + self.line_thickness / 2) & (x <= 2*self.square + 3*self.line_thickness / 2) & 
				      (y >= 2*self.square + 3*self.line_thickness / 2) & (y <= screen_height)):
					
					validity = self.check_available_positions(8)
					if (validity == True): position = 8
						
				elif ((x >= 2*self.square + 3*self.line_thickness / 2) & (x <= screen_width) & 
				      (y >= 2*self.square + 3*self.line_thickness / 2) & (y <= screen_height)):
					
					validity = self.check_available_positions(9)
					if (validity == True): position = 9

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

		if (self.token >= 5):			

			for X, O in zip(self.X_win, self.O_win):

				for index in range(3):

					if (X[index] in self.X_board): X_counter += 1
					if (O[index] in self.O_board): O_counter += 1

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

		X_win1 = [("X", 1), ("X", 2), ("X", 3)]
		X_win2 = [("X", 4), ("X", 5), ("X", 6)]
		X_win3 = [("X", 7), ("X", 8), ("X", 9)]
		X_win4 = [("X", 1), ("X", 4), ("X", 7)]
		X_win5 = [("X", 2), ("X", 5), ("X", 8)]
		X_win6 = [("X", 3), ("X", 6), ("X", 9)]
		X_win7 = [("X", 1), ("X", 5), ("X", 9)]
		X_win8 = [("X", 3), ("X", 5), ("X", 7)]
		O_win1 = [("O", 1), ("O", 2), ("O", 3)]
		O_win2 = [("O", 4), ("O", 5), ("O", 6)]
		O_win3 = [("O", 7), ("O", 8), ("O", 9)]
		O_win4 = [("O", 1), ("O", 4), ("O", 7)]
		O_win5 = [("O", 2), ("O", 5), ("O", 8)]
		O_win6 = [("O", 3), ("O", 6), ("O", 9)]
		O_win7 = [("O", 1), ("O", 5), ("O", 9)]
		O_win8 = [("O", 3), ("O", 5), ("O", 7)]
		self.X_win = [X_win1, X_win2, X_win3, X_win4, X_win5, X_win6, X_win7, X_win8]
		self.O_win = [O_win1, O_win2, O_win3, O_win4, O_win5, O_win6, O_win7, O_win8]
