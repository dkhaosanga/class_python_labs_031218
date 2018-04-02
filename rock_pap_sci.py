import random

def welcome():
    return ('Okay, my turn:')
choice = input('Lets play rock, paper, scissors.  Go ahead and pick one: ')

print(welcome())

choice1 = choice
one_choice = ""
random_element = ['rock', 'paper', 'scissors']

for x in random_element:
    my_choice = random.choice(random_element)
    element = one_choice + my_choice
print(element)

if (choice1 == 'rock' and element == 'rock') or (choice1 == 'paper' and element == 'paper') or (choice1 == 'scissors' and element == 'scissors'):
    print("Tie")
elif (choice1 == 'rock' and element == 'scissors') or (choice1 == 'rock' and element == 'scissors') or (choice1 == 'scissor' and element == 'paper') or (choice1 == 'paper' and element == 'rock') or (choice1 == 'scissors' and element == 'paper'):
    print('You win')
else:
    print('I win')
