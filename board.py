import pygame
from piece import Piece

WIDTH, HEIGHT, FPS = 1350, 850, 60
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 140, 0)
GRAY = (220, 220, 220)
DARKGRAY = (80, 80, 80)
WHITE = (255, 255, 255)

class Board:
    def __init__(self):
        self.numOfWhitePieces = 0
        self.numOfBlackPieces = 0
        self.boardPosition = []

    def createBoard(self, window):
        #create the virtual board
        for row in range(0,8):
            self.boardPosition.append([])
            for col in range(0,8):
                self.boardPosition[row].append(None)

        #fill the background to green
        window.fill(GREEN)
        
        #Left Border
        pygame.draw.line(window, BLACK, (0, 0), (0, HEIGHT), 50)
        #Right Border
        pygame.draw.line(window, BLACK, (837.5, 0), (837.5, HEIGHT), 25)
        #Bottom Border
        pygame.draw.line(window, BLACK, (0,850), (850, 850), 50)
        #Top Border
        pygame.draw.line(window, BLACK, (0, 0), (850, 0), 50)
        
        start = 125
        lineSize = 2
        for i in range(0, 7):
            #horizontal lines
            pygame.draw.line(window, BLACK, (0, start + i*100), (HEIGHT, start + i*100), lineSize)
            #vertical lines
            pygame.draw.line(window, BLACK, (start + i*100, 0), (start + i*100, HEIGHT), lineSize)

        #draw right side panel
        pygame.draw.rect(window, GRAY, (850, 0, 500, 850))

    def printBoard(self):
        print("number of white:", self.numOfWhitePieces, "/", "num of black:", self.numOfBlackPieces)
        for row in range(0,8):
            print(self.boardPosition[row])

    def getValidMoves(self, board, turn):
        pass