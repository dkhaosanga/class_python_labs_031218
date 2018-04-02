phonebook = {'Kieran': {'name': 'Kieran',
                        'number': 8456331959,
                        'phrase': 'Good code is not written, it\'s re-written.'},
            'Lambda': {'name': 'Lambda',
                         'number': 8454185633,
                         'phrase': 'I am a robot.'}}

# Create new contact_del
def add_contact(name, phone, phrase):
    pass

#retrieve contact_del
def search(query):
    if query in phonebook:
        return

#update exsisting contact_del
def update(name, phone, phrase):
    pass

#delete contact
def remove(query):
    pass

#display function
def display(entry):
    pass

def menu():
    while True:
        q = input('Would you like to (a)dd (s)earch (u)pdate or (q)uit: ').lower()
        if q == 's':
            search_term = ('Enter name, number, or phrase: ')
            search()
