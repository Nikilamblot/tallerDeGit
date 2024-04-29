-- Ejercicio 1.1
longitud :: [t] -> Integer
longitud [] = 0
longitud (_:xs) = longitud xs + 1

-- Ejercicio 1.2
ultimo :: [t] -> t
ultimo [x] = x
ultimo (x:xs) = ultimo xs

-- Ejercicio 1.3
principio :: [t] -> [t]
principio [x] = []
principio (x:xs) = x : principio xs

-- Ejercicio 1.4
reverso :: [t] -> [t]
reverso [] = []
reverso (x:xs) = ultimo (x:xs) : reverso (principio (x:xs))

-- Ejercicio 2.1
pertenece :: (Eq t) => t -> [t] -> Bool
pertenece _ [] = False
pertenece e (x:xs) = e == x || pertenece e xs

-- otra manera, con guardas: 
pertenece2 :: (Eq t) => t -> [t] -> Bool
pertenece2 e (a:b) | e == a = True
                   | otherwise = pertenece e b

-- Ejercicio 2.2
todosIguales :: (Eq t) => [t] -> Bool
todosIguales [] = False
todosIguales [x] = True
todosIguales (x:y:ys) = x == y && todosIguales (y:ys)

-- Ejercicio 2.3
todosDistintos :: (Eq t) => [t] -> Bool
todosDistintos [] = False
todosDistintos [x] = True
todosDistintos (x:y:ys) | x == y || todosDistintos (y:ys) = False
                        | otherwise = True

-- Ejercicio 2.4
hayRepetidos :: (Eq t) => [t] -> Bool
hayRepetidos [] = False
hayRepetidos [x] = False
hayRepetidos (x:xs) = pertenece x xs || hayRepetidos xs

-- Ejercicio 2.5
quitar :: (Eq t) => t -> [t] -> [t]
quitar e [] = []
quitar e (x:xs) | e == x = xs 
                | otherwise = x : quitar e xs

-- Ejercicio 2.6
quitarTodos :: (Eq t ) => t -> [t] -> [t]
quitarTodos e [] = []
quitarTodos e (x:xs) | e == x = quitarTodos e xs 
                     | otherwise = x : quitar e (quitarTodos e xs)

-- Ejercicio 2.7
eliminarRepetidos :: (Eq t) => [t] -> [t]
eliminarRepetidos [] = []
eliminarRepetidos [x] = [x]
eliminarRepetidos (x:y:ys) | x == y = x : quitarTodos x ys

-- Ejercicio 2.8
{--mismosElementosIzq :: (Eq t) => [t] -> [t] -> Bool
mismosElementosIzq [] [] = True
mismosElementosIzq [] _ = True
mismosElementosIzq (x:xs) (y:ys) = pertenece x (y:ys) && mismosElementos xs (y:ys)

mismosElementosDer :: (Eq t) => [t] -> [t] -> Bool
mismosElementosDer [] [] = True
mismosElementosDer _ [] = True
mismosElementosDer (x:xs) (y:ys) = pertenece y (x:xs) && mismosElementos (x:xs) ys--}

mismosElementosAux :: (Eq t) => [t] -> [t] -> Bool
mismosElementosAux [] _ = True
mismosElementosAux (x:xs) (y:ys) = pertenece x (y:ys) && mismosElementosAux xs (y:ys)

mismosElementos :: (Eq t) => [t] -> [t] -> Bool
mismosElementos (x:xs) (y:ys) = mismosElementosAux (x:xs) (y:ys) && mismosElementosAux (y:ys) (x:xs)

-- Ejercicio 3.3
maximo :: [Integer] -> Integer
maximo [x] = x
maximo (x:y:ys) | x > y = x
              | otherwise = maximo (y:ys)

-- Ejercicio 3.9
ordenar :: [Integer] -> [Integer]
ordenar [x] = [x]
ordenar (x:xs) = minimo (x:xs) : ordenar (quitar (minimo (x:xs)) (x:xs))

minimo :: [Integer] -> Integer
minimo [x] = x
minimo (x:y:ys) | x < y = x
              | otherwise = minimo (y:ys)

-- Ejercicio 4
--a)
sacarBlancosRepetidosAux :: [Char] -> [Char]
sacarBlancosRepetidosAux [] = []
sacarBlancosRepetidosAux [x] = [x]
sacarBlancosRepetidosAux [' ', ' '] = [' ']
sacarBlancosRepetidosAux (x:y:xs) | x == ' ' && y == ' ' = x : sacarBlancosRepetidos (xs)
                               | otherwise = x : y : sacarBlancosRepetidos (xs)

sacarBlancosFin :: [Char] -> [Char]
sacarBlancosFin [] = []
sacarBlancosFin [' ', ' '] = [' ']
sacarBlancosFin (x:xs) = x : sacarBlancosFin xs

