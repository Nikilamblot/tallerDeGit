from queue import LifoQueue as Pila
from queue import Queue as Cola
import random
import typing

# Funciones auxiliares
def pertenece(lista:list[str], palabra:str) -> bool:
    for sublista in lista:
        if sublista == palabra:
            return True
        else:
            res = False
    return res

#print(pertenece(['hola', 'soy', 'niki'], 'soy'))

def copiar_cola(c:Cola) -> Cola:
    cola_aux:Cola = Cola()
    res:Cola = Cola()
    while not c.empty():
        cola_aux.put(c.get())
    while not cola_aux.empty():
        res.put(cola_aux.get())
    return res

def perteneceNumeroACola(c:Cola, num:int) -> bool:
    while not c.empty():
        if num == c.get():
            return True
    return False

# Ejercicio 1.1
def contar_lineas(nombre_archivo:str) -> int:
    archivo = open(nombre_archivo,'r')
    archivo_lineas = archivo.readlines()
    archivo.close()
    return len(archivo_lineas)
#print(contar_lineas('niki8.txt'))

# Ejercicio 1.2
def crearListaPorLinea(linea:str) -> list[str]:
    palabra:str = ''
    palabras:list[str] = []
    for caracter in linea:
        if caracter == ' ' or caracter == '\n' or caracter == '"':
            palabras.append(palabra)
            palabra = ''
        else:
            palabra += caracter
    palabras.append(palabra)
    return palabras

#print(crearListaPorLinea('hola que tal\n'))

def existe_palabra(nombre_archivo:str, palabra:str) -> bool:
    archivo = open(nombre_archivo,'r')
    archivo_lineas = archivo.readlines()
    archivo.close()
    for linea in archivo_lineas:
        linea = crearListaPorLinea(linea)
        if pertenece(linea, palabra):
            return True
    return False
#print(existe_palabra('niki8.txt', 'que'))

# Ejercicio 2
def esComentario(linea:str) -> bool:
    if linea[0] == '#':
        return True
    elif linea[0] == ' ':
        for caracter in linea:
            if caracter == '#':
                return True
            elif caracter == ' ':
                res = False
            else:
                return False
        return res
    else:
        return False
#print(esComentario('esto no es un comentario   # esto tampoco'))

def clonar_sin_comentarios(nombre_archivo:str) -> None:
    archivo:typing.IO = open(nombre_archivo, 'r')
    nuevoArchivo:typing.IO = open('clonando.txt', 'w')
    archivo_lineas:list[str] = archivo.readlines()
    i = 0
    longitud = len(archivo_lineas)
    while i < longitud:
        if esComentario(archivo_lineas[i]) == True:
            i += 1
        else:
            nuevoArchivo.write(archivo_lineas[i])
            i += 1
    archivo.close()
    nuevoArchivo.close()
    nuevoArchivo = open('clonando.txt', 'r')
    contenido = nuevoArchivo.read()
    print(contenido)
    nuevoArchivo.close()

#print(clonar_sin_comentarios('niki8.txt'))

# Ejercicio 3
def invertir_lineas(nombre_archivo: str) -> None:
    archivo:typing.IO = open(nombre_archivo, 'r')
    archivo2:typing.IO = open('reverso.txt', 'w')
    archivoLineas:list[str] = archivo.readlines()
    i = len(archivoLineas)
    if i > 0:
        archivo2.write(archivoLineas[i-1] + '\n')
    while i >= 2:
        archivo2.write(archivoLineas[i-2])
        i -= 1
    archivo.close()
    archivo2.close()
    archivo2:typing.IO = open('reverso.txt', 'r')
    contenido = archivo2.read()
    print(contenido)
    archivo2.close()

#print(invertir_lineas('niki8.txt'))

# Ejercicio 4
def agregar_frase_al_final(nombre_archivo:str, frase:str) -> None:
    archivo:typing.IO = open(nombre_archivo, 'r')
    archivo_lineas:list[str] = archivo.readlines()
    longitud:int = len(archivo_lineas)
    archivo.close()
    archivo:typing.IO = open(nombre_archivo, 'a')
    if pertenece(archivo_lineas[longitud - 1], '\n'):
        archivo.write(frase)
    else:
        archivo.write('\n' + frase)
    archivo.close()
    archivo:typing.IO = open(nombre_archivo, 'r')
    contenido = archivo.read()
    print(contenido)
    archivo.close()

