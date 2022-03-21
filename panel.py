import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
LIGHTGRAY = (170,170,170)
DARKGREY = (100,100,100)

class Panel:
    def __init__(self):
        pygame.font.init()        

    def displayAll(self, window, turn, blackScore, whiteScore, toggle):
        self.displayTitle(window)
        self.displayPlayerTurn(window, turn)
        self.displayScore(window, blackScore, whiteScore)
        self.displayStartButton(window)
        self.displayValidCheckButton(window, toggle)

    def displayTitle(self, window):
        font = pygame.font.SysFont('Arial', 72)
        img = font.render("Othello Game", False, BLACK)
        window.blit(img, (925, 15))

    def displayPlayerTurn(self, window, turn):        
        font = pygame.font.SysFont('Arial', 32)
        img = font.render("Player Turn: {str}".format(str = turn), False, BLACK)
        window.blit(img, (980, 115))

    def displayScore(self, window, blackScore, whiteScore):
        font = pygame.font.SysFont('Arial', 42)
        img = font.render("Score: Black-{black}     White-{white}".format(black = blackScore, white = whiteScore), False, BLACK)
        window.blit(img, (900, 165))

    def displayStartButton(self, window):
        pygame.draw.rect(window, LIGHTGRAY, (900, 225, 150, 75))
        font = pygame.font.SysFont('Arial', 50)
        img = font.render("Start", False, BLACK)
        window.blit(img, (933, 232))
    
    def displayValidCheckButton(self, window, toggle):
        if toggle:
            pygame.draw.rect(window, DARKGREY, (1100, 225, 230, 75))
        else:
            pygame.draw.rect(window, LIGHTGRAY, (1100, 225, 230, 75))

        font = pygame.font.SysFont('Arial', 45)
        img = font.render("Valid Moves", False, BLACK)
        window.blit(img, (1115, 232))


