from abc import ABC, abstractmethod

class Appliance(ABC):

    @abstractmethod
    def turn_on(self):
        pass

    def info(self):
        print("This is a home appliance")


class WashingMachine(Appliance):
    def turn_on(self):
        print("Washing Machine is now running")


class Refrigerator(Appliance):
    def turn_on(self):
        print("Refrigerator is cooling")


w = WashingMachine()
r = Refrigerator()

w.info()
w.turn_on()

r.info()
r.turn_on()




w = WashingMachine()
r = Refrigerator()

w.info()
w.turn_on()

r.info()
r.turn_on()