import pygame
import random
import math

# initialize pygame
pygame.init()

# create screen
size = width, height = 600, 400
screen = pygame.display.set_mode(size)

# background
background = pygame.image.load("background.jpg")

# set game title and icons
pygame.display.set_caption("Sea Invaders")
icon = pygame.image.load("game_image.png")
pygame.display.set_icon(icon)

# load player image
player_image = pygame.image.load("spaceship.png")

# player score
score = 0

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
enemy_x_change = 0.5
enemy_y_change = 10


def enemy(x, y):
    # add enemy image and coordinates on screen
    screen.blit(enemy_image, (x, y))


# load bullet image
bullet_image = pygame.image.load("bullet.png")

# set bullet coordinates
bullet_x = 0
bullet_y = 350
bullet_x_change = 0
bullet_y_change = 0.5
bullet_state = 'ready'


def fire_bullet(x, y):
    # add enemy image and coordinates on screen
    global bullet_state
    bullet_state = 'fire'
    screen.blit(bullet_image, (x+8, y+5))


def isCollision(enemy_x, enemy_y, bullet_x, bullet_y):
    "check for collision"
    distance = math.sqrt((math.pow(enemy_x - bullet_x, 2)) +
                         (math.pow(enemy_y - bullet_y, 2)))
    if distance < 27:
        return True
    else:
        return False


# game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # check if key is pressed and update player coordinates appropraitely
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                player_x_change += 0.2

            if event.key == pygame.K_LEFT:
                player_x_change -= 0.2

            if event.key == pygame.K_SPACE:
                if bullet_state is 'ready':
                    bullet_x = player_x
                    fire_bullet(bullet_x, bullet_y)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_x_change = 0

    # set background colour
    screen.fill((0, 128, 128))

    screen.blit(background, (0, 0))

    # update player x coordinate
    player_x += player_x_change

    # set player boundaries
    if player_x <= 0:
        player_x = 0
    elif player_x >= 565:
        player_x = 565

    # update enemy x coordinate
    enemy_x += enemy_x_change

    # set enemy boundaries
    if enemy_x <= 0:
        enemy_x_change = 0.2
        enemy_y += enemy_y_change
    elif enemy_x >= 565:
        enemy_x_change -= 0.2
        enemy_y += enemy_y_change

    # call player function and pass coordinates
    player(player_x, player_y)

    # call enemy function and pass coordinates
    enemy(enemy_x, enemy_y)

    # bullet movement
    if bullet_y <= 0:
        bullet_y = 350
        bullet_state = 'ready'

    if bullet_state is 'fire':
        fire_bullet(bullet_x, bullet_y)
        bullet_y -= bullet_y_change

    collision = isCollision(enemy_x, enemy_y, bullet_x, bullet_y)
    if collision:
        bullet_y = 350
        bullet_state = 'ready'
        score += 5
        enemy_x = random.randint(0, 280)
        enemy_y = random.randint(50, 100)

    pygame.display.update()
