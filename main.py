import pygame
from pygame import mixer

import random
import math

# initialize pygame
pygame.init()

# create screen
size = width, height = 600, 400
screen = pygame.display.set_mode(size)

# background
background = pygame.image.load("background.jpg")

# add background song
mixer.music.load("background.wav")
mixer.music.play(-1)

# set game title and icons
pygame.display.set_caption("Sea Invaders")
icon = pygame.image.load("game_image.png")
pygame.display.set_icon(icon)

# load player image
player_image = pygame.image.load("spaceship.png")

# player score
score = 0
font = pygame.font.Font('freesansbold.ttf', 32)

text_x = 5
text_y = 5


def show_score(x, y):
    "render score on top left corner of screen"
    render_score = font.render("score : " + str(score), True, (255, 255, 255))
    screen.blit(render_score, (x, y))


# set player coordinates
player_x = 280
player_y = 350
player_x_change = 0
player_y_change = 0


def player(x, y):
    # add player image and coordinates on screen
    screen.blit(player_image, (x, y))


# enemy
enemy_image, enemy_x, enemy_y, enemy_x_change, enemy_y_change = [], [], [], [], []
num_of_enemies = 10

# load enemy image
for i in range(num_of_enemies):
    enemy_image.append(pygame.image.load("enemy.png"))

    # set enemy coordinates
    enemy_x.append(random.randint(0, 280))
    enemy_y.append(random.randint(50, 100))
    enemy_x_change.append(1.0)
    enemy_y_change.append(10)


def enemy(x, y, i):
    # add enemy image and coordinates on screen
    screen.blit(enemy_image[i], (x, y))


# load bullet image
bullet_image = pygame.image.load("bullet.png")

# set bullet coordinates
bullet_x = 0
bullet_y = 350
bullet_y_change = 2.0
bullet_state = 'ready'


def fire_bullet(x, y):
    # add enemy image and coordinates on screen
    global bullet_state
    bullet_state = 'fire'
    screen.blit(bullet_image, (x+8, y+5))


def isCollision(enemy_x, enemy_y, bullet_x, bullet_y):
    "check for collision"
    distance = math.sqrt(math.pow(enemy_x - bullet_x, 2) +
                         (math.pow(enemy_y - bullet_y, 2)))
    if distance < 20:
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
                player_x_change += 1.0

            if event.key == pygame.K_LEFT:
                player_x_change -= 1.0

            if event.key == pygame.K_SPACE:
                if bullet_state is 'ready':
                    bullet_sound = mixer.Sound("bullet.wav")
                    bullet_sound.play()
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
    for i in range(num_of_enemies):
        enemy_x[i] += enemy_x_change[i]

        # set enemy boundaries
        if enemy_x[i] <= 0:
            enemy_x_change[i] = 0.5
            enemy_y[i] += enemy_y_change[i]
        elif enemy_x[i] >= 565:
            enemy_x_change[i] -= 0.5
            enemy_y[i] += enemy_y_change[i]

        collision = isCollision(enemy_x[i], enemy_y[i], bullet_x, bullet_y)
        if collision:
            collision_sound = mixer.Sound("collision.wav")
            collision_sound.play()
            bullet_y = 350
            bullet_state = 'ready'
            score += 5
            enemy_x[i] = random.randint(0, 280)
            enemy_y[i] = random.randint(50, 100)

        # call enemy function and pass coordinates
        enemy(enemy_x[i], enemy_y[i], i)

    # call player function and pass coordinates
    player(player_x, player_y)

    # bullet movement
    if bullet_y <= 0:
        bullet_y = 350
        bullet_state = 'ready'

    if bullet_state is 'fire':
        fire_bullet(bullet_x, bullet_y)
        bullet_y -= bullet_y_change

    show_score(text_x, text_y)
    pygame.display.update()
