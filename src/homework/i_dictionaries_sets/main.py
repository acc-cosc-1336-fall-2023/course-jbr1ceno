#
import dictionary

def menu():
    print("1- Get p distance matrix ")
    print("2- Exit ")

menu()
option = int(input("Enter your option: "))

while option != 2:
    if option == 1:
        listTable = []
        listInput = ""
        while(listInput != "STOP"):
            listInput = str.upper(input("Enter the row or type STOP to finish: "))
            lengthInput = len(listInput)
            if(listInput != "STOP"):
                listTable.append(listInput)
        print("The matrix is: ", listTable)
        print("The p distance is: ", str(dictionary.get_p_distance_matrix(listTable)))

    else:
        print("Invalid option.")
    
    print()
    menu()
    option = int(input("Enter your option: "))

print("You have exited the program.")