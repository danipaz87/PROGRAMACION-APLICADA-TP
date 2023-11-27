from Figura3D import Figura3D
import math

class Cilindro(Figura3D):

    def __init__(self, punto, radio, altura):
        self.punto = punto
        self.radio = radio
        self.altura = altura
    
    def calcular_volumen(self):                #Polimorfismo
        return math.pi * self.radio * (self.radio + self.altura)

    def calcular_area_superficial(self):           #Polimorfismo
        return 2 * math.pi * self.radio * (self.radio + self.altura)