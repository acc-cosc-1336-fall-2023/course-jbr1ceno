#import src.examples.j_classes.menu

#def main():
#    src.examples.j_classes.menu.run_menu()

from src.examples.j_classes.customer import Customer
from src.examples.j_classes.customer_data import CustomerData

list_customers = [Customer(100, 200), Customer(500, 1000), Customer(1500, 750)]


data = CustomerData()

data.save_customers(list_customers)

read_customers = data.get_customers()

for customer in read_customers:
    print(customer.get_account(0).get_balance())