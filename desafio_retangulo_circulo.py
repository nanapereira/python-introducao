import math

class Retangulo:
    def __init__(self, ladox, ladoy):
        self.ladox = ladox
        self.ladoy = ladoy

    def calcular_area_retangulo(self, ladox, ladoy): 
        return ladox * ladoy

    def calcular_perimetro_retangulo(sel, ladox, ladoy):
        return (ladox * 2) + (ladoy + 2)

class Circulo:
    def __init__(self, raio):
        self.raio = raio

    def calcular_area_circulo(self, raio):
        return (raio ** 2) * math.pi

    def calcular_perimetro_circulo(self, raio):
        return 2 * math.pi * raio
        