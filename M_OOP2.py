

class Square:

    square_list = []

    def __init__(self, s):
        self.s1 = s
        self.square_list.append((self.s1))

    def calculate_perimeter(self):
        return 4 * self.s1

    def calculate_area(self):
        return self.s1*self.s1

    def __repr__(self):
        return " {} by {} by {} by {} units.".format(self.s1,self.s1,self.s1,self.s1)
    

        

a_sq = Square(6)
b_sq = Square(7)
c_sq = Square(10)

print (a_sq.calculate_perimeter())
print (a_sq)

print (b_sq.calculate_perimeter())
print (Square(7))

print (c_sq.calculate_perimeter())
print (Square(10))
