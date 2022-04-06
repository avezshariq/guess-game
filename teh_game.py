import pygame
import random

pygame.init()
clock = pygame.time.Clock()

# Variables
fps = 30


# Assets
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('Guess the Country')
bg = pygame.image.load('game_bg.png')
title = pygame.image.load('game_name.png')
unknown = pygame.image.load('unknown.png')
known = pygame.image.load('known.png')
space_bar = pygame.image.load('space_bar.png')
font = pygame.font.Font('freesansbold.ttf', 80)
color = (83, 76, 189)

# Stages
splash = True

y = 0
counter = 0
country = 'INDIA'
################[ SPLASH ]################
while splash:

    ## Keys
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            splash = False

        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    splash = False


    ## Display
    y += 5
    if y > 720:
        y = 0
    screen.blit(bg, (0,y))
    screen.blit(bg, (0, y - 720))
    screen.blit(title, (130, 150))
    screen.blit(space_bar, (335, 600))
    for i in range(5):
        screen.blit(known, (200 + i*200, 380))
        text = font.render(country[i], True, color)
        screen.blit(text, (215 + i*200, 415))
    start = int(counter/fps)
    for i in range(start, 5):
        screen.blit(unknown, (200 + i*200, 380))
    counter += 1
    if counter > fps*6:
        counter = 0

    pygame.display.update()
    clock.tick(fps)


pygame.quit()
