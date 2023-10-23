import dictionaries

#main program
phonebook = {}#empty dictionary

key = input("Enter key: ")
value = input("Enter value: ")

phonebook[key] = value

print(phonebook[key])

del phonebook[key] #deleting a dictionary

print(phonebook)


