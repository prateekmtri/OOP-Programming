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
            
                    