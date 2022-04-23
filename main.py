import pygame

# initialize pygame
pygame.init()

# create screen
size = width, height = 800, 600
screen = pygame.display.set_mode(size)

# set game title and icons
pygame.display.set_caption("Sea Invaders")
icon = pygame.image.load("game_image.png")
pygame.display.set_icon(icon)

# game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # set background colour
    screen.fill((0, 128, 128))
    pygame.display.update()
