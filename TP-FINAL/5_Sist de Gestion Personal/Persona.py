"""Diseña un sistema de gestión de personal para una empresa. Debes implementar las siguientes clases:
Persona: Una clase base que representa a una persona con atributos como nombre, edad y DNI. 
Utiliza el encapsulamiento para proteger los datos sensibles.
Empleado: Una subclase de Persona que agrega atributos como salario y cargo. 
Implementa el cálculo del salario en base al cargo y permite consultar el salario.
Gerente: Una subclase de Empleado que agrega atributos específicos de un gerente, como departamento.
Departamento: Una clase que contiene una lista de empleados y métodos para agregar, eliminar y consultar 
empleados.
Crea instancias de estas clases y demuestra cómo agregar empleados a un departamento, calcular salarios y 
acceder a la información de las personas
Importante: Se deberá escribir un detalle del ejercicio explicando de qué manera lo resolvieron, como aplicaron los 
distintos conceptos de la POO."""

class Persona:
    def __init__(self, nombre, edad, dni):
        self.nombre = nombre
        self.edad = edad
        self._dni = dni                       #Encapsulamiento
    
    def mostrar_info():                       #Abstraccion
        pass
        




