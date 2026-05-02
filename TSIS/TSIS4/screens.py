import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY  = (180, 180, 180)
DARK  = (60, 60, 60)

_font       = None
_title_font = None


def _get_fonts():
    global _font, _title_font
    if _font is None:
        _font       = pygame.font.SysFont("Arial", 28)
        _title_font = pygame.font.SysFont("Arial", 32)
    return _font, _title_font


def draw_menu(screen):
    font, _ = _get_fonts()
    screen.fill(WHITE)
    txt = font.render("SNAKE GAME - PRESS SPACE", True, BLACK)
    screen.blit(txt, (120, 180))
    pygame.display.update()


def draw_leaderboard(screen, data):
    font, title_font = _get_fonts()
    screen.fill(WHITE)

    title = title_font.render("LEADERBOARD", True, BLACK)
    screen.blit(title, (200, 20))

    start_x = 80
    start_y  = 90
    col_rank  = start_x
    col_name  = start_x + 80
    col_score = start_x + 300
    col_level = start_x + 420
    row_h     = 35

    pygame.draw.line(screen, GRAY, (start_x, start_y - 10), (550, start_y - 10), 2)
    screen.blit(font.render("RANK",  True, DARK), (col_rank,  start_y))
    screen.blit(font.render("NAME",  True, DARK), (col_name,  start_y))
    screen.blit(font.render("SCORE", True, DARK), (col_score, start_y))
    screen.blit(font.render("LVL",   True, DARK), (col_level, start_y))
    pygame.draw.line(screen, GRAY, (start_x, start_y + 25), (550, start_y + 25), 2)

    y = start_y + 40
    for i, row in enumerate(data):
        username, score, level, _ = row
        screen.blit(font.render(str(i + 1),       True, BLACK), (col_rank,  y))
        screen.blit(font.render(username[:12],     True, BLACK), (col_name,  y))
        screen.blit(font.render(str(score),        True, BLACK), (col_score, y))
        screen.blit(font.render(str(level),        True, BLACK), (col_level, y))
        pygame.draw.line(screen, (220, 220, 220), (start_x, y + 25), (550, y + 25), 1)
        y += row_h

    hint = font.render("ESC - back to menu", True, (120, 120, 120))
    screen.blit(hint, (180, 350))
    pygame.display.update()


def draw_game_over(screen, font, score, level, best):
    screen.fill((245, 245, 245))
    screen.blit(font.render("GAME OVER",         True, (0, 0, 0)),     (220, 80))
    screen.blit(font.render(f"Score: {score}",   True, (0, 0, 0)),     (240, 140))
    screen.blit(font.render(f"Level: {level}",   True, (0, 0, 0)),     (240, 170))
    screen.blit(font.render(f"Best:  {best}",    True, (0, 0, 0)),     (240, 200))
    screen.blit(font.render("R - Retry | M - Menu", True, (100,100,100)), (180, 300))


def draw_settings(screen, font, settings):
    screen.fill((245, 245, 245))
    screen.blit(font.render("SETTINGS",                              True, (0,0,0)),       (240,  80))
    screen.blit(font.render(f"Grid: {settings['grid']} (G)",         True, (0,0,0)),       (200, 140))
    screen.blit(font.render(f"Sound: {settings['sound']} (S)",       True, (0,0,0)),       (200, 170))
    screen.blit(font.render("ESC - Back | G - Toggle Grid | S - Toggle Sound",
                             True, (100,100,100)), (80, 300))