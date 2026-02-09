class Book:
    def __init__(self , book_id , title , author ):
        self.book_id = book_id
        self.book_title = title
        self.book_author = author
        self.__is_issued = False
    def show_book_info(self):
        print(f"Book Id : {self.book_id}")
        print(f"Book Title : {self.book_title}")
        print(f"Book_author : {self.book_author}")
        print(f"issued_book : {self.__is_issued}")
    
    def issue_book(self):
        if self.__is_issued == False:
            self.__is_issued = True
            print(f"Book issued sucessfully")
        else:
            print("Book alredy issued")  
            
    def return_book(self):
        if self.__is_issued == True:
            self.__is_issued = False
            print(f"Book Return")
        else:
            print("This book was not issued")
            

class Member:
    def __init__(self , member_id , name ):
        self.member_id = member_id 
        self.name = name
        self.book_taken = []
        
    def show_member_info(self):
        print(f"Member id : {self.member_id}")
        print(f"Member name : {self.name}")
        print(f"Book Taken : {self.book_taken}")

class Library:
    def __init__(self):
        self.book = []
        self.member = []
        
    def add_book(self, book_object):
        self.book.append(book_object)
        print("Book added to library")

    def add_member(self, member_object):
        self.member.append(member_object)
        print("Member added to library")
        
        
        
    def issue_book(self, book_id, member_id):
        for b in self.book:
            if b.book_id == book_id:
                for m in self.member:
                    if m.member_id == member_id:
                        b.issue_book()
                        m.book_taken.append(b.book_title)
                        
    def return_book(self, book_id, member_id):
         for b in self.book:
            if b.book_id == book_id:
                for m in self.member:
                    if m.member_id == member_id:
                        b.return_book()
                        if b.book_title in m.book_taken:
                            m.book_taken.remove(b.book_title) 
                            
                            
                            
 # Create books
b1 = Book(101, "Python", "ABC")
b2 = Book(102, "OOPS", "XYZ")

# Create member
m1 = Member(1, "Prateek")

# Create library
lib = Library()

# Add to library
lib.add_book(b1)
lib.add_book(b2)
lib.add_member(m1)

print("\n--- Issue Book ---")
lib.issue_book(101, 1)

print("\n--- Member Info ---")
m1.show_member_info()

print("\n--- Return Book ---")
lib.return_book(101, 1)

print("\n--- Member Info ---")
m1.show_member_info()
                           
                                               
                            
            
        
        
                
                    