# Prototipo de Mesa de Partes y Plataforma - Caja Arequipa (Agencia Cajamarca)

**Curso:** Fundamentos de Programacion (CIIN1205P) - UPN Cajamarca  
**Docente:** Ing. Frank Diaz Cabellos  
**Caso de Estudio:** Modulo de Recepcion de Reclamos, Requerimientos y Solicitudes Escritas (Jr. Comercio Nro. 560, Cajamarca).

## Descripcion del Problema
Actualmente el registro del Libro de Reclamaciones (`LR CK2 000001`) y solicitudes en Formato Multiple conlleva un tiempo promedio de 12.94 minutos por atencion debido al llenado manual y busqueda fisica en archivadores de palanca.

## Especificacion E-P-S (Entrada - Proceso - Salida)
- **Entradas:** DNI (8 digitos), Nombre del cliente, Tipo de tramite (1: Reclamo, 2: Requerimiento CNA, 3: Solicitud), Monto en soles, Prioridad (1-3) y Estado.
- **Procesos:** Validacion de datos, almacenamiento en arreglos paralelos, persistencia en archivo de texto, busqueda lineal y ordenamiento burbuja.
- **Salidas:** Comprobante en consola, reportes ordenados y archivo `expedientes_caja.txt`.
