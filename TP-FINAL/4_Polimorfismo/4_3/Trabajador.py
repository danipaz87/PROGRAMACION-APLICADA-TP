from  Empleado import Empleado

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