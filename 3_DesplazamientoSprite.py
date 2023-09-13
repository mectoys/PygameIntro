import pygame
# importar las constantes y eventos
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((640, 480), 0, 32)
sprite1 = pygame.image.load("./images/LogoYoutube.png")

pygame.display.set_caption("Desplazamiento con Teclado")

screen.fill((0, 0, 0))
pygame.display.update()
game_over = False
x, y = (0, 0)
clock = pygame.time.Clock()

while not game_over:

    dt = clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
    pressed = pygame.key.get_pressed()
    if pressed[K_UP]:
        y -= 0.5 * dt
    if pressed[K_DOWN]:
        y += 0.5 * dt
    if pressed[K_LEFT]:
        x -= 0.5 * dt
    if pressed[K_RIGHT]:
        x += 0.5 * dt
    if pressed[K_ESCAPE]:
        x = 0
        y = 0
    if x > (screen.get_width() -sprite1.get_width()):
        x=(screen.get_width() -sprite1.get_width())

    if y> (screen.get_height() -sprite1.get_height()):
        y=(screen.get_height() -sprite1.get_height())

    if x<0:
        x=0
    if y<0:
        y=0
    screen.fill((0, 0, 0))
    screen.blit(sprite1, (x, y))
    pygame.display.update()
pygame.quit()
