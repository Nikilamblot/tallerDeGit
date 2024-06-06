# Ejercicio 1
def ind_nesima_aparicion(s:list[int], n:int, elem:int) -> int:
    lista:list[int] = s.copy()
    i:int = 0
    posicion:int = -1
    if elem in lista:
        while n > 0 and i < len(lista):
            if lista[i] == elem:
                n -= 1
                if n == 0:
                    posicion = i
                i +=1
            else:
                i += 1
    return posicion

print(ind_nesima_aparicion([-1, 1, 1, 5, -7, 1, 3], 2, 1))

# Ejercicio 2
def mezclar(s1:list[int], s2:list[int]) -> list[int]:
    listaPar:list[int] = s1.copy()
    listaImpar:list[int] = s2.copy()
    listaNueva:list[int] = []
    i = 0
    while i < len(listaImpar):
        listaNueva.append(listaPar[i])
        listaNueva.append(listaImpar[i])
        i += 1
    return listaNueva

print(mezclar([1, 3, 0, 1], [4, 0, 2, 3]))

# Ejercicio 3
def frecuencia_posiciones_por_caballo(caballos:list[str], carreras:dict[str,list[str]]) -> dict[str,list[int]]:
    posiciones:dict[str,list[int]] = dict()
    for caballo in caballos:
        posiciones[caballo] = [0]*len(caballos)
    posicionesPorCarrera:list[list[str]] = list(carreras.values())
    for caballo in caballos:
        for carrera in posicionesPorCarrera:
            i:int = 0
            while i < len(carrera):
                if carrera[i] == caballo:
                    lugares:list[int] = posiciones[caballo]
                    lugares[i] += 1
                    i += 1
                else:
                    i += 1
    return posiciones

caballos= ["linda", "petisa", "mister", "luck" ]
carreras= {"carrera1":["linda", "petisa", "mister", "luck"],"carrera2":["petisa", "mister", "linda", "luck"]}

print(frecuencia_posiciones_por_caballo(caballos, carreras))

#Ejercicio 4
#m = [[1,2,2,1],[-5,6,6,-5],[0,1,1,0]]
def matriz_capicua(m:list[list[int]]) -> bool:
    res = True
    lista:list[list[int]] = m.copy()
    for sublista in lista:
        i:int = len(sublista) - 1
        inversa:list[int] = []
        while i >= 0:
            inversa.append(sublista[i])
            i -= 1
        if inversa != sublista:
            res = False
    return res

print(matriz_capicua([[1,2,2,1],[-5,6,6,-5],[0,1,1,0]]))