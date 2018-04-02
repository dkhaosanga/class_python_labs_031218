import random

def pw():
    return ("Hello, lets generate a password today: ")

alpha = "abcdefghijklmnopqrstuvwxyz"
pw_length = 10
password = ""


while True:
    for x in range(pw_length):
        new_pw = random.choice(alpha)
        password = password + new_pw
    break

print(pw())
print(password)
