import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((640, 480), 0, 32)
sprite1 = pygame.image.load("./images/LogoYoutube.png")

pygame.display.set_caption("Desplazamiento con Teclado")

screen.fill((0, 0, 0))
pygame.display.update()
game_over = False
x, y = (0, 0)

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
    pressed = pygame.key.get_pressed()
    if pressed[K_UP]:
        y -= 0.1
    if pressed[K_DOWN]:
        y += 0.1
    if pressed[K_LEFT]:
        x -= 0.1
    if pressed[K_RIGHT]:
        x += 0.1

    screen.blit(sprite1, (x, y))
    pygame.display.update()
pygame.quit()
