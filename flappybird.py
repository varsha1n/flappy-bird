import pygame
import sys
import random

pygame.init()
screen =pygame.display.set_mode((576, 1024))
background = pygame.image.load("cloud.jpg")
bird = pygame.image.load("assets/bluebird-midflap.png").convert()
while True:
    for event in pygame.event.get():
        if event. type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.blit(background, (0, 0))
    screen.blit(bird, (100,512))
    pygame.display.update()
