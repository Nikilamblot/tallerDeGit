import random

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

# Ejercicio 1.4
def ordenados(s:list[int]) -> bool:
    lista = s.copy()
    i = 0
    longitud = len(lista)
    while i < longitud - 1:
        if lista[i] < lista[i+1]:
            res = True
            i += 1
        else:
            return False
    return res

print(ordenados([1,2,7,4,5]))

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

# Ejercicio 1.8
def saldoActual(operaciones:list[(chr,int)]) -> int:
    i = 0
    longitud = len(operaciones)
    saldoInicial = 0
    while i < longitud:
        if (operaciones[i])[0] == 'I':
            saldoInicial += (operaciones[i])[1]
            i += 1
        elif (operaciones[i])[0] == 'R':
            saldoInicial -= (operaciones[i])[1]
            i += 1
        else:
            i +=1
    return saldoInicial

print(saldoActual([('R',2),('I',3),('R',4),('I',5)]))


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

# Ejercicio 2.4
def perteneceChr(lista:list[chr], letra:chr) -> bool:
    i:int = 0
    longitud:int = len(lista)
    while i < longitud:
        if letra == lista[i]:
            return True
        else:
            i += 1
    return False

def  reemplaza_vocales(frase:list[chr]) -> list[chr]:
    i:int = 0
    longitud:int = len(frase)
    while i < longitud:
        if perteneceChr(['a','e','i','o','u'], frase[i]):
            frase.remove(frase[i])
            frase.insert(i,'_')
            i += 1
        else:
            i += 1
    return frase

print (reemplaza_vocales(['h','o','l','a']))

# Ejercicio 2.6
def eliminar_repetidos(frase:str) -> str:
    i:int = 0
    fraseNueva:str = []
    longitud:int = len(frase)
    while i < longitud:
        if perteneceChr(fraseNueva, frase[i]):
            i += 1
        else:
            fraseNueva.append(frase[i])
            i += 1
    return fraseNueva

print (eliminar_repetidos('holoala'))

# Ejecicio 3
def notasMayores4(notas:list[int]) -> bool:
    res = notas.copy()
    i:int = 0
    longitud:int = len(res)
    while i < longitud:
        if res[i] >= 4:
            es = True
            i += 1
        else:
            return False
    return es

print(notasMayores4([7,4,5]))

#def promedio(notas:list[int]) -> float:
#    res = notas.copy()
#    i:int = 0
#    longitud:int = len(res)
#    total = 0
#    while i < longitud:
#        total += res[i]
#        i+=1
#    return (total/longitud)

def promedio(notas:list[int]) -> float:
    res = notas.copy()
    longitud:int = len(res)
    total = 0
    for i in range (0,longitud, 1):
        total += res[i]
    return (total/longitud)

print(promedio([7,4,5]))

def aprobado(notas:list[int]) -> int:
    res = notas.copy()
    if notasMayores4(res) == True and promedio(res) >= 7:
        numero = 1
    elif notasMayores4(res) == True and 4 <= promedio(res) <= 7:
        numero = 2
    else:
        numero = 3
    return numero

print(aprobado([7,8,9]))

# Ejercicio 4.1
def estudiantes() -> list[str]:
    alumno:str = input(f"Escriba un nombre: ")
    lista:list[str] = []
    while alumno != "Listo":
        lista.append(alumno)
        alumno = input(f"Escriba un nombre: ")
    return lista

#print (estudiantes())

# Ejercicio 4.2
def monedero_electronico() -> list[(chr,int)]:
    lista:list[(chr,int)] = []
    operacion:chr = 'C'
    while operacion != 'X':
        operacion:chr = input(f'Operacion a realizar: ')
        if operacion != 'X':
            monto:int = int(input(f'Monto para la operacion: '))
            lista.append((operacion,monto))
    return lista

#print(monedero_electronico())

# Ejercicio 4.3
def sieteYmedio() -> list[int]:
    total:float = 0
    lista:list[int] = []
    opciones:list[int] = [1,2,3,4,5,6,7,10,11,12]
    decision = "si"
    while decision == "si":
        numero:int = random.choice(opciones)
        print('Su carta es: ',numero)
        if numero == 10 or numero == 11 or numero == 12:
            total += 0.5
            print ('Su total es: ',total)
            lista.append(numero)
        else:
            total += numero
            print ('Su total es: ',total)
            lista.append(numero)
        if total <= 7.5:
            decision = input('Desea sacar otra carta? Si es así, responda "si", y en caso contrario responda "me planto": ')
        else:
            decision == "no"
            return print('Ha perdido, a continuación le dejamos su historial de cartas: ',lista)
    return lista

#print(sieteYmedio())

def pertenece_a_cada_uno_version_1(s:list[list[int]], e:int) -> list[bool]:
    lista:list[bool] = []
    for sublista in s:
        if pertenece (sublista,e):
            lista.append(True)
        else:
            lista.append(False)
    return lista

print (pertenece_a_cada_uno_version_1([[1,2,3,5],[5,6,7,8],[3,4,5,6]],4))

# Ejercicio 5.2
def pertenece_a_cada_uno_version_2 (lista:list[list[int]], e:int) -> list[bool]:
    i:int = 0
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

# Ejercicio 5.3
def mismaLongitud(lista:list[list[int]]) -> bool:
    i = 0
    longitud = len(lista)
    while i < longitud - 1:
        if len(lista[i]) == len(lista[i+1]):
            res = True
            i += 1
        else:
            return False
    return res

print(mismaLongitud([[1,2,3,4,5],[5,6,7,8,5],[3,4,5,6,7]]))

def es_matriz(s:list[list[int]]) -> bool:
    lista = s.copy()
    longitud = len(lista)
    if longitud > 0 and len(lista[0]) > 0 and mismaLongitud(lista) == True:
        return True
    else:
        return False

print(es_matriz([[1,2,3,4,5],[5,6,7,8,5],[3,4,5,6]]))

# Ejercicio 5.4
def filas_ordenadas(m:list[list[int]]) -> list[bool]:
    lista:list[bool] = []
    for sublista in m:
        if ordenados(sublista) == True:
            lista.append(True)
        else:
            lista.append(False)
    return lista

print(filas_ordenadas([[1,2,3,4,5],[5,6,7,8,5],[3,4,5,6]]))


#miLista = [5,2,3]
#for numero in miLista:
#    print(numero)

