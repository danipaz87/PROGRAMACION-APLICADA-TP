from Forma import Forma
import math 

class Circulo(Forma):
    def __init__(self, color, radio):
        super().__init__(color, dimensiones={"radio": radio})
        
    def calcular_area(self):
        return math.pi * self.dimensiones["radio"] **2
    
    def calcular_perimentro(self):
        return 2 * math.pi * self.dimensiones["radio"]

