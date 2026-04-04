import pygame

def rotate_hand(surface, angle, length_scale, clock_center):
    """
    Вращает стрелку, удерживая её конец (кольцо) в центре часов.
    """
    # 1. Масштабируем исходное изображение стрелки
    scaled_w = int(surface.get_width() * length_scale)
    scaled_h = int(surface.get_height() * length_scale)
    # Используем smoothscale для лучшего качества при масштабировании
    scaled_hand = pygame.transform.smoothscale(surface, (scaled_w, scaled_h))
    
    # 2. Определяем точку привязки (pivot) на отмасштабированном изображении.
    # Кольцо находится внизу стрелки, по центру ширины.
    pivot_x = scaled_w // 2
    pivot_y = scaled_h - (scaled_w // 2) # Смещаем чуть вверх от самого низа, в центр кольца

    # 3. Вычисляем вектор от геометрического центра изображения до точки привязки
    # В Pygame координаты идут от верхнего левого угла (0,0)
    image_center = (scaled_w // 2, scaled_h // 2)
    offset_center_to_pivot = pygame.math.Vector2(pivot_x - image_center[0], pivot_y - image_center[1])

    # 4. Вращаем вектор смещения.
    # Pygame rotate вращает против часовой стрелки, поэтому используем положительный угол.
    rotated_offset = offset_center_to_pivot.rotate(angle)

    # 5. Вращаем само изображение стрелки.
    # Чтобы стрелка вращалась по часовой, передаем отрицательный угол.
    rotated_image = pygame.transform.rotate(scaled_hand, -angle)
    
    # 6. Вычисляем новые координаты для вывода (blit) повернутого изображения.
    # Мы берем центр часов и вычитаем повернутый вектор смещения.
    # Это гарантирует, что точка привязки (кольцо) совпадет с центром часов.
    new_rect = rotated_image.get_rect(center = (clock_center[0] - rotated_offset.x, clock_center[1] - rotated_offset.y))
    
    return rotated_image, new_rect