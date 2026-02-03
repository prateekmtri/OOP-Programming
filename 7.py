class Count:
    "This is a countable number"
    def __init__(self, num):
        self.num = num
        
    def show_all_count(self):
       for count in  self.num:
        print(count)
       
object = Count([1,2,3,4,5,6,7,8,9,10])
object.show_all_count() 