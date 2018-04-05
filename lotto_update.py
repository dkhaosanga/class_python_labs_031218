import random

number = random.randint(1,99)
winning_numbers = []
lotto_numbers = []
cost = 0
number_guess = 0

def winning_pick6():
    for i in range (0,6):
        while number in winning_numbers:
            number = random.randint(1,99)
        winning_numbers.append(number)
        return winning_numbers

def user_pick6():
    for i in range (0,6):
        while number in lotto_numbers:
            number = random.randint(1,99)
        lotto_numbers.append(number)
        return lotto_numbers

def loop_guess(lotto_numbers):
    for number_guess in range (100000):
        cost = cost + 2
        if lotto_numbers != winning_numbers:
            print ('Sorry, you are not a winner.\nThe cost of tickets is $2, the total amount spent is ${}'.format(cost))
            print ('Your numbers are:\n{}'.format(lotto_numbers))
            print('The winning lottery numbers are:\n{}\n'.format(winning_numbers))
    # elif

    # else:
    #     print('Sorry, you are not a winner.  The tickets cost you ${} today.'.format(cost))
    #     print ('Your numbers are: {}'.format(lotto_numbers))
    #     print('The winning lottery numbers are:{}'.format(winning_numbers))
        else:
            # if winning_numbers == lotto_numbers:
            print ('The cost of tickets is ${}'.format(cost))
            break
# lotto_numbers.sort()
# print('The winning lottery numbers are:{}'.format(winning_numbers))

# if lotto_numbers != winning_number:
#     print('Sorry, after 100000 tries you did not win.')

# num_matches(winning_numbers, lotto_numbers)
# print(num_matches())
