import pygame


class Healthbars():
    def health_bar(self, arens, arenas_count, screen, current_health_1, current_health_2):
        # Create a new surface for the health bars
        health_bar_surface = pygame.Surface((1920, 1080), pygame.SRCALPHA)

        # Draw health bars on the new surface
        pygame.draw.rect(health_bar_surface, (0, 255, 0), (38, 20, current_health_1 * 3, 40))
        pygame.draw.rect(health_bar_surface, (255, 255, 255), (38, 20, current_health_1 * 3, 40), width=2)
        pygame.draw.rect(health_bar_surface, (0, 255, 0), (1560, 20, current_health_2 * 3, 40))
        pygame.draw.rect(health_bar_surface, (255, 255, 255), (1560, 20, current_health_2 * 3, 40), width=2)

        # Blit both the arena image and health bars onto the main screen
        screen.blit(arens[arenas_count], (0, 0))
        screen.blit(health_bar_surface, (0, 0))
