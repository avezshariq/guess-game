import pygame
import pygame.freetype
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
happy = pygame.image.load('happy.png')
sad = pygame.image.load('sad.png')
font = pygame.font.Font('PublicPixel-0W5Kv.ttf', 60)
fontS = pygame.font.Font('PublicPixel-0W5Kv.ttf', 30)
fontB = pygame.font.Font('PublicPixel-0W5Kv.ttf', 80)
color = (83, 76, 189)
red = (224, 88, 61)
green = (34, 201, 121)

# Stages
splash = True
chances = 8
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
    screen.blit(title, (100, 75))
    screen.blit(space_bar, (255, 550))

    for i in range(5):
        screen.blit(known, (200 + i*200, 300))
        text = font.render(country[i], True, color)
        screen.blit(text, (215 + i*200, 335))
    start = int(counter/fps)
    for i in range(start, 5):
        screen.blit(unknown, (200 + i*200, 300))
    counter += 1
    if counter > fps*6:
        counter = 0

    pygame.display.update()
    clock.tick(fps)


# Importing the list of countries
with open('countries_list.csv', newline='') as f:
    reader = csv.reader(f)
    countries = list(reader)

index = random.randint(0,len(countries)-1)
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
    remaining_chances = fontS.render('Remaining Chances = ' + str(chances), True, color)
    screen.blit(remaining_chances, (150, 50))

    ## Answer
    for i in range(len(country)):
        # Box
        screen.blit(known, (50 + i*100, 280))
        # Text
        text = font.render(country[i], True, color)
        screen.blit(text, (65 + i*100, 315))
        # Box
        if country[i] in correct:
            continue
        else:
            screen.blit(unknown, (50 + i*100, 280))

    user_guess = fontS.render('Your Guess is : ' + guess, True, color)
    screen.blit(user_guess, (115, 515))

    Utilized = fontS.render('Used alphabet : ', True, color)
    screen.blit(Utilized, (115, 615))

    Utilized1 = fontS.render(utilized, True, red)
    screen.blit(Utilized1, (600, 615))

    # Break from loop once you reach the correct answer
    if set(correct) == set(country):
        break


    pygame.display.update()
    clock.tick(fps)

################[ EXIT ]################
if game_over:
    start_print = 600
    screen.blit(bg, (0,0))
    screen.blit(happy if chances else sad, (100, 150))
    for letter in country:
        if letter in correct:
            answer = font.render(letter, True, green)
        else:
            answer = font.render(letter, True, red)
        answer_rect = answer.get_rect(center=(start_print, 350))
        screen.blit(answer, answer_rect)
        start_print += 60

pygame.display.update()

while game_over:
    ## Keys
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = False

    clock.tick(fps)

pygame.quit()
