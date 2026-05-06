import pygame
import random

from config import *
from config_loader import load_settings
from db import save_game, get_best

# created here with set_mode() — avoids duplicate display surface.

clock = pygame.time.Clock()
font  = None   # initialised lazily after pygame.init()


WHITE  = (245, 245, 245)
BLACK  = (20,  20,  20)
RED    = (220, 0,   0)
BLUE   = (0,   120, 255)
GOLD   = (255, 200, 0)
POISON = (80,  0,   0)

FOOD_TYPES = [
    ("normal", RED,    1,  10000, 70),
    ("rare",   BLUE,   3,   7000, 15),
    ("gold",   GOLD,   5,   5000,  5),
    ("poison", POISON, -2,  8000, 10),
]

POWER_TYPES = [
    ("speed",  (0,   200, 255)),
    ("slow",   (255, 140, 0)),
    ("shield", (200, 0,   200)),
]


def _font():
    global font
    if font is None:
        font = pygame.font.SysFont("Arial", 20)
    return font


def is_too_close(head, pos, radius=5):
    return (abs(head[0] - pos[0]) <= radius * BLOCK and
            abs(head[1] - pos[1]) <= radius * BLOCK)


def choose_food():
    total = sum(f[4] for f in FOOD_TYPES)
    r = random.randint(1, total)
    cur = 0
    for f in FOOD_TYPES:
        cur += f[4]
        if r <= cur:
            return f


def generate_food(snake, obstacles, head, now):
    food_type = choose_food()
    while True:
        pos = [
            random.randrange(0, SCREEN_WIDTH,  BLOCK),
            random.randrange(0, SCREEN_HEIGHT, BLOCK),
        ]
        if pos not in snake and pos not in obstacles and not is_too_close(head, pos):
            return {
                "pos":        pos,
                "type":       food_type[0],
                "color":      food_type[1],
                "value":      food_type[2],
                "spawn_time": now,
                "lifetime":   food_type[3],
            }


def should_draw_food(food, now):
    remaining = food["lifetime"] - (now - food["spawn_time"])
    if remaining <= 0:
        return False
    if remaining < 2000:
        return (now // 120) % 2 == 0
    return True


def generate_obstacles(level, snake, head):
    obstacles = []
    while len(obstacles) < level * 3:
        pos = [
            random.randrange(0, SCREEN_WIDTH,  BLOCK),
            random.randrange(0, SCREEN_HEIGHT, BLOCK),
        ]
        if pos not in snake and pos not in obstacles and not is_too_close(head, pos):
            obstacles.append(pos)
    return obstacles


def spawn_power_up(now):
    t = random.choice(POWER_TYPES)
    return {
        "type":       t[0],
        "color":      t[1],
        "pos":        [
            random.randrange(0, SCREEN_WIDTH,  BLOCK),
            random.randrange(0, SCREEN_HEIGHT, BLOCK),
        ],
        "spawn_time": now,
    }


def game_loop(screen, player_id):
    settings = load_settings()
    snake_color = tuple(settings.get("snake_color", [0, 180, 0]))
    show_grid   = settings.get("grid", False)

    f = _font()

    x = SCREEN_WIDTH  // 2
    y = SCREEN_HEIGHT // 2
    dx, dy = BLOCK, 0

    snake  = [[x, y]]
    length = 1
    score  = 0
    level  = 1

    obstacles = []
    now  = pygame.time.get_ticks()
    food = generate_food(snake, obstacles, snake[-1], now)

    power_up        = None
    power_spawn_time = 0
    speed_multiplier = 1
    power_end_time   = 0
    shield           = False

    best = get_best(player_id)

    running = True
    while running:
        now = pygame.time.get_ticks()
        screen.fill(WHITE)

        # optional grid
        if show_grid:
            for gx in range(0, SCREEN_WIDTH,  BLOCK):
                pygame.draw.line(screen, (230, 230, 230), (gx, 0), (gx, SCREEN_HEIGHT))
            for gy in range(0, SCREEN_HEIGHT, BLOCK):
                pygame.draw.line(screen, (230, 230, 230), (0, gy), (SCREEN_WIDTH, gy))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # BUG FIX: was bare return — score never saved
                save_game(player_id, score, level)
                pygame.quit()
                raise SystemExit

            if event.type == pygame.KEYDOWN:
                if   event.key == pygame.K_LEFT  and dx == 0: dx, dy = -BLOCK,  0
                elif event.key == pygame.K_RIGHT and dx == 0: dx, dy =  BLOCK,  0
                elif event.key == pygame.K_UP    and dy == 0: dx, dy =  0,     -BLOCK
                elif event.key == pygame.K_DOWN  and dy == 0: dx, dy =  0,      BLOCK

        x += dx
        y += dy

        # wall collision
        if x < 0 or x >= SCREEN_WIDTH or y < 0 or y >= SCREEN_HEIGHT:
            if shield:
                shield = False
                x, y = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2
            else:
                break   # go to save_game

        head = [x, y]
        snake.append(head)
        if len(snake) > length:
            snake.pop(0)

        # self collision
        if head in snake[:-1]:
            if shield:
                shield = False
            else:
                break   # go to save_game

        # obstacles
        if level >= 3 and not obstacles:
            obstacles = generate_obstacles(level, snake, head)

        for o in obstacles:
            pygame.draw.rect(screen, (60, 60, 60), (*o, BLOCK, BLOCK))
            if head == o:
                # BUG FIX: was bare return — score never saved
                break   # exit for-loop, then running=False below
        else:
            # only skip game-over if no obstacle was hit
            pass

        if head in obstacles:
            break   # go to save_game

        # power-ups
        if power_up is None:
            power_up         = spawn_power_up(now)
            power_spawn_time = now
        elif now - power_spawn_time > 8000:
            power_up = None

        if power_up:
            pygame.draw.rect(screen, power_up["color"], (*power_up["pos"], BLOCK, BLOCK))

        if power_up and head == power_up["pos"]:
            if power_up["type"] == "speed":
                speed_multiplier = 2
                power_end_time   = now + 5000
            elif power_up["type"] == "slow":
                speed_multiplier = 0.5
                power_end_time   = now + 5000
            elif power_up["type"] == "shield":
                shield = True
            power_up = None

        if speed_multiplier != 1 and now > power_end_time:
            speed_multiplier = 1

        # food expiry
        if now - food["spawn_time"] > food["lifetime"]:
            food = generate_food(snake, obstacles, head, now)

        if should_draw_food(food, now):
            pygame.draw.rect(screen, food["color"], (*food["pos"], BLOCK, BLOCK))

        # eat food
        if head == food["pos"]:
            if food["type"] == "poison":
                length = max(1, length - 2)
                snake  = snake[-length:]
                if length <= 1:
                    break   # BUG FIX: was return — score never saved
            else:
                length += 1
                score  += food["value"]

            level = score // 5 + 1
            food  = generate_food(snake, obstacles, head, now)

        # draw snake
        for s in snake:
            pygame.draw.rect(screen, snake_color, (*s, BLOCK, BLOCK))

        # HUD
        screen.blit(f.render(f"Score: {score}", True, BLACK), (10, 10))
        screen.blit(f.render(f"Level: {level}", True, BLACK), (10, 30))
        screen.blit(f.render(f"Best:  {best}",  True, BLACK), (10, 50))
        if shield:
            screen.blit(f.render("🛡 SHIELD", True, (200, 0, 200)), (10, 70))

        pygame.display.update()
        clock.tick(max(1, int((BASE_SPEED + level * 2) * speed_multiplier)))

    save_game(player_id, score, level)