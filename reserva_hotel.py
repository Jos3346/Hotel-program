import random

habitaciones = {
    "SI123": {
        "codigo": "SI123",
        "numero": 101,
        "tipo": "Simple",
        "estado": "Disponible"
    }
}

def generar_codigo_habitacion(tipo): 

    letras = tipo[:2].upper()
    numeros = str(random.randint(100, 999))
    codigo = letras + numeros
    return codigo

def agregar_habitacion():
    try:
        numero = int(input("Ingrese el número de la habitación: "))
        tipo = input("Ingrese el tipo de habitación (Simple, Doble, Suite): ").capitalize()
        if tipo not in ["Simple", "Doble", "Suite"]:
            print("Error: El tipo de habitación no es válido. Por favor, ingrese un tipo válido.")
            return
        
        codigo = generar_codigo_habitacion(tipo)
        while codigo in habitaciones:
            codigo = generar_codigo_habitacion(tipo)
        
        habitaciones[codigo] = {
            "codigo": codigo,
            "numero": numero,
            "tipo": tipo,
            "estado": "Disponible"
        }
        print(f"Habitación agregada exitosamente con código: {codigo}")
    except ValueError:
        print("Error: El tipo de habitación no es válido. Por favor, ingrese un tipo válido.")

def mostrar_habitaciones():
    if len(habitaciones) == 0:
        print("No hay habitaciones registradas.")
    else:
        print("\n===== LISTA DE HABITACIONES =====")

        for codigo in habitaciones:

            print("Código :", habitaciones[codigo]["codigo"])
            print("Número :", habitaciones[codigo]["numero"])
            print("Tipo :", habitaciones[codigo]["tipo"])
            print("Estado :", habitaciones[codigo]["estado"])
            print("----------------------------")

def buscar_habitacion():
    codigo = input("Ingrese el código de la habitación a buscar: ").upper()
    if codigo in habitaciones:
        print("Habitación encontrada:")
        print("Código :", habitaciones[codigo]["codigo"])
        print("Número :", habitaciones[codigo]["numero"])
        print("Tipo :", habitaciones[codigo]["tipo"])
        print("Estado :", habitaciones[codigo]["estado"])
    else:
        print("No se encontró ninguna habitación con ese código.")

def reservar_habitacion():
    codigo = input("Ingrese el código de la habitación a reservar: ").upper()
    if codigo in habitaciones:
        if habitaciones[codigo]["estado"] == "Disponible":
            habitaciones[codigo]["estado"] = "Reservada"
            print(f"Habitación {codigo} reservada exitosamente.")
        else:
            print(f"La habitación {codigo} no está disponible para reservar.")
    else:
        print("No se encontró ninguna habitación con ese código.")

def liberar_habitacion():
    codigo = input("Ingrese el código de la habitación a liberar: ").upper()
    if codigo in habitaciones:
        if habitaciones[codigo]["estado"] == "Reservada":
            habitaciones[codigo]["estado"] = "Disponible"
            print(f"Habitación {codigo} liberada exitosamente.")
        else:
            print(f"La habitación {codigo} no está reservada.")
    else:
        print("No se encontró ninguna habitación con ese código.")

def modificar_habitacion():
    codigo = input("Ingrese el código de la habitación a modificar: ").upper()
    if codigo in habitaciones:
        try:
            numero = int(input("Ingrese el nuevo número de la habitación: "))
            tipo = input("Ingrese el nuevo tipo de habitación (Simple, Doble, Suite): ").capitalize()
            if tipo not in ["Simple", "Doble", "Suite"]:
                print("Error: El tipo de habitación no es válido. Por favor, ingrese un tipo válido.")
                return
            habitaciones[codigo]["numero"] = numero
            habitaciones[codigo]["tipo"] = tipo
            
            print(f"Habitación {codigo} modificada exitosamente.")
        except ValueError:
            print("Error: El tipo de habitación no es válido. Por favor, ingrese un tipo válido.")
    else:
        print("No se encontró ninguna habitación con ese código.")

def eliminar_habitacion():
    codigo = input("Ingrese el código de la habitación a eliminar: ").upper()
    if codigo in habitaciones:
        del habitaciones[codigo]
        print(f"Habitación {codigo} eliminada exitosamente.")
    else:
        print("No se encontró ninguna habitación con ese código.")

def menu():
    while True:
        print("\n===== MENÚ DE RESERVA DE HABITACIONES =====")
        print("1. Agregar habitación")
        print("2. Mostrar habitaciones")
        print("3. Buscar habitación")
        print("4. Reservar habitación")
        print("5. Liberar habitación")
        print("6. Modificar habitación")
        print("7. Eliminar habitación")
        print("8. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_habitacion()
        elif opcion == "2":
            mostrar_habitaciones()
        elif opcion == "3":
            buscar_habitacion()
        elif opcion == "4":
            reservar_habitacion()
        elif opcion == "5":
            liberar_habitacion()
        elif opcion == "6":
            modificar_habitacion()
        elif opcion == "7":
            eliminar_habitacion()
        elif opcion == "8":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

menu()