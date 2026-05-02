import pygame
import sys
from player import Player

pygame.init()

WIDTH, HEIGHT = 600, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Music Player")

clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 36)

player = Player("practice9/music_player/music")


def draw():
    screen.fill((30, 30, 30))

    track_text = font.render(
        f"Track: {player.get_current_track_name()}",
        True,
        (255, 255, 255),
    )

    pos_text = font.render(
        f"Time: {player.get_position()} sec",
        True,
        (200, 200, 200),
    )

    controls_text = font.render(
        "P-Play S-Stop N-Next B-Back Q-Quit",
        True,
        (150, 150, 150),
    )

    screen.blit(track_text, (20, 50))
    screen.blit(pos_text, (20, 100))
    screen.blit(controls_text, (20, 200))


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                player.play()
            elif event.key == pygame.K_s:
                player.stop()
            elif event.key == pygame.K_n:
                player.next_track()
            elif event.key == pygame.K_b:
                player.prev_track()
            elif event.key == pygame.K_q:
                running = False

    draw()
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()