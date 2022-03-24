import pygame
from board import Board
from piece import Piece
from panel import Panel

class GameState:
    def __init__(self, window):
        self.board = Board()
        self.board.createBoard(window)    
        self.turn = "BLACK"
        self.panel = Panel()
        self.drawValid = False

        self.player1 = "PLAYER"
        self.player2 = "PLAYER"
        self.currentPlayer = "HUMAN"
        

    def startGame(self, window):
        #when start the game, clear everything in the board
        self.board = Board()
        self.turn = "BLACK"
        self.board.createBoard(window)

        #create, update board position, and draw the circles at the start of the game
        self.board.boardPosition[3][3] = Piece(3,3,"WHITE")
        self.board.boardPosition[3][4] = Piece(3,4,"BLACK")
        self.board.boardPosition[4][3] = Piece(4,3,"BLACK")
        self.board.boardPosition[4][4] = Piece(4,4,"WHITE")
        self.board.boardPosition[3][3].drawCircle(window)
        self.board.boardPosition[3][4].drawCircle(window)
        self.board.boardPosition[4][3].drawCircle(window)
        self.board.boardPosition[4][4].drawCircle(window)
        self.board.numOfBlackPieces = 2
        self.board.numOfWhitePieces = 2

        #self.board.printBoard()

    def update(self, window):
        self.board.drawBoard(window)
        if self.drawValid:
            self.board.drawValidMoves(window, self.turn)        
        self.updateDisplay(window)
        pygame.display.update()

    def addPiece(self):
        if self.turn == "WHITE":
            self.board.numOfWhitePieces += 1
        else:
            self.board.numOfBlackPieces += 1

    def takeTurn(self, row, col, window):
        flag = False      
        newPiece = Piece(row, col, self.turn)
        if self.board.boardPosition[row][col] == None:
            #check up
            if self.board.checkFlip(newPiece, -1, 0):
                flag = True
                #flip pieces
                self.board.flipPiece(newPiece, -1, 0)
            #check top right
            if self.board.checkFlip(newPiece, -1, 1):
                flag = True
                #flip pieces
                self.board.flipPiece(newPiece, -1, 1)
            #check right
            if self.board.checkFlip(newPiece, 0, 1):
                flag = True
                #flip pieces
                self.board.flipPiece(newPiece, 0, 1)
            #check bottom right
            if self.board.checkFlip(newPiece, 1, 1):
                flag = True
                #flip pieces
                self.board.flipPiece(newPiece, 1, 1)
            #check down
            if self.board.checkFlip(newPiece, 1, 0):
                flag = True
                #flip pieces
                self.board.flipPiece(newPiece, 1, 0)
            #check bottom left
            if self.board.checkFlip(newPiece, 1, -1):
                flag = True
                #flip pieces
                self.board.flipPiece(newPiece, 1, -1)
            #check left
            if self.board.checkFlip(newPiece, 0, -1):
                flag = True
                #flip pieces
                self.board.flipPiece(newPiece, 0, -1)
            #check top left
            if self.board.checkFlip(newPiece, -1, -1):
                flag = True
                #flip pieces
                self.board.flipPiece(newPiece, -1, -1)          

            #place the piece once and change the turn
            if flag:
                self.placePiece(row, col, newPiece, window)
                self.calculateWinner()
            else:
                #no valid moves
                if self.board.boardPosition[row][col] == None:
                    return                                     

            #end turn by counting all the pieces
            self.countPieces()

        else:
            #cant overlap pieces, so we dont want to change turns
            return
    
    def placePiece(self, row, col, piece, window):
        #put piece on board, draw piece and change turns
        self.board.boardPosition[row][col] = piece        
        self.board.boardPosition[row][col].drawCircle(window)
        self.changeTurn()

    def calculateWinner(self):
        opposingPiece = ""
        if self.turn == "WHITE":
            opposingPiece = "BLACK"
        else:
            opposingPiece = "WHITE"

        if len(self.board.getValidMoves(self.turn)) == 0 and len(self.board.getValidMoves(opposingPiece)) == 0:
            #game over
            self.countPieces()
            #display winner
            if self.board.numOfBlackPieces > self.board.numOfWhitePieces:
                print("Winner is Black with", self.board.numOfBlackPieces)
            elif self.board.numOfBlackPieces < self.board.numOfWhitePieces:
                print("Winner is White with", self.board.numOfWhitePieces)
            else:
                print("Tie Game!")
        else:
            if self.turn == "WHITE" and len(self.board.getValidMoves(self.turn)) == 0:
                print("skip white turn")
                self.changeTurn()
            elif self.turn == "BLACK" and len(self.board.getValidMoves(self.turn)) == 0:
                print("skip black turn")
                self.changeTurn()

    def changeTurn(self):
        if self.turn == "BLACK":
            self.turn = "WHITE"
        else:
            self.turn = "BLACK"

    def countPieces(self):
        #count the number pieces on the board
        w = 0
        b = 0
        for r in range(0,8):
            for c in range(0,8):
                if self.board.boardPosition[r][c] != None:
                    if self.board.boardPosition[r][c].color == "WHITE":
                        w += 1
                    else:
                        b += 1
        self.board.numOfWhitePieces = w
        self.board.numOfBlackPieces = b

    def updateDisplay(self, window):
        self.panel.displayAll(window, self.turn, self.board.numOfBlackPieces, self.board.numOfWhitePieces, self.drawValid, self.player1, self.player2)

    def toggleValidMoves(self):
        if self.drawValid:
            self.drawValid = False
        else:
            self.drawValid = True

    