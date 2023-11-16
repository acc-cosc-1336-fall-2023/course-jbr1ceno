import src.examples.j_classes.bank_account

class Customer:

    __list_accounts = []

    def __init__(self, checking_balance, savings_balance):
        self.__list_accounts.append(src.examples.j_classes.bank_account.BankAccount(checking_balance))#add one account to the list
        self.__list_accounts.append(src.examples.j_classes.bank_account.BankAccount(savings_balance))#add one account to the list

    def get_account(self, index):
        return self.__list_accounts[index]
    
