""" 


6 - Definir una función inversa() que calcule la inversión de una cadena. Por ejemplo la cadena "estoy probando" debería devolver la cadena "odnaborp yotse"

7 - Definir una función es_palindromo() que reconoce palíndromos (es decir, palabras que tienen el mismo aspecto escritas invertidas), ejemplo: es_palindromo ("radar") tendría que devolver True.

8 - Definir una función superposicion() que tome dos listas y devuelva True si tienen al menos 1 miembro en común o devuelva False de lo contrario. Escribir la función usando el bucle for anidado.

9 - Definir una función generar_n_caracteres() que tome un entero n y devuelva el caracter multiplicado por n. Por ejemplo: generar_n_caracteres(5, "x") debería devolver "xxxxx".

10 - Definir un histograma procedimiento() que tome una lista de números enteros e imprima un histograma en la pantalla. Ejemplo: procedimiento([4, 9, 7]) debería imprimir lo siguiente:
****
*********
*******
 """


"""  Ejercicio-1: Definir una función max() que tome como argumento dos números y devuelva el mayor de ellos. (Es cierto que python tiene una función max() incorporada, pero hacerla nosotros mismos es un muy buen ejercicio. """
#%% 
def max(num1, num2):
    if num1 > num2:
        return num1
    else: 
        return num2
print('El numero mayor es: ' + str(max(20, 40))) #Cambiar los valores para ver soluciones

""" Ejercicio-2:  Definir una función max_de_tres(), que tome tres números como argumentos y devuelva el mayor de ellos. """
#%% 
def max_de_tres(num1,num2,num3):
    if num1 > num2 and num1 > num3:
        return num1
    elif num2 > num1 and num2 > num3:
        return num2
    else:
        return num3
print ("El numero mayor es : "+ str(max_de_tres(12,20,32)))

#Ejercicio 3

""" 
3 - Definir una función que calcule la longitud de una lista o una cadena dada. (Es cierto que python tiene la función len() incorporada, pero escribirla por nosotros mismos resulta un muy buen ejercicio.
"""
#%% 
def longitud(cadena):
    contador = 0
    for i in cadena:
        contador += 1
    return contador
print(longitud(input('Ingrese el texto que quiere ser contado: '))) 

#Ejercicio 4
""" 
4 - Escribir una función que tome un carácter y devuelva True si es una vocal, de lo contrario devuelve False.
"""
#%%
def caracter(sera):
    sera = sera.lower() #lower se utiliza para convertir todos los caracteres de una cadena a minúsculas
    if sera == 'a' or sera == 'e' or sera == 'i' or sera == 'o' or sera == 'u':
        return True
    else:
        return False
print (caracter(input('Ingrese una sola letra: ')))

#Ejercicio 5
""" 
5 - Escribir una función sum() y una función multip() que sumen y multipliquen respectivamente todos los números de una lista. Por ejemplo: sum([1,2,3,4]) debería devolver 10 y multip([1,2,3,4]) debería devolver 24.
"""

# %%
