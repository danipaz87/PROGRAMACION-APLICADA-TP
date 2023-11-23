"""Coche: Crear la clase Coche con atributos privados y/o públicos según corresponda de velocidad y 
kilometraje. Definir métodos públicos para acelerar y registrar el kilometraje de manera segura."""


class Coche:
    def __init__(self , marca , modelo , color , kilometraje, velocidad):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.__kilometraje = kilometraje
        self.__velocidad = velocidad
        
    @property
    def kilometraje(self):
        return self.__kilometraje
    @property
    def velocidad(self):
        return self.__velocidad
    
    @kilometraje.setter
    def kilometraje(self, kilometraje):
        self.__kilometraje = kilometraje
    
    @velocidad.setter
    def velocidad(self, velocidad):
        self.__velocidad = velocidad
        
    def mostrar_info_coche(self):
        return f"Marca: {self.marca} Modelo: {self.modelo} Color: {self.color} KM: {self.kilometraje} Velocidad: {self.velocidad}" 
    
    def acelerar(self, acelerar):
        self.acelerar = acelerar
        if acelerar >0:
            self.__velocidad += self.acelerar
        return f"Ustedes acelero a : {self.acelerar} km/h"

    
    def registrar_kilometraje(self, kilometraje):
        self.kilometraje = kilometraje
        if kilometraje >0:
            self.__kilometraje = kilometraje
        return f"Usted avanzo: {self.kilometraje} kms."
            
coche = Coche("Renault" , "Duster", "rojo", 15000, 0)
print(coche.mostrar_info_coche())
print(coche.acelerar(20))
print(coche.mostrar_info_coche())
print(coche.registrar_kilometraje(50))
print(coche.mostrar_info_coche())