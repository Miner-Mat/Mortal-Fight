import pygame  # импортируем pygame
from healthbars import Healthbars  # Импортируем класс Healthbars

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
bg1 = pygame.image.load("location.jpg").convert_alpha()

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

# Арены для сражения
arens = [pygame.image.load("arenas/location.jpg"), pygame.image.load("arenas/location2.jpg"),
         pygame.image.load("arenas/location1.jpg"), pygame.image.load("arenas/location3.jpg"),
         pygame.image.load("arenas/location4.jpg")]

current_frame = 0  # текущий кадр
current_frame_run = 0  # последний обновлённый кадр бега персонажа
current_frame_fight = 0
animation_delay = 100  # Задержка между кадрами
last_update = pygame.time.get_ticks()  # последний обновлённый кадр

current_frame2 = 0
current_frame_run2 = 0

clock = pygame.time.Clock()

# Значения хэлф баров
current_health_1 = 100
current_health_2 = 100

# Флаги состояния положения персонажа
standing = True
left = False
right = True

standing2 = True
left2 = True
right2 = False

# Счетчик анимаций
count = 6

# Счетчик выбора арен
arenas_count = 2

# Текст - загаловок игры на входном экране
game_entery_name = pygame.font.Font("Fonts/unispace bd.ttf", 100)
text_surface = game_entery_name.render("MORTAL FIGHT", True, (255, 107, 107))

# Кнопка начала игры
play_button = pygame.Rect(830, 220, 300, 100)
play_text_font = pygame.font.Font("Fonts/unispace bd.ttf", 70)
play_text = play_text_font.render("PLAY", True, (255, 107, 107))
play_text_rect = play_text.get_rect(center=play_button.center)

# Кнопка выхода из игры
exit_button = pygame.Rect(830, 350, 300, 100)
exit_text_font = pygame.font.Font("Fonts/unispace bd.ttf", 70)
exit_text = exit_text_font.render("EXIT", True, (255, 107, 107))
exit_text_rect = exit_text.get_rect(center=exit_button.center)

# Кнопка возврата в меню игры
back_button = pygame.Rect(1230, 20, 50, 50)
back_image = pygame.transform.scale(pygame.image.load("krest.png").convert_alpha(), (40, 40))
back_image_rect = back_image.get_rect(center=back_button.center)

# Заголовок окна выбора арены
arena_text_font = pygame.font.Font("Fonts/unispace bd.ttf", 70)
arena_text = arena_text_font.render("ARENA", True, (255, 107, 107))

# Окно выбора арены
aren_window = pygame.Rect(230, 600, 600, 400)
arena = pygame.transform.scale(arens[arenas_count], (600, 400))
arena_rect = arena.get_rect(center=aren_window.center)

# Стрелки выбора арены
left_strelka = pygame.transform.scale(pygame.image.load("left_strelka.png"), (100, 100))
left_strelka_rect = left_strelka.get_rect(topleft=(100, 750))
right_strelka = pygame.transform.scale(pygame.image.load("right_strelka.png"), (100, 100))
right_strelka_rect = right_strelka.get_rect(topleft=(850, 750))
health = Healthbars()  # Объявляем класс хэлфбаров


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


flag = False
running = True  # флаг работы
while running:
    clock.tick(60)  # обновление экрана 60 раз в секунду
    arena = pygame.transform.scale(arens[arenas_count], (600, 400))
    if not flag:
        screen.fill((192, 6, 13))
        screen.blit(text_surface, (600, 50))
        pygame.draw.rect(screen, (170, 0, 0), play_button)
        screen.blit(play_text, play_text_rect)
        pygame.draw.rect(screen, (170, 0, 0), exit_button)
        screen.blit(exit_text, exit_text_rect)
        pygame.draw.rect(screen, (170, 0, 0), aren_window)
        screen.blit(arena, arena_rect)
        screen.blit(arena_text, (420, 500))
        screen.blit(left_strelka, (100, 750))
        screen.blit(right_strelka, (850, 750))

    if flag:
        health.health_bar(arens, arenas_count, screen, current_health_1, current_health_2)
        key_check()  # вызываем проверку нажатий
        screen.blit(arens[arenas_count], (0, 0))  # отрисовываем фон
        pygame.draw.rect(screen, (170, 0, 0), back_button)
        screen.blit(back_image, back_image_rect)

        key_work()  # вызываем обработку нажатий
        frame_check()  # вызываем проверку кадров
    pygame.display.update()  # обновляем окно

    # Скрипт выхода из игры
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if play_button.collidepoint(event.pos):
                flag = True
            elif left_strelka_rect.collidepoint(event.pos):
                arenas_count -= 1
                if arenas_count < 0:
                    arenas_count = len(arens) - 1
            elif right_strelka_rect.collidepoint(event.pos):
                arenas_count += 1
                if arenas_count >= len(arens):
                    arenas_count = 0
            elif back_button.collidepoint(event.pos):
                flag = False
                # Сбрасываем значения всех переменных до по умолчанию
                x, y = 160, 710
                early_x = -120
                final_x = 1720
                speed = 5
                x2, y2 = 1580, 710
                early_x2 = -120
                final_x2 = 1720
                speed2 = 5
                current_frame = 0
                current_frame_run = 0
                current_frame_fight = 0
                animation_delay = 100
                last_update = pygame.time.get_ticks()
                current_frame2 = 0
                current_frame_run2 = 0
                current_health_1 = 100
                current_health_2 = 100
                standing = True
                left = False
                right = True
                standing2 = True
                left2 = True
                right2 = False
                count = 6

            elif exit_button.collidepoint(event.pos):
                running = False

        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
