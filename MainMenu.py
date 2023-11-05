import pygame


class MainMenu:
    def __init__(self):
        self.font = pygame.font.SysFont('Arial', 100)
        self.title = self.font.render("Juego Principal", True, (255, 255, 255))
        self.title_position = (10, 10)
        self.second_menu = None

    def update(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return self.second_menu

        return self

    def draw(self, screen):
        screen.blit(self.title, self.title_position)
