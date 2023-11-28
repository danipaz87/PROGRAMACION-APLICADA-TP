from modulo1 import arrancar as auto_arranca

def frenar():
    return auto_arranca() + "Pise el freno para detener el vehiculo"

print(frenar())