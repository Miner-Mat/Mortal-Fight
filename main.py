import pygame  # импортируем pygame

# Инициализация Pygame
pygame.init()
screen = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)  # Задаём разрешение основного окна
pygame.display.set_caption("Mortal Fight")  # Задаём название программе
icon = pygame.image.load("logo.jpg")  # Загружаем логотип
pygame.display.set_icon(icon)  # Выставляем логотип

pygame.mixer.init()  # инициализируем функцию добавления музыки
pygame.mixer.music.load("music.mp3")  # Загружаем музыку
pygame.mixer.music.set_volume(0.5)  # Выставляем громкость
pygame.mixer.music.play(-1)  # Запускаем бесконечный цикл проигрывания

# Определяющие положение персонажа переменные
x, y = 160, 710
early_x = -120
final_x = 1720
speed = 5

# Определяющие положение второго персонажа переменные
x2, y2 = 1580, 710
early_x2 = -120
final_x2 = 1720
speed2 = 5

# Загружаем изображения
bg = pygame.image.load("location.jpg").convert_alpha()

# Анимации персонажа в момент неподвижности вправо
anim_st = [pygame.image.load("Character_st/1st.png"), pygame.image.load("Character_st/2st.png"),
           pygame.image.load("Character_st/3st.png"), pygame.image.load("Character_st/4st.png"),
           pygame.image.load("Character_st/5st.png"), pygame.image.load("Character_st/6st.png"),
           pygame.image.load("Character_st/7st.png")]

# Анимации персонажа в момент неподвижности влево
minus_anim_st = [pygame.image.load("-Character_st/1st.png"), pygame.image.load("-Character_st/2st.png"),
                 pygame.image.load("-Character_st/3st.png"), pygame.image.load("-Character_st/4st.png"),
                 pygame.image.load("-Character_st/5st.png"), pygame.image.load("-Character_st/6st.png"),
                 pygame.image.load("-Character_st/7st.png")]

# Анимации персонажа во время атаки
anim_fight = [pygame.image.load("Character_fight/Attack_1.png"), pygame.image.load("Character_fight/Attack_2.png"),
              pygame.image.load("Character_fight/Attack_3.png"), pygame.image.load("Character_fight/Attack_4.png"),
              pygame.image.load("Character_fight/Attack_5.png")]

# Анимации персонажа во время бега
anim_run = [pygame.image.load("charact_run/run1.png"), pygame.image.load("charact_run/run2.png"),
            pygame.image.load("charact_run/run3.png"), pygame.image.load("charact_run/run4.png"),
            pygame.image.load("charact_run/run5.png"), pygame.image.load("charact_run/run6.png"),
            pygame.image.load("charact_run/run7.png"), pygame.image.load("charact_run/run8.png")]

current_frame = 0  # текущий кадр
current_frame_run = 0  # последний обновлённый кадр бега персонажа
current_frame_fight = 0
animation_delay = 100  # Задержка между кадрами
last_update = pygame.time.get_ticks()  # последний обновлённый кадр

current_frame2 = 0
current_frame_run2 = 0

# Загружаем изображения первого и второго хэлфбара
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
left2 = True
right2 = False

count = 6


def health_bar():  # Отрисовка хэлф баров
    pygame.draw.rect(bg, (0, 255, 0), (38, 20, current_health_1 * 3, 40))
    pygame.draw.rect(bg, (255, 255, 255), (38, 20, current_health_1 * 3, 40), width=2)
    pygame.draw.rect(bg, (0, 255, 0), (1560, 20, current_health_2 * 3, 40))
    pygame.draw.rect(bg, (255, 255, 255), (1560, 20, current_health_2 * 3, 40), width=2)


def frame_check():  # Проверка кадров
    global current_frame, count, current_frame2, current_frame_fight
    if current_frame == 6:
        current_frame = 0
    elif count % 6 == 0:
        current_frame += 1
        current_frame2 += 1
    if current_frame2 == 6:
        current_frame2 = 0
    if current_frame_fight == 4:
        current_frame_fight = 0
    elif count % 6 == 0:
        current_frame_fight += 1
    count += 1


