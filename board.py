from linecache import checkcache
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

    def checkFlip(self, piece, checkRow, checkCol):
        opposingPiece = ""
        if piece.color == "WHITE":
            opposingPiece = "BLACK"
        else:
            opposingPiece = "WHITE"

        row = piece.row
        col = piece.column
        if (row + checkRow < 0) or (row + checkRow >= 8) or (col + checkCol < 0) or (col + checkCol >= 8):            
            return False

        if self.boardPosition[row + checkRow][col + checkCol] != None and self.boardPosition[row + checkRow][col + checkCol].color == opposingPiece:            
            while (row >= 0) and (row < 8) and (col >= 0) and (col < 8):
                row += checkRow
                col += checkCol                

                #TODO: there is an error here with list out of range
                if (self.boardPosition[row][col] == None):
                    print (row, col, ";", checkRow, checkCol)
                    return False
                if self.boardPosition[row][col].color == piece.color:
                    return True
                else:
                    #keep looping as we have encountered an opponent piece
                    pass                    
        return False

    def getValidMoves(self, board, turn):
        pass