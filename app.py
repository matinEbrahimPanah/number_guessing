import random

lower = input('enter lower bound : ')
upper = input('enter upper bound : ')

random_number = random.randint(int(lower), int(upper))

for i in range(5):
    guess = input('enter your guess : ')
    
    chance_left = 4 - i
    if int(guess) == random_number:
        print('you win')
        break
    elif int(guess) > random_number:
        print('your guess is too high')
    else:
        print('your guess is too low')
    print('you have ', chance_left, 'chance left')