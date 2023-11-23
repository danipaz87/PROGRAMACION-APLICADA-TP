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

class Gerente(Empleado):
    def __init__(self, nombre, salario, departamento, empleados_a_cargo):
        super().__init__(nombre, salario, departamento)
        self.empleados_a_cargo = empleados_a_cargo

    def mostrar_empleado(self):
        return f"Nombre: {self.nombre}\nSalario: ${self.salario}, Departamento: {self.departamento} , Cantidad de empleados a cargo: {self.empleados_a_cargo}"
    
    def tipo_empleado(self):
        return "El tipo de empleado es : Gerente General"  
    
    def calcular_salario(self):
        super().calcular_salario()
        return self.salario+(self.salario * 0.30) #plus gerencial

        
class Trabajador(Empleado):
    def __init__(self, nombre, salario, departamento, tareas, asistencia):
        super().__init__(nombre, salario, departamento)
        self.tareas = tareas
        self.asistencia = asistencia 
        
        
    def mostrar_empleado(self):
        return f"Nombre: {self.nombre}\nSalario: ${self.salario}, Departamento: {self.departamento} , Tarea: {self.tareas}"
    
    
    def tipo_empleado(self):
        return f"El tipo de empleado es : {self.tareas}"   
    
    def calcular_salario(self):
        super().calcular_salario()
        if self.asistencia is True:
            return self.salario+(self.salario * 0.15)
        else:
            return self.salario
    
empleados  = [Gerente(nombre="Leonardo Caldas", salario=950000, departamento="Gerencia", empleados_a_cargo="10"),
            Trabajador("Cristian Augusto", 450000, "Consultoria", "Asesorar clientes sobre el uso del sistema", True)] 

for empleado in empleados: 
    print(empleado.mostrar_empleado())
    print(empleado.tipo_empleado())
    print(f"Sueldo Calculado:" , empleado.calcular_salario())



