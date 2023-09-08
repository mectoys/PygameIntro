import pygame

# Inicializamos Pygame
pygame.init()

# Creamos una ventana de 640x480 píxeles
screen = pygame.display.set_mode((640, 480), 0, 32)

# Cargamos una imagen (sprite) desde el archivo "./images/MectoysLogo.png"
sprite1 = pygame.image.load("./images/LogoYoutube.png")
#Establecer la scala de un sprite
sprite1 = pygame.transform.scale(sprite1, (100, 100))
# Establecemos el título de la ventana
pygame.display.set_caption("Hola Pygame")

# Llenamos la pantalla con un color negro
screen.fill((0, 0, 0))

# Actualizamos la pantalla para que se muestre el fondo negro
pygame.display.update()

# Inicializamos una variable para controlar el bucle del juego
game_over = False
#Establecer el centrado optimo de un sprite
x = (screen.get_width() - sprite1.get_width()) / 2
y = (screen.get_height() - sprite1.get_height()) / 2

# Iniciamos un bucle principal del juego
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    # Dibujamos la imagen en la pantalla en la posición calculada (centrada)
    screen.blit(sprite1, (x, y))
    # función clave en Pygame para la representación gráfica. Te permite copiar una superficie
    # (en este caso, una imagen) en otra superficie (la pantalla),

    # Actualizamos la pantalla para mostrar la imagen
    pygame.display.update()

# Una vez que el bucle se ha completado (el usuario cerró la ventana),
# salimos de Pygame y cerramos la ventana
pygame.quit()
