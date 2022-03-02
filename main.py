import pygame
from board import Board

WIDTH, HEIGHT, FPS = 1350, 850, 60

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Othello')

board = Board()

def main():
    run = True
    clock = pygame.time.Clock()

    #run game loop
    while run:
        #check for any events that happened
        for event in pygame.event.get():
            #when player presses quit
            if event.type == pygame.QUIT:
                run = False
        
        board.createBoard(WINDOW)
        #framerate
        clock.tick(FPS)


    pygame.quit()

main()