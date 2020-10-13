class Person:
    def __init__(self, idade, nome):
        self.nome = nome
        self.idade = idade
        self.nomeclasse = self.__class__.__name__


class Client(Person):
    def coco(self):
        print("coco client")


class ClientVip(Client):
    pass


class Student(Person):
    pass

