"""Estudiante: Implementar la clase Estudiante con atributos como nombre, edad y calificaciones. Utilizar el 
encapsulamiento para proteger los datos que deban ser protegidos y proporcionar métodos públicos para
obtener dichos datos"""

class Estudiante:
    def __init__(self, nombre , edad, calificaciones):
        self.__nombre = nombre
        self.edad = edad
        self.__calificaciones = calificaciones
        
    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def calificaciones(self):
        return self.__calificaciones
    
        
    def mostrar_estudiante(self):
        return f"Nombre: {self.__nombre} Edad:  {self.edad} Calificación:  {self.__calificaciones}"
    
estudiante = Estudiante("Soledad Garcia", 40 , 10)
print(estudiante.mostrar_estudiante())