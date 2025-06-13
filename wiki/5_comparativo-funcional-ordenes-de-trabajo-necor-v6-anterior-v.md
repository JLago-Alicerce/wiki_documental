---
source: tmp_full.md
doc_source: 20221115_TraspasoConocimientos.docx
created: 2025-06-12T15:50:41.268772
---
# Comparativo Funcional: Órdenes de Trabajo (Necor@V6 Anterior vs. Nueva Aplicación)

Fecha de creación: \[DD/MM/AAAA\]

Versión: 1.1

Autores y Responsables: José Lago – Coordinación de Proyecto

Objetivo General: Definir las diferencias funcionales entre Necor@V6
(VB6) y la nueva plataforma, corrigiendo detalles detectados en la
revisión.

## Índice

1.  1\. Introducción

2.  2\. Metodología de Comparación

3.  3\. Descripción Funcional por Módulos

4.  3.1. Pantalla Principal / Grilla de Órdenes

5.  3.2. Formulario “Detalle” (Datos Generales)

6.  3.3. Pestaña “Consolidación” (Horas e Importes)

7.  3.4. Cambio de Estado (Flujo de Estados)

8.  3.5. Extracción de Informe / Exportación (PDF/Excel)

9.  3.6. Pestaña “Revisiones”

10. 3.7. Pestaña “Lista de Materiales”

11. 3.8. Pestaña “Referencias”

12. 3.9. Menú Contextual de Acciones Avanzadas

13. 3.10. Pestaña “Operaciones” y Consultas Relacionadas

14. 3.11. Pestaña “Reporte” y Gestión de Presupuesto

15. 3.12. Carga Masiva de Órdenes

16. 4\. Resumen de Brechas y Pendientes de Migración

17. 5\. Plan de Acción y Próximos Pasos

18. 6\. Anexos

## 1. Introducción

Contexto del Proyecto: La empresa migra la gestión de Órdenes de Trabajo
desde Necor@V6 (VB6) a la nueva plataforma consolidada.

Alcance del Documento: Contrastar funcionalidad de Necor@V6 con la nueva
aplicación, identificando brechas y validando migración completa.

Fuentes de Información: Análisis Funcional Necor@V6 y Análisis Funcional
NuevaApp. Revisión de vídeos y capturas de pantalla. Objetivo: Validar
presencia de todas las funcionalidades principales a nivel de negocio.

## 2. Metodología de Comparación

1\. Identificación de Módulos y Funcionalidades Clave: Basado en
estructura de ambas aplicaciones.

2\. Estructura de la Tabla de Comparación:

\- Funcionalidad / Campo

\- Descripción en Necor@V6 (App Anterior)

\- Descripción en la Nueva Aplicación

\- Estado de Migración (Migrado / Pendiente / Nuevo)

\- Observaciones / Comentarios

3\. Proceso de Revisión: Reunión con áreas de Desarrollo, QA y Negocio
para validar cada ítem.

## 3. Descripción Funcional por Módulos

### 3.1. Pantalla Principal / Grilla de Órdenes

| Funcionalidad / Campo | Necor@V6 (App Anterior) | Nueva Aplicación | Estado de Migración | Observaciones |
|----|----|----|----|----|
| Columnas de la grilla | Orden (ID OT), PDF (icono), Descripción, Revisión, Tipo, Tarea, Situación P/A, Grupo Cote, Estado, Centro Emisor, Centro Ejecutor, Plano L/M, Actividad, Partida, Precio Objetivo, % AV Plan, Grado de Definición, H.E. Previstas, H.E. Lanzadas, H.E. Consumidas | Orden, PDF, Descripción, Revisión, Tipo, Tarea, Situación P/A, Grupo Cote, Estado, Centro Emisor, Centro Ejecutor, Plano Origen, Actividad, Partida, Precio Objetivo, % AV Plan, Grado de Definición, H.E. Previstas, H.E. Lanzadas, H.E. Consumidas | Migrado | Se mantiene totalidad de columnas; se validó que “Plano Origen” renombrado como Plano L/M. |
| Filtrado / Búsqueda Rápida | Filtro por “Situación P/A”, barra de búsqueda por Descripción y Partida | Filtro por “Situación P/A”, “Revisión”, buscador por Descripción, Estado, Grupo | Migrado | Nuevo filtro por Revisión agregado. |
| Ordenamiento de Columnas | Reordenable por ID OT, Tipo, Obra | Reordenable por todos los encabezados, agrupar por Centros Emisor/Ejecutor | Migrado | Se agregó función de agrupación por Centros. |

