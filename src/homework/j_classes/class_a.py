import random

class die:
    
    __roll_value = 0
    
    def roll(self):
        self.__roll_value = random.randint(1, 6)

    def get_rolled_value(self):
        return self.__roll_value
    
    def __str__(self): #outputs: "The rolled value is 'whatever roll_value is' ."
        print("The rolled value is: " + str(self.__roll_value))
