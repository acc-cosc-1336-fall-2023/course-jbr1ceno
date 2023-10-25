import dictionaries
import sets
#main program
#a set is not an ordered list, meaning there is no order in the list, or random order
myset = set('abc')

print(myset)

myset.add('d')

print(myset)

for item in myset:
    print(item)