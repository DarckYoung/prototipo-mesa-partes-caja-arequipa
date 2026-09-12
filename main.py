# Prototipo de Mesa de Partes - Caja Arequipa (Agencia Cajamarca)
# Semana 3: Menu interactivo con ciclo while y validacion condicional

 ejecutando = True
while ejecutando:
    print("\n=======================================================")
    print("  SISTEMA DE MESA DE PARTES - CAJA AREQUIPA CAJAMARCA  ")
    print("=======================================================")
    print("1. Registrar nuevo expediente")
    print("2. Salir")
    opcion = input("Seleccione una opcion (1-2): ")

    if opcion == "1":
        dni = input("Ingrese DNI (8 digitos): ")
        if len(dni) == 8:
            nombre = input("Apellidos y nombres: ")
            prioridad = int(input("Prioridad (1=Alta, 2=Media, 3=Baja): "))
            if prioridad >= 1 and prioridad <= 3:
                print("[OK] Datos validos para el cliente:", nombre)
            else:
                print("[ERROR] Prioridad fuera de rango (1-3).")
        else:
            print("[ERROR] El DNI debe tener 8 digitos.")
    elif opcion == "2":
        print("Cerrando sistema...")
        ejecutando = False
    else:
        print("[ERROR] Opcion no valida.")
