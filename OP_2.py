
class Square:

    def __init__(self, s):
        self.s1 = s

    def change_size(self, a):
        self.a = a
        if self.a >= 0:
            self.s1 = self.s1 + self.a

        else:
            self.s1 = self.s1 - self.a
            
        return self.s1

a_square = Square(5)
print (a_square.change_size(2))      
        
