Este documento presenta un análisis funcional detallado de la pantalla
'Órdenes de Trabajo' de la aplicación Necor@V6 desarrollada en Visual
Basic 6. El objetivo es documentar las funcionalidades disponibles desde
la perspectiva del usuario, describiendo elementos de interfaz, acciones
posibles y flujos operativos detectados. Este informe es independiente
de cualquier comparación con versiones más recientes del software.

# 1. Elementos de Interfaz Identificados

La pantalla principal de gestión de órdenes de trabajo está compuesta
por los siguientes elementos visuales:

\- Menú superior con botones: Nuevo, Editar, Borrar, Imprimir, Salir.

\- Panel lateral izquierdo con filtros de búsqueda: Estado, Cliente,
Fecha, Tipo de orden.

\- Rejilla central con listado de órdenes activas (columnas: Nº Orden,
Cliente, Fecha Inicio, Fecha Fin, Estado, Técnico asignado).

\- Panel inferior con campos de observaciones generales y totales.

\- Botonera inferior con funciones: Guardar, Cancelar, Generar PDF,
Cerrar.

# 2. Flujos Funcionales Observados

\- Acceso a la pantalla de órdenes de trabajo desde el menú principal.

\- Creación de una nueva orden: pulsar 'Nuevo', completar campos,
guardar.

\- Búsqueda de órdenes por filtros (cliente, estado, fecha).

\- Edición de orden: seleccionar fila → pulsar 'Editar' → modificar
campos → pulsar 'Guardar'.

\- Eliminación de orden: seleccionar fila → pulsar 'Borrar'.

\- Impresión o generación de documento: botón 'Imprimir' o 'Generar
PDF'.

\- Acceso a datos extendidos desde pestañas internas: Tareas,
Materiales, Historial.

\- Cierre de la orden mediante campo de estado o botón específico.

# 3. Pestañas y Funcionalidades Asociadas

\- General: Campos principales como Nº orden, cliente, fechas,
observaciones y estado.

\- Tareas: Listado editable de tareas asignadas con tiempos y técnicos.

\- Materiales: Consumo de materiales con cantidad y coste.

\- Historial: Visualización de eventos registrados sobre la orden.

\- Facturación: Datos de cobro asociados si está habilitado.

# 4. Observaciones Funcionales

La aplicación presenta una estructura clara basada en pestañas, lo que
permite una navegación organizada. Los botones son consistentes en su
ubicación, aunque las acciones no siempre presentan mensajes de
confirmación visibles. Algunas acciones requieren selección previa desde
la tabla central, sin lo cual el botón no está habilitado.
