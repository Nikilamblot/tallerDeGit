from queue import LifoQueue as Pila
import random

# Ejercicio 1
def contar_lineas(nombre_archivo:str) -> int:
    archivo = open(nombre_archivo,'r')
    archivo_lineas = archivo.readlines()
    archivo.close()
    return len(archivo_lineas)
print(contar_lineas('niki8.txt'))

# Ejercicio 8
def generar_nros_al_azar(cantidad:int, desde:int, hasta:int) -> Pila[int]:
    pila = Pila()
    for _ in range (cantidad):
        pila.put(random.randint(desde,hasta))
    return pila

# Ejercicio 9
p9 = Pila()
p9.put(1)
p9.put(4)
p9.put(2)
p9.put(0)
p9.put(3)

def cantidad_elementos(p:Pila) -> int:
    pila:Pila = p
    cantidad:int = 0
    while not pila.empty():
        pila.get()
        cantidad += 1
    return cantidad

print(cantidad_elementos(p9))

# Ejercicio 10
def buscar_el_maximo(p:Pila[int]) -> int:
    pila:Pila[int] = p
    maximo:int= pila.get()
    while not pila.empty():
        candidato:int = pila.get()
        if candidato > maximo:
            maximo = candidato
    return maximo

p10 = Pila()
p10.put(1)
p10.put(4)
p10.put(2)
p10.put(0)
p10.put(3)

print(buscar_el_maximo(p10))

