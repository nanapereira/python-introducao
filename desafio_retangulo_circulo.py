import math

class Retangulo:
    def __init__(self, ladox, ladoy):
        self.ladox = ladox
        self.ladoy = ladoy

    def calcular_area_retangulo(self, ladox, ladoy): 
        area_retangulo = ladox * ladoy
        return area_retangulo

    def calcular_perimetro_retangulo(sel, ladox, ladoy):
        perimetro_retangulo = (ladox * 2) + (ladoy + 2)
        return perimetro_retangulo

class Circulo:
    def __init__(self, raio):
        self.raio = raio

    def calcular_area_circulo(self, raio):
        area_circulo = (raio ** 2) * math.pi
        return area_circulo

    def calcular_perimetro_circulo(self, raio):
        perimetro_circulo = 2 * math.pi * raio
        return perimetro_circulo
        