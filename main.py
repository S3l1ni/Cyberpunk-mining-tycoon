import pygame
from game import Game

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Cyberpunk Mining Tycoon")

game = Game(screen)
game.run()
pygame.quit()
