"""Empleado: Utilizar la clase Empleado del ejercicio de herencia y aplicar polimorfismo para calcular el 
salario de acuerdo con las reglas específicas de cada tipo de empleado. Luego, crear una lista de
empleados de diferentes tipos y utilizar el polimorfismo para calcular sus salarios."""


class Empleado():
    def __init__(self, nombre , salario , departamento):
        self.nombre = nombre
        self.salario = salario
        self.departamento = departamento
        
    def mostrar_empleado(self):
        pass
    
    def tipo_empleado(self):
        pass
    
    def calcular_salario(self):
        return "Calculando Salario del empleado"



