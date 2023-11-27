from abc import ABC, abstractmethod

class Figura3D(ABC):                            #Abstraccion

    def __init__(self):
        pass

    @abstractmethod
    def calcular_volumen(self):
        pass
    @abstractmethod
    def calcular_area_superficial(self):
        pass
    