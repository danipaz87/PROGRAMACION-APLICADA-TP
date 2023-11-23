"""Empleado: Crear las clases Empleado, Gerente y Trabajador. Se debe tener atributos como nombre, salario y 
departamento. Las subclases deben heredar y definir los métodos y atributos necesarios para
representar cada tipo de empleado."""

class Empleado():
    def __init__(self, nombre , salario , departamento):
        self.nombre = nombre
        self.salario = salario
        self.departamento = departamento
        
    def mostrar_empleado(self):
        pass
    
    def tipo_empleado(self):
        pass
        

class Gerente(Empleado):
    def __init__(self, nombre, salario, departamento, empleados_a_cargo):
        super().__init__(nombre, salario, departamento)
        self.empleados_a_cargo = empleados_a_cargo

    def mostrar_empleado(self):
        return f"Nombre: {self.nombre}, Salario: ${self.salario}, Departamento: {self.departamento} , Cantidad de empleados: {self.empleados_a_cargo}"
    
    def tipo_empleado(self):
        return "El tipo de empleado es : Gernete General"  

        
class Trabajador(Empleado):
    def __init__(self, nombre, salario, departamento, tareas):
        super().__init__(nombre, salario, departamento)
        self.tareas = tareas
        
    def mostrar_empleado(self):
        return f"Nombre: {self.nombre}, Salario: ${self.salario}, Departamento: {self.departamento} , Tarea: {self.tareas}"
    
    
    def tipo_empleado(self):
        return f"El tipo de empleado es : {self.tareas}"   
    
    
gerente = Gerente(nombre="Leonardo Caldas", salario=950000, departamento="Gerencia", empleados_a_cargo="10")
print(gerente.mostrar_empleado())
print(gerente.tipo_empleado())

trabajador = Trabajador("Cristian Augusto", 450000, "Consultoria", "Asesorar clientes sobre el uso del sistema")
print(trabajador.mostrar_empleado())
print(trabajador.tipo_empleado())
