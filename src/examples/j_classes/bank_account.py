import random

class BankAccount:
    __balance = 0 #__ hide it(variable) from other classes (private)

    def __init__(self, balance): #constructor -- initialize(run) class data/variables

        if(balance >= 0):
            self.__balance = balance
        else:
            self.__get_balance_from_db() #private function--not accessible from outside the class

    def get_balance(self): #other classes can see get_balance
        return self.__balance

    def deposit(self, amount):

        if(amount > 0):
            self.__balance += amount

    def withdraw(self, amount):

        if(amount > 0 and amount <= self.__balance):
            self.__balance -= amount

    def __get_balance_from_db(self): #db means database
        self.__balance = random.randint(0, 10000)