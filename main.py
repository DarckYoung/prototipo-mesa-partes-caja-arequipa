# ==============================================================================
# UNIVERSIDAD PRIVADA DEL NORTE (UPN) - SEDE CAJAMARCA
# Curso: Fundamentos de Programacion (CIIN1205P)
# Docente: Ing. Frank Diaz Cabellos
# Caso de Estudio: Caja Arequipa - Agencia Cajamarca (Jr. Comercio Nro. 560)
# Modulo: Plataforma de Atencion al Usuario (Reclamos y Solicitudes Escritas)
# ==============================================================================

import os

ARCHIVO_DATOS = "expedientes_caja.txt"

def validar_dni(dni_texto):
    """Verifica que el DNI tenga exactamente 8 digitos numericos."""
    dni_limpio = dni_texto.strip()
    return len(dni_limpio) == 8 and dni_limpio.isdigit()

def obtener_nombre_prioridad(nivel):
    """Convierte el nivel numerico de prioridad a texto descriptivo."""
    if nivel == 1:
        return "1-ALTA (Reclamo SBS)"
    elif nivel == 2:
        return "2-MEDIA (Solicitud)"
    else:
        return "3-BAJA (Requerimiento)"

def guardar_en_archivo(codigos, dnis, nombres, tipos, montos, prioridades, estados):
    """Guarda todos los registros de los arreglos paralelos en el archivo plano."""
    try:
        with open(ARCHIVO_DATOS, "w", encoding="utf-8") as archivo:
            for i in range(len(codigos)):
                linea = f"{codigos[i]}|{dnis[i]}|{nombres[i]}|{tipos[i]}|{montos[i]:.2f}|{prioridades[i]}|{estados[i]}\n"
                archivo.write(linea)
    except IOError as error:
        print(f"\n[ERROR DE ARCHIVO] No se pudo guardar la informacion: {error}")

