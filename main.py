import pygame
import random

# initialize pygame
pygame.init()

# create screen
size = width, height = 600, 400
screen = pygame.display.set_mode(size)

# set game title and icons
pygame.display.set_caption("Sea Invaders")
icon = pygame.image.load("game_image.png")
pygame.display.set_icon(icon)

# load player image
player_image = pygame.image.load("spaceship.png")

# set player coordinates
player_x = 280
player_y = 350
player_x_change = 0
player_y_change = 0


def player(x, y):
    # add player image and coordinates on screen
    screen.blit(player_image, (x, y))


# load enemy image
enemy_image = pygame.image.load("enemy.png")

# set enemy coordinates
enemy_x = random.randint(0, 280)
enemy_y = random.randint(50, 100)
enemy_x_change = 0
enemy_y_change = 0


def enemy(x, y):
    # add enemy image and coordinates on screen
    screen.blit(enemy_image, (x, y))


# game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # check if key is pressed and update player coordinates appropraitely
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                player_x_change += 0.5

            if event.key == pygame.K_LEFT:
                player_x_change -= 0.5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_x_change = 0

    # set background colour
    screen.fill((0, 128, 128))

    # call player function after screen.fill
    player_x += player_x_change

    # set player boundaries
    if player_x <= 0:
        player_x = 0
    elif player_x >= 565:
        player_x = 565

    # call player function and pass coordinates
    player(player_x, player_y)

    # call enemy function and pass coordinates
    enemy(enemy_x, enemy_y)

    pygame.display.update()
