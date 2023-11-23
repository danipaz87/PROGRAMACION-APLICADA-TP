"""Diseña un sistema de comercio electrónico para una tienda en línea. Debes implementar las siguientes clases:
Producto: Una clase que representa un producto con atributos como nombre, precio, cantidad en stock, etc.
CarritoCompra: Una clase que representa el carrito de compras de un cliente.
Debe permitir agregar, eliminar y calcular el total de los productos en el carrito.
Cliente: Una clase que representa a un cliente con atributos como nombre,dirección, carrito de compra, etc.
Crea instancias de estas clases y demuestra cómo un cliente puede agregar productos a su carrito, realizar una compra y calcular el total.
Importante: Se deberá escribir un detalle del ejercicio explicando de qué manera lo resolvieron, cómo aplicaron los distintos conceptos de la POO."""

class Producto():
    def __init__(self, cod_articu,  nombre, precio, cant_stock):
        self._cod_articu = cod_articu
        self.nombre = nombre
        self._precio = precio
        self.cant_stock = cant_stock
    
    @property
    def cod_articu(self):
        return self._cod_articu
    
    @property
    def precio(self):
        return self._precio
    
    def mostrar_abm_articulo(self):
        return f"Cód. articulo: {self._cod_articu} Descripción: {self.nombre} Precio: {self._precio}"
    
class Carrito:
    def __init__(self):
        self.productos = []
        
    def agregar_producto(self, producto):
        self.productos.append(producto)
    
    def quitar_producto(self, producto):
        if producto in self.productos:
            self.productos.remove(producto)
            
                  
    def calcular_total(self):
        total_productos = 0
        for item in self.productos:
            total_productos += 1
        return f"El total de productos es de : {total_productos}"
    
class Cliente:
    def __init__(self, nombre, direccion):
        self.nombre = nombre
        self.direccion = direccion
        self.carrito = Carrito()
        
    def crear_carrito(self, producto):
        return "Carrito creado"

    def eliminar_del_carrito(self):
        return "Carrito eliminado"

    def realizar_compra(self):
        total = self.__carrito.calcular_total()
        print(f"Compra realizada por {self.__nombre} por un total de ${total}.")
        self.carrito = Carrito()
        
bebida = Producto(1001,"Fernet", 4500 , 100)
alimento =Producto(2001,"Papas Lays", 1000 , 150 )

cliente = Cliente("Daniela Paz", "Av. Cabildo 1500 - CABA")
print("-----------------Creando Carrito------------------")
print(cliente.crear_carrito(1))
carrito = Carrito()
carrito.agregar_producto(bebida)
carrito.agregar_producto(alimento)
print("-----------------Carrito--------------------------")
print(bebida.mostrar_abm_articulo())
print(alimento.mostrar_abm_articulo())
print(carrito.calcular_total())
print("--------------eliminando articulo-----------------")
carrito.quitar_producto(alimento)
print("-----------------Carrito--------------------------")
print(bebida.mostrar_abm_articulo())
print(carrito.calcular_total())



