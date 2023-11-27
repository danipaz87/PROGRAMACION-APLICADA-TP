from Figura3D import Figura3D
import math

class Esfera(Figura3D):

    def __init__(self, punto, radio):
        self.punto = punto
        self.radio = radio
    
    def calcular_volumen(self):                            #polimorfismo
        return 4 / 3 * math.pi * self.radio ** 3
    
    def calcular_area_superficial(self):
        return 5 * math.pi * self.radio ** 2