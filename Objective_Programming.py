class Rectangle:
    
     def __init__(self, w, l):
         self.width = w
         self.length = l

     def calculate_perimeter(self):
         return 2 *(self.width + self.length)
        
class Square:

    def __init__(self, s):
        self.s1 = s

    def calculate_perimeter(self):
        return 4 * self.s1
        

a_rectangle = Rectangle(2,3)
print (a_rectangle.calculate_perimeter())

b_square = Square(3)
print (b_square.calculate_perimeter())
