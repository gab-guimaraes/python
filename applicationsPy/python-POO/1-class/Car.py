class Car:
    def __init__(self, marca, modelo, potencia):
        self.marca = marca
        self.modelo = modelo
        self.potencia = potencia

    # Getter
    @property
    def marca(self):
        return self._marca

    # Setter
    @marca.setter
    def marca(self, valor):
        self._marca = valor.title()


c1 = Car("Mitsubishi", "Lancer Evo", "290")

c2 = Car("Subaru", "WRX", "290")

print(c1.marca, c1.modelo, c1.potencia)

print(c2.marca, c2.modelo, c2.potencia)

