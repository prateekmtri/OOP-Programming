class Payment:
    def pay(self, amount):
        print("Processing payment...")

class UPI(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI")

class Card(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} using Card")


class Cash(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} using Cash")


p1 = UPI()
p2 = Card()
p3 = Cash()

p1.pay(500)
p2.pay(500)
p3.pay(500)
