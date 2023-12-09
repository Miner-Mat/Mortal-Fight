import pygame


class Healthbars():
    def health_bar(self, arens, arenas_count, screen, current_health_1, current_health_2):
        health_bar_surface = pygame.Surface((1920, 1080), pygame.SRCALPHA)

        pygame.draw.rect(health_bar_surface, (0, 255, 0), (38, 20, current_health_1 * 3, 40))
        pygame.draw.rect(health_bar_surface, (255, 255, 255), (38, 20, current_health_1 * 3, 40), width=2)
        pygame.draw.rect(health_bar_surface, (0, 255, 0), (1560, 20, current_health_2 * 3, 40))
        pygame.draw.rect(health_bar_surface, (255, 255, 255), (1560, 20, current_health_2 * 3, 40), width=2)

        screen.blit(arens[arenas_count], (0, 0))
        screen.blit(health_bar_surface, (0, 0))
