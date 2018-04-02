# def greeting(name, age=0): #default argument, optional, if you input the age the age will appear, if not 0 will appear
#     return 'Hello {}. You are {} years old'.format(name, age)
#
# #print(greeting('aljfd')) OR print(greeting('asdfasf', 33))
#('aljfd') - arguments
#
# when you don't know how many agruments you will have, use *(arugments) and **(dictionary),
#def add_number (*args, **) #indexable

#need to put equals
# def contants(**kwargs):
#     print(kwargs)
#
# contact (age=90, name='chris', phone=23453453)
#
#     print(kwargs['age'])

#arguments have to come before kwargs, so contact (age=90, name='chris', phone=23453453) is the same and then arguments need to go before age in 'a', 'b' etc
#and positional arguments need to go before agruments


##SETS
#set only holds unique items, only on of those items
# number_list = [1,1,2,3,3,3,5]
#
# print(number_list)
# print(set(number_list))
# #set is with curly brackets, unordered, no dupes, mutable (the set itself), but the values inside are immutable
# print({1,1,2,3,3,3,5})
#empty set is === set() just like an empty string is string = '', list()
