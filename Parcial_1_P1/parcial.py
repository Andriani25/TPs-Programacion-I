opciones_menu = ['1. Ingresar titulo (sin ejemplares)',
                 '2. Ingresar ejemplares disponibles (sin titulo)',
                 '3. Mostrar catalogo',
                 '4. Consultar disponibilidad',
                 '5. Listar agotados',
                 '6. Agregar titulo (con ejemplares)',
                 '7. Actualizar ejemplares (prestamos/devoluciones)',
                 '8. Ver catalogo completo',
                 '9. Salir'
                 ]

titulos = []
ejemplares = []

while True:
    print('=== Menu de Biblioteca ===')

    for opcion in opciones_menu:
        print(opcion)
 
    
    seleccion = input('Seleccione una opcion: ')

    if seleccion == "1":
        
        titulo = input('Ingresar titulo: ')

        while titulo in titulos or titulo == "":
            print('Titulo repetido o en blanco. Intente nuevamente')
            titulo = input('Ingrese un nuevo titulo: ')

        print(f'Titulo ingresado: {titulo}')
        titulos.append(titulo)
        posicion = titulos.index(titulo)
        ejemplares.insert(posicion, 0)

    elif seleccion == '2':
        
        if not titulos:
            print('No hay titulos ingresados. Primero deben existir titulos para poder ingresar cantidad de ejemplares ')
            continue

        for i, titulo in enumerate(titulos):
            print(f"{i + 1}, {titulo}")

        posicion = int(input('Seleccione el numero de titulo para ingresar ejemplares: ')) - 1

        while posicion < 0 or posicion >= len(titulos):
            print('Posicion invalida, intente nuevamente')
            posicion = int(input('Seleccione nuevamente un numero de titulo para ingresar ejemplares: ')) - 1

        cantidad = int(input('Ingrese cantidad de ejemplares: '))
        ejemplares[posicion] += cantidad
        print(f'Ejemplares disponibles actualmente para {titulos[posicion]}: {ejemplares[posicion]}')


    elif seleccion == '3':
        
         if not titulos:
            print('No hay titulos ingresados. Primero deben existir titulos para poder ingresar cantidad de ejemplares ')
            continue
         
         for i, titulo in enumerate(titulos):
            print(f"{i + 1}, {titulo}")


    elif seleccion == '4':

          if not titulos:
            print('No hay titulos ingresados. Primero deben existir titulos para poder ingresar cantidad de ejemplares ')
            continue
          
          titulo_consulta = input('Ingresar titulo a consultar: ')

          while True:
              if titulo_consulta in titulos:
                  posicion = titulos.index(titulo_consulta)
                  print(f'Ejemplares disponibles para {titulo_consulta}: {ejemplares[posicion]}')
                  break
              else:
                  print(f'El titulo: {titulo_consulta} no se encuentra en el catalogo')
                  print('Si desea nuevamente ingresar un titulo ingrese "s", si quiere volver al menu principal ingrese "n"')

                  if input().lower() == "s":
                      titulo_consulta = input('Ingresar titulo a consultar: ')
                  else:
                      break

    elif seleccion == '5':

        if not titulos:
            print('No hay titulos ingresados. Primero deben existir titulos para poder ingresar cantidad de ejemplares ')
            continue

        agotados = False

        for i in ejemplares:
            if i == 0:
                agotados = True
                break

        if agotados:
            print("== Libros agotados ==")
            for titulo in titulos:
                posicion = titulos.index(titulo)
                if ejemplares[posicion] == 0:
                    print(titulo)

    elif seleccion == '6':

        nuevo_titulo = input('Ingresar nuevo titulo: ')

        if nuevo_titulo in titulos:
            print(f'El titulo {nuevo_titulo} ya existe en el catalogo')
        else:
            titulos.append(nuevo_titulo)
            cantidad = int(input(f'Ingresar cantidad de ejemplares para {nuevo_titulo}: '))
            posicion = titulos.index(nuevo_titulo)
            ejemplares.insert(posicion, cantidad)
            print(f'Titulo "{nuevo_titulo}" agregado al catalogo con {cantidad} ejemplares disponibles')


    elif seleccion == '7':

        if not titulos:
            print('No hay titulos ingresados. Primero deben existir titulos para poder ingresar cantidad de ejemplares ')
            continue
        
        for i, titulo in enumerate(titulos):
            print(f'{i + 1}. {titulo}')

        posicion = int(input('Ingresar numero de libro: ')) - 1

        while posicion < 0 or posicion >= len(titulos):
            print('Posicion invalida, intente nuevamente')
            posicion = int(input('Seleccione el numero de titulo para ingersar ejemplares: ')) - 1

        accion = input('Ingrese "p" para prestamo o "d" para devolucion').lower()

        if accion == "p":
            if ejemplares[posicion] > 0:
                ejemplares[posicion] -= 1
                print(f'Prestamo realizado. Ejemplares disponibles para {titulos[posicion]}: {ejemplares[posicion]}')
            else:
                print(f'No hay ejemplares disponibles de {titulos[posicion]}')
        elif accion == "d":
            ejemplares[posicion] += 1
            print('Devolucion realizada')
        else:
            print('Accion es invalida. Use "p" para prestamo y "d" para devolucion: ')

    elif seleccion == '8':

        if not titulos:
            print('No hay titulos ingresados. Primero deben existir titulos para poder ingresar cantidad de ejemplares ')
            continue

        contador = 1
        print('=== Catalogo completo ===')

        for titulo in titulos:
            posicion = titulos.index(titulo)
            print(f'{contador}. {titulo} - Ejemplares disponibles: {ejemplares[posicion]}')
            contador += 1

    elif seleccion == '9':
        break

    