---
source: DTI-MIGRACION-HOST-R03.md
doc_source: DTI-MIGRACION-HOST-R03.docx
created: 2025-06-13T05:51:57.522134
---
# Accesibilidad de la información

Se considera imprescindible que la información especialmente relevante
pueda seguir siendo accesible a través de las aplicaciones Necor@PRYC y
Necor@NET. En el caso de PRYC, este ya dispone de funcionalidades de
consulta relacionadas con el área de órdenes de trabajo. En el caso de
NET, este igualmente dispone de funcionalidades de consulta relacionadas
con el área de ingeniería.

Sin embargo ninguna de estas dos aplicaciones dispone de funcionalidades
de consulta relacionadas con el resto de áreas de información
(aprovisionamiento, almacén, etc.).

Es por lo tanto el objeto de este apartado del documento el de
identificar las funcionalidades de consulta que deberían ser
implementadas en Necor@PRYC, con el fin de poder garantizar el acceso a
la información tras el apagado definitivo del HOST. Con carácter general
se considerarán todas las funcionalidades de consulta ya existentes en
Necor@, incluida logística (CORAL).

Quedan excluidas las funcionalidades relacionadas con la generación de
informes y explotación estadística específicas de Necora 3270 (SI2).
Igualmente quedan excluidas las funcionalidades de gestión de órdenes de
trabajo y sus derivadas (operaciones, materiales, componentes, cruces,
etc.) ya que estas ya han sido implementadas en la primera fase de
proyectos en curso.

Tampoco se consideran las funcionalidades de consulta de documentos
técnicos, avisos de revisión y documentos técnicos en producción, que ya
forman parte de Necor@NET, y cuyas funciones de consulta en Necor@PRYC
fueron desarrolladas igualmente en la primera fase del proyecto.

La **estrategia propuesta para la migración** de las funcionalidades de
Consulta es la siguiente:

1.  **Funcionalidad disponible** en Necor@. Quiere decir que se dispone
    de pantalla en Necor@ y únicamente habría que migrar los programas
    COBOL subyacentes a procedimientos almacenados SQL Server.

2.  **Funcionalidad <u>NO</u> disponible** en Necor@. Esto quiere decir
    que habría que desarrollar la funcionalidad desde el principio. Se
    deberá crear una pantalla o pantallas en Necor@ para la interacción
    del usuario, así como migrar los programas COBOL de consulta
    utilizados en 3270 a procedimientos almacenados SQL Server.

En principio se descarta para este estudio las funcionalidades NO
disponibles en Necor@ (segundo punto anterior), ya que supondría un
esfuerzo de desarrollo excesivamente costoso. Por lo tanto a
continuación pasaremos a relacionar las funcionalidades que consideramos
trasladables a Necor@PRYC dentro del primer escenario de funcionalidades
disponibles a día de hoy en Necor@.

### Demandas

| Funcionalidad | Observaciones |
|----|----|
| Consulta de demandas | Consulta general, demandas-líneas, consulta del presupuesto, seguimiento líneas demanda-líneas pedido |
| Ficha de datos generals | Verplano, Datos Entr., Notas, Anexos, Apuntes |
| Revisiones de demandas |  |
| Líneas de demanda | Ver línea detalle, ficha del código demandado/solucionado, últimos proveedores |
| Soluciones de acopio | Ver solución detalle, ver líneas de solución de acopio, ver todos los pedidos, ver datos económicos del pedido, ver datos entrega pedido, ficha del código demandado/solucionado, últimos proveedores |

### Pedidos

| Funcionalidad | Observaciones |
|----|----|
| Buscador de pedidos |  |
| Datos generales | Datos entr., Notas, Anexos, Observaciones |
| Datos g. importes |  |
| Emisiones |  |
| Líneas de pedido | Ficha del código, últimos proveedores, Ver operaciones |
| +Datos económicos |  |
| +Cant. Y Fechas |  |
| Hitos de pago |  |
| Demandas |  |

### Partes de trabajo

| Funcionalidad                 | Observaciones |
|-------------------------------|---------------|
| Buscador de partes de trabajo |               |

### Baseline

| Funcionalidad             | Observaciones |
|---------------------------|---------------|
| Buscador de baseline      |               |
| Datos generals            |               |
| Documetnos de la baseline |               |

### Almacén

| Funcionalidad           | Observaciones |
|-------------------------|---------------|
| Buscador de listas      |               |
| Buscador de depósito    |               |
| Buscador de existencias |               |

### Seguridad industrial

| Funcionalidad                      | Observaciones                        |
|------------------------------------|--------------------------------------|
| Buscador                           | SQL Server. Consultas puntuales DB2. |
| Pases de trabajadores de contratas | SQL Server. Consultas puntuales DB2. |
| Vehículos                          | SQL Server. Consultas puntuales DB2. |

### Logística

| Funcionalidad | Observaciones |
|----|----|
| Marcas funcionales | Consulta general, datos configuración, datos físicos, datos logísticos, notas generales, notas logísticas, datos técnicos, documentos PSA, PSA ampliado, textos del PSA, cabecera del PSA, manuales, gest. Doc., calidad |
| Documentos aprovisionamiento | Consulta general, datos generales PIDA, repuestos, herramientas, notas, manuales técnicos, datos marina, marcas funcionales |
| Documentos mantenimiento | Datos documento mantenimiento, datos pedido, notas, marcas funcionales |
| Manuales técnicos | Consulta general, datos pedido, notas, historial, datos marina, marcas funcionales |
| Docs. Técnicos suministrador | Consulta general, documentos técnicos suministrador, marcas funcionales |

