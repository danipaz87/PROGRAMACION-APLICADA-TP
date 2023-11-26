from Empleado import Empleado

class Trabajador(Empleado):
    def __init__(self, nombre, salario, departamento, tareas):
        super().__init__(nombre, salario, departamento)
        self.tareas = tareas
        
    def mostrar_empleado(self):
        return f"Nombre: {self.nombre}, Salario: ${self.salario}, Departamento: {self.departamento} , Tarea: {self.tareas}"
    
    
    def tipo_empleado(self):
        return f"El tipo de empleado es : {self.tareas}"   