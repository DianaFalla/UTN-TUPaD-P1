#
# DIANA FALLA
# 
# Actividad 1

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

nuevas_frutas = [('Naranja', 1200), ('Manzana', 1500), ('Pera', 2300)]

for fruta, precio in nuevas_frutas:
    precios_frutas[fruta] = precio

print(precios_frutas)

#Actividad 2

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450, 'Naranja': 1200, 'Manzana': 1500, 'Pera': 2300}

actualizaciones = [('Banana', 1330), ('Manzana', 1700), ('Melón', 2800)]

for fruta, precio in actualizaciones:
    precios_frutas[fruta] = precio

print(precios_frutas)

#--------------------------------
#Actividad 3

precios_frutas = {'Banana': 1330, 'Ananá': 2500, 'Melón': 2800, 'Uva': 1450, 'Naranja': 1200, 'Manzana': 1700, 'Pera': 2300}

frutas = sorted(precios_frutas.keys())

print(frutas)

#--------------------------------
#Actividad 4

# Diccionario para almacenar los contactos
contactos = {}

for i in range(5):
    nombre = input(f"Ingrese el nombre del contacto {i+1}: ")
    numero = input(f"Ingrese el número de teléfono de {nombre}: ")
    contactos[nombre] = numero

# Mostrar los contactos cargados
print("\nContactos cargados:")
for nombre, numero in contactos.items():
    print(f"{nombre}: {numero}")

# Consultar un número
while True:
    nombre = input("\nIngrese el nombre del contacto que desea consultar (o 'salir' para terminar): ")
    if nombre.lower() == 'salir':
        break
    if nombre in contactos:
        print(f"El número de teléfono de {nombre} es: {contactos[nombre]}")
    else:
        print(f"No se encontró un contacto con el nombre {nombre}")


#--------------------------------
#Actividad 5

frase = input("Ingrese una frase: ")

palabras = frase.lower().split()

palabras_unicas = set(palabras)

frecuencia_palabras = {}
for palabra in palabras:
    if palabra in frecuencia_palabras:
        frecuencia_palabras[palabra] += 1
    else:
        frecuencia_palabras[palabra] = 1

print("Palabras únicas:")
print(", ".join(palabras_unicas))
print("\nRecuento:")
for palabra, cantidad in frecuencia_palabras.items():
    print(f"{palabra}: {cantidad}")


#--------------------------------
#Actividad 6

# Diccionario para almacenar los nombres y notas de los alumnos
alumnos = {}

# Ingresar los nombres y notas de los alumnos
for i in range(3):
    nombre = input(f"Ingrese el nombre del alumno {i+1}: ")
    notas = []
    for j in range(3):
        nota = float(input(f"Ingrese la nota {j+1} de {nombre}: "))
        notas.append(nota)
    alumnos[nombre] = tuple(notas)

# Calcular y mostrar el promedio de cada alumno
for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"El promedio de {nombre} es: {promedio:.2f}")

#--------------------------------
#Actividad 7

# Sets de estudiantes que aprobaron Parcial 1 y Parcial 2
parcial1 = {1, 2, 3, 4, 5, 6}
parcial2 = {4, 5, 6, 7, 8, 9}

# Estudiantes que aprobaron ambos parciales
aprobados_ambos = parcial1 & parcial2
print("Estudiantes que aprobaron ambos parciales:", aprobados_ambos)

# Estudiantes que aprobaron solo uno de los dos parciales
aprobados_solo_uno = parcial1 ^ parcial2
print("Estudiantes que aprobaron solo uno de los dos parciales:", aprobados_solo_uno)

# Estudiantes que aprobaron al menos un parcial
aprobados_total = parcial1 | parcial2
print("Estudiantes que aprobaron al menos un parcial:", aprobados_total)

#--------------------------------
#Actividad 8

# Diccionario para almacenar el stock de productos
stock_productos = {
    "Manzanas": 10,
    "Peras": 20,
    "Plátanos": 30
}

