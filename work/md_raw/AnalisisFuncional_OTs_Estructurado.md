# Análisis Funcional: Necor@V6 - Órdenes de Trabajo

Documento descriptivo de funcionalidades extraídas de 7 vídeos de la
aplicación antigua en VB6 (Necor@V6).

En este informe se listan las columnas del grid principal, los campos
del formulario de detalles y las funcionalidades de las distintas
botoneras para orientar la migración funcional.

## 1. Video 1: Campos y Funcionalidades Básicas

1.  Grid principal: columnas visibles

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

2.  Campos en detalle (al cargar)

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

- Moneda / Usuario Creador / Fecha Creación / Responsable / Fecha Límite
  / Estado / Observaciones

3.  Funcionalidades principales

- Visualizar listado de OTs con filtros y ordenamiento

- Crear OT

- Modificar OT

- Eliminar OT

- Consolidar horas e importes

- Cambio de estado (Aprobada, Realizada, Lanzada)

- Exportar/Imprimir OT

- Carga Masiva

- Consultas adicionales

## 2. Video 2: Pestaña Revisiones

4.  Grid principal: columnas visibles

- Orden (ID OT)

- PDF

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

5.  Campos en detalle (al cargar)

- Añade campos en Revisiones: I.P.A. (checkbox)

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

6.  Funcionalidades principales

- Checkboxes para fases (Producción, Configuración)

- Botones: Nuevo, Modificar, Plano Origen, Imprimir

- Validación modal al no existir datos en Revisiones

## 3. Video 3: Confirmación de pestaña Lista de Materiales

7.  Grid principal: columnas visibles

- Orden (ID OT)

- PDF

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

8.  Campos en detalle (al cargar)

- Pestaña Lista de Materiales presente (sin nuevos campos este vídeo)

9.  Funcionalidades principales

- Acceso visual a pestaña Lista de Materiales

## 4. Video 4: Pestaña Referencias

10. Grid principal: columnas visibles

- Orden (ID OT)

- PDF

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

11. Campos en detalle (al cargar)

- Campos modal Referencias: Obra, OT, PDF, G.D., Descripción Larga,
  FA/CRA, GDC, Bloque, Módulo, Zona, Sit, GIN, SitPA, U.R. Realiz.,
  U.RevisPA, FFPressFin, FPenvProd

12. Funcionalidades principales

- Botones del modal: Buscar, Limpiar, Imprimir, Salir

## 5. Video 5: Menú Contextual de Acciones Avanzadas

13. Grid principal: columnas visibles

- Orden (ID OT)

- PDF

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

14. Campos en detalle (al cargar)

- Menú contextual: Cambio de Situación Masiva, Cambio a Producción,
  Cambio de Tipo de Avance, Duplicar OT, Envío a SAP, Crear OTs desde
  Planos, Alta Productos/Entregar

15. Funcionalidades principales

- Opciones rápidas de gestión: duplicar, integración SAP, generar OTs
  desde planos

## 6. Video 6: Pestaña Operaciones y Consultas

16. Grid principal: columnas visibles

- Orden (ID OT)

- PDF

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

17. Campos en detalle (al cargar)

- Campos en Operaciones: Orden, Línea, Descripción, Revisión, Clave
  Valoración, Encargado, Avance Proveedor, Usuario Avance, Fecha Último
  Avance, Demanda, Línea Demanda

18. Funcionalidades principales

- Consultas: Lista de Materiales, Productos a Entregar, Errores Avance
  Automático

- Botones: Mantenimiento, Ponderar Opera, Utilidades

## 7. Video 7: Pestaña Reporte y Presupuesto

19. Grid principal: columnas visibles

- Orden (ID OT)

- PDF

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

20. Campos en detalle (al cargar)

- Campos en Reporte: Cargo, Partida, Presupuesto, Presup Cargo, Presup
  Partida, Control Agrupación (Por Agrupación/Por Partida), Fecha
  Reparto

- Checkboxes: Presupuesto, Grado Definición, Órdenes bloqueadas en
  Borrador, Reparto sin Bloquear

21. Funcionalidades principales

- Botones rápidos en Reporte: F7 Carga OOTT, F10 Importa OOTT, F9
  Liberar Presupuesto
