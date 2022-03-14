import pygame

BLACK = (0, 0, 0)

class Panel:
    def __init__(self):
        pygame.font.init()        

    def displayAll(self, window, turn, blackScore, whiteScore):
        self.displayTitle(window)
        self.displayPlayerTurn(window, turn)
        self.displayScore(window, blackScore, whiteScore)

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
        window.blit(img, (900, 200))

