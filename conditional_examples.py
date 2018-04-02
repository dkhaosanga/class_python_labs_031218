name = input('What is your name?: ')
age = input('How old are you?: ')
birth_year = 2018 - int(age)
print('Hey, {}!'.format(name))

if birth_year < 1985:
    print("Sooo Old")
elif birth_year < 1990:
    print("not old")
else:
    print(asdfa)

print('You were born in {}'.format(birth_year))

#if to start a conditional, only one per conditional block
#elif first thing (and only one) that is true, one of these things has to be true, order does matter (middle of conditional block)
#else end of a conditional, only one per conditional block

#int() turns something into an integer if it can be
#float() turns into floats
#str()
