phonebook = {'kieran': {'name': 'kieran',
                        'phone': 8456331959,
                        'phrase': 'Good code is not written, it\'s re-written.'},
            'lambda': {'name': 'lambda',
                         'phone': 8454185633,
                         'phrase': 'I am a robot.'}}


phonebook['clifford'] = {'name': 'clifford', 'phone': '9890784657', 'phrase': 'i am the big red dog'}
# print(phonebook)


def create_new(name, phone, phrase):
    if name not in phonebook:
        phonebook[name] = {'name': name, 'phone': phone, 'phrase': phrase}
    else:
        print('Name is already used, choose another option')


def search(query):
    entry_list = []
    if query in phonebook:
        entry_list.append(phonebook[query])
    else:
        for key, value in phonebook.items():
            for k, v in value.items():
                if query in str(v):
                    entry_list.append(value)
    return entry_list

#
# #to update a list in the phonebook dictionary
# phonebook = []
# for d in phonebooklist:
#     phonebook = {}
#     for b in d.keys():
#         if
# #
def delete_contact(name, phone, phrase):
    contact_del = input('Enter contact name to delete: ')
    del phonebook [contact_del]
    print('Delection of {} has completed.'.format(contact_del))
delete_contact()

def display(entry):
    print ('Name: {}'.format(entry['name']))
    print ('Phone: {}'.format(entry['phone']))
    print ('Phrase: {}'.format(entry['phrase']))


def menu():
    while True:
        q = input('Would you like to (a)dd (s)earch (u)pdate (r)emove or (q)uit?: ').lower()
        if q == 's':
            search_term = input('Enter name, phone, or phrase: ')
            results = search(search_term)
            for i in results:
                display(i)
        elif q == 'a':
            name = input('What is the first name of person to add?: ')
            phone = int(input('What is the phone number to add?: '))
            phrase = input ('What is the phrase to add?: ')
            create_new(name, phone, phrase)
        #elif q == 'u'
        #     update()
        elif q == 'r'
            remove()
        else:
            print('I did not understand that.  Try again.')

menu()

# def display_info (phonebook, name):
#     if name in phonebook:
#         print ('First_Name: {}'.format(phonebook[name],['first_name']))
#         print ('Last_Name: {}'.format(phonebook[name],['last_name']))
#         print ('Phone: {}'.format(phonebook[name],['phone']))
#     else:
#         print("I can't find name")

# def display_info (phonebook, name):
#     if name in phonebook:
#         name = ('Name: {}'.format(phonebook[name],['name']))
#         number = ('Phone_Number: {}'.format(phonebook[name],['number']))
#         phrase = ('Phrase: {}'.format(phonebook[name],['phrase']))
#         return name, number, phrase
#     raise KeyError

##to look for user
# for item in phonebook:
#     print (item)
# for user in phonebook:
#     print (user)

# print(phonebook['Lambda'])
#
# name_to_add = input('Name to add is: ')
# while name_to_add in phonebook:
#      print ('Name is {}'.format(name_to_add))
#      print ('Name exists, adding int to end...')
#      name_to_add += '_' + str('x')
#
# phonebook[name_to_add] = {'first_name': 'n', 'last_name': 'b', 'phone': 'num'}
#
# print(phonebook)
