class BankAccount:
    def __init__(self, account_number, initial_balance=0):
        self.__account_number = account_number
        self.__balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Deposited: " + str(amount) + ". New balance: " + str(self.__balance) + ".")
        else:
            print("Deposit must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.__balance:
                self.__balance -= amount
                print("Withdrew: " + str(amount) + ". New balance: " + str(self.__balance) + ".")
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal must be positive.")

    def get_balance(self):
        return self.__balance

    def get_account_number(self):
        return self.__account_number

if __name__ == "__main__":
    my_account = BankAccount(account_number="123456789", initial_balance=1000)
    print("Account Number: " + my_account.get_account_number())
    print("Initial Balance: " + str(my_account.get_balance()))

    my_account.deposit(500)
    my_account.withdraw(200)
    my_account.withdraw(1500)

    print("Final Balance: " + str(my_account.get_balance()))