### 3.2. Formulario “Detalle” (Datos Generales)

| Funcionalidad / Campo | Necor@V6 (App Anterior) | Nueva Aplicación | Estado de Migración | Observaciones |
|----|----|----|----|----|
| Establecimiento | Desplegable “Establecimiento” (ej. “2 – ASTILLERO FERROL”) | No aplica (se ingresa automáticamente desde usuario) | Migrado | Campo removido en UI; se asume contexto del usuario. |
| Obra | Desplegable “Obra” (ej. “0212 – F105”) | Mismo desplegable con vínculo a proyecto | Migrado |  |
| Centro Emisor / Centro Ejecutor | Campos separados con valores numéricos | Combina y autocompleta según Grupo Cote | Migrado | Validar consistencia de datos en migración. |
| Tipo Orden | Desplegable con códigos (B, G, etc.) | Desplegable con opciones ampliadas según perfil | Migrado | Confirmar que todos los valores históricos estén presentes. |
| Tarea | Desplegable / automática según plantilla | Asignación dinámica basada en Grupo Cote | Migrado |  |
| Sección / Grupo Cote | Campos editables manualmente | Autocompletan la descripción de Grupo Cote | Migrado |  |
| Zona / Bloque / Módulo | Tres desplegables independientes | Autocompletar “Zona” al seleccionar “Bloque” | Migrado |  |
| Prod. Intermedio | Selección múltiple (“TUB”) | Selección múltiple con búsqueda interna | Migrado |  |
| Descripción Corta / Larga | Campos de texto libre con mínimo validación | Validación de longitud y autocompletar en largo | Migrado |  |
| Situación P/A | Checkboxes “Aprobada”, “Realizada”, “Lanzada” | Reemplazado por desplegable “Situación P/A” con valores “Producción”, “Configuración”, “Bloqueada” | Migrado | Actualizar procedimientos de flujo de estado. |
| I.P.A. / Materiales | Checkbox I.P.A. y selección de Materiales básico | Checkbox con validación de stock en tiempo real | Migrado |  |
| Horas Presup. / Reales / H.E. Previstas / Lanzadas / Consumidas / Imputadas | Campos numéricos estáticos | Cálculo automático, validación de máximo, desglose en pestaña “Consolidación” | Migrado | Se renombró “Horas Presup.” a “Horas Presup. vs Real”. |
| Avance (%) | Calculado tras consolidar | Actualización en tiempo real al modificar horas | Migrado |  |
| Grado de Definición (%) | Valor numérico simple (“03”) | Tooltip explicativo y validación de rango | Migrado |  |
| Últimas Revisiones (Lanzada / Aprobada / Configuración) | Campos fecha solo lectura | Se registra historial en pestaña “Revisiones” | Migrado |  |
| Aviso de Revisión Pendiente | Señalización manual | Checkbox específico en “Revisiones” | Nuevo | Nuevo módulo “Revisiones”. |
| Cuenta / Partida de cargo | Campo libre o desplegable simple | Desplegable con validación de finanzas | Migrado |  |
| Av. Tasa (%) / Av. Pint (%) | No disponible en formulario principal | Mostrado en “Revisiones” | Migrado |  |
| Moneda | Desplegable básico (EUR, USD) | Integración con cotizaciones diarias | Migrado |  |
| Usuario Creador / Fecha Creación | Solo lectura | Incluye también “Usuario Modificador” y “Fecha Última Modificación” | Migrado |  |
| Responsable | Desplegable usuarios | Validación: no cambio si OT está cerrada | Migrado |  |
| Fecha Límite | Campo fecha sin validación de pasadas | Validación para evitar fechas previas | Migrado |  |
| Estado | Desplegable: BORRADOR, APROBADO, EN CURSO, CERRADO | Reemplazado por “Situación P/A” | Migrado | Verificar mapeo de estados antiguos. |
| Observaciones / Notas Internas | Campo texto libre | Permite adjuntar documentos (PDF, imágenes) | Migrado |  |

