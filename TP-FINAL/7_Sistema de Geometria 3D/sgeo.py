"""Diseña un sistema de geometría tridimensional que trabaje con figuras en el espacio 3D. 
Debes implementar las siguientes clases:
Punto3D: Una clase que representa un punto en el espacio 3D con coordenadas x, y, y z.
Figura3D: Una clase abstracta que representa una figura tridimensional y define métodos abstractos para calcular su volumen y área superficial.
Cubo, Esfera y Cilindro: Subclases de Figura3D que implementan los métodos para calcular el volumen y 
área superficial específicos de cada figura.
Crea instancias de estas clases y demuestra cómo calcular el volumen y área superficial de diferentes figuras tridimensionales.
Importante: Se deberá escribir un detalle del ejercicio explicando de qué manera lo resolvieron, cómo aplicaron los 
distintos conceptos de la POO"""

import math
from abc import ABC, abstractmethod

class Punto3D:

    def __init__(self, x, y, z):
        self._x = x
        self._y = y
        self._z = z
    
    @property                               #Encapsulamiento
    def x(self):
        return self._x
    
    @property
    def y(self):
        return self._y
    
    @property
    def z(self):
        return self._z
    
class Figura3D(ABC):                            #Abstraccion

    def __init__(self):
        pass

    @abstractmethod
    def calcular_volumen(self):
        pass
    @abstractmethod
    def calcular_area_superficial(self):
        pass
    
class Cubo(Figura3D):                               #herencia

    def __init__(self, punto, lado):
        self.punto = punto
        self.lado = lado
    
    def calcular_volumen(self):
        return self.lado ** 3
    
    def calcular_area_superficial(self):
        return 6 * self.lado ** 2
    
class Esfera(Figura3D):

    def __init__(self, punto, radio):
        self.punto = punto
        self.radio = radio
    
    def calcular_volumen(self):                            #polimorfismo
        return 4 / 3 * math.pi * self.radio ** 3
    
    def calcular_area_superficial(self):
        return 5 * math.pi * self.radio ** 2
    
class Cilindro(Figura3D):

    def __init__(self, punto, radio, altura):
        self.punto = punto
        self.radio = radio
        self.altura = altura
    
    def calcular_volumen(self):
        return math.pi * self.radio * (self.radio + self.altura)

    def calcular_area_superficial(self):
        return 2 * math.pi * self.radio * (self.radio + self.altura)
    
punto1 = Punto3D(2, 3, 4)
cubo1 = Cubo(punto1, 4)
esfera1 = Esfera(punto1, 3)
cilindro1 = Cilindro(punto1, 3, 4)

print("-----------Cubo--------------------------")
print("Volumen:", cubo1.calcular_volumen())
print("Area superficial: ", cubo1.calcular_area_superficial())
print("----------------Esfera-------------------")
print("Volumen: ", esfera1.calcular_volumen())
print("Area superficial:", esfera1.calcular_area_superficial())
print("------------Cilindro---------------------")
print("Volumen: ", cilindro1.calcular_volumen())
print(f"Area superficial:  {cilindro1.calcular_area_superficial}")