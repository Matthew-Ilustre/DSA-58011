class Circle:
    def __init__(self, radius ):
        self.radius = radius


    def Perimeter(self) :
        pi = 3.14
        print( pi * (self.radius * self.radius))

C = Circle(2)
C.Perimeter()
