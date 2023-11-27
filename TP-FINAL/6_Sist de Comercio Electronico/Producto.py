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
    
    @property                                   #Encapsulamiento
    def cod_articu(self):
        return self._cod_articu
    
    @property
    def precio(self):
        return self._precio
    
    def mostrar_abm_articulo(self):
        return f"Cód. articulo: {self._cod_articu} Descripción: {self.nombre} Precio $: {self._precio}"
    
    
        



