import random

winning_numbers = random.sample(range(1,99),6)

def user_lotter_numbers():
    cost = 0
    num_match = 0
    for n in range (100000):
        lotto_numbers = random.sample(range(1,99),6)
        # lotto_numbers = [1, 2, 3, 4, 5, 5]
        cost = cost + 2
        if lotto_numbers != winning_numbers:
            print ('The cost of a ticket is $2, the total amount spent is ${}'.format(cost))
            print('The winning lottery numbers are:\n{}'.format(winning_numbers))
            print ('The lottery numbers you picked are:\n{}\n'.format(lotto_numbers))
        else:
            print('Winner!  Congrats, all you numbers matched!')
            break
    return lotto_numbers

def winner(lotto_numbers):
    num_match = 0
    for i in lotto_numbers:
        if i in winning_numbers:
            num_match += num_match + 1
            print ('You matched {} numbers out of 6.'.format(num_match))
            if num_match == 1:
                print('You won $4!')
            elif num_match == 2:
                print('You won $7!')
            elif num_match == 3:
                print('You won $100!')
                print ('Your numbers are:\n{}'.format(lotto_numbers))
                print('The winning lottery numbers are:\n{}'.format(winning_numbers))
            elif num_match == 4:
                print('You won $50000!')
                print ('Your numbers are:\n{}'.format(lotto_numbers))
                print('The winning lottery numbers are:\n{}'.format(winning_numbers))
            elif num_match == 5:
                print('You won $1000000!')
                print ('Your numbers are:\n{}'.format(lotto_numbers))
                print('The winning lottery numbers are:\n{}'.format(winning_numbers))
            elif num_match == 6:
                print('You won $25000000!')
                print ('Your numbers are:\n{}'.format(lotto_numbers))
            #     print('The winning lottery numbers are:\n{}'.format(winning_numbers))


user_lotter_numbers()
winner(user_lotter_numbers())
