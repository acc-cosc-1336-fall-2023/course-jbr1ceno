import class_a

def display_menu():
    print('1- Roll Die')
    print('2 - Exit Program')

def run_menu():

    menu_option = 0

    while(menu_option != '2'):
        display_menu()
        menu_option = input("Enter choice: ")
        handle_menu(menu_option)

def handle_menu(menu_option):
    if(menu_option == '1'):
        tryAgain = "YES"
        while(tryAgain.upper() == "YES"):
            roll_number = class_a.die()
            roll_number.roll()
            roll_number.get_rolled_value()
            roll_number.__str__()
            tryAgain = input("Do you want to roll again? If so write YES, if not write something else: ")
            
        

    elif(menu_option == '2'):
        print('Exiting... ')
    else:
        print("Invalid choice")