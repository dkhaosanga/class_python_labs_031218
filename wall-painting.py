def hello():
    return ('Hello, lets calculate how much your paint will be.')

def solution(width, height, cost):
    gallons = (width * height)/400
    return gallons * cost

def price_of_paint():
    width = float(input('Enter width in ft: '))
    height = float(input('Enter height in ft: '))
    cost = float(input('Enter cost of paint: '))
    print ('The cost of paint will be: ')
    return solution(width, height, cost)

print(hello())
print(price_of_paint())
