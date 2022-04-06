# Guess the City

import random
cities = ['chicago', 'washington', 'la', 'nyc', 'paris', 'hyderabad', 'mumbai', 'tokyo', 'delhi', 'jakarta', 'madrid', 'sydney', 'shanghai']
city = cities[random.randint(0, len(cities) - 1)]
print('Welcome to GUESS THE CITY game')
print('Instructions:')
print('You have 5 chances')
chances = 5
print('You use up a chance if you are wrong, otherwise you still have the same chances left')
print('Good Luck !!!')
print()
print('_ '* len(city))
correct = []
while chances > 0:
    guess = input('What is your guess: ')
    if guess in city:
        print('Good Job. Remaining chances = ', chances)
        correct.append(guess)
    else:
        chances = chances - 1
        print('Give it another try. Remaning chances = ', chances)
    print()
    for letter in city:
        if letter in correct:
            print(letter, ' ', end='')
        else:
            print('_ ', end='')
    print()

    if set(correct) == set(city):
        break
print()
if chances > 0:
    print('Well Done !!! You win !')
else:
    print('Better luck next time')







