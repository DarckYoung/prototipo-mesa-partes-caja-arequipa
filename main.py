# Prototipo de Mesa de Partes - Caja Arequipa (Agencia Cajamarca)
# Semana 5: Normalizacion de cadenas (.strip, .upper, .isdigit)

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
    print("1. Registrar expediente")
    print("2. Listar expedientes")
    print("3. Salir")
    opcion = input("Seleccione opcion: ").strip()

    if opcion == "1":
        dni = input("DNI (8 digitos): ").strip()
        while not (dni.isdigit() and len(dni) == 8):
            print("[ERROR] El DNI debe contener exactamente 8 digitos numericos.")
            dni = input("DNI (8 digitos): ").strip()
            
        nombre = input("Apellidos y Nombres: ").strip().upper()
        tipo = input("Tipo de tramite: ").strip().upper()
        monto = float(input("Monto S/: ").strip())
        prioridad = int(input("Prioridad (1-3): ").strip())
        
        codigo = f"EXP-{len(codigos) + 1:04d}"
        codigos.append(codigo)
        dnis.append(dni)
        nombres.append(nombre)
        tipos.append(tipo)
        montos.append(monto)
        prioridades.append(prioridad)
        estados.append("PENDIENTE")
        print(f"[OK] Expediente {codigo} registrado para {nombre}.")
    elif opcion == "2":
        for i in range(len(codigos)):
            print(f"{codigos[i]} | {dnis[i]} | {nombres[i]} | S/ {montos[i]:.2f}")
    elif opcion == "3":
        ejecutando = False
