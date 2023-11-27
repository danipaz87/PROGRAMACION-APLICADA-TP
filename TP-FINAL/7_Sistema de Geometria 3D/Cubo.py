from Figura3D import Figura3D

class Cubo(Figura3D):                               #herencia

    def __init__(self, punto, lado):
        self.punto = punto
        self.lado = lado
    
    def calcular_volumen(self):                        #Polimorfismo
        return self.lado ** 3
    
    def calcular_area_superficial(self):                #Polimorfismo
        return 6 * self.lado ** 2