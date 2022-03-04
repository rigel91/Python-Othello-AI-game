import pygame
from board import Board

class GameState:
    def __init__(self, window):
        self.board = Board()
        self.board.createBoard(window)
        self.turn = "BLACK"

    def update(self):
        pygame.display.update()

    def changeTurn(self):
        if self.turn == "BLACK":
            self.turn = "WHITE"
        else:
            self.turn = "BLACK"