####     Práctico 4: Estructuras repetitivas

import random
###  DIANA FALLA REPOMA

## ACTIVIDAD 1
##  1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
##  (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

for i in range(101):
    print(i)


## ACTIVIDAD 2
## 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de dígitos que contiene.

num = int(input("Ingresa un número entero: "))  
cant = len(str(abs(num))) 
print(f"Número ingresado: {num} , la cantidad de digitos que tiene es:  {cant} ")


## ACTIVIDAD 3
#  3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
#     dados por el usuario, excluyendo esos dos valores.

num1 = int(input("Ingresa el primer numero entero: "))
num2 = int(input("Ingresa el segundo numero entero: "))

if num1 < num2:
    inicio = num1 + 1
    fin = num2
else:
    inicio = num2 + 1
    fin = num1

suma = 0
for x in range(inicio, fin):
    suma += x
suma = sum(range(inicio, fin))

print(f"La suma de los números entre {num1} y {num2}, excluyéndolos, es: {suma}")


## ACTIVIDAD 4
## 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en secuencia. 
# El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.

acum = 0 

print("Ingrese sus números para sumarlos. SI INGRESA 0 finaliza.")

while True:
    numero = int(input("Ingrese un número entero: "))
    if numero == 0: 
        break
    acum += numero 

print(f"La Suma es: {acum}")


## ACTIVIDAD 5
#  Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
#   programa debe mostrar cuántos intentos fueron necesarios para acertar el número.


num_azar = random.randint(0, 9)

print("ADIVINA - Debe ser un número entre el 0 y 9")

cont = 0  
adivinaste = False 

while not adivinaste:
    
    numero_1 = int(input("Ingresa UN NUMERO: "))
    cont += 1  

    if numero_1 == num_azar:
        print("ADIVINASTE !!!!!!")
        adivinaste = True  
    elif numero_1 < num_azar:
        print("Prueba con un numero MAYOR")  
    else:
        print("Prueba con un NUMERO MENOR")  

print(f"TOTAL DE INTENTOS: {cont} ")


## ACTIVIDAD 6
# Desarrolla un programa que imprima en pantalla todos los números pares comprendidos entre 0 y 100, en orden decreciente.

print("ACTIVIDAD 6 - Pares entre 0 y 100 en orden decreciente:")

for num_x in range(100, -1, -2):
    print(num_x)



## ACTIVIDAD 7
#  Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un número entero positivo 
# indicado por el usuario.

valor1 = int(input("Ingresa UN NUMERO ENTERO POSITIVO: "))
if valor1 >= 0:
    suma = 0
    limite= valor1 + 1
    for i in range(limite):  
        suma += i
    print(f"La suma entre 0 y {valor1} es: {suma}")
else:
    print("Ingresa un número entero positivo")


## ACTIVIDAD 8

cont_pares = 0
cont_impares = 0
cont_positivos = 0
cont_negativos = 0

print(f"Ingresa 100 números enteros:")

for i in range(100):
    numero = int(input(f"Ingresa un número {i + 1}: "))  

    if numero > 0:
        cont_positivos += 1
    elif numero < 0:
        cont_negativos += 1

    if numero % 2 == 0:
        cont_pares += 1
    else:
        cont_impares += 1

print(f"\nTOTALES:")
print(f"TOTAL de números pares: {cont_pares}")
print(f"TOTAL de números impares: {cont_impares}")
print(f"TOTAL de números positivos: {cont_positivos}")
print(f"TOTAL de números negativos: {cont_negativos}")


## ACTIVIDAD 9

suma = 0

print(f"Ingresa 100 números enteros:")

for i in range(100):
    numero = int(input(f"Ingresa el número {i + 1}: ")) 
    suma += numero 

media = suma / 100

print(f"\nLa media es: {media}")


## ACTIVIDAD 10

# Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

numero_y = int(input("Ingrese UN NUMERO a INVERTIR: "))
numero_pos = abs(numero_y)

numero_inv = 0

while numero_pos > 0:
    digito = numero_pos % 10  
    numero_inv = numero_inv * 10 + digito 
    numero_pos //= 10 

if numero_y < 0:
    numero_inv = -numero_inv

print(f"El número invertido es: {numero_inv}")
