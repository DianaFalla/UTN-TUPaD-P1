# EJERCICIO 1
# Crear una función llamada imprimir_hola_mundo que imprima por pantalla el mensaje: “Hola Mundo!”. 
# Llamar a esta función desde el
# programa principal.
print("EJERCICIO 1")

def imprimir_hola_mundo():
    print("Hola Mundo!")

imprimir_hola_mundo()

# EJERCICIO 2
# Crear una función llamada saludar_usuario(nombre) que reciba
# como parámetro un nombre y devuelva un saludo personalizado
print("EJERCICIO 2")

def saludar_usuario(nombre):
    return f"Hola {nombre}!"

def main():
    nombre = input("Por favor, ingrese su nombre: ")
    saludo = saludar_usuario(nombre)
    print(saludo)

main()

# ---------------------------------------------------------
#Ejercicio 3
print("EJERCICIO 3")

def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

def main():
    nombre = input("Por favor, ingresa tu nombre: ")
    apellido = input("Por favor, ingresa tu apellido: ")
    edad = int(input("Por favor, ingresa tu edad: "))
    residencia = input("Por favor, ingresa tu residencia: ")
    
    informacion_personal(nombre, apellido, edad, residencia)

main()

# ---------------------------------------------------------
# Ejercicio 4
print("EJERCICIO 4")

import math

def calcular_area_circulo(radio):
    return math.pi * (radio ** 2)

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

def main():
    radio = float(input("Por favor, introduce el radio del círculo: "))
    
    area = calcular_area_circulo(radio)
    perimetro = calcular_perimetro_circulo(radio)
    
    print(f"El área del círculo es: {area:.2f}")
    print(f"El perímetro del círculo es: {perimetro:.2f}")

main()

# ---------------------------------------------------------
# Ejercicio 5
print("EJERCICIO 5")

def segundos_a_horas(segundos):
    return segundos / 3600

def main():
    segundos = float(input("Por favor, ingrese la cantidad de segundos: "))
    
    horas = segundos_a_horas(segundos)
    
    print(f"{segundos} segundos son equivalentes a {horas:.2f} horas")

main()

# ---------------------------------------------------------
# Ejercicio 6
print("EJERCICIO 6")

def tabla_multiplicar(numero):
    print(f"Tabla de multiplicar del {numero}:")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

def main():
    numero = int(input("Por favor, introduce un número: "))
    
    tabla_multiplicar(numero)

main()

# ---------------------------------------------------------
# Ejercicio 7
print("EJERCICIO 7")

def operaciones_basicas(a, b):
    try:
        suma = a + b
        resta = a - b
        multiplicacion = a * b
        division = a / b
        return suma, resta, multiplicacion, division
    except ZeroDivisionError:
        print("Error: No se puede dividir por cero")
        return None

def main():
    try:
        a = float(input("Por favor, ingrese el primer número: "))
        b = float(input("Por favor, ingrese el segundo número: "))
        
        resultado = operaciones_basicas(a, b)
        
        if resultado is not None:
            suma, resta, multiplicacion, division = resultado
            print(f"Resultados de las operaciones con {a} y {b}:")
            print(f"Suma: {a} + {b} = {suma}")
            print(f"Resta: {a} - {b} = {resta}")
            print(f"Multiplicación: {a} * {b} = {multiplicacion}")
            print(f"División: {a} / {b} = {division}")
    except ValueError:
        print("Error: Debes introducir números válidos")

main()


# ---------------------------------------------------------
# Ejercicio 8
print("EJERCICIO 8")

def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

def main():
    try:
        peso = float(input("Por favor, ingrese tu peso en kilogramos: "))
        altura = float(input("Por favor, ingrese tu altura en metros: "))
        
        imc = calcular_imc(peso, altura)
        
        print(f"Tu IMC es: {imc:.2f}")
        
        if imc < 18.5:
            print("Tu estado de peso es: Bajo peso")
        elif imc < 25:
            print("Tu estado de peso es: Peso normal")
        elif imc < 30:
            print("Tu estado de peso es: Sobrepeso")
        else:
            print("Tu estado de peso es: Obesidad")
    except ValueError:
        print("Error: Debes introducir números válidos")

main()

# ---------------------------------------------------------
# Ejercicio 9
print("EJERCICIO 9")

def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def main():
    try:
        celsius = float(input("Por favor, ingrese la temperatura en grados Celsius: "))
        
        fahrenheit = celsius_a_fahrenheit(celsius)
        
        print(f"{celsius}°C es equivalente a {fahrenheit:.2f}°F")
    except ValueError:
        print("Error: Debes introducir un número válido")

main()

# ---------------------------------------------------------
# Ejercicio 10
print("EJERCICIO 10")

def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    return promedio

def main():
    try:
        a = float(input("Por favor, ingrese el primer número: "))
        b = float(input("Por favor, ingrese el segundo número: "))
        c = float(input("Por favor, ingrese el tercer número: "))
        
        promedio = calcular_promedio(a, b, c)
        
        print(f"El promedio de {a}, {b} y {c} es: {promedio:.2f}")
    except ValueError:
        print("Error: Debes introducir números válidos")

main()
