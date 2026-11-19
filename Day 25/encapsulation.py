class BankAccount:

    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount
        print("Deposited:", amount)

    def display_balance(self):
        print("Current Balance:", self.__balance)


# User input
balance = float(input("Enter initial balance: "))
amount = float(input("Enter deposit amount: "))

account = BankAccount(balance)

account.deposit(amount)
account.display_balance()