### 3.3. Pestaña “Consolidación” (Horas e Importes)

| Funcionalidad / Campo | Necor@V6 (App Anterior) | Nueva Aplicación | Estado de Migración | Observaciones |
|----|----|----|----|----|
| Horas reales imputadas | Actualización estática tras consolidar | Validación automática de máximo según Horas Previstas, calculo en tiempo real | Migrado |  |
| Horas presupuestadas (Objetivo) | Editable en consolidación | Renombrado como “Horas Presup. vs Real”, porcentaje desviación | Migrado |  |
| Importes (Horas Real / Consolidada) | Cálculo básico sobre tarifa recurso | Desglose por Cargo / Partida en pestaña “Reporte” | Migrado |  |
| Avance (actualización) | Porcentaje tras consolidar informe | Actualización en tiempo real tras operación | Migrado |  |
| Consolidación Masiva | Agrupa varias OTs en consolidación | Botón “Carga Masiva” con pre-filtro y validación de plantilla | Migrado |  |

### 3.4. Cambio de Estado (Flujo de Estados)

| Funcionalidad / Campo | Necor@V6 (App Anterior) | Nueva Aplicación | Estado de Migración | Observaciones |
|----|----|----|----|----|
| Botón “Cambio de situación” | Menú desplegable para nuevo estado; actualiza Fecha de Cierre | Desplegable “Situación P/A” permite cambio masivo y bloqueos | Migrado |  |
| Transición “Aprobado” → “En Curso” | Cambio manual desde formulario | Validación: solo Supervisor puede cambiar, restricción de roles | Migrado |  |
| Transición “En Curso” → “Cerrado” | Bloquea horas reales y presupuestarias | Validación de operaciones abiertas, bloqueo automático | Migrado |  |

### 3.5. Extracción de Informe / Exportación (PDF/Excel)

| Funcionalidad / Campo | Necor@V6 (App Anterior) | Nueva Aplicación | Estado de Migración | Observaciones |
|----|----|----|----|----|
| Botón “Generar Informe” | Descarga PDF/Excel resumen horas, estado e importes | Opción “Informe Resumido” o “Detalle”, formato unificado | Migrado |  |
| Reporte Consolidado de Presupuesto | No disponible | Pestaña “Reporte” con desglose Cargo / Partida, filtros y agrupaciones | Nuevo | Requiere formación a usuarios. |

### 3.6. Pestaña “Revisiones”

| Funcionalidad / Campo | Necor@V6 (App Anterior) | Nueva Aplicación | Estado de Migración | Observaciones |
|----|----|----|----|----|
| Pestaña “Revisiones” | No existía módulo específico | Campos I.P.A., Tipo Avance, Avances y checkboxes, historial de revisiones | Nuevo | Validar cumplimiento de auditoría. |

### 3.7. Pestaña “Lista de Materiales”

| Funcionalidad / Campo | Necor@V6 (App Anterior) | Nueva Aplicación | Estado de Migración | Observaciones |
|----|----|----|----|----|
| Pestaña “Lista de Materiales” | No documentada en app anterior | Tab con columnas: Material, Cantidad, Unidad, Ubicación, etc., con búsqueda | Nuevo | Definir columnas exactas. |

### 3.8. Pestaña “Referencias”

| Funcionalidad / Campo | Necor@V6 (App Anterior) | Nueva Aplicación | Estado de Migración | Observaciones |
|----|----|----|----|----|
| Submódulo “Referencias” | Listado básico de documentos técnicos | Modal con columnas: Obra, OT, PDF, G.D., Descripción Larga, FA/CRA, GDC, Bloque, Módulo, Zona, Sit, GIN, SitPA, U.R. Realiz., U.RevisPA, FFPressFin, FPenvProd | Migrado |  |
| Botones: “Buscar”, “Limpiar”, “Imprimir”, “Salir” | No aplica | Disponibles en modal de Referencias | Migrado |  |

### 3.9. Menú Contextual de Acciones Avanzadas

