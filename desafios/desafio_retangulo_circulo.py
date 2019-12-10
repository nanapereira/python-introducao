from math import pi

class Retangulo:
    def __init__(self, lado_x, lado_y):
        self.lado_x = lado_x
        self.lado_y = lado_y

    def calcular_area_retangulo(self): 
        return self.lado_x * self.lado_y

    def calcular_perimetro_retangulo(self):
        return (self.lado_x * 2) + (self.lado_y * 2)

class Circulo:
    def __init__(self, raio):
        self.raio = raio

    def calcular_area_circulo(self):
        return (self.raio ** 2) * math.pi

    def calcular_perimetro_circulo(self):
        return 2 * math.pi * self.raio
        