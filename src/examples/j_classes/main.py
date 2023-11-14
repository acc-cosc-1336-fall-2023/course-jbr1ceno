import bank_account, atm, menu

list_accounts = []

account = bank_account.BankAccount(50)

list_accounts.append(account)

account = bank_account.BankAccount(50)

list_accounts.append(account)

account = bank_account.BankAccount(50)

list_accounts.append(account)

for account in list_accounts:
    print(account)
