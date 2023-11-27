import pygame  # импортируем pygame

# Инициализация Pygame
pygame.init()
screen = pygame.display.set_mode((900, 515))
pygame.display.set_caption("Mortal Fight")
icon = pygame.image.load("logo.jpg")
pygame.display.set_icon(icon)

pygame.mixer.init()
pygame.mixer.music.load("music.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

# Определяющие положение персонажа координаты
x, y = -10, 110
early_x = -120
final_x = 700
speed = 5

# Определяющие координаты положения второго персонажа
x2, y2 = 600, 110
early_x2 = -120
final_x2 = 700
speed2 = 5

# Загружаем изображения
bg = pygame.image.load("location.jpg")
player = pygame.image.load("Character1/character.png")
player2 = pygame.image.load("Character1/-character.png")

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

current_frame2 = 4

health_bar_1 = pygame.image.load("health_bar.png")
health_bar_2 = pygame.image.load("health_bar.png")

clock = pygame.time.Clock()

# Значения хэлф баров
current_health_1 = 100
current_health_2 = 100

standing = True
left = False
right = True

standing2 = True
left2 = False
right2 = True

running = True  # флаг работы
while running:
    clock.tick(60)  # обновление экрана 60 раз в секунду

    # Привязываем кнопки для передвижения
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
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
    if keys[pygame.K_d]:
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

    if keys[pygame.K_LEFT]:
        if x2 - speed2 < early_x2:
            x2 = early_x2
            if current_frame2 == 0:
                current_frame2 = 9
            current_frame2 -= 1
        else:
            x2 -= speed2
            if current_frame2 == 0:
                current_frame2 = 9
            current_frame2 -= 1
        standing2 = False
        right2 = False
        left2 = True

    if keys[pygame.K_RIGHT]:
        if x2 + speed2 > early_x2:
            x2 = final_x2
            if current_frame2 == 21:
                current_frame2 = 12
            current_frame2 += 1
        else:
            x2 += speed2
            if current_frame2 == 21:
                current_frame2 = 12
            current_frame2 += 1
        standing2 = False
        right2 = False
        left2 = True

    # Отображаем элементы игры на экране
    screen.blit(bg, (0, 0))
    if not keys[pygame.K_a] and not keys[pygame.K_d]:
        if left:
            screen.blit(pygame.image.load("Character1/character.png"), (x, y))
        elif left2:
            screen.blit(pygame.image.load("Character1/-character.png"), (x2, y2))
        elif right:
            screen.blit(player, (x, y))
        elif right2:
            screen.blit(player2, (x2, y2))
    elif keys[pygame.K_a] and not keys[pygame.K_d]:
        screen.blit(anim_images[current_frame], (x, y))
        screen.blit(anim_images[current_frame2], (x2, y2))
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