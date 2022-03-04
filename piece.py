import pygame

DARKGRAY = (80, 80, 80)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class Piece:
    def __init__(self, row, column, type):
        self.row = row
        self.column = column        
        self.color = type

        self.x = 0
        self.y = 0
        self.calculatePosition()
    
    #calculates the exact middle position of each space on the board for the piece
    def calculatePosition(self):
        self.x = self.column * 100 + 75
        self.y = self.row * 100 + 75

    #draws the piece onto the board
    def drawCircle(self, window):
        if self.color == "WHITE":
            #draw white circle
            pygame.draw.circle(window, DARKGRAY, (self.x+1, self.y+3), 35)
            pygame.draw.circle(window, WHITE, (self.x, self.y), 36)
        elif self.color == "BLACK":
            #draw black circle
            pygame.draw.circle(window, DARKGRAY, (self.x+1, self.y+3), 35)
            pygame.draw.circle(window, BLACK, (self.x, self.y), 36)
        else:
            print("Wrong type of piece")
        