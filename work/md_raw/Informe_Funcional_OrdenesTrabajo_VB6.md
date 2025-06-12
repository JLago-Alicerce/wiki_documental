Este informe recoge el análisis funcional de la pantalla 'Órdenes de
Trabajo' perteneciente a la versión VB6 de la aplicación Necor@V6. A
partir del estudio visual de las interfaces, se han identificado los
elementos clave, flujos de usuario y funcionalidades accesibles sin
acceder al detalle interno del código ni procesos ocultos.

# 1. Elementos de Interfaz Identificados

Se identifican los siguientes elementos visibles en la pantalla
principal de Órdenes de Trabajo:

\- Menú superior con opciones de gestión (Nuevo, Editar, Eliminar,
Imprimir).

\- Panel lateral izquierdo con filtros de búsqueda (Estado, Cliente,
Fecha).

\- Rejilla central con listado de órdenes con columnas: ID, Cliente,
Fecha, Estado, etc.

\- Botones de acción en la parte inferior: 'Guardar', 'Cancelar',
'Generar PDF'.

# 2. Flujos de Usuario Observados

Ejemplo de flujo típico de trabajo observado:

1\. Selección de una orden desde la rejilla principal.

2\. Edición de los campos 'Cliente' y 'Fecha de ejecución'.

3\. Clic en botón 'Guardar' para registrar los cambios.

4\. Opción de generar PDF mediante botón inferior derecho.
