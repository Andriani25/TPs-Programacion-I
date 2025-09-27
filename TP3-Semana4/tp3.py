import random

# Actividad 1: Crea un programa que imprima en pantalla todos los numeros enteros desde 0 a 100
# Pondremos un condicional para saber si queremos o no, que se ejecute el print de los 100 numeros, para comodidad mia.

actividad_1 = input("¿Quieres imprimir los numeros del 0 al 100? (s/n): ")

if(actividad_1.lower() == 's'):
 for i in range(101):
    print(i)
else:
    print("Actividad 1 salteada.")

# Actividad 2: Desarrolla un programa que solicite al usuario un numero entero y determine la cantidad de digitos que contiene.

num_a2 = input("Ingrese un numero entero: ")

if num_a2.isnumeric():
   print(f"El numero {num_a2} tiene {len(num_a2)} digitos.")
else:
    print("El valor ingresado no es un numero entero.")

# Actividad 3: Escriba un programa que sume todos los numeros enteros que se encuentren entre dos numeros ingresados por el usuario.

num1_a3 = input("Ingrese el primer numero entero: ")
while(not num1_a3.isnumeric()):
   num1_a3 = input("El valor ingresado no es un numero entero, ingresa otro valor: ")

num2_a3 = input("Ingrese el segundo numero entero: ")
while(not num2_a3.isnumeric()):
   num2_a3 = input("El valor ingresado no es un numero entero, ingresa otro valor: ")

if(num1_a3.isnumeric() and num2_a3.isnumeric()):
    suma = 0
    for i in range(int(num1_a3) + 1, int(num2_a3)):
        suma += i
    print(f"La suma de los numeros enteros entre {num1_a3} y {num2_a3} es: {suma}.")

# Actividad 4: Elabora un programa que permita al usuario ingresar numeros enteros y los sume en secuencia hasta que ingrese un 0.

suma = 0
num_a4 = input("Ingrese un numero entero (0 para finalizar): ")

while num_a4 != "0":
    if(num_a4.isnumeric()):
     suma += int(num_a4)
     print(f"Suma actual: {suma}")
    else:
        print("El valor ingresado no es un numero entero.")
    num_a4 = input("Ingrese un numero entero (0 para finalizar): ")

# Actividad 5: Crea un juego en el que el usuario deba adivinar un numero secreto entre 1 y 9. Ademas debe
# contar la cantidad de intentos realizados hasta que el usuario adivine correctamente.

random_num = random.randint(1, 9)
intentos = 0
adivinado = False

while not adivinado:
    print(random_num)
    num = input("Adivina el numero entre 1 y 9: ")
    if(num.isnumeric()):
     while int(num) != random_num:
      intentos += 1
      num = input("Incorrecto, intenta de nuevo: ")

     if(num.isnumeric() and int(num) == random_num):
        intentos += 1
        adivinado = True
        print(f"Felicidades, adivinaste el numero {random_num} en {intentos} intentos.")
    else: 
     num = input("El valor ingresado no es un numero entero, ingresa otro valor: ")

# Actividad 6: Desarrolla un programa que imprima en pantalla de manera decresciente los numeros pares desde 100 hasta 0.
# Utilizare el mismo condicional que en la actividad 1 para no llenar la pantalla de numeros.

actividad_1 = input("¿Quieres imprimir los numeros del 0 al 100? (s/n): ")

if(actividad_1.lower() == 's'):
 for i in range(100, -1, -2):
    print(i)
else:
    print("Actividad 6 salteada.")

# Actividad 7: Crea un programa que le solicite al usuario ingresar un numero positivo y calcule la suma de todos los numeros enteros
# entre 1 y ese numero.

num_a7 = input("Ingrese un numero entero positivo: ")
suma = 0

while(not num_a7.isnumeric() or int(num_a7) <= 0):
   num_a7 = input("El valor ingresado no es un numero entero positivo, ingresa otro valor: ")

if(num_a7.isnumeric() and int(num_a7) > 0):
    for i in range(1, int(num_a7) + 1):
        suma += i
    print(f"La suma de los numeros enteros entre 1 y {num_a7} es: {suma}.")

# Actividad 8: Escribe un programa que permita al usuario ingresar 100 numeros enteros, y indicar cuantos de ellos son pares, cuantos impares,
# cuantos positivos y cuantos negativos.

contador_num = 10
pares = 0
impares = 0
positivos = 0
negativos = 0

num_a8 = input(f"Ingrese numeros enteros hasta finalizar, quedan {contador_num}: ")

while contador_num > 0:
   while(not num_a8.isnumeric()):
      num_a8 = input("El valor ingresado no es un numero entero, ingresa otro valor: ")

   if(int(num_a8) % 2 == 0):
        pares += 1

   if(int(num_a8) % 2 != 0):
        impares += 1

   if(int(num_a8) > 0):
        positivos += 1

   if(int(num_a8) < 0):
      negativos += 1
 
   num_a8 = input(f"Ingrese numeros enteros hasta finalizar, quedan {contador_num}: ")
   contador_num -= 1
   
if(contador_num < 1):
 print(f"Numeros pares: {pares}, numeros impares: {impares}, numeros positivos: {positivos}, numeros negativos: {negativos}.")

# Actividad 9: Crea un programa que solicite al usuario ingresar 100 numeros enteros y que calcule la media de esos valors.

contador_num = 0
suma = 0
promedio: 0

num_a9 = input(f"Ingrese numeros enteros hasta finalizar, quedan {10 - contador_num}: ")

while contador_num < 10:
 while(not num_a9.isnumeric()):
    num_a9 = input("El valor ingresado no es un numero entero, ingresa otro valor: ")
 
 suma += int(num_a9)
 contador_num += 1
 num_a9 = input(f"Ingrese numeros enteros hasta finalizar, quedan {10 - contador_num}: ")
 
 if(contador_num == 10):
    promedio = suma / 10
    print(f"El promedio de los numeros ingresados es: {promedio}.")

# Actividad 10: Escriba un programa que invierta el numero ingresado por el usuario

num_a10 = input("Ingrese un numero entero para invertirlo: ")

while(not num_a10.isnumeric()):
    num_a10 = input("El valor ingresado no es un numero entero, ingresa otro valor: ")

if(num_a10.isnumeric()):
   num_invertido = num_a10[::-1]
   print(f"El numero {num_a10} invertido es: {num_invertido}.")