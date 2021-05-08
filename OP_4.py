class Shape(): 
    def what_am_i(self): 
        print("I am a shape.") 

class Rectangle(Shape): 
    def __init__(self, width, length):
        self.width = width 
        self.length = length 

    def calculate_perimeter(self): 
        return (self.width * 2) + (self.length * 2)

class Square(Shape): 
    def __init__(self, s1):
        self.s1 = s1 

    def calculate_perimeter(self):
        return self.s1 * 4 

arectangle = Rectangle(10, 80)
asquare = Square(60)
arectangle.what_am_i()
asquare.what_am_i()
