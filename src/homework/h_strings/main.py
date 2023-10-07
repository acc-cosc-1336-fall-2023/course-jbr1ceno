import strings

def menu():
    print("1-Hamming Distance ")
    print("2-Dna Complement ")
    print("3-Exit ")

menu()
option = int(input("Enter your option: "))

while option != 3:
    if option == 1:
        dna1 = str.upper(input("Enter DNA sequence, make sure they are both the same length: "))
        dna2 = str.upper(input("Enter another DNA strand: "))
        print("The hamming distance of the DNA strands are: ", str(strings.get_hamming_distance(dna1, dna2)))

    elif option == 2:
        dna = str.upper(input("Enter DNA sequence: "))
        print("The DNA strand's reverse complement is: ", str(strings.get_dna_complement(dna)))
            

    else:
        print("Invalid option.")
    
    print()
    menu()
    option = int(input("Enter your option: "))

print("You have exited the program.")