from FiguraGeometrica import FiguraGeometrica
import math

class Circulo(FiguraGeometrica):
    def __init__(self, radio):
        self.radio = radio
        
    def calculararea(self):
        return math.pi * self.radio**2
    
    def calcularperimetro(self):
        return 2 * math.pi * self.radio