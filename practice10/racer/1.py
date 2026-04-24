import pygame, sys
from pygame.locals import *
import random, time
 
# Initializing pygame
pygame.init()
 
# Setting up FPS
FPS = 60
FramePerSec = pygame.time.Clock()
 
# Creating colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
 
# Screen settings
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

# Game variables
SPEED = 5
SCORE = 0
COINS = 0  # Number of collected coins
 
# Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)
 
# Load background
background = pygame.image.load("Practice 10/images/road.png")
 
# Create display
DISPLAYSURF = pygame.display.set_mode((400,600))
pygame.display.set_caption("Game")
 
# Enemy class
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Practice 10/images/Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)  
 
    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        
        # If enemy goes off screen → reset position and increase score
        if self.rect.top > SCREEN_HEIGHT:
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
 
# Coin class
class Coin(pygame.sprite.Sprite):
    def __init__(self, enemies):
        super().__init__()
        self.image = pygame.image.load("Practice 10/images/Coin.png")
        self.rect = self.image.get_rect()
        self.enemies = enemies  
        self.spawn()
    
    def spawn(self):
        while True:
            self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)
            # check if no coalision with enemy
            if not pygame.sprite.spritecollideany(self, self.enemies):
                break
    
    def move(self):
        self.rect.move_ip(0, SPEED)
        
        if self.rect.top > SCREEN_HEIGHT:
            self.spawn()
# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Practice 10/images/Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
        
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        
        # Move left
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        
        # Move right
        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)
 
# Create objects
P1 = Player()
E1 = Enemy()
 
# Sprite groups
enemies = pygame.sprite.Group()
enemies.add(E1)

C1 = Coin(enemies)

coins = pygame.sprite.Group()
coins.add(C1)

all_sprites = pygame.sprite.Group()
all_sprites.add(P1, E1, C1)
 
# Speed increase event
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)
 
# Game loop
while True:
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.5
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
 
    # Draw background
    DISPLAYSURF.blit(background, (0,0))
    
    # Draw score (top-left)
    # scores = font_small.render(str(SCORE), True, BLACK)
    # DISPLAYSURF.blit(scores, (10,10))
    
    # Draw coins count (top-right)
    coins_text = font_small.render(f"Coins: {COINS}", True, BLACK)
    DISPLAYSURF.blit(coins_text, (SCREEN_WIDTH - 120, 10))
 
    # Move and draw sprites
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()
 
    # Collision: player with enemy → game over
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound('Practice 10/sounds/crash.mp3').play()
        time.sleep(0.5)
                    
        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30,250))
           
        pygame.display.update()
        for entity in all_sprites:
            entity.kill() 
        
        time.sleep(2)
        pygame.quit()
        sys.exit()
    
    # Collision: player with coins → collect coin
    collected_coins = pygame.sprite.spritecollide(P1, coins, True)
    if collected_coins:
        COINS += 1
        
        # Spawn a new coin after collecting
        new_coin = Coin(enemies)
        coins.add(new_coin)
        all_sprites.add(new_coin)
         
    pygame.display.update()
    FramePerSec.tick(FPS)