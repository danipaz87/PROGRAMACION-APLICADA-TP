from FiguraGeometrica import FiguraGeometrica

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