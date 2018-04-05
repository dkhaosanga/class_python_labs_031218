import random

def menu():
    print("Let's play the lottery!")
    print ('1. Lottery Simulator')
    print ('2. Exit')

Menu = True

while Menu:
    menu()
    choice = input('Enter 1 or 2\n')

    if choice == '1':
        def user_numbers():
            user_quick_numbers = []
            user_numbers = random.sample(range(1,99),6)
            return user_numbers



        def winning_numbers():
            lotto_numbers = []
            return random.sample(range(1, 99), 6)
        lottery_numbers = winning_numbers()


        def match_list(list1,list2):
            set1 = list1
            set2 = list2
            list3 = set(list1).intersection(list2)
            return len(list3)

        def results():
            user_numbers1 = user_numbers()
            match = match_list(user_numbers1, lottery_numbers)
            if match == 1:
                print ('\nCongratulations, you won $4!')
                print ('Players Numbers: {}'.format(user_numbers1))
                print ('Lottery Numbers: {}\n'.format(lottery_numbers))

            elif match == 2:
                print ('\nCongratulations, you won $7!')
                print ('Players Numbers: {}'.format(user_numbers1))
                print ('Lottery Numbers: {}\n'.format(lottery_numbers))

            elif match == 3:
                print ('\nCongratulations, you won $100!')
                print ('Players Numbers: {}'.format(user_numbers1))
                print ('Lottery Numbers: {}\n'.format(lottery_numbers))

            elif match == 4:
                print ('\nCongratulations, you won $50,000!')
                print ('Players Numbers: {}'.format(user_numbers1))
                print ('Lottery Numbers: {}\n'.format(lottery_numbers))

            elif match == 5:
                print ('Congratulations, you won $1,000,000!')
                print ('Players Numbers: {}'.format(user_numbers1))
                print ('Lottery Numbers: {}\n'.format(lottery_numbers))

            elif match == 6:
                print ('Congratulations, you won the JACKPOT!!\n$25,000,000')
                print ('Players Numbers: {}'.format(user_numbers1))
                print ('Lottery Numbers: {}\n'.format(lottery_numbers))

            else:
                print ('\nSorry, you are not a winner.')
                print ('You lost $2')
                print ('Players Numbers: {}'.format(user_numbers1))
                print ('Lottery Numbers: {}\n'.format(lottery_numbers))

        for n in range(100000):
            results()
        Menu = False


    elif choice == '2':
        print('See you next time!')
        Menu = False

    else:
        print('Sorry, I did not understand. Please try again.\n')
        Menu = True
