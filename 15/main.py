from typing import Self


class Rectangle():
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __add__(self, other: Self):
        return Rectangle(self.width+other.width, self.height)

    def __str__(self):
        return f"это прямоугольник со сторонами {self.width} и {self.height}"


rectangle1 = Rectangle(10, 2)
rectangle2 = Rectangle(20, 2)
print(rectangle1+rectangle2)


class Games:
    def __init__(self, year, name):
        self.__year = year
        self.name = name

    def getName(self):
        return self.__year


class XboxGames(Games):
    def __init__(self, year, name, XboxCode):
        super().__init__(year, name)
        self.XboxCode = XboxCode

    def getName(self):
        return f'This is name of the xbox game {self.name}'


class PCGames(Games):
    def __init__(self, year, name, PCCode):
        super().__init__(year, name)
        self.PCCode = PCCode

    def getName(self):
        return f'This is name of the PC game {self.name}'


class PS4Games(Games):
    def __init__(self, year, name, PS4Code):
        super().__init__(year, name)
        self.PS4 = PS4Code

    def getName(self):
        return f'This is name of the PS4 game {self.name}'


class MobileGames(Games):
    def __init__(self, year, name, MobileCode):
        super().__init__(year, name)
        self.MobileCode = MobileCode

    def getName(self):
        return f'This is name of the mobile game {self.name}'


class Country:
    def __init__(self):
        pass


class Russia(Country):
    def __init__(self, population):
        super().__init__()
        self.__population = population

    def setPopulation(self):
        self.__population = int(input())

    def getPopulation(self):
        return self.__population


class Germany(Country):
    def __init__(self, population):
        super().__init__()
        self.__population = population

    def setPopulation(self):
        self.__population = int(input())

    def getPopulation(self):
        return self.__population


class Canada(Country):
    def __init__(self, population):
        super().__init__()
        self.__population = population

    def setPopulation(self):
        self.__population = int(input())

    def getPopulation(self):
        return self.__population
