#dictionary (iterator can be cast into a dictionary)
#dict()

# dictionary = {'key': 'value', 'key2': 'value2'}
#
# print(dictionary['key'])

phonebook = {'jones': {'first_name': 'Chris', 'last_name': 'Jones', 'phone': '5038909073'}}
# print(phonebook)
# print(phonebook['jones']['first_name'])

#phonebook['dover'] =  {'first_name': 'Sheri', 'last_name': 'Dover', 'phone': '5030989073'}
#print(phonebook)

# for i in phonebook: #this will only print out jones and dover, because that is the only value in "phonebook"
#     print(i)

##this deletes/removes dover from the "phonebook" so when you print it won't show up
# print('deleting')
# del phonebook['dover']

##to add name in the "phonebook"
# name_to_add = 'jones'
# while name_to_add in phonebook:
#         print ('Name is {}'.format(name_to_add))
#         print ('Name exists, adding int to end...')
#         name_to_add += '_' + str('x')
#
#
# phonebook[name_to_add] = {'first_name': 'Sheri', 'last_name': 'Dover', 'phone': '5030989073'} #if this was tabbed in it would go on forever because it would be withiaån the while loop
# print(phonebook)

##this is to pass errors (specific things and multiple things), explicitly scilencing:
#try:
#   print(phonebook['dover'])
#except KeyError:
#   print('There is no key by that value')
#finally: #will always excute, even if there was already a KeyError or ValueError

##combining two dictionaries together (starting methods...)
# phonebook2 =  {'dover': {'first_name': 'Sheri', 'last_name': 'Dover', 'phone': '5030989073'}}
#
# phonebook.update(phonebook2) #concatenating two dictionaries together
#print(phonebook.keys) prints all the keys, .values() = values, .items().  to print these out as a list do print(list(phonebook.keys()))

##checking to see if the key is there
# phonebook = {'key': 'value1', 'key1': 'value2'}
#
# new = phonebook.get('key5' , "no key") #change 'key into something else and it won't print out value1, instead "no key will print out"
# print(new)
