
num_to_words: {0:'zero', 1: 'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six',
            7:'seven', 8:'eight', 9:'nine', 10:'ten', 11:'eleven', 12:'twelve',
            13:'thirteen', 14:'fourteen', 15:'fifteen', 16:'sixteen',
            17:'seventeen', 18:'eighteen', 19:'nineteen'}
muliples_tens: {20:'twenty', 30:'thirty', 40:'forty', 50:'fifty', 60:'sixty',
            70:'seventy', 80:'eighty', 90:'ninety'}


def number_input():
    number = input('What number would you like to tranlate between 1-99?:')

def number_to_word(number):
    if 0 <= number < 19:
        return num_to_words[number]
    elif 20 <= number <= 99:
        tens, below_ten = divmod(number, 10)
        if below_ten > 0:
            print (num_to_words2[tens - 2] + '-' + num_to_words[below_ten])
    else:
        print('number is out of range.')

number()
