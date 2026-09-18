# Prototipo de Mesa de Partes - Caja Arequipa (Agencia Cajamarca)
# Semana 4: Estructura de listas paralelas en memoria

codigos = []
dnis = []
nombres = []
tipos = []
montos = []
prioridades = []
estados = []

ejecutando = True
while ejecutando:
    print("\n=== SISTEMA DE MESA DE PARTES - CAJA AREQUIPA ===")
    print("1. Registrar nuevo expediente")
    print("2. Listar expedientes registrados")
    print("3. Salir")
    opcion = input("Seleccione una opcion (1-3): ")

    if opcion == "1":
        correlativo = len(codigos) + 1
        codigo = "EXP-" + str(correlativo).zfill(4)
        dni = input("DNI (8 digitos): ")
        nombre = input("Cliente: ")
        tipo = input("Tipo de tramite: ")
        monto = float(input("Monto S/: "))
        prioridad = int(input("Prioridad (1=Alta, 2=Media, 3=Baja): "))
        
        codigos.append(codigo)
        dnis.append(dni)
        nombres.append(nombre)
        tipos.append(tipo)
        montos.append(monto)
        prioridades.append(prioridad)
        estados.append("PENDIENTE")
        print("[OK] Registrado con codigo:", codigo)
    elif opcion == "2":
        for i in range(len(codigos)):
            print(codigos[i], dnis[i], nombres[i], tipos[i], montos[i], prioridades[i], estados[i])
    elif opcion == "3":
        ejecutando = False
