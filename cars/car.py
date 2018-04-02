
class Car:
    number_of_wheels: 4

    def __init__(self, color, number_of_doors, make):
        self.color = color
        self.number_of_doors = number_of_doors
        self.make = make

    def honk(self):
        print('honk')
