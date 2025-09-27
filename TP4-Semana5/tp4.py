import random

# ACTIVIDAD 1

notas = [7, 9, 4, 10, 6, 8, 5, 3, 9, 2]

print("Notas de los estudiantes:")
for nota in notas:
    print(nota, end=" ")
print()

suma = 0
for nota in notas:
    suma += nota
promedio = suma / len(notas)
print("Promedio:", promedio)

mayor = notas[0]
menor = notas[0]
for nota in notas:
    if nota > mayor:
        mayor = nota
    if nota < menor:
        menor = nota
print("Nota más alta:", mayor)
print("Nota más baja:", menor)

# ACTIVIDAD 2

productos = []
i = 0
while i < 5:
    prod = input("Ingrese un producto: ")
    productos.append(prod)
    i += 1

print("Lista de productos:")
for prod in productos:
    print(prod)

productos_ordenados = sorted(productos)
print("Lista ordenada:")
for prod in productos_ordenados:
    print(prod)

eliminar = input("¿Qué producto desea eliminar?: ")

if eliminar in productos:
 productos.remove(eliminar)
 print("Lista actualizada:")
 for prod in productos:
    print(prod)
else:
 print("El producto no está en la lista.")

# ACTIVIDAD 3

numeros = []
for i in range(15):
    numeros.append(random.randint(1, 100))

pares = []
impares = []

for num in numeros:
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

print("Lista original:")
for num in numeros:
    print(num, end=" ")
print("\nCantidad de pares:", len(pares))
print("Cantidad de impares:", len(impares))

# ACTIVIDAD 4

lista_con_repetidos = [1, 3, 2, 4, 3, 5, 2, 1, 6, 4, 7]
sin_repetidos = []

for elem in lista_con_repetidos:
    repetido = False
    for nuevo in sin_repetidos:
        if elem == nuevo:
            repetido = True
    if not repetido:
        sin_repetidos.append(elem)

print("Lista sin repetidos:")
for elem in sin_repetidos:
    print(elem, end=" ")

# ACTIVIDAD 5

estudiantes = ["Ana", "Luis", "Marta", "Juan", "Sofía", "Pedro", "Carla", "Nico"]

print("Lista de estudiantes:")
for est in estudiantes:
    print(est)

opcion = input("¿Desea agregar o eliminar un estudiante? (agregar/eliminar): ")

if opcion == "agregar":
    nuevo = input("Ingrese el nombre del nuevo estudiante: ")
    estudiantes.append(nuevo)
elif opcion == "eliminar":
    borrar = input("Ingrese el nombre del estudiante a eliminar: ")
    if borrar in estudiantes:
        estudiantes.remove(borrar)
    else:
        print("El estudiante no está en la lista.")

print("Lista final de estudiantes:")
for est in estudiantes:
    print(est)

# ACTIVIDAD 6

numeros = [10, 20, 30, 40, 50, 60, 70]
rotada = [0] * len(numeros)

for i in range(len(numeros)):
    if i == len(numeros) - 1:
        rotada[0] = numeros[i]
    else:
        rotada[i + 1] = numeros[i]

print("Lista original:")
for num in numeros:
    print(num, end=" ")
print("\nLista rotada:")
for num in rotada:
    print(num, end=" ")

# ACTIVIDAD 7

temperaturas = [
    [10, 20], [12, 22], [8, 18],
    [15, 25], [11, 19], [9, 21], [13, 23]
]

suma_min = 0
suma_max = 0
for i in range(7):
    suma_min += temperaturas[i][0]
    suma_max += temperaturas[i][1]

prom_min = suma_min / 7
prom_max = suma_max / 7

print("Promedio mínimas:", prom_min)
print("Promedio máximas:", prom_max)

mayor_amplitud = 0
dia_mayor = 0
for i in range(7):
    amplitud = temperaturas[i][1] - temperaturas[i][0]
    if amplitud > mayor_amplitud:
        mayor_amplitud = amplitud
        dia_mayor = i + 1
print("Día con mayor amplitud térmica:", dia_mayor)

# ACTIVIDAD 8

notas = [
    [7, 8, 6],
    [5, 6, 7],
    [9, 8, 10],
    [4, 5, 6],
    [8, 7, 9]
]

print("Promedio de cada estudiante:")
for i in range(5):
    suma = 0
    for j in range(3):
        suma += notas[i][j]
    prom = suma / 3
    print("Estudiante", i + 1, ":", prom)

print("Promedio de cada materia:")
for j in range(3):
    suma = 0
    for i in range(5):
        suma += notas[i][j]
    prom = suma / 5
    print("Materia", j + 1, ":", prom)

# ACTIVIDAD 9

tablero = [["-" , "-" , "-"],
           ["-" , "-" , "-"],
           ["-" , "-" , "-"]]

def mostrar_tablero():
    for i in range(3):
        for j in range(3):
            print(tablero[i][j], end=" ")

turno = "X"
jugadas = 0
while jugadas < 9:
    print("Turno de:", turno)
    fila = int(input("Fila (0-2): "))
    col = int(input("Columna (0-2): "))

    if tablero[fila][col] == "-":
        tablero[fila][col] = turno
        mostrar_tablero()
        jugadas += 1
        
        if turno == "X":
            turno = "O"
        else:
            turno = "X"
    else:
        print("Casilla ocupada, intenta de nuevo.")


# ACTIVIDAD 10

ventas = [
    [10, 15, 20, 25, 18, 22, 30],
    [5, 8, 6, 7, 9, 10, 12],
    [20, 18, 22, 25, 30, 28, 35],
    [12, 14, 16, 18, 15, 13, 17]
]

print("Total por producto:")
for i in range(4):
    total = 0
    for j in range(7):
        total += ventas[i][j]
    print("Producto", i + 1, ":", total)

mayor_ventas = 0
dia_max = 0
for j in range(7):
    suma = 0
    for i in range(4):
        suma += ventas[i][j]
    if suma > mayor_ventas:
        mayor_ventas = suma
        dia_max = j + 1
print("Día con mayores ventas:", dia_max)

max_producto = 0
prod_max = 0
for i in range(4):
    suma = 0
    for j in range(7):
        suma += ventas[i][j]
    if suma > max_producto:
        max_producto = suma
        prod_max = i + 1
print("Producto más vendido:", prod_max)

