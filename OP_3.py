class Shape:

    def __init__(self, l, w):
        self.length = l
        self.width = w

    def what_am_i(self):
        print ("I am a shape")
        

class Rectangle(Shape):

    def what_am_i(self):
        print ("I am a rectangle of {} by {}".format (self.length, self.width))

class Square (Shape):

    def what_am_i(self):
        print ("I am a square of {}".format (self.length))


a_rectangle = Rectangle(2,3)
print (a_rectangle.what_am_i())
        
b_square = Square(4,4)
print (b_square.what_am_i())        
    
    