#print(agregar_frase_al_final('niki8.txt', 'Niki'))

# Ejercicio 5
def agregar_frase_al_principio(nombre_archivo:str, frase:str) -> None:
    archivo:typing.IO = open(nombre_archivo, 'r')
    contenido = archivo.read()
    archivo.close()

    archivo:typing.IO = open(nombre_archivo, 'w')
    archivo.write(frase + '\n' + contenido)
    archivo.close()

    archivo:typing.IO = open(nombre_archivo, 'r')
    contenidoFinal = archivo.read()
    print (contenidoFinal)
    archivo.close()

#print(agregar_frase_al_principio('niki8.txt', 'Bienvenidos'))

# Ejercicio 8
def generar_nros_al_azar(cantidad:int, desde:int, hasta:int) -> Pila[int]:
    pila = Pila()
    for _ in range (cantidad):
        pila.put(random.randint(desde,hasta))
    return pila

pila = generar_nros_al_azar(4,1,10)
#print(pila.get())
#print(pila.get())
#print(pila.get())
#print(pila.get())

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

#print(cantidad_elementos(p9))

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

#print(buscar_el_maximo(p10))

# Ejercicio 11
def esta_bien_balanceada(s:str) -> bool:
    pila = Pila()
    for caracter in s:
        if caracter == '(':
            pila.put('(')
        elif caracter == ')':
            if pila.empty():
                return False
            else:
                pila.get()
    return pila.empty()

#print(esta_bien_balanceada('1 + ) 2 x 3 ( ( )'))

# Ejercicio 12
def evaluar_expresion(s:str) -> float:
    pila:Pila[float] = Pila()
    for caracter in s:
        if caracter != ' ' and caracter != '+' and caracter != '-' and caracter != '/' and caracter != '*':
            pila.put(caracter)
        elif caracter == '+':
            operando1:float = float(pila.get())
            operando2:float = float(pila.get())
            resultado:float = operando1 + operando2
            pila.put(resultado)
        elif caracter == '-':
            operando1:float = float(pila.get())
            operando2:float = float(pila.get())
            resultado:float = -(operando1 - operando2)
            pila.put(resultado)
        elif caracter == '/':
            operando1:float = float(pila.get())
            operando2:float = float(pila.get())
            resultado:float = operando1 / operando2
            pila.put(resultado)
        elif caracter == '*':
            operando1:float = float(pila.get())
            operando2:float = float(pila.get())
            resultado:float = operando1 * operando2
            pila.put(resultado)
    rta:float = pila.get()
    return rta

#print(evaluar_expresion('"3 4 + 5 * 2 -'))

# Ejercicio 13
def cola_nros_random(cantidad:int, desde:int, hasta:int) -> Cola[int]:
    cola:Cola[int] = Cola()
    pila:Pila[int] = generar_nros_al_azar(cantidad, desde, hasta)
    while not pila.empty():
        numero = pila.get()
        cola.put(numero)
    return cola

cola = cola_nros_random(4,1,10)
#print(cola.queue)

# Ejercicio 14
c14 = Cola()
c14.put(1)
c14.put(2)
c14.put(3)
c14.put(4)

def cantidad_elementos(c:Cola) -> int:
    cola:Cola = copiar_cola(c)
    cantidad:int = 0
    while not cola.empty():
        cola.get()
        cantidad += 1
    return cantidad

#print(cantidad_elementos(c14))

# Ejercicio 15
c15 = Cola()
c15.put(1)
c15.put(7)
c15.put(3)
c15.put(4)

def buscar_el_maximo(c:Cola[int]) -> int:
    cola:Cola = copiar_cola(c)
    maximo:int = cola.get()
    while not cola.empty():
        candidato:int = cola.get()
        if candidato > maximo:
            maximo = candidato
    return maximo

#print(buscar_el_maximo(c15))

# Ejercicio 16.1
def armar_secuencia_de_bingo() -> Cola[int]:
    cola:Cola[int] = Cola()
    cantidad:int = 100
    for _ in range (cantidad):
        numero = random.randint(0,99)
        if not perteneceNumeroACola(cola,numero):
            cola.put(numero)
    return cola

c = armar_secuencia_de_bingo()
print(c.queue)