def cargar_desde_archivo(codigos, dnis, nombres, tipos, montos, prioridades, estados):
    """Carga los expedientes previos desde el archivo de texto al iniciar el programa."""
    if not os.path.exists(ARCHIVO_DATOS):
        datos_semilla = [
            ("EXP-0001", "71458923", "QUISPE ROJAS MARIA ELENA", "RECLAMO LIBRO", 450.00, 1, "PENDIENTE"),
            ("EXP-0002", "42896514", "SANCHEZ DIAZ CARLOS ALBERTO", "REQUERIMIENTO CNA", 0.00, 3, "EN PROCESO"),
            ("EXP-0003", "73910482", "VASQUEZ TORRES LUCIA FERNANDA", "SOLICITUD EXCESO PAGO", 85.50, 2, "PENDIENTE"),
            ("EXP-0004", "18234567", "MENDOZA CHAVEZ JORGE LUIS", "RECLAMO LIBRO", 1200.00, 1, "ATENDIDO")
        ]
        for reg in datos_semilla:
            codigos.append(reg[0])
            dnis.append(reg[1])
            nombres.append(reg[2])
            tipos.append(reg[3])
            montos.append(reg[4])
            prioridades.append(reg[5])
            estados.append(reg[6])
        guardar_en_archivo(codigos, dnis, nombres, tipos, montos, prioridades, estados)
        return

    try:
        with open(ARCHIVO_DATOS, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                linea = linea.strip()
                if linea != "":
                    partes = linea.split("|")
                    if len(partes) == 7:
                        codigos.append(partes[0])
                        dnis.append(partes[1])
                        nombres.append(partes[2])
                        tipos.append(partes[3])
                        montos.append(float(partes[4]))
                        prioridades.append(int(partes[5]))
                        estados.append(partes[6])
    except Exception as error:
        print(f"\n[AVISO] Error al leer el archivo de datos: {error}")

def registrar_expediente(codigos, dnis, nombres, tipos, montos, prioridades, estados):
    """Solicita y valida los datos de un nuevo tramite y lo agrega a los arreglos."""
    print("\n" + "=" * 68)
    print("  REGISTRO DE NUEVO EXPEDIENTE - PLATAFORMA CAJA AREQUIPA")
    print("=" * 68)

    correlativo = len(codigos) + 1
    nuevo_codigo = f"EXP-{correlativo:04d}"
    print(f"Codigo asignado automaticamente: {nuevo_codigo}")

    while True:
        dni = input("Ingrese DNI del cliente (8 digitos): ").strip()
        if validar_dni(dni):
            break
        print("  -> [ERROR] El DNI debe contener exactamente 8 digitos numericos.")

    while True:
        nombre = input("Ingrese Apellidos y Nombres del cliente: ").strip().upper()
        if len(nombre) >= 5:
            break
        print("  -> [ERROR] El nombre no puede estar vacio (minimo 5 caracteres).")

    print("\nSeleccione el Tipo de Tramite observado en agencia:")
    print("  [1] RECLAMO LIBRO (Formato LR CK2 - Plazo legal 15 dias habiles)")
    print("  [2] REQUERIMIENTO CNA (Certificado de No Adeudo / Constancias)")
    print("  [3] SOLICITUD EXCESO PAGO (Formato Multiple / Devolucion o Seguro)")

    while True:
        opc_tipo = input("Opcion de tramite (1-3): ").strip()
        if opc_tipo == "1":
            tipo_tramite = "RECLAMO LIBRO"
            prioridad_sugerida = 1
            break
        elif opc_tipo == "2":
            tipo_tramite = "REQUERIMIENTO CNA"
            prioridad_sugerida = 3
            break
        elif opc_tipo == "3":
            tipo_tramite = "SOLICITUD EXCESO PAGO"
            prioridad_sugerida = 2
            break
        else:
            print("  -> [ERROR] Seleccione una opcion valida entre 1 y 3.")

    while True:
        try:
            monto = float(input("Ingrese monto involucrado en S/ (0 si no aplica): ").strip())
            if monto >= 0:
                break
            print("  -> [ERROR] El monto no puede ser negativo.")
        except ValueError:
            print("  -> [ERROR] Debe ingresar un valor numerico valido (ejemplo: 150.50).")

    print(f"\nPrioridad sugerida segun normativa SBS: {prioridad_sugerida} (1=Alta, 2=Media, 3=Baja)")
    while True:
        try:
            entrada_prio = input(f"Presione ENTER para aceptar ({prioridad_sugerida}) o ingrese 1, 2 o 3: ").strip()
            if entrada_prio == "":
                prioridad = prioridad_sugerida
                break
            prioridad = int(entrada_prio)
            if 1 <= prioridad <= 3:
                break
            print("  -> [ERROR] La prioridad debe ser 1 (Alta), 2 (Media) o 3 (Baja).")
        except ValueError:
            print("  -> [ERROR] Ingrese un numero entero (1, 2 o 3).")

    estado_inicial = "PENDIENTE"

    codigos.append(nuevo_codigo)
    dnis.append(dni)
    nombres.append(nombre)
    tipos.append(tipo_tramite)
    montos.append(monto)
    prioridades.append(prioridad)
    estados.append(estado_inicial)

    guardar_en_archivo(codigos, dnis, nombres, tipos, montos, prioridades, estados)
    print(f"\n[EXITO] Expediente {nuevo_codigo} registrado y respaldado en '{ARCHIVO_DATOS}'.")

def mostrar_tabla_expedientes(codigos, dnis, nombres, tipos, montos, prioridades, estados):
    """Imprime en consola el listado completo de expedientes en formato tabular."""
    total = len(codigos)
    if total == 0:
        print("\n[AVISO] No existen expedientes registrados en el sistema.")
        return

    print("\n" + "=" * 112)
    print(f"{'CODIGO':<10} | {'DNI':<9} | {'APELLIDOS Y NOMBRES':<30} | {'TIPO TRAMITE':<22} | {'MONTO S/':>9} | {'PRIORIDAD':<10} | {'ESTADO':<10}")
    print("-" * 112)
    for i in range(total):
        etiqueta_prio = "1-ALTA" if prioridades[i] == 1 else ("2-MEDIA" if prioridades[i] == 2 else "3-BAJA")
        print(f"{codigos[i]:<10} | {dnis[i]:<9} | {nombres[i][:30]:<30} | {tipos[i]:<22} | {montos[i]:>9.2f} | {etiqueta_prio:<10} | {estados[i]:<10}")
    print("=" * 112)
    print(f"Total de expedientes en bandeja: {total}")

def buscar_expediente(codigos, dnis, nombres, tipos, montos, prioridades, estados):
    """Implementa el algoritmo de Busqueda Lineal por Codigo o por DNI."""
    if len(codigos) == 0:
        print("\n[AVISO] No hay expedientes registrados para realizar busquedas.")
        return

    print("\n--- BUSQUEDA SECUENCIAL DE EXPEDIENTES ---")
    criterio = input("Ingrese el Codigo (ej. EXP-0001) o el DNI (8 digitos) a buscar: ").strip().upper()

    encontrados = 0
    print("-" * 70)
    for i in range(len(codigos)):
        if codigos[i] == criterio or dnis[i] == criterio:
            encontrados += 1
            print(f"Resultado #{encontrados} encontrado en posicion [{i}]:")
            print(f"  * Codigo de Expediente : {codigos[i]}")
            print(f"  * DNI del Cliente      : {dnis[i]}")
            print(f"  * Titular              : {nombres[i]}")
            print(f"  * Tipo de Tramite      : {tipos[i]}")
            print(f"  * Monto Involucrado    : S/ {montos[i]:.2f}")
            print(f"  * Nivel de Prioridad   : {obtener_nombre_prioridad(prioridades[i])}")
            print(f"  * Estado Actual        : {estados[i]}")
            print("-" * 70)

    if encontrados == 0:
        print(f"[SIN RESULTADOS] No se encontro ningun expediente asociado a '{criterio}'.")
    else:
        print(f"[RESUMEN] Se localizaron {encontrados} coincidencia(s).")

def intercambiar_registros(codigos, dnis, nombres, tipos, montos, prioridades, estados, i, j):
    """Intercambia simultaneamente los elementos en las posiciones i y j de las 7 listas paralelas."""
    codigos[i], codigos[j] = codigos[j], codigos[i]
    dnis[i], dnis[j] = dnis[j], dnis[i]
    nombres[i], nombres[j] = nombres[j], nombres[i]
    tipos[i], tipos[j] = tipos[j], tipos[i]
    montos[i], montos[j] = montos[j], montos[i]
    prioridades[i], prioridades[j] = prioridades[j], prioridades[i]
    estados[i], estados[j] = estados[j], estados[i]

def ordenar_burbuja(codigos, dnis, nombres, tipos, montos, prioridades, estados, modo):
    """Implementa el algoritmo Bubble Sort sincronizado sobre los arreglos paralelos."""
    n = len(codigos)
    if n <= 1:
        print("\n[AVISO] Se requieren al menos 2 expedientes para ejecutar el ordenamiento.")
        return

    for i in range(n - 1):
        hubo_intercambio = False
        for j in range(n - 1 - i):
            debe_intercambiar = False
            if modo == 1:
                if prioridades[j] > prioridades[j + 1]:
                    debe_intercambiar = True
            elif modo == 2:
                if nombres[j] > nombres[j + 1]:
                    debe_intercambiar = True

            if debe_intercambiar:
                intercambiar_registros(codigos, dnis, nombres, tipos, montos, prioridades, estados, j, j + 1)
                hubo_intercambio = True

        if not hubo_intercambio:
            break

    guardar_en_archivo(codigos, dnis, nombres, tipos, montos, prioridades, estados)
    if modo == 1:
        print("\n[ORDENAMIENTO EXITOSO] Expedientes ordenados por PRIORIDAD (1-Alta -> 3-Baja).")
    else:
        print("\n[ORDENAMIENTO EXITOSO] Expedientes ordenados ALFABETICAMENTE por titular (A -> Z).")
    mostrar_tabla_expedientes(codigos, dnis, nombres, tipos, montos, prioridades, estados)

def actualizar_estado_expediente(codigos, dnis, nombres, tipos, montos, prioridades, estados):
    """Permite buscar un expediente por codigo y actualizar su estado operativo."""
    codigo_buscar = input("\nIngrese el Codigo del expediente a actualizar (ej. EXP-0001): ").strip().upper()
    indice = -1
    for i in range(len(codigos)):
        if codigos[i] == codigo_buscar:
            indice = i
            break

    if indice == -1:
        print(f"[ERROR] El expediente '{codigo_buscar}' no existe.")
        return

    print(f"Expediente seleccionado: {codigos[indice]} - {nombres[indice]} (Estado actual: {estados[indice]})")
    print("Seleccione nuevo estado: [1] PENDIENTE  |  [2] EN PROCESO  |  [3] ATENDIDO")
    opc_est = input("Opcion (1-3): ").strip()
    if opc_est == "1":
        estados[indice] = "PENDIENTE"
    elif opc_est == "2":
        estados[indice] = "EN PROCESO"
    elif opc_est == "3":
        estados[indice] = "ATENDIDO"
    else:
        print("[ERROR] Opcion invalida. No se realizaron cambios.")
        return

    guardar_en_archivo(codigos, dnis, nombres, tipos, montos, prioridades, estados)
    print(f"[EXITO] Estado del expediente {codigo_buscar} actualizado a '{estados[indice]}'.")

def menu_principal():
    """Funcion controladora principal del sistema."""
    codigos, dnis, nombres, tipos, montos, prioridades, estados = [], [], [], [], [], [], []
    cargar_desde_archivo(codigos, dnis, nombres, tipos, montos, prioridades, estados)

    while True:
        print("\n" + "=" * 68)
        print("  SISTEMA DE MESA DE PARTES DIGITAL - CAJA AREQUIPA (CAJAMARCA)")
        print("  Modulo: Plataforma de Atencion al Usuario (Jr. Comercio 560)")
        print("=" * 68)
        print("  [1] Registrar nuevo expediente (Reclamo / Requerimiento / Solicitud)")
        print("  [2] Buscar expediente por Codigo o DNI (Busqueda Lineal)")
        print("  [3] Ordenar expedientes por Prioridad SBS (Ordenamiento Burbuja)")
        print("  [4] Ordenar expedientes Alfabeticamente por Cliente (Burbuja)")
        print("  [5] Mostrar bandeja completa de expedientes")
        print("  [6] Actualizar estado de un expediente (Pendiente/En Proceso/Atendido)")
        print("  [7] Salir y guardar cambios")
        print("=" * 68)

        opcion = input("Seleccione una opcion (1-7): ").strip()

        if opcion == "1":
            registrar_expediente(codigos, dnis, nombres, tipos, montos, prioridades, estados)
        elif opcion == "2":
            buscar_expediente(codigos, dnis, nombres, tipos, montos, prioridades, estados)
        elif opcion == "3":
            ordenar_burbuja(codigos, dnis, nombres, tipos, montos, prioridades, estados, modo=1)
        elif opcion == "4":
            ordenar_burbuja(codigos, dnis, nombres, tipos, montos, prioridades, estados, modo=2)
        elif opcion == "5":
            mostrar_tabla_expedientes(codigos, dnis, nombres, tipos, montos, prioridades, estados)
        elif opcion == "6":
            actualizar_estado_expediente(codigos, dnis, nombres, tipos, montos, prioridades, estados)
        elif opcion == "7":
            guardar_en_archivo(codigos, dnis, nombres, tipos, montos, prioridades, estados)
            print("\n[SISTEMA CERRADO] Datos resguardados en 'expedientes_caja.txt'. Hasta pronto.")
            break
        else:
            print("\n[ERROR] Opcion no valida. Por favor ingrese un numero entre 1 y 7.")

if __name__ == "__main__":
    menu_principal()
