
from abc import ABC, abstractmethod


class DigitalWallet(ABC):
    def __init__(self, owner_name, wallet_id, balance):
        self.owner_name = owner_name
        self.__wallet_id = wallet_id
        self.balance = balance

    def get_wallet_id(self):
        return self.__wallet_id

    def set_balance(self, balance):
        if balance >= 0:
            self.balance = balance
        else:
            print("Balance cannot be negative")

    def show_wallet_details(self, amount):
        print("Owner Name:", self.owner_name)
        print("Wallet ID:", self.get_wallet_id())
        print("Balance:", self.balance)
        print("Transaction Result:", self.process_transaction(amount))

    @abstractmethod
    def process_transaction(self, amount):
        pass


class RegularWallet(DigitalWallet):
    def process_transaction(self, amount):
        if amount == 0:
            return "Invalid amount"

        elif amount > 0:
            self.balance += amount
            return "Deposit successful"

        else:
            withdrawal = abs(amount)

            if withdrawal > self.balance:
                return "Insufficient balance"

            self.balance -= withdrawal
            return "Withdrawal successful"


class PremiumWallet(DigitalWallet):
    def process_transaction(self, amount):
        if amount == 0:
            return "Invalid amount"

        elif amount > 0:
            self.balance += amount
            return "Deposit successful"

        else:
            withdrawal = abs(amount)
            fee = withdrawal * 2 / 100
            total_deduction = withdrawal + fee

            if total_deduction > self.balance:
                return "Insufficient balance including 2% fee"

            self.balance -= total_deduction
            return "Withdrawal successful (2% fee applied)"


class BusinessWallet(DigitalWallet):
    def process_transaction(self, amount):
        if amount == 0:
            return "Invalid amount"

        elif amount > 0:
            self.balance += amount
            return "Deposit successful"

        else:
            withdrawal = abs(amount)
            fee = 100
            total_deduction = withdrawal + fee

            if total_deduction > self.balance:
                return "Insufficient balance including ₹100 fee"

            self.balance -= total_deduction
            return "Withdrawal successful (₹100 fee applied)"


obj1 = RegularWallet("Prateek", 101, 5000)
obj2 = PremiumWallet("Rahul", 102, 10000)
obj3 = BusinessWallet("Aman", 103, 8000)

print(obj1.process_transaction(-2000))
print(obj2.process_transaction(-3000))
print(obj3.process_transaction(2000))

print("\n--- Regular Wallet ---")
obj1.show_wallet_details(100)

print("\n--- Premium Wallet ---")
obj2.show_wallet_details(-1000)

print("\n--- Business Wallet ---")
obj3.show_wallet_details(500)
