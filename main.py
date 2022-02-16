import pygame

WIDTH, HEIGHT, FPS = 1000, 800, 60

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Othello')

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
        
        #framerate
        clock.tick(FPS)

    pygame.quit()

main()