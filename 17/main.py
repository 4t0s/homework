from math import gcd
import datetime


class Number:
    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        return self.num + other.num

    def __sub__(self, other):
        return self.num - other.num

    def __mul__(self, other):
        return self.num * other.num

    def __div__(self, other):
        return self.num / other.num


class Drob:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        if num1 == 0 or num2 == 0:
            num1 = 1
            num2 = 2
            print("Выполнение невозможно")

    def __add__(self, other):
        num1 = self.num1*other.num2+(other.num1*self.num2)
        num2 = gcd(self.num1, other.num2)
        return Drob(num1, num2)

    def __sub__(self, other):
        num1 = self.num1*other.num2-(other.num1*self.num2)
        num2 = gcd(self.num1, other.num2)
        return Drob(num1, num2)

    def __mul__(self, other):
        num1 = self.num1 * other.num1
        num2 = self.num2 * other.num2
        return Drob(num1, num2)

    def __truediv__(self, other):
        num1 = self.num1 * other.num2
        num2 = self.num2 * other.num1
        return Drob(num1, num2)

    def __str__(self):
        return f"{self.num1} / {self.num2}"


fr1 = Drob(6, 2)
fr2 = Drob(13, 4)

fr3 = fr1+fr2

print(fr3)


class Library:
    def __init__(self, name, address, number_of_books):
        self.address = address
        self.name = name
        self.number_of_books = number_of_books

    def __add__(self, other):
        return self.number_of_books + other

    def __sub__(self, other):
        return self.number_of_books - other

    def __iadd__(self, other):
        self.number_of_books += other
        return self.number_of_books

    def __isub__(self, other):
        self.number_of_books -= other
        return self.number_of_books

    def __gt__(self, other):
        return self.number_of_books > other.number_of_books

    def __lt__(self, other):
        return self.number_of_books < other.number_of_books

    def __ge__(self, other):
        return self.number_of_books >= other.number_of_books

    def __le__(self, other):
        return self.number_of_books <= other.number_of_books

    def __eq__(self, other):
        return self.number_of_books == other.number_of_books

    def __ne__(self, other):
        return self.number_of_books != other.number_of_books


class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __sub__(self, other):
        x = datetime.date(self.year, self.month, self.day)
        y = datetime.date(other.year, other.month, other.day)
        z = (x-y).days

        return z

    def __add__(self, other):
        y = datetime.date(1, 1, other)
        x = datetime.date(self.year+1, self.month+1, self.day) + datetime.timedelta(days=other)
        return x


a = Date(2021, 2, 12)
b = Date(2020, 2, 12)
c = a-b-1
print(c)
d = a+2
print(d)

class Area:
    def __init__(self,dia,h):
        self.dia-dia
        self.h=h
    def make_area(self,diametr,height):
        self.diametr=diametr
        self.height=height
        return self.diametr*self.height
    