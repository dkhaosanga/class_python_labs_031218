# def change():
#     amount_of_change = int(input('Hello, how much change do you need?: '))
#     num_of_quarters = int(amount_of_change/25)
#     num_of_dimes = int((amount_of_change - (num_of_quarters)*25)/10)
#     num_of_nickels = int((amount_of_change - (num_of_dimes)*10 - (num_of_quarters)*25)/5)
#     num_of_pennies = int(amount_of_change - (num_of_dimes)*10 - (num_of_quarters)*25 - (num_of_nickels)*5)
#     change_map = {"quarters": num_of_quarters, "dimes": num_of_dimes, "nickels": num_of_nickels, 'pennies': num_of_pennies}
#     print ('Here is the change you need: ')
#     return change_map
#
#
# print (change())

def change():
    amount_of_change = int(input('Hello, how much change do you need?: '))
    num_of_quarters = (amount_of_change//25)
    num_of_dimes = ((amount_of_change - (num_of_quarters)*25)//10)
    num_of_nickels = ((amount_of_change - (num_of_dimes)*10 - (num_of_quarters)*25)//5)
    num_of_pennies = (amount_of_change - (num_of_dimes)*10 - (num_of_quarters)*25 - (num_of_nickels)*5)
    change_map = {"quarters": num_of_quarters, "dimes": num_of_dimes, "nickels": num_of_nickels, 'pennies': num_of_pennies}
    print ('Here is the change you need: ')
    return change_map

print (change())




def change_in_cents():
    return input('What is the total change, less than 100?: ')

def quarters(t):
    return (int(t) // 25, int(t) % 25)

def dimes(t):
    return (int(t) // 10, int(t) % 10)

def nickels(t):
    return (int(t) // 5, int(t) % 5)

def find_change():
    total_change = change_in_cents()
    q, remainder = quarters(total_change, 25)
    d, ramainder = dimes(remainder, 10)
    n, p = nickels(remainder, 5)

    print('You will need: {} quarters, {} dimes, {} nickels, and {} pennies.'.format(q, d, n, p))


find_change()
