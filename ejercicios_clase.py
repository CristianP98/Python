"""  Ejercicio-1: Definir una función max() que tome como argumento dos números y devuelva el mayor de ellos. (Es cierto que python tiene una función max() incorporada, pero hacerla nosotros mismos es un muy buen ejercicio. """

#%% 
def calcular(a: int, b: int)-> int:
    if a > b:
        return a
    else:
        return b
calcular(2,4)