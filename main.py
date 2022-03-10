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
    #boundary of board
    if col > 25 and col < 825 and row > 25 and row < 825:
        x = (row-25)//100
        y = (col-25)//100
    return x, y

def main():
    run = True
    clock = pygame.time.Clock()
    #run game loop
    while run:
        #check for any events that happened
        for event in pygame.event.get():
            #get the row and column from mouse click
            if event.type == pygame.MOUSEBUTTONDOWN:
                position = pygame.mouse.get_pos()
                row, col = getRowCol(position)
                
                #player takes their turn
                game.takeTurn(row, col, WINDOW)

            #when player presses spacebar                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game.startGame(WINDOW)
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