"""
Напишите программу, в которой есть главный класс с текстовым полем. В главное
классе должен быть метод для присваивания значения полю: без аргументов и с одним
текстовым аргументом. Объект главного класса создаётся передачей одного текстового
аргумента конструктору. На основе главного класса создается класса потомок. В классепотомке нужно добавить числовое поле. У конструктора класса-потомка два аргумента.
"""
class Main:
    def __init__(self,text):
        None
    def set_text(self):
        self.text=int(input())
class Potomok(Main):
    def __init__(self,text,number):
        super(Main,self).__init__
    def set_number(self):
        self.number=int(input())