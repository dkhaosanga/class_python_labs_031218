#
# def is_palindrome(word):
#     if word == word[::-1]:
#         return True
#     else:
#         return False
#
# print(is_palindrome('dog'))
# print(is_palindrome('mom'))


def is_palindrome():
    word = input('Enter a word to check if it is a palindrome: ')
    if word.lower() == word[::-1].lower():
        return True
    else:
        return False

print(is_palindrome())
