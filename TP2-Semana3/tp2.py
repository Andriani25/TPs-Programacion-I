from statistics import mode, median, mean
import random

# Actividad 1:  Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años
# el programa debe imprimir "Eres mayor de edad"

edad = int(input("Escribe tu edad: "))
if edad > 18:
    print("Eres mayor de edad")

# Actividad 2: Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, el programa debe imprimir "Aprobado",
# en caso contrario debe imprimir "Desaprobado".

nota = int(input("Escribe tu nota: "))

if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

# Actividad 3: Escribir un programa que permita ingresar solo números pares. Si el numero es par, imprimir "El numero es par", en caso contrario,
# imprimir "Por favor ingrese un numero par".

numero = int(input("Escribe un numero: "))
if numero % 2 == 0:
    print("El numero es par")
else:
    print("Por favor ingrese un numero par")

# Actividad 4: Escribir un programa que solicite al usuario su edad e imprima por pantalla a cual categoria pertenece:
# Niño (0-12), Adolescente (13-17), Adulto Joven (18 - 30), Adulto (30+)

edad = int(input("Escribe tu edad: "))

if 0 <= edad <= 12:
    print("Niño")
elif 13 <= edad <= 17:
    print("Adolescente")
elif 18 <= edad <= 30:
    print("Adulto Joven")
elif edad > 30:
    print("Adulto")
else:
    print("Edad no valida")

# Actividad 5: Escribir un programa que solicite al usuario que ingrese una contraseña de entre 8 a 14 caracteres.
# Si la contraseña es correcta, imprimir "Contraseña correcta", en caso contrario, imprimir "Contraseña incorrecta".

contrasena = input("Escribe una contraseña (8-14 caracteres): ")

if 8 <= len(contrasena) <= 14:
    print("Contraseña correcta")
else:
    print("Contraseña incorrecta")

# Actividad 6: Utilizando el paquete statistics, escribir un programa que calcule la media, mediana y moda de una lista de números.

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

num_media = mean(numeros_aleatorios)
num_mediana = median(numeros_aleatorios)
num_moda = mode(numeros_aleatorios)

print(f"Lista de numeros: {numeros_aleatorios}")
print(f"Media: {num_media}")
print(f"Mediana: {num_mediana}")
print(f"Moda: {num_moda}")

if (num_media > num_mediana and num_mediana > num_moda):
    print("La lista tiene sesgo positvo")
elif (num_media < num_mediana and num_mediana < num_moda):
    print("La lista tiene sesgo negativo")
elif (num_media == num_mediana and num_mediana == num_moda):
    print("La lista es simetrica")

# Actividad 7: Escribir un programa que solicite al usuario un string. Si este string finaliza en una vocal, añadirle un signo de exclamacion
# al final y mostrarlo por pantalla. Si no finaliza en vocal, mostrarlo como ingresó por pantalla.

string = input("Escribe un string: ")
vocales = "aeiouAEIOU"
if string[-1] in vocales:
    string += "!"

print(string)

# Actividad 8: Escribir un programa que solicite al usuario que escriba su nombre y elija una opcion de un menu:
# 1. Si quiere su nombre en mayusculas
# 2. Si quiere su nombre en minusculas
# 3. Si quiere su nombre con la primer letra en mayuscula

nombre = input("Escribe tu nombre: ")
print("Elija una opcion del menu:")
print("1. Nombre en mayusculas")
print("2. Nombre en minusculas")
print("3. Nombre con la primer letra en mayuscula")

opcion = int(input("Escribe el numero de la opcion: "))

if opcion == 1:
    print(nombre.upper())
elif opcion == 2:
    print(nombre.lower())
elif opcion == 3:
    print(nombre.capitalize())

# Actividad 9: Escribir un programa que solicite al usuario la magnitud de un terremoto, clasifique la magnitud segun
# la escala de Richter e imprima por pantalla la clasificacion correspondiente:

magnitud = float(input("Escribe la magnitud del terremoto: "))

if 0 <= magnitud < 3:
    print("Muy leve")
elif 3 <= magnitud < 4:
    print("Leve")
elif 4 <= magnitud < 5:
    print("Moderado")
elif 5 <= magnitud < 6:
    print("Fuerte")
elif 6 <= magnitud < 7:
    print("Muy fuerte")
elif 7 <= magnitud < 8:
    print("Extremo")

# Actividad 10: Escribir un programa que solicite al usuario en que hemisferio se encuentra (Norte o Sur), ademas del mes del año (1-12) y dia.
# El programa debe imprimir la estacion del año en la que se encuentra el usuario.

hemisferio = input("Escribe en que hemisferio te encuentras (Norte/Sur): ")
mes = int(input("Escribe el mes del año (1-12): "))
dia = int(input("Escribe el dia del mes: ")) 

if hemisferio.lower() == "norte":
    if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
        print("Invierno")
    elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia < 21):
        print("Primavera")
    elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia < 21):
        print("Verano")
    elif (mes == 9 and dia >= 22) or (mes in [10, 11]) or (mes == 12 and dia < 21):
        print("Otoño")
    else:
        print("Fecha no valida")
elif hemisferio.lower() == "sur":
    if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
        print("Verano")
    elif (mes == 3 and dia > 20) or (mes in [4, 5]) or (mes == 6 and dia < 21):
        print("Otoño")
    elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia < 21):
        print("Invierno")
    elif (mes == 9 and dia >= 21) or (mes in [10, 11]) or (mes == 12 and dia < 21):
        print("Primavera")
    else:
        print("Fecha no valida")