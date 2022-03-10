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
        self.validMovesList = []

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

    def drawBoard(self, window):
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

        #draw right side panel
        pygame.draw.rect(window, GRAY, (850, 0, 500, 850))

        start = 125
        lineSize = 2
        for i in range(0, 7):
            #horizontal lines
            pygame.draw.line(window, BLACK, (0, start + i*100), (HEIGHT, start + i*100), lineSize)
            #vertical lines
            pygame.draw.line(window, BLACK, (start + i*100, 0), (start + i*100, HEIGHT), lineSize)

        #draw pieces
        for r in range(0, 8):
            for c in range(0,8):
                if self.boardPosition[r][c] != None:
                    self.boardPosition[r][c].drawCircle(window)


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

                if row < 8 and row >= 0 and col < 8 and col >= 0 and (self.boardPosition[row][col] == None):
                    return False
                if row < 8 and row >= 0 and col < 8 and col >= 0 and self.boardPosition[row][col].color == piece.color:
                    return True
                else:
                    #keep looping as we have encountered an opponent piece
                    pass                    
        return False

    def getValidMoves(self, turn):
        self.validMovesList = []
        for row in range(0,8):
            for col in range(0,8):
                if self.boardPosition[row][col] == None:
                    newPiece = Piece(row, col, turn)
                    #check up
                    if self.checkFlip(newPiece, -1, 0):
                        self.validMovesList.append(newPiece)
                    #check top right
                    if self.checkFlip(newPiece, -1, 1):
                        self.validMovesList.append(newPiece)
                    #check right
                    if self.checkFlip(newPiece, 0, 1):
                        self.validMovesList.append(newPiece)
                    #check bottom right
                    if self.checkFlip(newPiece, 1, 1):
                        self.validMovesList.append(newPiece)
                    #check down
                    if self.checkFlip(newPiece, 1, 0):
                        self.validMovesList.append(newPiece)
                    #check bottom left
                    if self.checkFlip(newPiece, 1, -1):
                        self.validMovesList.append(newPiece)
                    #check left
                    if self.checkFlip(newPiece, 0, -1):
                        self.validMovesList.append(newPiece)
                    #check top left
                    if self.checkFlip(newPiece, -1, -1):
                        self.validMovesList.append(newPiece)
        #return len(self.validMovesList)
    
    def drawValidMoves(self, window, turn):
        self.getValidMoves(turn)
        for move in self.validMovesList:
            move.calculatePosition()
            pygame.draw.circle(window, RED, (move.x, move.y), 15)
