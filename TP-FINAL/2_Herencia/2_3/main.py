from Circulo import Circulo
from Rectangulo import Rectangulo

circulo = Circulo("Rojo", 2)
print("-----------Cicrculo-----------------")
print("Area Circulo:" , circulo.calcular_area())
print("Perimetro Circulo:" , circulo.calcular_perimentro())

rectangulo = Rectangulo("Verde", 2,3)
print("-----------Rectangulo---------------")
print("Area Rectangulo:" , rectangulo.calcular_area())
print("Perimetro Rectangulo:" , rectangulo.calcular_perimentro())