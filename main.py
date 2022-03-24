from turtle import pos
import pygame
from gamestate import GameState
from piece import Piece

WIDTH, HEIGHT, FPS = 1350, 850, 60

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Othello')

game = GameState(WINDOW)

def getRowCol(pos):
    x = -5
    y = -5
    #between 25 and 825 for both rows and columns
    col, row = pos    
    x = (row-25)//100
    y = (col-25)//100
    return x, y

def main():
    isGameStarted = False

    run = True
    clock = pygame.time.Clock()
    #run game loop
    while run:
        #check if game has started or not
        if isGameStarted == False and (game.board.numOfBlackPieces > 2 or game.board.numOfWhitePieces > 2):
            isGameStarted = True
        #check for any events that happened
        for event in pygame.event.get():            
            #get the row and column from mouse click
            if event.type == pygame.MOUSEBUTTONDOWN:
                #get the position of the mouse
                position = pygame.mouse.get_pos()                                
                
                #start button
                if position[0] > 899 and position[0] < 1050 and position[1] > 224 and position[1] < 300:
                    game.startGame(WINDOW)
                    isGameStarted = True
                    print(game.player1, "VS", game.player2)
                #valid moves button
                elif position[0] > 1099 and position[0] < 1330 and position[1] > 224 and position[1] < 300:
                    game.toggleValidMoves()

                if isGameStarted == False:
                    if position[0] > 900 and position[0] < 1050 and position[1] > 403 and position[1] < 475:
                        game.player1 = "PLAYER"
                    elif position[0] > 900 and position[0] < 1050 and position[1] > 500 and position[1] < 575:
                        game.player1 = "RANDOM"
                    elif position[0] > 900 and position[0] < 1050 and position[1] > 600 and position[1] < 675:
                        game.player1 = "EASY"
                    elif position[0] > 900 and position[0] < 1050 and position[1] > 700 and position[1] < 775:
                        game.player1 = "HARD"

                    if position[0] > 1175 and position[0] < 1325 and position[1] > 403 and position[1] < 475:
                        game.player2 = "PLAYER"
                    elif position[0] > 1175 and position[0] < 1325 and position[1] > 500 and position[1] < 575:
                        game.player2 = "RANDOM"
                    elif position[0] > 1175 and position[0] < 1325 and position[1] > 600 and position[1] < 675:
                        game.player2 = "EASY"
                    elif position[0] > 1175 and position[0] < 1325 and position[1] > 700 and position[1] < 775:
                        game.player2 = "HARD"
                            
                if game.currentPlayer == "HUMAN":
                    #human plays
                    #boundary of board
                    if position[0] > 25 and position[0] < 825 and position[1] > 25 and position[1] < 825:
                        row, col = getRowCol(position)
                        #player takes their turn
                        game.takeTurn(row, col, WINDOW)
                else:
                    #bot plays
                    pass
                    
            #when player presses spacebar                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game.board.boardPosition = []
                    isGameStarted = False
                elif event.key == pygame.K_c:
                    game.board.drawValidMoves(WINDOW, game.turn)
            #when player presses quit
            if event.type == pygame.QUIT:
                run = False
        
        game.update(WINDOW)
        #framerate
        clock.tick(FPS)

    pygame.quit()

main()