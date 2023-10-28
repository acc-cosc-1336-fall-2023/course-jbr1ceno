import dictionary

def menu():
    print("1 - Add or Update Item ")
    print("2 - Delete Item ")
    print("3 - Exit ")

menu()
option = int(input("Enter your option: "))
itemDictionary = {}

while option != 3:
    if option == 1:
        addUpdateItem = str(input("Add or update item: "))
        addUpdateQuantity = int(input("Add or update quantity: "))
        dictionary.add_inventory(addUpdateItem, addUpdateQuantity, itemDictionary)
        print("\n", str(itemDictionary))

    elif option == 2:
        deleteItem = str(input("Type in the item you want to delete: "))
        print(dictionary.remove_inventory_widget(deleteItem, itemDictionary))
        print(itemDictionary)
            

    else:
        print("Invalid option.")
    
    print()
    menu()
    option = int(input("Enter your option: "))

print("You have exited the program.")