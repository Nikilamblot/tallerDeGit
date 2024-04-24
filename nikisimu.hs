-- Ejercicio 1
relacionesValidas :: [(String, String)] -> Bool
relacionesValidas [] = True
relacionesValidas ((a,b):xs) | a == b = False
                                   | pertenece (a,b) xs = False
                                   | otherwise = relacionesValidas xs

tuplasIguales :: (String, String) -> (String, String) -> Bool
tuplasIguales (a,b) (c,d) | a == d && b == c = True
                          | a == c && b == d = True
                          | otherwise = False

pertenece :: (String, String) -> [(String, String)] -> Bool
pertenece _ [] = False
pertenece (a,b) ((x,y):xs) | tuplasIguales (a,b) (x,y) = True
                           | otherwise = pertenece (a,b) xs

--------------------------------
personas :: [(String, String)] -> [String]
personas [] = []
personas ((a,b):xs) = quitarrepetidos (a : b : personas xs)

quitarrepetidos :: [String] -> [String]
quitarrepetidos [] = []
quitarrepetidos (x:xs) | pertenece2 x xs = quitarrepetidos xs
                       | otherwise = x : quitarrepetidos xs



pertenece2 :: String -> [String] -> Bool
pertenece2 _ [] = False
pertenece2 e (x:xs) | e == x = True
                    | otherwise = pertenece2 e xs