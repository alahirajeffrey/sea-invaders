import pygame

# initialize pygame
pygame.init()

# create screen
size = width, height = 800, 600
screen = pygame.display.set_mode(size)

# game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
