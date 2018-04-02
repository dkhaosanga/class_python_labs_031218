
def menu():
    first = int(input('What is the first number you want to calculate?: '))
    operation = input('What operation would you like to execute(+-*/)?: ')
    second = int(input('What is the second number you want to calculate?: '))
    if operation == '+':
        print('{} + {} = '.format(first, second),(first + second))
    elif operation == '-':
        print('{} - {} = '.format(first, second),(first - second))
    elif operation == '*':
        print('{} * {} = '.format(first, second),(first * second))
    elif operation == '/':
        print('{} / {} = '.format(first, second),(first / second))
    else:
        print('You have not typed a valid operator, try again.')

menu()
