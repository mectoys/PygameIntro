import pygame

pygame.init()

screen = pygame.display.set_mode((640, 480), 0, 32)

pygame.display.set_caption("Hola Mundo")

screen.fill((0, 0, 0))
pygame.display.update()

game_over = False

# Bucle principal del juego
while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

pygame.quit()
