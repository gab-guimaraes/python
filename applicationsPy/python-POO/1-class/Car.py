class Car:

    def __init__(self, marca, modelo, potencia):
        self.marca = marca
        self.modelo = modelo
        self.potencia = potencia

    def imprimi(self):
        print(self.marca, ", ", self.modelo, ", ", self.potencia)


    #Getter
    @property
    def marca(self):
        return self._marca

    #Setter
    @marca.setter
    def marca(self, marca):
        self.marca = marca


c1 = Car("Mitsubishi", "Lancer Evo", "290")
print(c1.imprimi())
