import pygame

class Healthbars():
    def health_to_all(self, arens, current_health_1, current_health_2):
        for i in arens:
            pygame.draw.rect(i, (0, 255, 0), (38, 20, current_health_1 * 3, 40))
            pygame.draw.rect(i, (255, 255, 255), (38, 20, current_health_1 * 3, 40), width=2)
            pygame.draw.rect(i, (0, 255, 0), (1560, 20, current_health_2 * 3, 40))
            pygame.draw.rect(i, (255, 255, 255), (1560, 20, current_health_2 * 3, 40), width=2)

    def health_bar(self, arens, arenas_count, current_health_1, current_health_2):  # Отрисовка хэлф баров
        pygame.draw.rect(arens[arenas_count], (0, 255, 0), (38, 20, current_health_1 * 3, 40))
        pygame.draw.rect(arens[arenas_count], (255, 255, 255), (38, 20, current_health_1 * 3, 40), width=2)
        pygame.draw.rect(arens[arenas_count], (0, 255, 0), (1560, 20, current_health_2 * 3, 40))
        pygame.draw.rect(arens[arenas_count], (255, 255, 255), (1560, 20, current_health_2 * 3, 40), width=2)
