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
    def createBoard(self, window):
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

        pygame.display.update()