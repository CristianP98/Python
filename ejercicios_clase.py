#Ejercicio-1: Definir una función max() que tome como argumento dos números y devuelva el mayor de ellos. (Es cierto que python tiene una función max() incorporada, pero hacerla nosotros mismos es un muy buen ejercicio.

#%% 
def calcular(a: int, b: int)-> int:
    if a > b:
        return a
    else:
        return b
calcular(2,4)

#Ejercicio-2:  Definir una función max_de_tres(), que tome tres números como argumentos y devuelva el mayor de ellos.
#%%
def calcular_tres(
        a: input,
        b: input,
        c: input)-> int:
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c    
calcular_tres(2,3,5)

#3 - Definir una función que calcule la longitud de una lista o una cadena dada. (Es cierto que python tiene la función len() incorporada, pero escribirla por nosotros mismos resulta un muy buen ejercicio.
#%%
def calcular_nombres(nombres):
    contador = 0
    for i in nombres:
            contador += 1
    return contador
print(calcular_nombres(input('Ingrese el texto que quiere ser contado: ')))