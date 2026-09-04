# Prototipo de Mesa de Partes - Caja Arequipa (Agencia Cajamarca)
# Semana 2: Variables tipadas y lectura basica por consola

print("--- RECEPCION DE EXPEDIENTES - CAJA AREQUIPA ---")
codigo = "EXP-0001"
dni = input("Ingrese DNI del cliente: ")
nombre = input("Ingrese apellidos y nombres: ")
tipo = input("Ingrese tipo de tramite (Reclamo / Requerimiento / Solicitud): ")
monto = float(input("Ingrese monto involucrado (S/): "))
prioridad = int(input("Ingrese prioridad (1=Alta, 2=Media, 3=Baja): "))

print("Expediente registrado:", codigo, "| DNI:", dni, "| Cliente:", nombre, "| Monto: S/", monto)
