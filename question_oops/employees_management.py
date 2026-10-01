from abc import ABC, abstractmethod


class Employee(ABC):

    def __init__(self, name, employee_id, salary):
        self.name = name
        self.__employee_id = employee_id
        self.salary = salary

    # Getter
    def get_employee_id(self):
        return self.__employee_id

    # Normal method
    def show_salary(self):
        print("Salary:", self.salary)

    # Abstract method
    @abstractmethod
    def calculate_bonus(self):
        pass

    # Normal method
    def show_details(self):
        print("Name:", self.name)
        print("Employee ID:", self.get_employee_id())
        print("Salary:", self.salary)
        print("Bonus:", self.calculate_bonus())


class Developer(Employee):

    def calculate_bonus(self):
        return self.salary * 10 / 100


class Manager(Employee):

    def calculate_bonus(self):
        return self.salary * 20 / 100


obj1 = Developer("Prateek", 101, 50000)
obj2 = Manager("Rahul", 102, 80000)

obj1.show_details()

print()

obj2.show_details()