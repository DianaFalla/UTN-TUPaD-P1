# ---------------------------------------------------------
#  DIANA FALLA
#
#Ejercicio 1
print("EJERCICIO 1")

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

def main():
    try:
        num = int(input("Por favor, ingrese un número entero positivo: "))
        
        if num < 0:
            print("Error: El número debe ser un entero positivo.")
        else:
            for i in range(1, num + 1):
                print(f"El factorial de {i} es: {factorial(i)}")
    except ValueError:
        print("Error: Debes ingresar un número entero válido")

if __name__ == "__main__":
    main()

# ---------------------------------------------------------
#Ejercicio 2
print("EJERCICIO 2")

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def main():
    try:
        pos = int(input("Por favor, ingrese la posición de la serie de Fibonacci que deseas ver hasta: "))
        
        if pos < 0:
            print("Error: La posición debe ser un número entero no negativo.")
        else:
            print("La serie de Fibonacci hasta la posición", pos, "es:")
            for i in range(pos + 1):
                print(f"F({i}) = {fibonacci(i)}")
    except ValueError:
        print("Error: Debes introducir un número entero válido")

if __name__ == "__main__":
    main()

# ---------------------------------------------------------
#Ejercicio 3
print("EJERCICIO 3")

def potencia(base, exponente):
    if exponente == 0:
        return 1
    elif exponente < 0:
        return 1 / potencia(base, -exponente)
    else:
        return base * potencia(base, exponente - 1)

def main():
    try:
        base = float(input("Por favor, ingrese la base: "))
        exponente = int(input("Por favor, ingrese el exponente: "))
        
        resultado = potencia(base, exponente)
        print(f"{base} elevado a la potencia de {exponente} es: {resultado}")
    except ValueError:
        print("Error: Debes ingresar números válidos")

if __name__ == "__main__":
    main()

# ---------------------------------------------------------
#Ejercicio 4
print("EJERCICIO 4")

def decimal_a_binario(n):
    if n == 0:
        return '0'
    elif n == 1:
        return '1'
    else:
        return decimal_a_binario(n // 2) + str(n % 2)

def main():
    try:
        num = int(input("Por favor, ingrese un número entero positivo: "))
        
        if num < 0:
            print("Error: El número debe ser un entero positivo.")
        else:
            binario = decimal_a_binario(num)
            print(f"La representación binaria de {num} es: {binario}")
    except ValueError:
        print("Error: Debes ingresar un número entero válido")

if __name__ == "__main__":
    main()

# ---------------------------------------------------------
#Ejercicio 5
print("EJERCICIO 5")

def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    else:
        return palabra[0].lower() == palabra[-1].lower() and es_palindromo(palabra[1:-1])

def main():
    palabra = input("Por favor, ingrese una palabra: ")
    palabra = palabra.replace(" ", "").lower()  # elimina espacios y convierte a minúsculas
    
    if es_palindromo(palabra):
        print(f"La palabra '{palabra}' es un palíndromo.")
    else:
        print(f"La palabra '{palabra}' no es un palíndromo.")

if __name__ == "__main__":
    main()

# ---------------------------------------------------------
#Ejercicio 6
print("EJERCICIO 6")

def suma_digitos(n):
    if n < 10:
        return n
    else:
        return n % 10 + suma_digitos(n // 10)

def main():
    try:
        num = int(input("Por favor, ingrese un número entero positivo: "))
        
        if num < 0:
            print("Error: El número debe ser un entero positivo.")
        else:
            suma = suma_digitos(num)
            print(f"La suma de los dígitos de {num} es: {suma}")
    except ValueError:
        print("Error: Debes ingresar un número entero válido")

if __name__ == "__main__":
    main()

# ---------------------------------------------------------
#Ejercicio 7
print("EJERCICIO 7")

def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)

def main():
    try:
        n = int(input("Por favor, ingrese el número de bloques en el nivel más bajo: "))
        
        if n < 1:
            print("Error: El número de bloques debe ser un entero positivo.")
        else:
            total_bloques = contar_bloques(n)
            print(f"El total de bloques necesarios es: {total_bloques}")
    except ValueError:
        print("Error: Debes ingresar un número entero válido")

if __name__ == "__main__":
    main()


# ---------------------------------------------------------
#Ejercicio 8
print("EJERCICIO 8")


def contar_digito(numero, digito):
    if numero < 10:
        return 1 if numero == digito else 0
    else:
        return (1 if numero % 10 == digito else 0) + contar_digito(numero // 10, digito)

def main():
    numero = int(input("Por favor, ingrese un número entero positivo: "))
    digito = int(input("Por favor, ingrese un dígito (0-9): "))
    print(f"El dígito {digito} aparece {contar_digito(numero, digito)} veces en el número {numero}.")

if __name__ == "__main__":
    main()