import pygame

pygame.init()
screen = pygame.display.set_mode((900, 515))
pygame.display.set_caption("Mortal Fight")
icon = pygame.image.load("logo.jpg")
pygame.display.set_icon(icon)

bg = pygame.image.load("location.jpg")
player = pygame.image.load("character.png")

health_bar_1 = pygame.image.load("health_bar.png")
health_bar_2 = pygame.image.load("health_bar.png")

current_health_1 = 100
current_health_2 = 100

running = True
while running:
    screen.blit(bg, (0, 0))
    screen.blit(player, (-20, 80))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

    pygame.draw.rect(bg, (0, 255, 0), (10, 20, current_health_1 * 3, 20))
    pygame.draw.rect(bg, (0, 255, 0), (580, 20, current_health_1 * 3, 20))
