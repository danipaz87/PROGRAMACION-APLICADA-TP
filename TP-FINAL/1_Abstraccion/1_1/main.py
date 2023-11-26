from Circulo import Circulo
from Rectangulo import Rectangulo
from Triangulo import Triangulo



circulo = Circulo(2)
print("-----------Cicrculo-----------------")
print("Area Circulo:", circulo.calculararea())
print("Perimetro Circulo:", circulo.calcularperimetro())

rectangulo = Rectangulo(2,3)
print("-----------Rectangulo---------------")
print("Area Rectangulo:" ,rectangulo.calculararea())
print("Perimetro Rectangulo:" ,rectangulo.calcularperimetro())

triangulo = Triangulo(2,3,4,5,6)
print("-----------Triangulo---------------")
print("Area Triangulo:", triangulo.calculararea())
print("Perimetro Triangulo:" ,triangulo.calcularperimetro())