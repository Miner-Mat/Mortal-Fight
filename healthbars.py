import pygame

class Healthbars():
    def health_bar(self, bg, current_health_1, current_health_2):  # Отрисовка хэлф баров
        pygame.draw.rect(bg, (0, 255, 0), (38, 20, current_health_1 * 3, 40))
        pygame.draw.rect(bg, (255, 255, 255), (38, 20, current_health_1 * 3, 40), width=2)
        pygame.draw.rect(bg, (0, 255, 0), (1560, 20, current_health_2 * 3, 40))
        pygame.draw.rect(bg, (255, 255, 255), (1560, 20, current_health_2 * 3, 40), width=2)
