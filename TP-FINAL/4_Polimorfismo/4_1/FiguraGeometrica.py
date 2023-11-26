"""FiguraGeometrica: Utilizar la clase FiguraGeometrica del ejercicio de abstracción y crear un método 
muestre información específica de la figura utilizando polimorfismo. Luego, crear una lista de figuras
geométricas de diferentes tipos y utilizar el polimorfismo para imprimir su información."""


from math import pi 

class FiguraGeometrica:
    def __init__(self, nombre):
        self.nombre = nombre

    def calculararea(self):
        return "Calculando area de la Figura"
    
    def calcularperimetro(self):
        return "Calculando perimetro de la Figura"
    
    def mostrar_informacion(self):
        return "Mostrando informacion de la Figura"
    
class Circulo(FiguraGeometrica):
    def __init__(self, nombre,  radio):
        super().__init__(nombre)
        self.radio = radio
        
    def calculararea(self):
        return pi * self.radio**2
    
    def calcularperimetro(self):
        return 2 * pi * self.radio
    
    def mostrar_informacion(self):
        return f"Nombre de la Forma: {self.nombre} Radio: {self.radio} "
    
class Rectangulo(FiguraGeometrica):
    def __init__(self, nombre,  base, altura):
        super().__init__(nombre)
        self.base = base
        self.altura = altura

    def calculararea(self):
        return (self.base * self.altura)

    def calcularperimetro(self):
        return 2 * (self.base + self.altura)
    
    def mostrar_informacion(self):
        return f"Nombre de la Forma: {self.nombre} Base: {self.base} Altura: {self.altura} "

class Triangulo(FiguraGeometrica):
    def __init__(self, nombre , base, altura, lado1, lado2, lado3):
        super().__init__(nombre)
        self.base = base
        self.altura = altura
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def calculararea(self):
        return (self.base * self.altura) / 2

    def calcularperimetro(self):
        return self.lado1 + self.lado2 + self.lado3

    def mostrar_informacion(self):
        return f"Nombre de la Forma: {self.nombre} Base: {self.base} Altura: {self.altura} Lados: {self.lado1} , {self.lado2}, {self.lado3}"
    

figura = [Circulo("Circulo",2), Rectangulo("Rectangulo", 2,3), Triangulo("Triangulo", 2,3,4,5,6)] 


for figuras in figura:
    print(figuras.mostrar_informacion())
    print(f"Area:", figuras.calculararea())
    print(f"Perimetro:" , figuras.calcularperimetro())



