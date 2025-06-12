# Análisis Funcional: Necor@V6 - Órdenes de Trabajo

Informe consolidado de la interfaz de Necor@V6, describiendo las
columnas del grid principal, los campos del formulario de detalles y las
funcionalidades asociadas a las distintas botoneras y pestañas.

## Pantalla Principal: Grilla de Órdenes de Trabajo

1.  Columnas visibles en la grilla:

- Orden (ID OT)

- PDF (icono)

- Descripción

- Revisión

- Tipo

- Tarea

- Situación P/A

- Grupo Cote

- Estado

- Centro Emisor

- Centro Ejecutor

- Plano Origen

- Actividad

- Partida

- Precio Objetivo

- AV. Plan (%)

- Grado de Definición (%)

- H.E. Previstas

- H.E. Lanzadas

- H.E. Consumidas

## Formulario de Detalles (Datos Generales)

2.  Campos en el formulario de Detalles:

- Establecimiento

- Obra

- Centro Emisor / Centro Ejecutor

- Tipo Orden

- Tarea

- Sección

- Grupo Cote

- Zona / Bloque / Módulo

- Prod. Intermedio

- Descripción Corta / Larga

- Situación P/A (Aprobada, Realizada, Lanzada)

- I.P.A. (checkbox)

- Materiales (checkbox)

- Horas Presup. / Reales / H.E. Previstas / H.E. Lanzadas / H.E.
  Consumidas / H.E. Imputadas

- Avance (%)

- Grado de Definición (%)

- Últimas revisiones (Lanzada / Aprobada / Configuración)

- Aviso de Revisión Pendiente

- Cuenta / Partida de cargo

- Av. Tasa (%) / Av. Pint (%)

- Moneda / Usuario Creador / Fecha de Creación / Responsable / Fecha
  Límite / Estado / Observaciones

## Pestaña Revisiones

3.  Campos y checkboxes en Revisiones:

- I.P.A. (checkbox)

- Situación P/A: Producción (checkbox), Configuración (checkbox)

- Materiales (checkbox)

- Horas Presupuestadas

- H.E. Previstas / H.E. Lanzadas / H.E. Consumidas / H.E. Imputadas

- Av. Tasa (%)

- Av. Pint (%)

- Situación Serv. (checkbox)

- Tipo Avance (checkbox)

- Aviso de Revisión Pendiente

- Cuenta / Partida de cargo

- Botones: Nuevo, Modificar, Plano Origen, Imprimir

## Pestaña Lista de Materiales

4.  Descripción:

- La pestaña "Lista de Materiales" está disponible junto a otras
  pestañas, sin mostrar campos adicionales en esta vista.

## Pestaña Referencias

5.  Campos del modal Referencias:

- Obra

- Orden de Trabajo

- PDF

- G.D.

- Descripción Larga

- FA/CRA

- GDC

- Bloque

- Módulo

- Zona

- Sit

- GIN

- SitPA

- U.R. Realiz.

- U.RevisPA

- FFPressFin

- FPenvProd

- Botones: Buscar, Limpiar, Imprimir, Salir

## Menú Contextual de Acciones Avanzadas

6.  Opciones del menú contextual:

- Cambio de Situación Masiva

- Cambio de Situación a Producción

- Cambio de Tipo de Avance

- Duplicar Órdenes

- Envío a SAP

- Crear Órdenes desde Planos (Cabecera y Componentes)

- Alta Productos/Entregar

## Pestaña Operaciones

7.  Campos en Operaciones:

- Orden

- Línea

- Descripción

- Revisión

- Clave Valoración

- Encargado

- Avance Proveedor

- Usuario Avance

- Fecha Último Avance

- Demanda

- Línea Demanda

- Botones: Mantenimiento, Ponderar Opera, Utilidades

## Pestaña Reporte y Presupuesto

8.  Campos en Reporte:

- Cargo

- Partida

- Presupuesto

- Presup Cargo

- Presup Partida

- Control Agrupación (Por Agrupación / Por Partida)

- Fecha Reparto

- Checkboxes: Presupuesto, Grado Definición, Órdenes bloqueadas en
  Borrador, Reparto sin Bloquear

- Botones rápidos: F7 Carga OOTT, F10 Importa OOTT, F9 Liberar
  Presupuesto

## Checklist Consolidado de Funcionalidades

| Funcionalidad             | Descripción breve                            |
|---------------------------|----------------------------------------------|
| Visualizar listado de OTs | Grilla con filtros y ordenamiento            |
| Crear OT                  | Formulario nuevo con campos obligatorios     |
| Modificar OT              | Campo Detalle y Consolidación editables      |
| Eliminar OT               | Eliminar/logical desde detalle               |
| Consolidar horas/importes | Campos de horas e importes                   |
| Cambio de Estado          | Checkboxes para fases                        |
| Exportar/Imprimir OT      | Botón Imprimir orden                         |
| Carga Masiva              | Importar múltiples OTs                       |
| Revisiones                | Pestaña con campos de avance y checkboxes    |
| Lista de Materiales       | Pestaña presente sin campos adicionales      |
| Referencias               | Listado de documentos técnicos referenciados |
| Acciones Avanzadas        | Menú contextual con duplicar, SAP, planos    |
| Operaciones               | Pestaña con listado de operaciones y campos  |
| Reporte / Presupuesto     | Pestaña con presupuesto y controles          |
