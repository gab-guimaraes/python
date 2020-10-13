class Carobj:
    def __init__(self, potencia):
        self.__potencia = potencia
        self.__marcaDoCarro = None


    @property
    def potencia(self):
        return self.__potencia

    @property
    def marcaDoCarro(self):
        return self.__marcaDoCarro

    @marcaDoCarro.setter
    def marcaDoCarro(self, marcaDoCarro):
        self.__marcaDoCarro = marcaDoCarro


class Marca:
    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome


