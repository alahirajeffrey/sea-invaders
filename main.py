import pygame

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

# add player image and coordinates on screen


def player():
    screen.blit(player_image, (player_x, player_y))


# game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # set background colour
    screen.fill((0, 128, 128))

    # call player function after screen.fill
    player()

    pygame.display.update()
