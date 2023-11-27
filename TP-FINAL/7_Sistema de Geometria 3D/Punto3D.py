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