import pygame

WIDTH, HEIGHT, FPS = 1350, 850, 60
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 140, 0)
GRAY = (220, 220, 220)
WHITE = (255, 255, 255)

class Board:
    def createBoard(self, window):
        window.fill(GREEN)
        #pygame.draw.rect(window, RED, (5, 5, 100, 100))
        
        #Left Border
        pygame.draw.line(window, BLACK, (0, 0), (0, HEIGHT), 50)
        #Right Border
        pygame.draw.line(window, BLACK, (837.5, 0), (837.5, HEIGHT), 25)
        #Bottom Border
        pygame.draw.line(window, BLACK, (0,850), (850, 850), 50)
        #Top Border
        pygame.draw.line(window, BLACK, (0, 0), (850, 0), 50)

        #draw verical lines
        pygame.draw.line(window, BLACK, (0, 125), (850, 125), 2)
        pygame.draw.line(window, BLACK, (0, 225), (850, 225), 2)
        pygame.draw.line(window, BLACK, (0, 325), (850, 325), 2)
        pygame.draw.line(window, BLACK, (0, 425), (850, 425), 2)
        pygame.draw.line(window, BLACK, (0, 525), (850, 525), 2)
        pygame.draw.line(window, BLACK, (0, 625), (850, 625), 2)
        pygame.draw.line(window, BLACK, (0, 725), (850, 725), 2)
        #draw horizontal lines
        pygame.draw.line(window, BLACK, (125, 0), (125, 850), 2)
        pygame.draw.line(window, BLACK, (225, 0), (225, 850), 2)
        pygame.draw.line(window, BLACK, (325, 0), (325, 850), 2)
        pygame.draw.line(window, BLACK, (425, 0), (425, 850), 2)
        pygame.draw.line(window, BLACK, (525, 0), (525, 850), 2)
        pygame.draw.line(window, BLACK, (625, 0), (625, 850), 2)
        pygame.draw.line(window, BLACK, (725, 0), (725, 850), 2)
        
        #draw right side panel
        pygame.draw.rect(window, GRAY, (850, 0, 500, 850))
        
        #draw circle
        pygame.draw.circle(window, BLACK, (75, 75), 36)
        
        pygame.draw.circle(window, BLACK, (177, 78), 35)
        pygame.draw.circle(window, WHITE, (175, 75), 36)        
        
        pygame.display.update()