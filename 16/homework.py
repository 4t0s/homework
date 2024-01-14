class Device:
    def __init__(self, company, name,turn_on):
        self.company=company
        self.name=name
        self.turn_on=turn_on
class Blender(Device):
    def __init__(self, company, name, rapira, type):
        self.super(Device, self).__init__
        self.rapira=rapira
        self.type=type
    def shake_em_up_shake_em_up_shake_em(self):
        self.turn_on = True
class CoffeeMachine(Device):
    def __init__(self, company, name, temperature, beans):
        self.super(Device, self).__init__
        self.temperature=temperature
        self.beans = beans
    def latte(self):
        self.beans = 'latte'
    def cappucino(self):
        self.beans = 'cappucino'
    def raf_na_kokosovom_moloke(self):
        self.beans = 'raf'
class MeatGrinder(Device):
    def __init__(self, company, name, bones, technology_grade, motivation):
        self.super(Device, self).__init__
        self.bones = bones
        self.technology_grade=technology_grade
        self.motivation=motivation
    def grinding(self):
        self.motivation=True
        if self.bones==True:
            return "it cracked bones too"


class Ship:
    def __init__(self,name, country, size):
        self.country = country
        self.size = size
        self.name = name
        self.__can_it_swim = False
    def swim(self):
        if self.can_it_swim==True:
            return "it swimming"
class Frigate:
    def __init__(self,name, country, size, max_speed,min_speed,actual_speed):
        self.super(Ship, self).__init__
        self.country = country
        self.size = size
        self.name = name
        self.__can_it_swim = False
        self.max_speed= max_speed
        self.min_speed = min_speed
        self.actual_speed = actual_speed
    def ship_in_port(self):
        self.can_it_swim=True
        if self.actual_speed>self.max_speed or self.actual_speed<self.min_speed:
            return "Kanye doesnt allow you to reach this speed in international port of Kim Kardashyan"
class Cruiser:
    def __init__(self,name, country, size, amount_of_people,amount_of_tickets):
        self.super(Ship, self).__init__
        self.country = country
        self.size = size
        self.name = name
        self.__can_it_swim = False
        self.amount_of_people = amount_of_people
        self.amount_of_tickets = amount_of_tickets
    def ordering_tickets(self):
        self.__can_it_swim=False
        if self.amount_of_people<self.amount_of_tickets:
            return 'Yes it is possible'
class Destroyer:
    def __init__(self, name, country, size, power_of_guns):
        self.super(Ship, self).__init__
        self.country = country
        self.size = size
        self.name = name
        self.__can_it_swim = False
        self.__destroyed_ships = []
        self.power_of_guns = power_of_guns
    def destroying_ships(self,other):
        self.__can_it_swim=True
        if self.power_of_guns>other.power_of_guns:
            self.__destroyed_ships.append(other.name)


class Circle:
    def __init__(self, radius):
        self.radius = radius
class Square:
    def __init__(self, side):
        self.side = side
class Circle_in_Square(Circle, Square):
    def __init__(self,radius, side):
        self.super(Circle, Square).__init__
        self.radius = radius
        self.side = side


class Door:
    def __init__(self, DoorSize):
        self.DoorSize = DoorSize
class Wheel:
    def __init__(self, WheelSize, WheelType):
        self.WheelSize = WheelSize
        self.WheelType = WheelType
class Engine:
    def __init__(self, litres, power):
        self.litres = litres
        self.power = power
class Automobile(Engine, Wheel, Door):
    def __init__(self, litres, power, WheelSize, WheelType, DoorSize):
        self.super(Engine, Wheel, Door).__init__
        self.litres = litres
        self.power = power 
        self.WheelSize = WheelSize
        self.WheelType = WheelType
        self.DoorSize = DoorSize


