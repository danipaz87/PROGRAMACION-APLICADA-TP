"""FiguraGeometrica: Utilizar clases FiguraGeometrica, Circulo, Rectangulo y Triangulo y que contenga métodos 
y atributos relacionados con el cálculo del área y perímetro de una figura geométrica. Definan los
métodos y atributos necesarios para calcular el área y el perímetro de cada tipo de figura utilizando 
los conceptos de abstracción."""

from math import pi 

class FiguraGeometrica:
    def __init__(self):
        pass

    def calculararea(self):
        pass
    
    def calcularperimetro(self):
        pass
    
class Circulo(FiguraGeometrica):
    def __init__(self, radio):
        self.radio = radio
        
    def calculararea(self):
        return pi * self.radio**2
    
    def calcularperimetro(self):
        return 2 * pi * self.radio
    
class Rectangulo(FiguraGeometrica):
    def __init__(self,  base, altura):
        self.base = base
        self.altura = altura

    def calculararea(self):
        return (self.base * self.altura)

    def calcularperimetro(self):
        return 2 * (self.base + self.altura)

class Triangulo(FiguraGeometrica):
    def __init__(self,base, altura, lado1, lado2, lado3):
        self.base = base
        self.altura = altura
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def calculararea(self):
        return (self.base * self.altura) / 2

    def calcularperimetro(self):
        return self.lado1 + self.lado2 + self.lado3
    

circulo = Circulo(2)
print("Area Circulo:", circulo.calculararea())
print("Perimetro Circulo:", circulo.calcularperimetro())

rectangulo = Rectangulo(2,3)
print("Area Rectangulo:" ,rectangulo.calculararea())
print("Perimetro Rectangulo:" ,rectangulo.calcularperimetro())

triangulo = Triangulo(2,3,4,5,6)
print("Area Triangulo:", triangulo.calculararea())
print("Perimetro Triangulo:" ,triangulo.calcularperimetro())
