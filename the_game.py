import pygame
import random
import csv

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
medal = pygame.image.load('medal.png')
sad = pygame.image.load('sad.png')
font = pygame.font.Font('freesansbold.ttf', 80)
color = (83, 76, 189)
red = (224, 88, 61)
green = (34, 201, 121)

# Stages
splash = True
chances = 5
game_over = True

y = 0
counter = 0
country = 'INDIA'
################[ SPLASH ]################
while splash:

    ## Keys
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            splash = False
            chances = 0
            game_over = False

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


# Importing the list of countries
with open('countries_list.csv', newline='') as f:
    reader = csv.reader(f)
    countries = list(reader)

index = random.randint(0,len(countries))
country = countries[index][0].lower()

guess = ''
correct = []
utilized = ''
################[ GAME ]################
while chances:

    ## Keys
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            chances = 0
            game_over = False

        if event.type == pygame.KEYDOWN:
            guess = pygame.key.name(event.key)
            if guess in country:
                correct.append(guess)
            else:
                utilized += guess
                chances -= 1

    ## Display
    y += 5
    if y > 720:
        y = 0
    screen.blit(bg, (0,y))
    screen.blit(bg, (0, y - 720))
    remaining_chances = font.render('Remaining Chances = ' + str(chances), True, color)
    screen.blit(remaining_chances, (150, 50))

    ## Answer
    for i in range(len(country)):
        # Box
        screen.blit(known, (100 + i*120, 280))
        # Text
        text = font.render(country[i], True, color)
        screen.blit(text, (115 + i*120, 315))
        # Box
        if country[i] in correct:
            continue
        else:
            screen.blit(unknown, (100 + i*120, 280))

    user_guess = font.render('Your Guess is : ' + guess, True, color)
    screen.blit(user_guess, (115, 515))

    Utilized = font.render('Used alphabet : ', True, color)
    screen.blit(Utilized, (115, 615))

    Utilized1 = font.render(utilized, True, red)
    screen.blit(Utilized1, (750, 615))

    # Break from loop once you reach the correct answer
    if set(correct) == set(country):
        break


    pygame.display.update()
    clock.tick(fps)

################[ EXIT ]################
if game_over:
    start_print = 600
    screen.blit(bg, (0,0))
    screen.blit(medal if chances else sad, (100, 150))
    for letter in country:
        if letter in correct:
            answer = font.render(letter, True, green)
        else:
            answer = font.render(letter, True, red)
        answer_rect = answer.get_rect(center=(start_print, 350))
        screen.blit(answer, answer_rect)
        start_print += 50

pygame.display.update()

while game_over:
    ## Keys
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = False

    clock.tick(fps)

pygame.quit()
