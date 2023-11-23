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
    
    def mostrar_info():
        pass
        
class Empleado(Persona):                       #Herencia     
    def __init__(self, nombre, edad, dni, salario, cargo):
        super().__init__(nombre, edad, dni)   
        self._salario = salario
        self.cargo = cargo
        
    @property
    def dni(self):                            #Encapsulamiento   
        return self._dni
    
    @property
    def salario(self):
        return self._salario
    
    @salario.setter
    def salario(self, salario):
        self._salario = salario
    
    def mostrar_info(self):
        return f"Nombre: {self.nombre} Edad: {self.edad} DNI:{self.dni} Salario: {self.salario} cargo: {self.cargo}"
    
    def calcular_salario(self):
        if self.cargo == "Administrativo":
            return self.salario * 0.1
        elif self.cargo == "Gerente":
            return self.salario * 0.3
        elif self.cargo == "Vendedor":
            return self.salario * 0.2
        
    
    def consultar_salario(self):
        if self.cargo == "Administrativo":
            return f"El salario es de: $ {self.salario}"
        elif self.cargo == "Gerente":
            return f"El salario es de: $ {self.salario}"
        elif self.cargo == "Vendedor":
            return f"El salario es de: $ {self.salario}"
    
class Gerente(Empleado):                          #Herencia
    def __init__(self, nombre, edad, dni, salario, cargo, departamento,emp_a_cargo, bono_objectivo):
        super().__init__(nombre, edad, dni, salario, cargo) 
        self.departamento = departamento
        self.emp_a_cargo = emp_a_cargo
        self.bono_objetivo = bono_objectivo
        
    def mostrar_info(self):
        return f"Nombre: {self.nombre} Edad: {self.edad} DNI:{self.dni} Salario: {self.salario} cargo: {self.cargo} Departamento: {self.departamento} Empleados a cargo: {self.emp_a_cargo}"
        
    def calcular_salario(self):                     #Polimorfismo
        if self.bono_objetivo is True:
            return self.salario+(self.salario * 0.1)
        else:
            return self.salario

        
class Departamento:
    def __init__(self):
        self.empleados = []
    
    def agregar_empleado(self, empleado):
        self.empleados.append(empleado)
    
    def eliminar_empleado(self, empleado):
        self.empleados.remove(empleado)
    
    def consultar_empleado(self):
        for empleado in self.empleados:
            return self.empleados
        
empleado = Empleado("Marisa Perez", 40 , 15465897, 500000, "Vendedor")
gerente = Gerente("Andres La Civita",50,16123852,1000000,"Gerente","Gerencia", 10 , 50000)

departamento = Departamento()


departamento.agregar_empleado(empleado)
departamento.agregar_empleado(gerente)

print("-----------------Empleados--------------------------")
empleado_departamento = departamento.consultar_empleado()
for empleado in empleado_departamento:
    print(empleado.mostrar_info())

print("-----------------Salarios--------------------------")
salario_calculado = empleado.calcular_salario()
print(empleado.consultar_salario())

salario_calculado = gerente.calcular_salario()
print(gerente.consultar_salario())



