# Importamos para realizar el Ejercicio 6
import random
from statistics import mode, median, mean




##### Ejercicio 1
#Escribir un programa que solicite la edad del usuario. 
#Si el usuario es mayor de 18 años, deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

#Ingrese su edad
edad = int(input("Por favor, ingrese su edad: "))

# Si la edad es mayor que 18, "Es mayor de edad"
if edad > 18:
  print("Es mayor de edad")


#### Ejercicio 2
#Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6,
#deberá mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el mensaje “Desaprobado”.

nota_alumno = float(input("Ingrese su nota: "))

if nota_alumno >=6:
  print("Aprobado")

else:
  print("Desaprobado")



#### Ejercicio 3
# Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un número par, 
# imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso contrario, imprimir 
# por pantalla "Por favor, ingrese un número par". 
# Nota: investigar el uso del operador de módulo (%) en Python para evaluar si un número es par o impar.

num = int(input("Ingrese un número (entero): "))

if num % 2 == 0:
  print("Ha ingresado un número PAR")

else:
  print("Por favor, ingrese un número par")



#### Ejercicio 4

# Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las siguientes categorías pertenece:
#   Niño/a:** menor de 12 años.
#   Adolescente:** mayor o igual que 12 años y menor que 18 años.
#   Adulto/a joven:** mayor o igual que 18 años y menor que 30 años.
#   Adulto/a:** mayor o igual que 30 años.

usuario_edad = int(input("Ingrese su edad: "))

if edad < 0:
  print("Debe ingresar un número positivo")

elif usuario_edad < 12:
  print("Niño/a")

elif 12 <= usuario_edad < 18:
  print("Adolescente")

elif 18 <= usuario_edad < 30:
  print("Adulto/a joven")

else:
  print("Adulto/a")

#### Ejercicio 5

contrasena = input("Ingrese su contraseña entre 8 y 14 caracteres: ")

if 8 <= len(contrasena) <= 14:
  print("Ingreso una contraseña correcta")
else:
  print("Debe ingresar una contraseña entre 8 y 14 caracteres")



#### Ejercicio 6
# Se importo en las primeras lineas de todo este código

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)


if media > mediana > moda:
  print("Sesgo positivo o a la derecha")

elif media < mediana < moda:
  print("Sesgo negativo o a la izquierda")

elif media == mediana == moda:
  print("No hay sesgo")

else:
  print("No se puede identificar si tiene o no")


################################
### Ejercicio 7

palabra = input("Ingrese una frase o palabra: ")

if palabra[-1] in ("AEIOUaeiou"):
  print(f"{palabra}!")

else:
  print(palabra)

################################
### Ejercicio 8

nombre = input("Ingrese su nombre: ")

print("""
Elija una OPCION:
1. Si quiere su nombre en mayúsculas.
2. Si quiere su nombre en minúsculas.
3. Si quiere su nombre con la primera letra mayúscula.
""")
opcion = int(input("Ingrese el número de la OPCION: "))

if opcion == 1:
  nombre_mayus = nombre.upper()
  print(nombre_mayus)

elif opcion == 2:
  nombre_min = nombre.lower()
  print(nombre_min)

elif opcion == 3:
  nombre_tit = nombre.title()
  print(nombre_tit)

else:
  print("Por favor, ingrese solamentete 1, 2 o 3")




################################
### Ejercicio 9

magnitud_terr = float(input("Ingrese la magnitud del terremoto - escala de Ritcher: "))

if magnitud_terr < 3:
  print("Muy leve")
elif 3 <= magnitud_terr < 4:
  print("Leve")
elif 4 <= magnitud_terr < 5:
  print("Moderado")
elif 5 <= magnitud_terr < 6:
  print("Fuerte")
elif 6 <= magnitud_terr < 7:
  print("Muy fuerte")
else:
  print("Extremo")

################################
### Ejercicio 10


hemisferio = input("Ingrese el hemisferio N/S: ")
hemisferio = hemisferio.upper()

mes = int(input("Por favor, ingrese el mes del año con números: "))

dia = int(input("Por favor, ingrese el día del mes: "))


if hemisferio == "S":
  if (mes == 12 and dia >= 21) or (mes in (1,2)) or (mes == 3 and dia <= 20):
    print("Verano")
  elif (mes == 3 and dia >= 21) or (mes in (4,5)) or (mes == 6 and dia <= 20):
    print("Otoño")
  elif (mes == 6 and dia >= 21) or (mes in (7,8)) or (mes == 9 and dia <= 20):
    print("Invierno")
  elif (mes == 9 and dia >= 21) or (mes in (10,11)) or (mes == 12 and dia <= 20):
    print("Primavera")
elif hemisferio == "N":
  if (mes == 12 and dia >= 21) or (mes in (1,2)) or (mes == 3 and dia <= 20):
    print("Invierno")
  elif (mes == 3 and dia >= 21) or (mes in (4,5)) or (mes == 6 and dia <= 20):
    print("Primavera")
  elif (mes == 6 and dia >= 21) or (mes in (7,8)) or (mes == 9 and dia <= 20):
    print("Verano")
  elif (mes == 9 and dia >= 21) or (mes in (10,11)) or (mes == 12 and dia <= 20):
    print("Otoño")