while True:
    print("\nOpciones:")
    print("1. Consultar stock de un producto")
    print("2. Agregar unidades al stock de un producto")
    print("3. Agregar un nuevo producto")
    print("4. Salir")

    opcion = input("Ingrese la opción deseada: ")

    if opcion == "1":
        producto = input("Ingrese el nombre del producto: ")
        if producto in stock_productos:
            print(f"El stock de {producto} es: {stock_productos[producto]}")
        else:
            print(f"No se encontró el producto {producto}")

    elif opcion == "2":
        producto = input("Ingrese el nombre del producto: ")
        if producto in stock_productos:
            unidades = int(input("Ingrese la cantidad de unidades a agregar: "))
            stock_productos[producto] += unidades
            print(f"Se agregaron {unidades} unidades al stock de {producto}. Nuevo stock: {stock_productos[producto]}")
        else:
            print(f"No se encontró el producto {producto}. Puede agregarlo como un nuevo producto en la opción 3.")

    elif opcion == "3":
        producto = input("Ingrese el nombre del nuevo producto: ")
        if producto not in stock_productos:
            unidades = int(input("Ingrese la cantidad de unidades iniciales: "))
            stock_productos[producto] = unidades
            print(f"Se agregó el producto {producto} con un stock inicial de {unidades}.")
        else:
            print(f"El producto {producto} ya existe. Puede agregar unidades al stock en la opción 2.")

    elif opcion == "4":
        print("Saliendo del programa...")
        break

    else:
        print("Opción inválida. Por favor, ingrese una opción válida.")

    print("\nStock actual:")
    for producto, stock in stock_productos.items():
        print(f"{producto}: {stock}")


#--------------------------------
#Actividad 9

# Agenda de eventos
agenda = {
    ("Lunes", "10:00"): "Reunión",
    ("Martes", "15:00"): "Clase de Inglés",
    ("Miércoles", "12:00"): "Almuerzo con amigos",
    ("Jueves", "18:00"): "Entrenamiento deportivo",
    ("Viernes", "10:00"): "Reunión de equipo"
}

def consultar_evento(dia, hora):
    if (dia, hora) in agenda:
        print(f"El {dia} a las {hora} tienes: {agenda[(dia, hora)]}")
    else:
        print(f"No hay eventos programados para el {dia} a las {hora}")

def agregar_evento(dia, hora, evento):
    if (dia, hora) in agenda:
        print(f"Ya hay un evento programado para el {dia} a las {hora}: {agenda[(dia, hora)]}")
        respuesta = input("¿Desea reemplazar el evento? (s/n): ")
        if respuesta.lower() == "s":
            agenda[(dia, hora)] = evento
            print(f"Evento actualizado: {dia} a las {hora} - {evento}")
        else:
            print("No se ha actualizado el evento.")
    else:
        agenda[(dia, hora)] = evento
        print(f"Evento agregado: {dia} a las {hora} - {evento}")

def mostrar_agenda():
    print("Agenda de eventos:")
    for (dia, hora), evento in agenda.items():
        print(f"{dia} a las {hora}: {evento}")

while True:
    print("\nOpciones:")
    print("1. Consultar evento")
    print("2. Agregar evento")
    print("3. Mostrar agenda")
    print("4. Salir")

    opcion = input("Ingrese la opción deseada: ")

    if opcion == "1":
        dia = input("Ingrese el día: ")
        hora = input("Ingrese la hora (formato 12:00): ")
        consultar_evento(dia, hora)

    elif opcion == "2":
        dia = input("Ingrese el día: ")
        hora = input("Ingrese la hora (formato 12:00): ")
        evento = input("Ingrese el evento: ")
        agregar_evento(dia, hora, evento)

    elif opcion == "3":
        mostrar_agenda()

    elif opcion == "4":
        print("Saliendo del programa...")
        break

    else:
        print("Opción inválida. Por favor, ingrese una opción válida.")


#--------------------------------
#Actividad 10

# Diccionario original
paises_capitales = {
    "Argentina": "Buenos Aires",
    "Chile": "Santiago",
    "Uruguay": "Montevideo",
    "Brasil": "Brasilia",
    "Perú": "Lima"
}

# Crear un nuevo diccionario con las claves invertidas
capitales_paises = {valor: clave for clave, valor in paises_capitales.items()}

# Imprimir los diccionarios
print("Original:")
for pais, capital in paises_capitales.items():
    print(f"{pais}: {capital}")

print("\nInvertido:")
for capital, pais in capitales_paises.items():
    print(f"{capital}: {pais}")
