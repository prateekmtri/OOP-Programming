from abc import ABC, abstractmethod


# Abstract Class
class LibraryMember(ABC):

    def __init__(self, name, member_id):
        self.name = name
        self.__member_id = member_id

    # Getter
    def get_member_id(self):
        return self.__member_id

    # Abstract Method
    @abstractmethod
    def borrow_book(self):
        pass


# Child Class 1
class Student(LibraryMember):

    def borrow_book(self):
        print(self.name, "can borrow 3 books")


# Child Class 2
class Teacher(LibraryMember):

    def borrow_book(self):
        print(self.name, "can borrow 10 books")


# Objects
student = Student("Prateek", 101)
teacher = Teacher("Rahul", 102)


# Using methods
print("Name:", student.name)
print("Member ID:", student.get_member_id())
student.borrow_book()

print()

print("Name:", teacher.name)
print("Member ID:", teacher.get_member_id())
teacher.borrow_book()