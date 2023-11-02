#

def write_to_file(file_name):
    out_file = open(file_name, 'w'); # out_file is a variable but could represent a file
    
    #write to file
    out_file.write('John Locke\n')
    out_file.write('David Hume\n')
    out_file.write('Edmund Burke\n')

    #close the file
    out_file.close()

def read_from_file(file_name):
    in_file = open(file_name, 'r')

    file_contents = in_file.read()

    #close file
    in_file.close() #always explicitly close

    print(file_contents)

def read_each_line_from_file(file_name):
    in_file = open(file_name, 'r')

    line1 = in_file.readline()
    line2 = in_file.readline()
    line3 = in_file.readline()

    in_file.close();

    print(line1.rstrip('\n')) #if we don't want spaces, strip the new line
    print(line2.rstrip('\n'))
    print(line3.rstrip('\n'))

#from book 6.4
def write_names_to_file(file_name, file_mode):
    out_file = open(file_name, file_mode)

    user_choice = 'y'

    while(user_choice == 'y' or user_choice == 'Y'):
        name = input("Enter programming language: ")
        out_file.write(name + '\n')
        user_choice = input("Type y to continue...")

    out_file.close()

def read_from_file_while(file_name):
    in_file = open(file_name, 'r')

    line = in_file.readline()

    while(line != ''):
        print(line.rstrip('\n'))
        line = in_file.readline()

    in_file.close()

def read_from_file_for(file_name):
    in_file = open(file_name, 'r')

    for line in in_file:
        print(line.rstrip('\n'))

    in_file.close()

def write_sales_data(file_name, file_mode):
    out_file = open(file_name, file_mode)

    user_choice = 'y'

    while(user_choice.upper() == 'Y'):
        amount = input("Enter sales data: ")
        out_file.write(amount + '\n')
        user_choice = input("Type y to continue... ")

    out_file.close()

def read_sales_data(file_name): #FIX THIS LATER
    in_file = open(file_name, 'r')

    total_sales = 0

    for amount in in_file:
        print(f'{float(amount):.2f}')
        total_sales += float(amount)
    
    print('-------')
    print(f'{total_sales:.2f}')

    in_file.close()