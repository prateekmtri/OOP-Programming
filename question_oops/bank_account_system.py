from abc import ABC, abstractmethod


class BankAccount(ABC):

    def __init__(self, account_holder, account_number, balance):
        self.account_holder = account_holder
        self.__account_number = account_number
        self.balance = balance

    # Getter
    def get_account_number(self):
        return self.__account_number

    # Setter
    def set_balance(self, balance):
        self.balance = balance

    # Normal method
    def show_balance(self):
        print("Balance:", self.balance)

    # Normal parent method
    def show_account_details(self):
        print("Account Holder:", self.account_holder)
        print("Account Number:", self.get_account_number())
        print("Balance:", self.balance)
        print("Interest:", self.calculate_interest())

    # Abstract method
    @abstractmethod
    def calculate_interest(self):
        pass


class SavingsAccount(BankAccount):

    def calculate_interest(self):
        return self.balance * 5 / 100


class CurrentAccount(BankAccount):

    def calculate_interest(self):
        return self.balance * 2 / 100


class FixedDeposit(BankAccount):

    def calculate_interest(self):
        return self.balance * 8 / 100


# Objects
obj1 = SavingsAccount("Prateek", 101, 50000)
obj2 = CurrentAccount("Rahul", 102, 80000)
obj3 = FixedDeposit("Aman", 103, 100000)


# Using setter to change balance
obj1.set_balance(60000)


# Display details
obj1.show_account_details()

print()

obj2.show_account_details()

print()

obj3.show_account_details()