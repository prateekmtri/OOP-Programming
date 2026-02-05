class Payment:
    def pay(self, amount):
        print("Processing payment...")

class UPI(Payment):
    def pay(self, amount):
        super().pay(amount)   # parent method call
        print(f"Paid ₹{amount} using UPI")


obj = Payment()
obj =  UPI()

obj.pay(5000)