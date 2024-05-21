# Ejercicio 1.1
def pertenece (lista:list[int], numero:int) -> bool:
    condicion:bool = True
    i:int = 0
    longitud:int = len(lista)
    while i < longitud:
        if lista[i] == numero:
            return condicion
        else:
            i += 1
    return False

print (pertenece ([1,2,3,4], 3))

#Ejercicio 1.3
def suma_total(lista:list[int])-> int:
    total:int = 0
    i:int = 0
    longitud:int = len(lista)
    while i < longitud:
        total += lista[i]
        i += 1
    return total

print (suma_total ([1,2,3,4]))

# Ejercicio 1.7
def tiene_minuscula(contra:str) -> bool:
    longitud:int = len(contra)
    condicion:bool
    i:int = 0
    while i < longitud:
        if (contra[i] >= "a") and (contra[i] <= "z"):
            return True
        else:
            i += 1
    return False

print (tiene_minuscula("HOLA"))

def tiene_mayuscula(contra:str) -> bool:
    longitud:int = len(contra)
    condicion:bool
    i:int = 0
    while i < longitud:
        if (contra[i] >= "A") and (contra[i] <= "Z"):
            return True
        else:
            i += 1
    return False

print (tiene_mayuscula("hola"))

def tiene_num(contra:str) -> bool:
    longitud:int = len(contra)
    condicion:bool
    i:int = 0
    while i < longitud:
        if (contra[i] >= "0") and (contra[i] <= "9"):
            return True
        else:
            i += 1
    return False

print (tiene_num("hola"))

def fortaleza (contra:str) -> str:
    longitud:int = len(contra)
    i:int = 0
    while i < longitud:
        if (longitud > 8) and (tiene_minuscula(contra) == True) and (tiene_mayuscula(contra) == True) and (tiene_num(contra) == True):
            return "VERDE"
        elif longitud < 5:
            return "ROJA"
        else:
            return "AMARILLA"

print (fortaleza("hola"))

# Ejercicio 2.1
def es_par(numero:int) -> bool:
    if numero % 2 == 0:
        return True
    else:
        return False


def borra_pares (lista:list[int]) -> list [int]:
    i:int = 0
    longitud:int = len(lista)
    while i < longitud:
        if es_par(lista[i]) == True:
            lista.remove(lista[i])
            lista.insert(i,0)
            i += 1
        else:
            i += 1
    return lista

print (borra_pares([1,2,3,4,5]))

# Ejercicio 5.2
def pertenece_a_cada_uno_version_2 (lista:list[list[int]], e:int) -> list[bool]:
    i = 0
    longitud:int = len(lista)
    while i < longitud:
        if pertenece (lista[i],e):
            lista.remove(lista[i])
            lista.insert(i,True)
            i += 1
        else:
            lista.remove(lista[i])
            lista.insert(i,False)
            i += 1
    return lista

print (pertenece_a_cada_uno_version_2([[1,2,3,4,5],[5,6,7,8],[3,4,5,6]],4))