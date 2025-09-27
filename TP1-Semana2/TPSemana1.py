# Ejercicio 1

print("Hola mundo!")

# Ejercicio 2

nombre = input("Escribe tu nombre: ")
print(f"Hola, {nombre}!")

# Ejercicio 3

nombre = input("Escribe tu nombre: ")
apellido = input("Escribe tu apellido: ")
edad = input("Escribe tu edad: ")
residencia = input("Escribe tu ciudad de residencia: ")
print(f"Hola, soy {nombre} {apellido}!. Tengo {edad} años y vivo en {residencia}.")

# Ejercicio 4

numero = int(input("Escribe el radio de un circulo: "))
perimetro = 2 * 3.14 * numero
area = 3.14 * numero ** 2
print(f"El perimetro del circulo es {perimetro} y el area es {area}.")

# Ejercicio 5

segundos = int(input("Escribe una cantidad de segundos: "))
horas = segundos // 3600
print(f"{segundos} segundos son {horas} horas.")

# Ejercicio 6

numero = int(input("Escribe un numero: "))
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")

# Ejercicio 7

numero = int(input("Escribe un numero distinto de 0: "))
numero1 = int(input("Escribe otro numero distinto de 0: "))
print(f"La suma de {numero} y {numero1} es {numero + numero1}. La resta es {numero - numero1}. La multiplicacion es {numero * numero1}. La division es {numero / numero1}.")

# Ejercicio 8

altura = int(input("Escriba su altura: "))
peso = int(input("Escriba su peso: "))
imc = peso / (altura / 100) ** 2
print(f"Su IMC es {imc:.2f}.")

# Ejercicio 9

temperatura = int(input("Escriba una temperatura en grados Celsius: "))
temperatura_fahrenheit = (temperatura * 9/5) + 32
print(f"{temperatura} grados Celsius son {temperatura_fahrenheit:.2f} grados Fahrenheit.")

# Ejercicio 10

numero1 = int(input("Escribe un numero: "))
numero2 = int(input("Escribe otro numero: "))
numero3 = int(input("Escribe un tercer numero: "))
promedio = (numero1 + numero2 + numero3) / 3
print(f"El promedio de {numero1}, {numero2} y {numero3} es {promedio:.2f}.")
