"""Forma: Implementar las clases Forma, Circulo y Rectangulo. La o las clases deben contener atributos como 
color y dimensiones. Las subclases deben heredar y definir métodos y atributos para calcular el área y 
el perímetro de cada forma."""

import math 

class Forma:
    def __init__(self, color, dimensiones):
        self.color = color
        self.dimensiones = dimensiones
        
    def calcular_area(self):
        pass
    
    def calcular_perimentro(self):
        pass

class Circulo(Forma):
    def __init__(self, color, radio):
        super().__init__(color, dimensiones={"radio": radio})
        
    def calcular_area(self):
        return math.pi * self.dimensiones["radio"] **2
    
    def calcular_perimentro(self):
        return 2 * math.pi * self.dimensiones["radio"]

class Rectangulo(Forma):
    def __init__(self, color, base , altura):
        super().__init__(color, dimensiones ={"base": base , "altura": altura})
        
    def calcular_area(self):
        return (self.dimensiones["base"] * self.dimensiones["altura"])
    
    def calcular_perimentro(self):
        return 2 * (self.dimensiones["base"] + self.dimensiones["altura"])
    
circulo = Circulo("Rojo", 2)
print("Area Circulo:" , circulo.calcular_area())
print("Perimetro Circulo:" , circulo.calcular_perimentro())

rectangulo = Rectangulo("Verde", 2,3)
print("Area Rectangulo:" , rectangulo.calcular_area())
print("Perimetro Rectangulo:" , rectangulo.calcular_perimentro())