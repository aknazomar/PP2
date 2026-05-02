import pygame


class Ball:
    def __init__(self, x, y, radius, screen_width, screen_height, color, var):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.var = var

        self.screen_width = screen_width
        self.screen_height = screen_height

        self.speed = 20

    def update(self, keys, var):
        if (var == 1):
            if keys[pygame.K_LEFT]:
                self.x -= self.speed
            if keys[pygame.K_RIGHT]:
                self.x += self.speed
            if keys[pygame.K_UP]:
                self.y -= self.speed
            if keys[pygame.K_DOWN]:
                self.y += self.speed
        else:
            if keys[pygame.K_a]:
                self.x -= self.speed
            if keys[pygame.K_d]:
                self.x += self.speed
            if keys[pygame.K_w]:
                self.y -= self.speed
            if keys[pygame.K_s]:
                self.y += self.speed

        self.x = max(self.radius, min(self.x, self.screen_width - self.radius))
        self.y = max(self.radius, min(self.y, self.screen_height - self.radius))

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)