| Funcionalidad / Campo | Necor@V6 (App Anterior) | Nueva Aplicación | Estado de Migración | Observaciones |
|----|----|----|----|----|
| Menú “Acciones Avanzadas” | Cambio de situación masivo básico | Incluye: Cambio de Situación Masiva, Cambio a Producción, Tipo Avance, Duplicar OT, Envío a SAP, Crear desde Planos, Alta Productos/Entregar | Migrado |  |
| “Duplicar Órdenes” | No disponible | Duplica una o varias OTs seleccionadas | Nuevo |  |
| “Envío a SAP” | No disponible | Envía masivo a ERP SAP con validaciones | Nuevo | Coordinar con equipo SAP. |
| “Crear Órdenes desde Planos” | No disponible | Genera OTs a partir de planos cargados | Nuevo | Validar formatos de planos. |

### 3.10. Pestaña “Operaciones” y Consultas

| Funcionalidad / Campo | Necor@V6 (App Anterior) | Nueva Aplicación | Estado de Migración | Observaciones |
|----|----|----|----|----|
| Pestaña “Operaciones” | Gestión básica en consolidación | Listado de operaciones con columnas: Orden, Línea, Descripción, Revisión, Clave Valoración, Encargado, Avance Proveedor, Usuario Avance, Fecha Último Avance, Demanda, Línea Demanda | Migrado |  |
| Botones “Mantenimiento”, “Ponderar Opera”, “Utilidades” | No aplicable | Disponibles para editar y calcular datos de línea | Migrado |  |
| Consultas Complementarias | No disponible | Modal: Lista Materiales, Productos a Entregar, Errores Avance Automático | Migrado | Validar roles y permisos. |

### 3.11. Pestaña “Reporte” y Gestión de Presupuesto

| Funcionalidad / Campo | Necor@V6 (App Anterior) | Nueva Aplicación | Estado de Migración | Observaciones |
|----|----|----|----|----|
| Pestaña “Reporte” | No disponible | Tab con columnas: Cargo, Partida, Presupuesto, Presup Cargo, Presup Partida, Control Agrupación (Por Agrupación / Por Partida), Fecha Reparto | Nuevo |  |
| Menu “Consulta de Presupuesto” | No disponible | Modal con listado de partidas y agrupaciones | Nuevo |  |
| Checkboxes y Filtros | No disponible | Filtros: Presupuesto, Grado Definición, Órdenes bloqueadas, Reparto sin Bloquear | Nuevo |  |
| Botones rápidos: F7, F10, F9 | No disponible | F7 Carga OOTT, F10 Importa OOTT, F9 Liberar Presupuesto | Nuevo |  |

### 3.12. Carga Masiva de Órdenes

| Funcionalidad / Campo | Necor@V6 (App Anterior) | Nueva Aplicación | Estado de Migración | Observaciones |
|----|----|----|----|----|
| Carga Masiva de OTs | Consolidación masiva básica | Carga de archivos Excel/CSV con validación al vuelo | Migrado | Definir guía de plantilla. |

## 4. Resumen de Brechas y Pendientes de Migración

- Verificar mapeo de estados “Situación” vs “Situación P/A”.

- Validar campos de “Revisiones” conforme a auditoría.

- Definir columnas exactas en “Lista de Materiales”.

- Probar integración “Envío a SAP” y coordinar con ERP.

- Validar mapeo “Cargo”/“Partida” en reporte.

- Documentar y validar plantilla de “Carga Masiva”.

- Planificar formación de nuevos módulos.

## 5. Plan de Acción y Próximos Pasos

19. Asignar responsables a cada brecha con fechas límite.

20. Programar pruebas de validación de cada módulo.

21. Actualizar documentación de usuario y guías.

22. Revisar con área SAP las pruebas de envío masivo.

23. Realizar sesión de formación para usuarios finales.

24. Agendar reunión de cierre de brechas.

## 6. Anexos

1\. Capturas Principales: Se incluyen en documento de diapositiva A3.

2\. Glosario de Términos: OT, I.P.A., Cargo, Partida.

3\. Tabla Maestra de Campos: En hoja de cálculo adjunta.


ÍNDICE

