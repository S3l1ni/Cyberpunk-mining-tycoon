import pygame
from player import Player

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.player = Player(300, 500, 30, 30)
        self.running = True
        self.gravity = 0.5
        self.player.y_velocity = 0
        self.ground_level = 570
        self.move_speed = 0.9 # Скорость движения
        self.jump_strength = -13 # Сила прыжка
        self.jump_dampening = 0.55 # Затухание прыжка


    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            keys = pygame.key.get_pressed()
            if keys[pygame.K_a]:
                self.player.move(-self.move_speed, 0)
            if keys[pygame.K_d]:
                self.player.move(self.move_speed, 0)
            if keys[pygame.K_w] and self.player.on_ground:
                self.player.y_velocity = self.jump_strength

            # Гравитация и затухание прыжка
            self.player.y_velocity += self.gravity
            if self.player.y_velocity > 15:
                self.player.y_velocity = 15
            if self.player.y_velocity > 0 and not self.player.on_ground:
                self.player.y_velocity *= self.jump_dampening

            self.player.move(0, self.player.y_velocity)

            # Проверка столкновения с землей
            if self.player.rect.bottom > self.ground_level:
                self.player.rect.bottom = self.ground_level
                self.player.y_velocity = 0
                self.player.on_ground = True
            else:
                self.player.on_ground = False

            self.screen.fill((0, 0, 0))
            pygame.draw.rect(self.screen, (100, 100, 100), (0, self.ground_level, 800, 30))
            self.player.draw(self.screen)
            pygame.display.flip()