#python3

from math import *

# Ejercicio 1

# 1)
def imprimirHolaMundo() -> None: print ("Hola Mundo")


# 2)
def imprimirUnVerso() -> None: print ("It's new, the shape of your body\nIt's blue, the feeling I've got\nAnd it's ooh, whoa, oh\nIt's a cruel summer\nIt's cool, that's what I tell 'em\nNo rules, in breakable heaven\nBut ooh, whoa, oh\nIt's a cruel summer\nWith you")

# 3)
def raizDe2() -> float: 
    x = round (sqrt (2), 4)
    return x

# 4)
def factorial2() -> int:
    return factorial (2)

# 5)
def perimetro() -> float:
    return 2 * pi

# Ejercicio 2

# 1)
def imprimirSaludo(nombre:str) -> None: 
    print ("Hola " + nombre)

# 2)
def raizCuadradaDe(numero:int) -> float:
    return sqrt (numero)

# 3) 
def fahrenheitACelsius(t:float) -> float:
    return ((t - 32) * 5)/9

# 4)
def imprimirDosVeces(estribillo:str) -> None:
    return ((estribillo + "\n")*2)

# 5)
def esMultiploDe(n:int, m:int) -> bool:
    if n % m == 0:
        return True
    else:
        return False
    
# 6)
def esPar(numero:int) -> bool:
    if esMultiploDe (numero, 2) == True:
        return True
    else:
        return False

# 7)
def cantidadDePizzas(comensales:int, minCantDePorciones: int) -> int:
    return ceil((comensales * minCantDePorciones)/8)

# Ejercicio 3

# 1)
def algunoEs0(numero1:int, numero2:int) -> bool:
    res = numero1 == 0 or numero2 == 0
    return res

# 2)
