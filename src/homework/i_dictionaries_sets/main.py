#
import dictionary

def menu():
    print("1- Get p distance matrix ")
    print("2- Exit ")

menu()
option = int(input("Enter your option: "))
lenTMP = 11

while option != 2:
    if option == 1:
        listTable = []
        listInput = ""
        while(lenTMP > 10):
            listInput = str.upper(input("Enter the row or type STOP to finish: "))
            lenTMP = len(listInput)
            if(lenTMP > 10):
                print("The row length has to be <= 10, please enter the row again. ")
            else:
                listTable.append(listInput)

        while(listInput != "STOP"):
            listInput = str.upper(input("Enter the row or type STOP to finish: "))
            lengthInput = len(listInput)
            if(listInput != "STOP" and lengthInput == lenTMP):
                listTable.append(listInput)
            else:
                print("The row length has to be equal to ", str(lenTMP), ". Please enter again. ")
        print("The matrix is: ", listTable)
        print("The p distance is: ", str(dictionary.get_p_distance_matrix(listTable)))
    else:
        print("Invalid option.")
    
    print()
    menu()
    option = int(input("Enter your option: "))

print("You have exited the program.")