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
""" 
#Otra forma de hacerlo#
string = "hola"
print(len(string))
"""

""" 
#otra forma de hacerlo#
def contar_chars (string: str):
    pass
    
#%% tests
string = "Hola, qué tal?"
assert contar_chars(string)
"""


#4 - Escribir una función que tome un carácter y devuelva True si es una vocal, de lo contrario devuelve False.
#%%
def vocal(vocales):
    if vocales == 'a' or vocales == 'e'or vocales == 'i' or vocales == 'o' or vocales == 'u':
        return True
    else:
        return False
    

"""
#Como saber si hay algo en una coleccion de datos..

Verificar si el elemento esta en una lista

frutas = ["manzana, "pera", "kiwi"]
fruta_random = "kiwi"
print(fruta_random in frutas)

"""


""" 
#otra forma de hacer el ejercicio

vocales_lista = ["a","e","i","o","u"]
def verificar_vocal(vocal: str) -> bool:
  pass

#%% tests
assert verificar_vocal('a') == True
assert verificar_vocal('z') == False

"""

#Ejercicio-5: Escribir una función que calcule la longitud de una lista o una cadena dada. (Es cierto que python tiene la función len() incorporada, pero escribirla por nosotros mismos resulta un muy buen ejercicio.

#%% suma
sum(lista: list) -> int | float:
pass
#%% multiplicacion
def multiplicacion(lista: list) -> int | float:

#%% tests
assert sum([1, 2, 3, 4]) == 10
assert multiplicacion ([1, 2, 3, 4]) == 24