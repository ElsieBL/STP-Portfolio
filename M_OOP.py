class Square:

    square_list = []

    def __init__(self, s):
        self.s1 = s
        self.square_list.append((self.s1))

    def calculate_perimeter(self):
        return 4 * self.s1

    def calculate_area(self):
        return self.s1*self.s1

    def print_size(self):
        print("This is a square of size {} units.".format(self.s1))

a_sq = Square(6)
b_sq = Square (7)
c_sq = Square (10)

a_sq.print_size()
b_sq.print_size()
c_sq.print_size()

print (a_sq.calculate_perimeter())
print (a_sq.calculate_area())
print (Square.square_list)
