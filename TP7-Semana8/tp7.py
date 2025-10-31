import os

# Actividad 1

def crear_archivo_inicial():

  if(not os.path.exists("productos.txt")):
    productos_iniciales = [
        "Lapicera,120.5,30\n",
        "Cuaderno,450.0,15\n",
        "Goma,80.0,50\n"
    ]
    with open("productos.txt", "w") as archivo:
        archivo.writelines(productos_iniciales)
    print("Archivo 'productos.txt' creado con 3 productos iniciales.")

  else:
     print("El archivo 'productos.txt' ya existe.")

# Actividad 2

def mostrar_productos():
 
 if(os.path.exists("productos.txt")):
  with open("productos.txt", "r") as archivo:
    lineas = archivo.readlines()

    for linea in lineas:
     nombre, precio, cantidad = linea.strip().split(",")
     print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")
 
 else:
    print("El archivo 'productos.txt' no existe. Por favor, cree el archivo primero.")

# Actividad 3

def agregar_producto():

    if(not os.path.exists("productos.txt")):
        print("El archivo 'productos.txt' no existe. Por favor, cree el archivo primero.")
        return

    nombre = input("Ingrese el nombre del producto: ")
    precio = input("Ingrese el precio: ")
    cantidad = input("Ingrese la cantidad: ")
    with open("productos.txt", "a") as archivo:
        archivo.write(f"{nombre},{precio},{cantidad}\n")
    print("Producto agregado correctamente.")

# Actividad 4

def cargar_productos_en_lista():
    productos = []

    if(not os.path.exists("productos.txt")):
        print("El archivo 'productos.txt' no existe. Por favor, cree el archivo primero.")
        return

    with open("productos.txt", "r") as archivo:
        for linea in archivo:
         nombre, precio, cantidad = linea.strip().split(",")
         producto = {
                  "nombre": nombre,
                  "precio": float(precio),
                  "cantidad": int(cantidad)}
         productos.append(producto)

    return productos

# Actividad 5

def buscar_producto(productos):
    nombre_buscar = input("Ingrese el nombre del producto a buscar: ")
    encontrado = False
    for producto in productos:
        if producto["nombre"].lower() == nombre_buscar.lower():
            print(f"Producto encontrado: {producto}")
            encontrado = True
            break
    if not encontrado:
        print("El producto no existe.")

# Actividad 6

def guardar_productos(productos):

    if(not os.path.exists("productos.txt")):
        print("El archivo 'productos.txt' no existe. Por favor, cree el archivo primero.")
        return

    with open("productos.txt", "w") as archivo:
        for p in productos:
            archivo.write(f"{p['nombre']},{p['precio']},{p['cantidad']}\n")
    print("Archivo actualizado correctamente.")

# Ejecución de las actividades

def menu():
    while True:
        print("\n--- MENÚ DE PRODUCTOS ---")
        print("1. Crear archivo inicial")
        print("2. Mostrar productos")
        print("3. Agregar producto")
        print("4. Crear lista de productos desde archivo")
        print("5. Buscar producto en lista por nombre")
        print("6. Actualizar archivo con lista")
        print("7. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            crear_archivo_inicial()
        elif opcion == "2":
            mostrar_productos()
        elif opcion == "3":
            agregar_producto()
        elif opcion == "4":
            productos = cargar_productos_en_lista()
            print("Productos cargados en la lista:")
            for producto in productos:
             print(producto)
        elif opcion == "5":
            productos = cargar_productos_en_lista()
            buscar_producto(productos)
        elif opcion == "6":
            productos = cargar_productos_en_lista()
            guardar_productos(productos)
        elif opcion == "7":
            print("Programa finalizado.")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

menu()