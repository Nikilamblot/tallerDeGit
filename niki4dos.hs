-- Ejercicio 1
fib :: Integer -> Integer
fib 0 = 0
fib 1 = 1
fib n = fib (n - 1) + fib (n - 2)

-- Ejercicio 2
parteEntera :: Float -> Integer
parteEntera x | x >= 0 && x < 1 = 0
              | otherwise = parteEntera (x - 1) + 1

-- Ejercicio 3
esDivisible :: Integer -> Integer -> Bool
esDivisible x y | x == 0 = True
                | x < 0 = False
                | otherwise = esDivisible (x - y) y

-- Ejercicio 4
sumaImpares :: Integer -> Integer
sumaImpares n | n == 1 = 1
              | otherwise = sumaImpares (n - 1) + 2 * n - 1 

-- Ejercicio 5
medioFact :: Integer -> Integer
medioFact n | n == 0 = 1
            | n == 1 = 1
            | otherwise = medioFact (n - 2) * n

-- Ejercicio 6
sumaDigitos :: Integer -> Integer
sumaDigitos n | n > 0 && n < 10 = n
              | otherwise = sumaDigitos (div n 10) + (mod n 10)

-- Ejercicio 7
todosDigitosIguales :: Integer -> Bool
todosDigitosIguales n | n < 10 = True
                      | otherwise = todosDigitosIguales (sacarUnidades n) && ultimoDigito (sacarUnidades n) == ultimoDigito n

sacarUnidades :: Integer -> Integer
sacarUnidades n = div n 10

ultimoDigito :: Integer -> Integer
ultimoDigito n = mod n 10

-- Ejercicio 8
iesimoDigito :: Integer -> Integer -> Integer
iesimoDigito n i | cantDigitos n == i = mod n 10
                 | otherwise = iesimoDigito (sacarUnidades n) i

cantDigitos :: Integer -> Integer
cantDigitos n | n < 10 = 1
              | otherwise = cantDigitos (div n 10) + 1

-- Ejercicio 9
esCapicua :: Integer -> Bool
esCapicua n | cantDigitos n == 1 = True
            | cantDigitos n == 2 = todosDigitosIguales n
            | otherwise = iesimoDigito n 1 == iesimoDigito n (cantDigitos n) && esCapicua (sacarUltyPrim n)

sacarUltyPrim :: Integer -> Integer
sacarUltyPrim n | cantDigitos n == 1 || cantDigitos n == 2 = n
                | otherwise = mod (sacarUnidades 10) 10

-- Ejercicio 10
-- a)
f1 :: Int -> Int
f1 n | n == 0 = 1
     | otherwise = f1 (n - 1) + 2^n

-- b)
f2 :: Int -> Float -> Float
f2 n q | n == 1 = q
       | otherwise = f2 (n - 1) q + q^n

-- Ejercicio 11
eAprox :: Int -> Float
eAprox n | n == 0 = 1
         | otherwise = eAprox (n - 1) + 1 / fromIntegral (fact n)

fact :: Int -> Int
fact n | n == 0 = 1
       | otherwise = fact (n - 1) * n

e :: Float
e = eAprox 10

-- Ejercicio 12
raizDe2Aprox :: Integer -> Float
raizDe2Aprox n | n == 1 = 1
               | otherwise = sucesion n - 1

sucesion :: Integer -> Float
sucesion n | n == 1 = 2
           | otherwise = 2 + 1/sucesion (n - 1)

-- Ejercicio 13
g :: Int -> Int -> Int
g q m | m == 1 = q
      | otherwise = g q (m - 1) + q ^ m

f :: Int -> Int -> Int
f n m | n == 1 = g 1 m
      | otherwise = g n m + f (n - 1) m

-- Ejercicio 14
{--sumaPotencias :: Integer -> Integer -> Integer -> Integer--}

-- Ejercicio 15
sumaRacionales :: Integer -> Integer -> Float
sumaRacionales n q | n == 1 = 1/ fromIntegral q
                   | otherwise = sumaRacionales (n - 1) q + fromIntegral n / fromIntegral q

sumaRacionalesposta :: Integer -> Integer -> Float
sumaRacionalesposta n m | m == 1 = fromIntegral (suma n)
                        | otherwise = sumaRacionalesposta n (m - 1) + sumaRacionales n m

