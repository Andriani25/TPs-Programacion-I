# Ejercicio 1

def imprimir_hola_mundo():
    print("Hola Mundo!")

imprimir_hola_mundo()

# Ejercicio 2

def saludar_usuario(nombre):
    return f"Hola {nombre}!"

nombre = input("Ingrese su nombre: ")
print(saludar_usuario(nombre))

# Ejercicio 3

def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

print("Ingrese su información personal:")

nombre = input("Nombre: ")
apellido = input("Apellido: ")
edad = input("Edad: ")
residencia = input("Lugar de residencia: ")

informacion_personal(nombre, apellido, edad, residencia)

# Ejercicio 4

def calcular_area_circulo(radio):
    return 3.1416 * (radio ** 2)

def calcular_perimetro_circulo(radio):
    return 2 * 3.1416 * radio

radio = float(input("Ingrese el radio del círculo: "))
print("Área:", calcular_area_circulo(radio))
print("Perímetro:", calcular_perimetro_circulo(radio))

# Ejercicio 5

def segundos_a_horas(segundos):
    return segundos / 3600

segundos = int(input("Ingrese la cantidad de segundos: "))
print("Equivalen a", segundos_a_horas(segundos), "horas")

# Ejercicio 6

def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

numero = int(input("Ingrese un número: "))
tabla_multiplicar(numero)

# Ejercicio 7

def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else "Indefinida (división por cero)"
    return (suma, resta, multiplicacion, division)

a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))

resultados = operaciones_basicas(a, b)

print("Resultados de las operaciones básicas:")
print(f"Suma: {resultados[0]}")
print(f"Resta: {resultados[1]}")
print(f"Multiplicación: {resultados[2]}")
print(f"División: {resultados[3]}")

# Ejercicio 8

def calcular_imc(peso, altura):
    return peso / (altura ** 2)

peso = float(input("Ingrese su peso (kg): "))
altura = float(input("Ingrese su altura (m): "))

print("Su IMC es:", round(calcular_imc(peso, altura), 2))

# Ejercicio 9

def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

celsius = float(input("Ingrese la temperatura en °C: "))
print("Equivale a", celsius_a_fahrenheit(celsius), "°F")

# Ejercicio 10

def calcular_promedio(a, b, c):
    return (a + b + c) / 3

a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))
c = float(input("Ingrese el tercer número: "))

print("El promedio es:", calcular_promedio(a, b, c))
