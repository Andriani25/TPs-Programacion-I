# Actividad 1

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

print(precios_frutas)

# Actividad 2

precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

print(precios_frutas)

# Actividad 3

frutas = list(precios_frutas.keys())
print(frutas)

# Actividad 4

telefonos = {}

for i in range(5):
    nombre = input("Ingrese el nombre del contacto: ")
    numero = input("Ingrese el número de teléfono: ")
    telefonos[nombre] = numero

buscar = input("Ingrese el nombre a buscar: ")
if buscar in telefonos:
    print(f"El número de {buscar} es {telefonos[buscar]}")
else:
    print("Ese contacto no existe.")

# Actividad 5

frase = input("Ingrese una frase: ").lower()
palabras = frase.split()

unicas = set(palabras)
print("Palabras únicas:", unicas)

conteo = {}
for palabra in palabras:
    conteo[palabra] = conteo.get(palabra, 0) + 1

print("Conteo de palabras:", conteo)

# Actividad 6

alumnos = {}

for i in range(3):
    nombre = input("Ingrese el nombre del alumno: ")
    notas = []
    for j in range(3):
        nota = float(input(f"Ingrese la nota {j+1} de {nombre}: "))
        notas.append(nota)
    alumnos[nombre] = tuple(notas)

for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"El promedio de {nombre} es {promedio:.2f}")

# Actividad 7

parcial1 = {1, 2, 3, 4, 5}
parcial2 = {4, 5, 6, 7, 8}

# Ambos parciales
ambos = parcial1 & parcial2
print("Aprobaron ambos:", ambos)

# Solo uno
solo_uno = parcial1 ^ parcial2
print("Aprobaron solo uno:", solo_uno)

# Al menos uno
al_menos_uno = parcial1 | parcial2
print("Aprobaron al menos uno:", al_menos_uno)


# Actividad 8

stock = {'Pan': 10, 'Leche': 20, 'Huevos': 12}

producto = input("Ingrese un producto: ")

if producto in stock:
    print(f"Stock actual de {producto}: {stock[producto]}")
    agregar = int(input("¿Cuántas unidades desea agregar? "))
    stock[producto] += agregar
else:
    nuevo_stock = int(input("Producto nuevo. Ingrese cantidad inicial: "))
    stock[producto] = nuevo_stock

print("Stock actualizado:", stock)

# Actividad 9

agenda = {
    ('Lunes', '10:00'): 'Reunión de equipo',
    ('Martes', '14:00'): 'Clase de Python',
    ('Viernes', '18:00'): 'Cena con amigos'
}

dia = input("Ingrese el día: ")
hora = input("Ingrese la hora (HH:MM): ")

evento = agenda.get((dia, hora))
if evento:
    print(f"Actividad: {evento}")
else:
    print("No hay actividad programada en ese horario.")

# Actividad 10

paises = {
    'Argentina': 'Buenos Aires',
    'Francia': 'París',
    'Italia': 'Roma',
    'Japón': 'Tokio'
}

capitales = {capital: pais for pais, capital in paises.items()}
print(capitales)
