#main program
phonebook = {'Chris': '555-1111', 'Katie': '555-2222', 'Joanne':'555-3333'}
#print(phonebook)

#print(phonebook['Chris'])
#print(phonebook['Katie'])

for key in phonebook:               #key AKA formal name: target variable
    print(key, phonebook[key])      #shows key with its values
    print(phonebook[key])           #shows just the values of the keys
    
print("values only")
for value in phonebook.values():    #.values() is a built in function in the dictionaries for python
    print(value)                    #only shows the values of the keys

print("dictionary items")
for item in phonebook.items():      #.items() is a built in function
    print(item)                     #tuple



