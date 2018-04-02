import random

def smile():
    eyes = [':',';','=']
    nose = ['-', '^', 'o']
    mouths = ['D','p','|',']']
    print (random.choice(eyes),random.choice(nose),random.choice(mouths))

smile()
