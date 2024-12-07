import pygame

class Player:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = (255, 0, 0)
        self.y_velocity = 0 # Скорость по вертикали
        self.on_ground = True # На земле ли игрок

    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)