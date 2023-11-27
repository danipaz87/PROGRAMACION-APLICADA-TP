from Producto import Producto

class CarritoCompra(Producto):                   #Herencia
    def __init__(self):
        self.productos = []
        
    def agregar_producto(self, producto):
        self.productos.append(producto)
    
    def quitar_producto(self, producto):
        if producto in self.productos:
            self.productos.remove(producto)
            
    def calcular_total_cantidad(self):
        total_productos = 0
        for item in self.productos:
            total_productos += 1
        return f"El total de productos es de : {total_productos}"
    
    def calcular_total_importe(self):
        suma = 0
        for producto in self.productos:
            suma += producto._precio
        return f"El total es de $ : {suma}"