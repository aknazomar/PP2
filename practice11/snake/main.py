import pygame
from game import game_loop
from db import get_top, get_or_create_player, init_db
from screens import draw_leaderboard

pygame.init()

init_db()

screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Snake")

font = pygame.font.SysFont("Arial", 30)

state     = "MENU"
username  = ""
player_id = None
running   = True

while running:
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if state == "MENU":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if username.strip():
                        player_id = get_or_create_player(username)
                        state = "GAME"
                elif event.key == pygame.K_l:
                    state = "LEADERBOARD"
                elif event.key == pygame.K_BACKSPACE:
                    username = username[:-1]
                else:
                    if event.unicode.isprintable():
                        username += event.unicode

        elif state == "LEADERBOARD":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    state = "MENU"

    if state == "MENU":
        screen.blit(
            font.render("Enter username: " + username, True, (0, 0, 0)),
            (50, 180),
        )
        screen.blit(
            font.render("ENTER - Play | L - Leaderboard", True, (120, 120, 120)),
            (50, 230),
        )

    elif state == "GAME":
        game_loop(screen, player_id)
        username = ""        # clear name after game ends
        state    = "MENU"

    elif state == "LEADERBOARD":
        data = get_top()
        draw_leaderboard(screen, data)

    pygame.display.update()

pygame.quit()