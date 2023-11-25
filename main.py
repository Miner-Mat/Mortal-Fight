import pygame  # импортируем pygame

# Инициализация Pygame
pygame.init()
screen = pygame.display.set_mode((900, 515))
pygame.display.set_caption("Mortal Fight")
icon = pygame.image.load("logo.jpg")
pygame.display.set_icon(icon)

# Определяющие положение персонажа координаты
x, y = -10, 110
early_x = -120
final_x = 700
speed = 5

# Загружаем изображения
bg = pygame.image.load("location.jpg")
player = pygame.image.load("Character1/character.png")

anim_images = [pygame.image.load("Character1/-run10.png"), pygame.image.load("Character1/-run9.png"),
               pygame.image.load("Character1/-run8.png"), pygame.image.load("Character1/-run7.png"),
               pygame.image.load("Character1/-run6.png"), pygame.image.load("Character1/-run5.png"),
               pygame.image.load("Character1/-run4.png"),
               pygame.image.load("Character1/-run3.png"),
               pygame.image.load("Character1/-run2.png"),
               pygame.image.load("Character1/-run1.png"), pygame.image.load("Character1/-character.png"),
               pygame.image.load("Character1/character.png"),
               pygame.image.load("Character1/run1.png"), pygame.image.load("Character1/run2.png"),
               pygame.image.load("Character1/run3.png"), pygame.image.load("Character1/run4.png"),
               pygame.image.load("Character1/run5.png"), pygame.image.load("Character1/run6.png"),
               pygame.image.load("Character1/run7.png"), pygame.image.load("Character1/run8.png"),
               pygame.image.load("Character1/run9.png"), pygame.image.load("Character1/run10.png")]
current_frame = 3
animation_delay = 100  # Задержка между кадрами
last_update = pygame.time.get_ticks()

health_bar_1 = pygame.image.load("health_bar.png")
health_bar_2 = pygame.image.load("health_bar.png")

clock = pygame.time.Clock()

# Значения хэлф баров
current_health_1 = 100
current_health_2 = 100

standing = True
left = False
right = True

running = True  # флаг работы
while running:
    clock.tick(60)  # обновление экрана 60 раз в секунду

    # Привязываем кнопки для передвижения
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        if x - speed < early_x:
            x = early_x
            if current_frame == 0:
                current_frame = 9
            current_frame -= 1
        else:
            x -= speed
            if current_frame == 0:
                current_frame = 9
            current_frame -= 1
        standing = False
        right = False
        left = True
    if keys[pygame.K_RIGHT]:
        if x + speed > final_x:
            x = final_x
            if current_frame == 21:
                current_frame = 12
            current_frame += 1
        else:
            x += speed
            if current_frame == 21:
                current_frame = 12
            current_frame += 1
        standing = False
        right = True
        left = False

    # Отображаем элементы игры на экране
    screen.blit(bg, (0, 0))
    if not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
        if left:
            screen.blit(pygame.image.load("Character1/-character.png"), (x, y))
        elif right:
            screen.blit(player, (x, y))
    else:
        screen.blit(anim_images[current_frame], (x, y))
    pygame.display.update()

    # Скрипт выхода из игры
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

    # Отрисовка хэлф баров
    pygame.draw.rect(bg, (0, 255, 0), (18, 20, current_health_1 * 3, 20))
    pygame.draw.rect(bg, (255, 255, 255), (18, 20, current_health_1 * 3, 20), width=2)
    pygame.draw.rect(bg, (0, 255, 0), (580, 20, current_health_1 * 3, 20))
    pygame.draw.rect(bg, (255, 255, 255), (580, 20, current_health_1 * 3, 20), width=2)
