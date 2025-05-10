#### Práctico 5: Listas

###   DIANA FALLA REPOMA

## ACTIVIDAD 1
#  Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función range.

lista_4 = list(range(4, 101, 4))
print(lista_4)


## ACTIVIDAD 2
#   Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el penúltimo

generos_musica = ["rock", "pop", "salsa", "cumbia", "Metal"]
print(generos_musica[3])


## ACTIVIDAD 3
# Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por pantalla.

lista_vacia = []
lista_vacia.append("rojo")
lista_vacia.append("verde")
lista_vacia.append("azul")

print(lista_vacia)


## ACTIVIDAD 4
# Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”,
#  respectivamente. Imprimir la lista resultante por pantalla. 

animales = ["tigre", "leon", "jirafa", "elefante"]

animales[1] = "loro"
animales[3] = "oso"

print(animales)

## ACTIVIDAD 5
# Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza.

numeros=[8,15,3,22,7]
numeros.remove(max(numeros))
print(numeros)

# RESPUESTA ACTIVIDAD 5:Ç
# Primero crea una lista llamada numeros, con los numeros indicados dentro de los corchetes
#  En la siguiente linea encuentra cual es el valor maximo y ese elimina de la lista
#  Finalmente imprime por pantalla la lista resultante



## ACTIVIDAD 6
# Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por pantalla los dos primeros.

numeros = list(range(10, 31, 5))
print(numeros[0:2])


## ACTIVIDAD 7
# Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores cualesquiera.

autos = ["sedan", "polo", "suran", "gol"]

autos[1] = "Nivus"
autos[2] = "Taos"

print(autos)


## ACTIVIDAD 8
# Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append
# directamente. Imprimir la lista resultante por pantalla

dobles = []

dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)

print(dobles)


## ACTIVIDAD 9

compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

compras[2].append("jugo")
compras[1][1] = "tallarines"
compras[0].remove("pan")

print(compras)


## ACTIVIDAD 10

lista_anidada = [15, True, [25.5,57.9,30.6], False]
print(lista_anidada)