def key_check():  # Проверка нажатий
    global x, current_frame_run, early_x, early_x2, standing, right, left, speed, final_x
    global standing2, right2, left2, x2, current_frame_run2, speed2, final_x2, early_x2
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        if x - speed < early_x:
            x = early_x
            if current_frame_run == 0:
                current_frame_run = 7
            current_frame_run -= 1
        else:
            x -= speed
            if current_frame_run == 0:
                current_frame_run = 7
            current_frame_run -= 1
        standing = False
        right = False
        left = True

    if keys[pygame.K_d]:
        if x + speed > final_x:
            x = final_x
            if current_frame_run == 7:
                current_frame_run = 0
            current_frame_run += 1
        else:
            x += speed
            if current_frame_run == 7:
                current_frame_run = 0
            current_frame_run += 1
        standing = False
        right = True
        left = False

    if keys[pygame.K_LEFT]:
        if x2 - speed2 < early_x2:
            x2 = early_x2
            if current_frame_run2 == 0:
                current_frame_run2 = 7
            current_frame_run2 -= 1
        else:
            x2 -= speed2
            if current_frame_run2 == 0:
                current_frame_run2 = 7
            current_frame_run2 -= 1
        standing2 = False
        left2 = True
        right2 = False

    if keys[pygame.K_RIGHT]:
        if x2 + speed2 > final_x2:
            x2 = final_x2
            if current_frame_run2 == 7:
                current_frame_run2 = 0
            current_frame_run2 += 1
        else:
            x2 += speed2
            if current_frame_run2 == 7:
                current_frame_run2 = 0
            current_frame_run2 += 1
        standing2 = False
        left2 = False
        right2 = True


def key_work():  # Обработка нажатий
    global current_health_2
    keys = pygame.key.get_pressed()
    if keys[pygame.K_f]:
        current_health_2 -= 25

    if not keys[pygame.K_a] and not keys[pygame.K_d] and not keys[pygame.K_f]:
        if left:
            screen.blit(pygame.transform.scale(minus_anim_st[current_frame], (170, 300)), (x, y))
        if right:
            screen.blit(pygame.transform.scale(anim_st[current_frame], (170, 300)), (x, y))
    elif keys[pygame.K_a]:
        screen.blit(pygame.transform.flip(pygame.transform.scale(anim_run[current_frame], (290, 300)), True, False),
                    (x, y))
    elif keys[pygame.K_d]:
        screen.blit(pygame.transform.scale(anim_run[current_frame], (290, 300)), (x, y))
    elif keys[pygame.K_f]:
        screen.blit(pygame.transform.scale(anim_fight[current_frame_fight], (290, 300)), (x, y))

    if not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT] and not keys[pygame.K_f]:
        if right2:
            screen.blit(
                pygame.transform.flip(pygame.transform.scale(minus_anim_st[current_frame2], (170, 300)), True, False),
                (x2, y2))
        if left2:
            screen.blit(pygame.transform.flip(pygame.transform.scale(anim_st[current_frame2], (170, 300)), True, False),
                        (x2, y2))
    elif keys[pygame.K_LEFT]:
        screen.blit(pygame.transform.flip(pygame.transform.scale(anim_run[current_frame2], (290, 300)), True, False),
                    (x2, y2))
    elif keys[pygame.K_RIGHT]:
        screen.blit(pygame.transform.scale(anim_run[current_frame2], (290, 300)), (x2, y2))


running = True  # флаг работы
while running:
    clock.tick(60)  # обновление экрана 60 раз в секунду
    health_bar()  # вызываем отрисовку хэлф баров

    key_check()  # вызываем проверку нажатий
    screen.blit(bg, (0, 0))  # отрисовываем фон

    key_work()  # вызываем обработку нажатий
    frame_check()  # вызываем проверку кадров
    pygame.display.update()  # обновляем окно

    # Скрипт выхода из игры
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
