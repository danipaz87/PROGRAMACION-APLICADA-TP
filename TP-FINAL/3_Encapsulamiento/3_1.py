"""CuentaBancaria: Crear la clase CuentaBancaria con atributos privados y públicos para el saldo y titular. 
Definir métodos para depositar, retirar y consultar el saldo de la cuenta."""


class CuentaBancaria:
    def __init__(self, titular , tipo_cuenta,  saldo):
        self.__titular = titular 
        self.tipo_cuenta = tipo_cuenta
        self.__saldo = saldo
        
    @property
    def titular(self):
        return self.__titular
    
    @property
    def saldo(self):
        return self.__saldo
    
    @saldo.setter 
    def saldo(self, saldo):
        self.__saldo = saldo
        
    
    def depositar(self, importe):
        self.importe = importe 
        if importe > 0:
            self.__saldo += importe
        return importe
    
    def retirar(self, importe):
        self.importe = importe
        if importe <= self.__saldo:
            self.__saldo -= importe
        return importe
    
    def consultar_saldo(self):
        return self.__saldo
    
cuenta = CuentaBancaria("Nicolas Toural", "Caja de Ahorro", 500000)
print("Titular:", cuenta.titular, "Tipo de cuenta:", cuenta.tipo_cuenta , "Saldo: $" , cuenta.saldo)
print("Deposito realizado $:" , cuenta.depositar(500))
print("Su saldo es de: $", cuenta.consultar_saldo())

print("Titular:", cuenta.titular, "Tipo de cuenta:", cuenta.tipo_cuenta , "Saldo: $" , cuenta.saldo)
print("Retiro realizado $:" , cuenta.retirar(1000))
print("Su saldo es de: $", cuenta.consultar_saldo())
