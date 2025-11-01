import os

# Listas

catalogo = []

lineas_csv = ["TITULO,CANTIDAD\n","El Señor de los Anillos,5\n","1984,0\n","Ficciones,3\n"]

# Funciones

def verificar_titulo_existente(titulo):
    for libro in catalogo:
        if libro["TITULO"].lower() == titulo.lower():
            return libro
    return False

def modificar_archivo(titulo, cantidad):

    modified_lines = []

    with open("catalogo_libros.csv", "r") as archivo:
     for linea in archivo:
        if(linea.startswith(titulo)):
            linea = f"{titulo},{cantidad}\n"

        modified_lines.append(linea)

    with open("catalogo_libros.csv", "w") as archivo:
        archivo.writelines(modified_lines)

def ingresar_titulos():
    
    cantidad_de_titulos = int(input("Ingrese la cantidad de títulos a agregar: "))
    
    for i in range(cantidad_de_titulos):
        titulo = input("Ingrese el título del libro: ")

        if(verificar_titulo_existente(titulo)):
            print("El título ya existe en el catálogo. Intente con otro título.")
            continue

        cantidad = int(input("Ingrese la cantidad disponible: "))
        nuevo_libro = {"TITULO": titulo, "CANTIDAD": cantidad}

        with open("catalogo_libros.csv", "a") as archivo:
            archivo.write(f"{titulo},{cantidad}\n")

        catalogo.append(nuevo_libro)

    print("Títulos ingresados correctamente.")
        
def ingresar_ejemplares(titulo, cantidad):

    titulo_finded = verificar_titulo_existente(titulo)

    if(titulo_finded):
        titulo_finded["CANTIDAD"] += cantidad
        modificar_archivo(titulo, titulo_finded["CANTIDAD"])
    else:
        print("El título no se encuentra en el catálogo.")

def mostrar_catalogo():
    print("\nCatálogo de libros:")
    for libro in catalogo:
        print(f"Título: {libro['TITULO']}, Cantidad disponible: {libro['CANTIDAD']}")

def consultar_disponibilidad():
    titulo = input("Ingrese el título del libro a consultar: ")
    
    for libro in catalogo:
        if libro["TITULO"].lower() == titulo.lower():
            if libro["CANTIDAD"] > 0:
                print(f"El libro '{libro['TITULO']}' está disponible. Cantidad: {libro['CANTIDAD']}")
            else:
                print(f"El libro '{libro['TITULO']}' no está disponible.")
            return
    
    print("El título no se encuentra en el catálogo.")

def listar_agotados():
    print("\nLibros agotados:")
    agotados = [libro for libro in catalogo if libro["CANTIDAD"] == 0]
    
    if not agotados:
        print("No hay libros agotados.")
    else:
        for libro in agotados:
            print(f"Título: {libro['TITULO']}")

def agregar_titulo_individual():

    titulo = input("Ingrese el título del libro: ")

    verificar_titulo_existente(titulo)
    if(verificar_titulo_existente(titulo)):
        print("El título ya existe en el catálogo. Intente con otro título.")
        return

    cantidad = int(input("Ingrese la cantidad disponible: "))
    nuevo_libro = {"TITULO": titulo, "CANTIDAD": cantidad}
    catalogo.append(nuevo_libro)
    modificar_archivo(titulo,cantidad)
    print("Título ingresado correctamente.")

def actualizar_ejemplares(libro):
   
   verificar_titulo_existente(libro)
   if(not verificar_titulo_existente(libro)):
       print("El título no se encuentra en el catálogo.")
       return

   accion = input("¿Desea agregar o quitar ejemplares? (agregar/quitar): ").strip().lower()

   if(accion not in ['agregar', 'quitar']):
       print("Acción inválida. Por favor, intente nuevamente.")
       return
   
   if(accion == 'agregar'):
       ingresar_ejemplares(libro, 1)
       modificar_archivo(libro, 1)

   if(accion == 'quitar'):
       for l in catalogo:
           if l["TITULO"].lower() == libro.lower():
               if l["CANTIDAD"] > 0:
                   l["CANTIDAD"] -= 1
                   print(f"Se ha quitado un ejemplar del título '{l['TITULO']}'.")
                   modificar_archivo(libro,l["CANTIDAD"])
               else:
                   print(f"No hay ejemplares disponibles para el título '{l['TITULO']}'.")
               return   

# Programa Principal

def menu():

    if(not os.path.exists("catalogo_libros.csv")):
     with open("catalogo_libros.csv", "w") as archivo:
        archivo.writelines(lineas_csv)
     print("Archivo 'catalogo_libros.csv' creado con el catálogo inicial.")
     
    while True:

     with open("catalogo_libros.csv", 'r') as archivo:
         for lineas in archivo:
          if(lineas.startswith("TITULO")):
             continue
          libro, cantidad = lineas.strip().split(',')
          if(verificar_titulo_existente(libro)):
              continue
          nuevo_libro = {
            "TITULO": libro,
            "CANTIDAD": int(cantidad)
          }
          catalogo.append(nuevo_libro)

     print("\nMenú de opciones:")
     print("1. Ingresar nuevos títulos")
     print("2. Ingresar ejemplares a un título existente")
     print("3. Mostrar catálogo de libros")
     print("4. Consultar disponibilidad de un título")
     print("5. Listar títulos agotados")
     print("6. Ingresar titulo individual")
     print("7. Actualizar ejemplares de un título")
     print("0. Salir")
        
     opcion = input("Seleccione una opción: ")
        
     if opcion == '1':
            ingresar_titulos()
     elif opcion == '2':

        libro = input("Ingrese el título del libro al que desea agregar ejemplares: ")
        cantidad = int(input("Ingrese la cantidad de ejemplares a agregar: "))
        ingresar_ejemplares(libro, cantidad)

     elif opcion == '3':
            mostrar_catalogo()
     elif opcion == '4':
            consultar_disponibilidad()
     elif opcion == '5':
            listar_agotados()
     elif opcion == '6':
            agregar_titulo_individual()
     elif opcion == '7':
            libro = input("Ingrese el título del libro que desea actualizar: ")
            actualizar_ejemplares(libro)
     elif opcion == '0':
            print("Saliendo del programa. ¡Hasta luego!")
            break
     else:
            print("Opción inválida. Por favor, intente nuevamente.")

menu()