sacarBlancosRepetidos :: [Char] -> [Char] 
sacarBlancosRepetidos [] = []
sacarBlancosRepetidos [x] = [x]
sacarBlancosRepetidos [' ', ' '] = [' ']
sacarBlancosRepetidos (x:y:xs) = sacarBlancosFin (sacarBlancosRepetidosAux (x:y:xs))

-- b)
contarPalabras :: [Char] -> Integer
contarPalabras [] = 0
contarPalabras [x] = 1
contarPalabras (x:y:xs) | y == ' ' = 1 + contarPalabras xs
                        | otherwise = contarPalabras (y:xs)

sacarBlancosPrin :: [Char] -> [Char]
sacarBlancosPrin [] = []
sacarBlancosPrin [' '] = []
sacarBlancosPrin (x:xs) | x == ' ' = xs
                        | otherwise = (x:xs)

-- c)
espaciosRepetidos :: [Char] -> [Char]
espaciosRepetidos [] = []
espaciosRepetidos [' '] = []
espaciosRepetidos [x] = [x]
espaciosRepetidos (x:y:ys) | x == ' ' && y == ' ' = espaciosRepetidos (y:ys)
                           | otherwise = x : y : espaciosRepetidos (ys)

primeraPalabraAux :: [Char] -> [Char]
primeraPalabraAux [] = []
primeraPalabraAux [' '] = []
primeraPalabraAux (x:xs) | x /= ' ' = x : primeraPalabraAux xs
                         | otherwise = []

primeraPalabra :: [Char] -> [Char]
primeraPalabra [] = []
primeraPalabra [' '] = []
primeraPalabra (x:xs) = primeraPalabraAux (sacarEspacioPrin (espaciosRepetidos(x:xs)))

sacarEspacioPrin :: [Char] -> [Char]
sacarEspacioPrin [] = []
sacarEspacioPrin [' '] = []
sacarEspacioPrin (x:xs) | x == ' ' = xs
                        | otherwise = (x:xs)

sacarEspacioFin :: [Char] -> [Char]
sacarEspacioFin [] = []
sacarEspacioFin [' '] = []
sacarEspacioFin (x:xs) = x : sacarEspacioFin xs

sacarPrimeraPalabraAux :: [Char] -> [Char] -> [Char]
sacarPrimeraPalabraAux xs [] = xs
sacarPrimeraPalabraAux (x:xs) (y:ys) | x == y = sacarPrimeraPalabraAux xs ys
                                     | otherwise = xs
sacarPrimeraPalabra :: [Char] -> [Char]
sacarPrimeraPalabra (x:xs) = sacarEspacioPrin (sacarPrimeraPalabraAux (sacarEspacioPrin(espaciosRepetidos(x:xs))) (primeraPalabra (x:xs))) 

palabras :: [Char] -> [[Char]]
palabras [] = []
palabras [x] = [[x]]
palabras (x:xs) = primeraPalabra (x:xs) : palabras (sacarEspacioFin (espaciosRepetidos (sacarPrimeraPalabra xs)))

--d)
cantLetras :: [Char] -> Integer
cantLetras [] = 0
cantLetras [x] = 1
cantLetras (x:xs) = 1 + cantLetras xs

primerElemento :: [[Char]] -> [Char]
primerElemento [] = []
primerElemento ((x:xs):ys) = (x:xs)

sacarPrimerElemento :: [[Char]] -> [[Char]]
sacarPrimerElemento [] = []
sacarPrimerElemento ((x:xs):ys) = ys

aux :: [[Char]] -> [Char]
aux [] = []
aux [x] = x 
aux ((x:xs):ys) | cantLetras (x:xs) >= cantLetras (primerElemento ys) = aux ((x:xs) : sacarPrimerElemento ys)
                | otherwise = aux ys

palabraMasLarga :: [Char] -> [Char]
palabraMasLarga [] = []
palabraMasLarga [x] = [x]
palabraMasLarga (x:xs) = aux (palabras (x:xs))

-- e)
aplanar :: [[Char]] -> [Char]
aplanar [] = []
aplanar [x] = x
aplanar ((x:xs):ys) = (x:xs) ++ aplanar ys

-- g)
aplanarConNBlancos :: [[Char]] -> Integer -> [Char]
aplanarConNBlancos [] _ = []
aplanarConNBlancos [x] _ = x
aplanarConNBlancos ((x:xs):ys) n = (x:xs) ++ (nBlancos n) ++ aplanarConNBlancos ys n

nBlancos :: Integer -> [Char]
nBlancos 0 = []
nBlancos 1 = [' ']
nBlancos n = [' '] ++ nBlancos (n - 1)