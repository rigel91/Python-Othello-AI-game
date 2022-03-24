import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
LIGHTGRAY = (170,170,170)
DARKGRAY = (100,100,100)

class Panel:
    def __init__(self):
        pygame.font.init()        

    def displayAll(self, window, turn, blackScore, whiteScore, toggle, player1, player2):
        self.displayTitle(window)
        self.displayPlayerTurn(window, turn)
        self.displayScore(window, blackScore, whiteScore)
        self.displayStartButton(window)
        self.displayValidCheckButton(window, toggle)

        self.displayPlayer1Option(window, player1)
        self.displayVS(window)
        self.displayPlayer2Option(window, player2)

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
            pygame.draw.rect(window, DARKGRAY, (1100, 225, 230, 75))
        else:
            pygame.draw.rect(window, LIGHTGRAY, (1100, 225, 230, 75))

        font = pygame.font.SysFont('Arial', 45)
        img = font.render("Valid Moves", False, BLACK)
        window.blit(img, (1115, 232))

    def displayPlayer1Option(self, window, toggle):
        if toggle == "PLAYER":
            pygame.draw.rect(window, DARKGRAY, (900, 400, 150, 75))
            font = pygame.font.SysFont('Arial', 50)
            img = font.render("Player", False, BLACK)
            window.blit(img, (920, 407))
        else:
            pygame.draw.rect(window, LIGHTGRAY, (900, 400, 150, 75))
            font = pygame.font.SysFont('Arial', 50)
            img = font.render("Player", False, BLACK)
            window.blit(img, (920, 407))

        if toggle == "RANDOM":
            pygame.draw.rect(window, DARKGRAY, (900, 500, 150, 75))
            font = pygame.font.SysFont('Arial', 45)
            img = font.render("Random", False, BLACK)
            window.blit(img, (905, 509))
        else:
            pygame.draw.rect(window, LIGHTGRAY, (900, 500, 150, 75))
            font = pygame.font.SysFont('Arial', 45)
            img = font.render("Random", False, BLACK)
            window.blit(img, (905, 509))

        if toggle == "EASY":
            pygame.draw.rect(window, DARKGRAY, (900, 600, 150, 75))
            font = pygame.font.SysFont('Arial', 50)
            img = font.render("Easy", False, BLACK)
            window.blit(img, (930, 607))
        else:
            pygame.draw.rect(window, LIGHTGRAY, (900, 600, 150, 75))
            font = pygame.font.SysFont('Arial', 50)
            img = font.render("Easy", False, BLACK)
            window.blit(img, (930, 607))

        if toggle == "HARD":
            pygame.draw.rect(window, DARKGRAY, (900, 700, 150, 75))
            font = pygame.font.SysFont('Arial', 50)
            img = font.render("Hard", False, BLACK)
            window.blit(img, (930, 707))
        else:
            pygame.draw.rect(window, LIGHTGRAY, (900, 700, 150, 75))
            font = pygame.font.SysFont('Arial', 50)
            img = font.render("Hard", False, BLACK)
            window.blit(img, (930, 707))

    def displayVS(self, window):
        font = pygame.font.SysFont('Arial', 75)
        img = font.render("VS", False, BLACK)
        window.blit(img, (1074, 550))

    def displayPlayer2Option(self, window, toggle):
        if toggle == "PLAYER":
            pygame.draw.rect(window, DARKGRAY, (1175, 400, 150, 75))
            font = pygame.font.SysFont('Arial', 50)
            img = font.render("Player", False, BLACK)
            window.blit(img, (1190, 407))
        else:
            pygame.draw.rect(window, LIGHTGRAY, (1175, 400, 150, 75))
            font = pygame.font.SysFont('Arial', 50)
            img = font.render("Player", False, BLACK)
            window.blit(img, (1190, 407))

        if toggle == "RANDOM":
            pygame.draw.rect(window, DARKGRAY, (1175, 500, 150, 75))
            font = pygame.font.SysFont('Arial', 45)
            img = font.render("Random", False, BLACK)
            window.blit(img, (1180, 509))
        else:
            pygame.draw.rect(window, LIGHTGRAY, (1175, 500, 150, 75))
            font = pygame.font.SysFont('Arial', 45)
            img = font.render("Random", False, BLACK)
            window.blit(img, (1180, 509))

        if toggle == "EASY":
            pygame.draw.rect(window, DARKGRAY, (1175, 600, 150, 75))
            font = pygame.font.SysFont('Arial', 50)
            img = font.render("Easy", False, BLACK)
            window.blit(img, (1205, 607))
        else:
            pygame.draw.rect(window, LIGHTGRAY, (1175, 600, 150, 75))
            font = pygame.font.SysFont('Arial', 50)
            img = font.render("Easy", False, BLACK)
            window.blit(img, (1205, 607))

        if toggle == "HARD":
            pygame.draw.rect(window, DARKGRAY, (1175, 700, 150, 75))
            font = pygame.font.SysFont('Arial', 50)
            img = font.render("Hard", False, BLACK)
            window.blit(img, (1205, 707))
        else:
            pygame.draw.rect(window, LIGHTGRAY, (1175, 700, 150, 75))
            font = pygame.font.SysFont('Arial', 50)
            img = font.render("Hard", False, BLACK)
            window.blit(img, (1205, 707))


