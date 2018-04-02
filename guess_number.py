import random

random_number = random.randint(1,10)
number_guess = 0

while number_guess < 10:
    guess = int(input('What is your guess for the number?: '))
    number_guess = number_guess + 1

    if guess == random_number:
        print ('You guessed the number correct! You guessed my number in {} guesses!'.format(number_guess))
        break
    elif guess > random_number:
        print ('Too high')
    elif guess < random_number:
        print ('Too low')

if guess != random_number:
    print('Sorry, out of guesses.  The correct number was {}'.format(random_number))
