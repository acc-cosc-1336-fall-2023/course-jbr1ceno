import dictionaries

#main program
phonebook = {'Chris': '555-1111', 'Katie': '555-2222', 'Joanne':'555-3333'}

exists = dictionaries.is_key_in_dictionary('Chris', phonebook)

print(exists)

for key, value in phonebook.items():
    print(key, value)

for name, number in phonebook.items():
    print(name, number)


