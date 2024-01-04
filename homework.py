"""
Реализуйте класс «Автомобиль». Необходимо хранить в полях класса: название модели,
год выпуска, производителя, объем двигателя, цвет машины, цену. Реализуйте методы класса
для ввода данных, вывода данных, реализуйте доступ к отдельным полям через методы класса
"""
class Automobile():
    def __init__(self, name, date, company, V, color, price):
        self.name = name
        self.date = date
        self.company = company
        self.V = V
        self.color=color
        self.__price = price
    def get_price(self):
        return self.__price

"""
Реализуйте класс «Книга». Необходимо хранить в полях класса: название книги, год
выпуска, издателя, жанр, автора, цену. Реализуйте методы класса для ввода данных, вывода
данных, реализуйте доступ к отдельным полям через методы класса.
"""
class Book():
    def __init__(self, name, date, company, genre, authority, price):
        self.name = name
        self.date = date
        self.genre = genre
        self.company = company
        self.authority=authority
        self.__price = price
    def get_price(self):
        return self.__price
"""
Реализуйте класс «Стадион». Необходимо хранить в полях класса: название стадиона,
дату открытия, страну, город, вместимость. Реализуйте методы класса для ввода данных,
вывода данных, реализуйте доступ к отдельным полям через методы класса.
"""
class Stadium():
    def __init__(self, name, date, country, city, vmestimost):
        self.name = name
        self.date = date
        self.country = country
        self.__vmestimost = vmestimost
        self.city=city
    def get_vmestimost(self):
        return self.__vmestimost
"""
я не  понял последнее задание
"""