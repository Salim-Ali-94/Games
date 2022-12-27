import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
import pygame as pg
import tic_tac_toe as ttt
from constants import *


def game_manager():

	TTT = ttt.TicTacToe()
	end = False

	while not end:

		TTT.insert()
		pg.display.update()
		TTT.check_game_condition()
		clock.tick(framerate)

		
		

if __name__ == "__main__":

	pg.init()
	pg.display.set_caption("Tic-Tac-Toe")
	clock = pg.time.Clock()
	game_manager()
