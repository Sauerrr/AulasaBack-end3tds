class Forma():
    def area (self):
        pass

class Quadrado(Forma):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado ** 2
    
quadrado = Quadrado(12)

print(quadrado.area())

class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio

class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio
    
    def area(self):
        return 3.14 * self.raio

circulo = Circulo(12)
print(circulo.area()) 