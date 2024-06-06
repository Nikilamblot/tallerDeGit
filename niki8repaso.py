from queue import LifoQueue as Pila
from queue import Queue as Cola
import random
import typing

#funciones útiles
def copiarPila(p:Pila) -> Pila:           # Copia una Pila
    lista1:list = []
    lista2:list = []
    pCopia:Pila = Pila()
    while not p.empty():
        lista1.append(p.get())
    while len(lista1) > 0:
        lista2.append(lista1.pop())
    for i in lista2:
        p.put(i)
        pCopia.put(i)
    return pCopia

def copiarCola(c:Cola) -> Cola:           # Copia una Cola
    cCopia:Cola = Cola()
    lista:list = []
    while not c.empty():
        lista.append(c.get())
    for i in lista:
        c.put(i)
        cCopia.put(i)
    return cCopia

# Ejercicio 8
def generar_nros_al_azar(cantidad:int, desde:int, hasta:int) -> Pila[int]:
    pila:Pila[int] = Pila()
    for i in range (cantidad):
        pila.put(random.randint(desde,hasta))
    return pila
pila = generar_nros_al_azar(4,1,10)
#print(pila.get())
#print(pila.get())
#print(pila.get())
#print(pila.get())

# Ejercicio 9
def cantidad_elementos(p:Pila) -> int:
    pila_aux:Pila = Pila()
    cantidad:int = 0
    while not p.empty():
        pila_aux.put(p.get())
        cantidad += 1
    while not pila_aux.empty():
        p.put(pila_aux.get())
    return cantidad

p9 = Pila()
for i in [1,2,3,4]:
    p9.put(i)

#print(cantidad_elementos(p9))

# Ejercicio 10
def buscar_el_maximo(p:Pila[int]) -> int:
    pila:Pila[int] = copiarPila(p)
    maximo:int = pila.get()
    while not pila.empty():
        candidato:int = pila.get()
        if candidato > maximo:
            maximo = candidato
    return maximo

p10 = Pila()
for i in [1,7,3,4]:
    p10.put(i)

print(buscar_el_maximo(p10))

# Ejercicio 11
