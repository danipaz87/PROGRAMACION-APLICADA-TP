from FiguraGeometrica import FiguraGeometrica

class Rectangulo(FiguraGeometrica):
    def __init__(self,  base, altura):
        self.base = base
        self.altura = altura

    def calculararea(self):
        return (self.base * self.altura)

    def calcularperimetro(self):
        return 2 * (self.base + self.altura)