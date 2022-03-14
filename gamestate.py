import this
import pygame
from board import Board
from piece import Piece
from panel import Panel

class GameState:
    def __init__(self, window):
        self.board = Board()
        self.board.createBoard(window)    
        self.turn = "BLACK"
        #self.startGame()
        self.panel = Panel()
        

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
        #TODO: redraw board every update
        self.board.drawBoard(window)
        self.board.drawValidMoves(window, self.turn)
        #self.panel.displayPlayerTurn(window, self.turn)   
        self.panel.displayAll(window, self.turn, self.board.numOfBlackPieces, self.board.numOfWhitePieces)
        pygame.display.update()

    def addPiece(self):
        if self.turn == "WHITE":
            self.board.numOfWhitePieces += 1
        else:
            self.board.numOfBlackPieces += 1

    def takeTurn(self, row, col, window):
        flag = False
        #TODO: if valid move then place piece down; need to create a flipped function        
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
            else:
                #no valid moves
                pass
        else:
            #cant overlap pieces, so we dont want to change turns
            return
    
    def placePiece(self, row, col, piece, window):
        #put piece on board, draw piece and change turns
        self.board.boardPosition[row][col] = piece        
        self.board.boardPosition[row][col].drawCircle(window)
        self.changeTurn()

    def changeTurn(self):
        if self.turn == "BLACK":
            self.turn = "WHITE"
        else:
            self.turn = "BLACK"

    def flipPiece(self):
        pass

    