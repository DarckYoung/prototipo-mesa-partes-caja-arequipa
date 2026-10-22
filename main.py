# Prototipo Modular de Mesa de Partes - Caja Arequipa (Agencia Cajamarca)
# Semana 7: Refactorizacion en funciones modulares y manejo de excepciones try-except

ARCHIVO_DATOS = "expedientes_caja.txt"

def validar_dni(dni_texto):
    dni_limpio = dni_texto.strip()
    return len(dni_limpio) == 8 and dni_limpio.isdigit()

def guardar_en_archivo(codigos, dnis, nombres, tipos, montos, prioridades, estados):
    try:
        with open(ARCHIVO_DATOS, "w", encoding="utf-8") as archivo:
            for i in range(len(codigos)):
                linea = f"{codigos[i]}|{dnis[i]}|{nombres[i]}|{tipos[i]}|{montos[i]:.2f}|{prioridades[i]}|{estados[i]}\n"
                archivo.write(linea)
    except IOError as e:
        print(f"[ERROR] No se pudo guardar en archivo: {e}")

def buscar_expediente(codigos, dnis, nombres, tipos, montos, prioridades, estados):
    print("\n--- BUSQUEDA SECUENCIAL DE EXPEDIENTES ---")
    criterio = input("Ingrese Codigo (ej. EXP-0001) o DNI (8 digitos): ").strip().upper()
    encontrado = False
    for i in range(len(codigos)):
        if codigos[i] == criterio or dnis[i] == criterio:
            print(f"[ENCONTRADO] {codigos[i]} | DNI: {dnis[i]} | Cliente: {nombres[i]} | Tramite: {tipos[i]} | Estado: {estados[i]}")
            encontrado = True
    if not encontrado:
        print(f"[AVISO] No se encontro ningun expediente para: {criterio}")

def intercambiar_registros(codigos, dnis, nombres, tipos, montos, prioridades, estados, i, j):
    codigos[i], codigos[j] = codigos[j], codigos[i]
    dnis[i], dnis[j] = dnis[j], dnis[i]
    nombres[i], nombres[j] = nombres[j], nombres[i]
    tipos[i], tipos[j] = tipos[j], tipos[i]
    montos[i], montos[j] = montos[j], montos[i]
    prioridades[i], prioridades[j] = prioridades[j], prioridades[i]
    estados[i], estados[j] = estados[j], estados[i]

def ordenar_burbuja(codigos, dnis, nombres, tipos, montos, prioridades, estados, modo):
    n = len(codigos)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if (modo == 1 and prioridades[j] > prioridades[j + 1]) or (modo == 2 and nombres[j] > nombres[j + 1]):
                intercambiar_registros(codigos, dnis, nombres, tipos, montos, prioridades, estados, j, j + 1)
