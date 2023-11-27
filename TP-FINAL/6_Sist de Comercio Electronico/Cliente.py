from CaritoCompra import CarritoCompra

class Cliente:
    def __init__(self, nombre, direccion):
        self.nombre = nombre
        self.direccion = direccion
        self.carrito = CarritoCompra()
        
    def crear_carrito(self, producto):
        return "Carrito creado"

    def eliminar_del_carrito(self):
        return "Carrito eliminado"

    def realizar_compra(self):
        return(f"{self.nombre} esta realizando una compra,  a entregar en: {self.direccion}.")