suma :: Integer -> Integer
suma x | x == 1 = 1
       | otherwise = suma (x - 1) + x

-- Ejercicio 16
-- a)
{--menorDivisor :: Integer -> Integer
menorDivisor n = menorDivisorDesde n 2

menorDivisorDesde :: Integer -> Integer -> Integer
menorDivisorDesde x y | x == y = 1
                      | mod x y == 0 = y
                      | otherwise = menorDivisorDesde x (y + 1)

-- b)
esPrimo :: Integer -> Bool
esPrimo n = menorDivisor n == n--}

-- c)
sonCoprimos :: Integer -> Integer -> Bool
sonCoprimos x y | x == y = False
                | otherwise = not (mod x (menorDivisorDesde2 x y 2) == 0 && mod y (menorDivisorDesde2 x y 2) == 0)

menorDivisorDesde2 :: Integer -> Integer -> Integer -> Integer
menorDivisorDesde2 x y z | mod x z == 0 && mod y z == 0 = z
                         | otherwise = menorDivisorDesde2 x y (z + 1)

-- d)
{--auxiliar :: Integer -> Integer -> Integer
auxiliar n k | n == 0 = 0
             | n == 1 = 2
             | esPrimo k = auxiliar (n-1) (k+1)
             | otherwise = auxiliar n (k+1)

nEsimoPrimo :: Integer -> Integer
nEsimoPrimo n = auxiliar n 2--}

-- Ejercicio 17

esFibonacci :: Integer -> Bool
esFibonacci n = fibonacciDesde n 1

fibonacciDesde :: Integer -> Integer -> Bool
fibonacciDesde n k | n == 0 = True
                   | n == 1 = True
                   | n < fib k = False
                   | otherwise = n == fib k || fibonacciDesde n (k+1)

-- Ejercicio 18
mayorDigitoPar :: Integer -> Integer
mayorDigitoPar n | aux n 1 == 0 = -1
                 | otherwise = aux n 1

esPar :: Integer -> Bool
esPar x = mod x 2 == 0

maximo :: Integer -> Integer -> Integer
maximo x y | x == y = x
           | x > y = x
           | x < y = y
 
aux :: Integer -> Integer -> Integer
aux x i | i > cantDigitos x = 0
        | esPar (iesimoDigito x i) == False = aux x (i+1)
        | otherwise = maximo (iesimoDigito x i) (aux x (i+1))
        
-- Ejercicio 19
esSumaInicialDePrimos :: Int -> Bool
esSumaInicialDePrimos n = n == sumaPrimos n 2

menorDivisorDesde :: Int -> Int -> Int
menorDivisorDesde x y | x == y = x
                      | mod x y == 0 = y
                      | otherwise = menorDivisorDesde x (y + 1)

menorDivisor :: Int -> Int
menorDivisor x = menorDivisorDesde x 2

esPrimo :: Int -> Bool
esPrimo x = menorDivisor x == x

sumaPrimos :: Int -> Int -> Int
sumaPrimos y x | y == sumaPrimos y (x - 1) = y
               | y < sumaPrimos y (x -1) = y - 1
               | esPrimo x == True = x + sumaPrimos y (x + 1)
               | otherwise = sumaPrimos y (x + 1)

-- Ejercicio 20
sumaDivisoresDesde :: Int -> Int -> Int
sumaDivisoresDesde n k | n < k = 0
                       | mod n k == 0 = k + sumaDivisoresDesde n (k + 1)
                       | otherwise = sumaDivisoresDesde n (k + 1)

sumaDiv :: Int -> Int
sumaDiv n = sumaDivisoresDesde n 1

maximo2 :: Int -> Int -> Int
maximo2 x y | x == y = x
           | x > y = x
           | x < y = y

maxSumaDiv :: Int -> Int -> Int
maxSumaDiv x y | x == y = sumaDiv x
               | x == y - 1 = maximo2 (sumaDiv x) (sumaDiv y)
               | sumaDiv x >= sumaDiv (x + 1) = maxSumaDiv (x + 2) y
               | otherwise = maxSumaDiv (x + 1) y

--tomaValorMax :: Int -> Int -> Int
--tomaValorMax x y 