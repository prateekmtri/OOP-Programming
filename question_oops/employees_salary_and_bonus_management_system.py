
from abc import ABC, abstractmethod


class Employee(ABC):
    def __init__(self, name, employee_id, basic_salary, experience_years):
        self.name = name
        self.__employee_id = employee_id
        self.basic_salary = basic_salary
        self.experience_years = experience_years

    def get_employee_id(self):
        return self.__employee_id

    def set_basic_salary(self, basic_salary):
        self.basic_salary = basic_salary

    def show_details(self):
        print("Employee Name:", self.name)
        print("Employee ID:", self.get_employee_id())
        print("Basic Salary:", self.basic_salary)
        print("Experience:", self.experience_years, "years")
        print("Final Salary:", self.calculate_salary())

    @abstractmethod
    def calculate_salary(self):
        pass


class Developer(Employee):
    def calculate_salary(self):
        bonus = self.basic_salary * 15 / 100
        final_salary = self.basic_salary + bonus
        return final_salary


class Manager(Employee):
    def calculate_salary(self):
        bonus = self.basic_salary * 25 / 100

        if self.experience_years > 5:
            extra_amount = 20000
        else:
            extra_amount = 0

        final_salary = self.basic_salary + bonus + extra_amount
        return final_salary


class Intern(Employee):
    def calculate_salary(self):
        bonus = self.basic_salary * 5 / 100
        final_salary = self.basic_salary + bonus

        if self.experience_years < 1:
            final_salary = final_salary - 2000

        return max(0, final_salary)


obj1 = Developer("Prateek", 101, 50000, 3)
obj2 = Manager("Rahul", 102, 80000, 7)
obj3 = Intern("Aman", 103, 15000, 0)

obj1.set_basic_salary(60000)

obj1.show_details()
print()

obj2.show_details()
print()

obj3.show_details()
