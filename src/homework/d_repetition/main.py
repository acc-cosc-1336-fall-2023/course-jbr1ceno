import repetition

def menu():
    print("Homework 3 Menu ")
    print("Enter 1 for Factorial ")
    print("Enter 2 for Sum odd numbers ")
    print("Enter 3 to exit the program ")

menu()
option = int(input("Enter your option: "))

while option != 3:
    if option == 1:
        facNum = int(input("Enter a number to find the factorial: "))
        print("Your factorial is: ", int(repetition.get_factorial(facNum)))
        exitProg = input("If you want to exit, type yes to exit. If not, type no or something else to continue. ")
        if(exitProg == "Yes" or exitProg == "yes"):
            break

    elif option == 2:
        
        sumOddNum = -1

        while(sumOddNum <= 0 or sumOddNum >= 100):

            sumOddNum = int(input("Enter a number greater than 0 but less than 100: "))
            
            if(sumOddNum > 0 and sumOddNum < 100):
                print("The number you typed is: ", sumOddNum)
                print("So the sum of the odd numbers is: ", int(repetition.sum_odd_numbers(sumOddNum)))
            else:
                print("Number is outside the range, try again." )
            

    else:
        print("Invalid option.")
    
    print()
    menu()
    option = int(input("Enter your option: "))

print("You have exited the program.")