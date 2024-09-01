"""
El codigo tiene como objetivo codificar y decodificar mensajes deacuerdo a un algoritmo el cual he denominado
algoritmo de la espiral hacia dentro, es bastante sencillo lo que hace es dividir al texto en arreglos de 3 caracteres
la primera posicion la deja en su lugar, despues toma la segunda posicion y la coloca al final
y la tercera posicion la coloca al medio, adicionalmente para codificarlo aumenta caracteres aleatorios en medio de cada
caracter dando como resultado final un arreglo de 5 caracteres

En caso de que el mensaje no sea multiplo de 3, y tenga caracteres con arreglos incompletos lo que hara el programa será:
en caso de que sobre un caracter repetirá el proceso inicial y dejara al caracter en esa posicion
en caso de que sobren 2 caracteres repetirá el segundo caracter en la posicion final y la del medio
Ejemplo: Hola
codificado quedaria asi: Hxlxoa , donde las x son los caracteres aleatorios, en este ejemplo hay 4 caracteres a codificar
por lo que el cuarto caracter solo se lo adiciona al final [Hxlxo][a]
en el caso de que sobren 2 caracteres quedaria asi
Ejemplo: Adios
codificacion: Axixdoxsxs , siguiendo la condicion de que repita el segundo caracter en la posicion final y del medio
para cumplir con la condicion, ya que este algoritmo primero genera la posicion final y despues la del medio y para evitar
confuciones con un caracter aleatorio decidi que simplemente lo repita
si se quisiese decodificar "Axixdoxsxs", quedaria asi "Adioss"
"""
import random
import string

def caracter_random():
    return random.choice(string.ascii_letters)

def codificar(mensaje):
    arreglo = ""
    longitud = len(mensaje)
    resto = longitud % 3

    for i in range(0, longitud - resto, 3):
        bloque = mensaje[i:i + 3]
        arreglo += bloque[0]            # Primer carácter
        arreglo += caracter_random()    # Carácter aleatorio
        arreglo += bloque[-1]           # Último carácter
        arreglo += caracter_random()    # Carácter aleatorio
        arreglo += bloque[1]            # Carácter del medio

    # Manejo del resto de caracteres
    if resto == 1:
        arreglo += mensaje[-1]          # Agrega el último carácter al final
    elif resto == 2:
        arreglo += mensaje[-2]          # Agrega el penúltimo carácter
        arreglo += caracter_random()    # Carácter aleatorio
        arreglo += mensaje[-1]          # Agrega el último carácter
        arreglo += caracter_random()    # Carácter aleatorio
        arreglo += mensaje[-1]          # Repite el penúltimo carácter

    return arreglo

def decodificar(codificacion):
    result = ""
    longitud = len(codificacion)
    resto = longitud % 5

    # Procesamiento de los bloques de 5 caracteres
    for i in range(0, longitud - resto, 5):
        bloque = codificacion[i:i + 5]
        result += bloque[0]          
        result += bloque[4]          
        result += bloque[2]          

    # Manejo del resto de caracteres
    if resto == 1:
        result += codificacion[-1]  
    elif resto == 2:
        result += codificacion[-2]  
        result += codificacion[-1]  

    return result

print("Selecciona una opción:")
print("1. Codificar")
print("2. Decodificar")
opcion = input("Opción: ")

if opcion == "1":
    parrafo = input("Introduce un párrafo para codificar: ")
    resultado = codificar(parrafo)
    print("Texto codificado:", resultado)

elif opcion == "2":
    parrafo_codificado = input("Introduce un parrafo para decodificar: ")
    resultado = decodificar(parrafo_codificado)
    print("Texto decodificado:", resultado)

else:
    print("Opción no válida.")
