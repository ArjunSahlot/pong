import pygame


WIDTH, HEIGHT = 1000, 650
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

def main(win):
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


main(WINDOW)
