"""Forma: Implementar las clases Forma, Circulo y Rectangulo. La o las clases deben contener atributos como 
color y dimensiones. Las subclases deben heredar y definir métodos y atributos para calcular el área y 
el perímetro de cada forma."""


class Forma:
    def __init__(self, color, dimensiones):
        self.color = color
        self.dimensiones = dimensiones
        
    def calcular_area(self):
        pass
    
    def calcular_perimentro(self):
        pass