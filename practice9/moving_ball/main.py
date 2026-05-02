import pygame
import sys
from ball import Ball

pygame.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

ball = Ball(WIDTH // 2, HEIGHT // 2, 25, WIDTH, HEIGHT, (255, 0, 0), 1)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    ball.update(keys, 1)

    screen.fill((255, 255, 255))
    ball.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()