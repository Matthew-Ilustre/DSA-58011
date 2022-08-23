class Circle:
    def __init__(self, radius ):
        self.radius = radius


    def Perimeter(self) :
        pi = 3.14
        print(2 * pi * self.radius)

C = Circle(2)
C.Perimeter()