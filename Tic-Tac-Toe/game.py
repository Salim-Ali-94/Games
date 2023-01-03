import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
import pygame as pg
import tic_tac_toe as ttt
from constants import *


def gameManager():

	TTT = ttt.TicTacToe()
	end = False

	while not end:

		TTT.insert()
		pg.display.update()
		TTT.checkGameCondition()
		clock.tick(FRAMERATE)

		
		

if __name__ == "__main__":

	pg.init()
	pg.display.set_caption("Tic-Tac-Toe")
	clock = pg.time.Clock()
	gameManager()
