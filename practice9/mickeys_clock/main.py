import pygame
import time
import math
import os
from clock import rotate_hand

# Инициализация
WIDTH, HEIGHT = 800, 800
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey's Clock")
clock_timer = pygame.time.Clock()

# Настройка путей
base_path = os.path.dirname(__file__)
img_dir = os.path.join(base_path, 'images')

def load_image(name):
    path = os.path.join(img_dir, name)
    if not os.path.exists(path):
        print(f"ОШИБКА: Файл не найден по адресу: {path}")
        return None
    return pygame.image.load(path).convert_alpha()

# Загрузка (имена файлов должны быть как в Шаге 1)
bg = load_image('board.png') 
hand_min = load_image('righthand.png') # Правая рука - минуты
hand_sec = load_image('lefthand.png')  # Левая рука - секунды

if not bg or not hand_min or not hand_sec:
    print("Программа остановлена из-за отсутствия файлов.")
    pygame.quit()
    exit()

bg = pygame.transform.scale(bg, (WIDTH, HEIGHT))
center = (WIDTH // 2, HEIGHT // 2)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Логика времени
    t = time.localtime()
    # Для секунд используем time.time() для плавности
    seconds = t.tm_sec
    minutes = t.tm_min

    # Углы (вычитаем 90, если стрелка в исходном файле смотрит ВПРАВО)
    # Если стрелка в файле смотрит вверх, оставляем так:
    sec_angle = seconds * 6
    min_angle = minutes * 6

    # Отрисовка
    screen.blit(bg, (0, 0))

    # Рисуем стрелки (Минутная короче - 0.27, Секундная длиннее - 0.22)
    img_m, rect_m = rotate_hand(hand_min, min_angle, 0.22, center)
    screen.blit(img_m, rect_m)

    img_s, rect_s = rotate_hand(hand_sec, sec_angle, 0.25, center)
    screen.blit(img_s, rect_s)

    pygame.display.flip()
    clock_timer.tick(30)

pygame.quit()