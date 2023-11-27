from Producto import Producto
from Cliente import Cliente
from CaritoCompra import CarritoCompra


bebida = Producto(1001,"Fernet", 4500 , 100)
alimento =Producto(2001,"Papas Lays", 1000 , 150 )

cliente = Cliente("Daniela Paz", "Av. Cabildo 1500 - CABA")
print("-----------------Creando Carrito------------------")
print(cliente.crear_carrito(1))
print(cliente.realizar_compra())
carrito = CarritoCompra()
carrito.agregar_producto(bebida)
carrito.agregar_producto(alimento)
print("-----------------Carrito--------------------------")
print(bebida.mostrar_abm_articulo())
print(alimento.mostrar_abm_articulo())
print(carrito.calcular_total_cantidad())
print(carrito.calcular_total_importe())
print("--------------eliminando articulo-----------------")
carrito.quitar_producto(alimento)
print(alimento.mostrar_abm_articulo())
print("-----------------Carrito--------------------------")
print(bebida.mostrar_abm_articulo())
print(carrito.calcular_total_cantidad())
print(carrito.calcular_total_importe())
