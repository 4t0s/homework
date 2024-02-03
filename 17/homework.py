import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def __eq__(self, other):
        return self.radius == other.radius

    def __gt__(self, other):
        return 2 * math.pi * self.radius > 2 * math.pi * other.radius

    def __lt__(self, other):
        return 2 * math.pi * self.radius < 2 * math.pi * other.radius

    def __ge__(self, other):
        return 2 * math.pi * self.radius >= 2 * math.pi * other.radius

    def __le__(self, other):
        return 2 * math.pi * self.radius <= 2 * math.pi * other.radius

    def __iadd__(self, increase):
        self.radius += increase
        return self

    def __isub__(self, decrease):
        self.radius -= decrease
        return self

class Complex:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        return Complex(self.real + other.real, self.imaginary + other.imaginary)

    def __sub__(self, other):
        return Complex(self.real - other.real, self.imaginary - other.imaginary)

    def __mul__(self, other):
        return Complex((self.real * other.real) - (self.imaginary * other.imaginary),
                       (self.real * other.imaginary) + (self.imaginary * other.real))

    def __truediv__(self, other):
        denominator = (other.real ** 2) + (other.imaginary ** 2)
        return Complex(((self.real * other.real) + (self.imaginary * other.imaginary)) / denominator,
                       ((self.imaginary * other.real) - (self.real * other.imaginary)) / denominator)

class Airplane:
    def __init__(self, passengers):
        self.passengers = passengers

    def __eq__(self, other):
        return self.passengers == other.passengers

    def __gt__(self, other):
        return self.passengers > other.passengers

    def __lt__(self, other):
        return self.passengers < other.passengers

    def __ge__(self, other):
        return self.passengers >= other.passengers

    def __le__(self, other):
        return self.passengers <= other.passengers

    def __iadd__(self, increase):
        self.passengers += increase
        return self

    def __isub__(self, decrease):
        self.passengers -= decrease
        return self

class Flat:
    def __init__(self, area):
        self.area = area

    def __eq__(self, other):
        return self.area == other.area

    def __ne__(self, other):
        return self.area != other.area

circle1 = Circle(5.0)
circle2 = Circle(7.0)

if circle1 == circle2:
    print("The radii are equal")
else:
    print("The radii are not equal")

if circle1 > circle2:
    print("Circle 1 > Circle 2")
else:
    print("Circle 1 < 2")

circle1 += 2.0
print("New radius:", circle1.radius)

c1 = Complex(3.0, 4.0)
c2 = Complex(2.0, -1.0)

result_add = c1 + c2

plane1 = Airplane(150)
plane2 = Airplane(200)

if plane1 == plane2:
    print("The number of passengers is equal.")
else:
    print("The number of passengers is not equal.")

if plane1 > plane2:
    print("Plane 1 has more passengers than Plane 2.")
else:
    print("Plane 1 has fewer passengers than Plane 2.")

plane1 += 50
print("New number:", plane1.passengers)

flat1 = Flat(100)
flat2 = Flat(120)

if flat1 == flat2:
    print("The areas are equal.")
else:
    print("The areas are not equal.")

if flat1 != flat2:
    print("The areas are not equal.")
else:
    print("The areas are equal.")
