<!--
---
source: EstadoActualPlataformaBBD_V27_3_42.md
doc_source: EstadoActualPlataformaBBD_V27_3_42.docx
inserted: 2025-06-18T23:14:04.862970
---
-->

<div class="fragment-meta">source: EstadoActualPlataformaBBD_V27_3_42.md | doc: EstadoActualPlataformaBBD_V27_3_42.docx | inserted: 2025-06-18T23:14:04.862970</div>

# ÍNDICE

[1. Objeto del documento [5](#_Toc199209672)](#_Toc199209672)

[2. Descripción del sistema actual [6](#_Toc199209673)](#_Toc199209673)

[2.1. Núcleo HOSTDB2 (MASQL20171/HOSTDB2)
[7](#_Toc199209674)](#_Toc199209674)

[2.2. Plataforma Necor@ clásica (MASQL20142/SQL20142)
[7](#_Toc199209675)](#_Toc199209675)

[2.3. Plataforma Necor@ extendida (MASQL20142/NECORANET)
[7](#_Toc199209676)](#_Toc199209676)

[2.4. Clientes internacionales (SQL Server 2022)
[8](#_Toc199209677)](#_Toc199209677)

[2.5. Servicios intermedios (MASERVF9)
[8](#_Toc199209678)](#_Toc199209678)

[2.6. Flujos de carga y extracción [9](#_Toc199209679)](#_Toc199209679)

[3. Detalle técnico por servidor/instancia
[10](#_Toc199209680)](#_Toc199209680)

[3.1. MASQL20171/HOSTDB2 [10](#_Toc199209681)](#_Toc199209681)

[3.1.1. Características generales [10](#_Toc199209682)](#_Toc199209682)

[3.1.2. Contenido migrado [11](#_Toc199209683)](#_Toc199209683)

[3.1.3. V6 y creación de V6_2 [11](#_Toc199209684)](#_Toc199209684)

[3.1.4. Antecedentes del proyecto HOST
[12](#_Toc199209685)](#_Toc199209685)

[3.1.5. Interfaces SSIS en entorno HOST consolidado (AWD/ALHD)
[14](#_Toc199209686)](#_Toc199209686)

[(a) Funciones de los Paquetes SSIS
[14](#funciones-de-los-paquetes-ssis)](#funciones-de-los-paquetes-ssis)

[(b) Características Técnicas
[14](#características-técnicas)](#características-técnicas)

[3.2. MASQL20142/SQL20142 – (MASQL20222)
[15](#_Toc199209689)](#_Toc199209689)

[3.2.1. Características generales [15](#_Toc199209690)](#_Toc199209690)

[3.2.2. Contexto y dependencias [15](#_Toc199209691)](#_Toc199209691)

[3.3. MASQL20142/NECORANET – (MASQL20222)
[17](#_Toc198809881)](#_Toc198809881)

[3.3.1. Características generales [17](#_Toc199209693)](#_Toc199209693)

[3.3.2. Contexto y dependencias [17](#_Toc199209694)](#_Toc199209694)

[3.4. MASQL20221/SQLTURK [19](#_Toc198809882)](#_Toc198809882)

[3.4.1. Características generales [19](#_Toc199209696)](#_Toc199209696)

[3.4.2. Contexto y dependencias [19](#_Toc199209697)](#_Toc199209697)

[3.5. MASQL20221/SQLNORWAY [20](#_Toc198809883)](#_Toc198809883)

[3.5.1. Características generales [20](#_Toc199209699)](#_Toc199209699)

[3.5.2. Contexto y dependencias [20](#_Toc199209700)](#_Toc199209700)

[3.6. MASERVF9 – (Antiguo MANECNET)
[22](#_Toc199209701)](#_Toc199209701)

[3.6.1. Características generales [22](#_Toc199209702)](#_Toc199209702)

[3.6.2. Funciones y contexto [23](#_Toc199209703)](#_Toc199209703)

[3.6.3. Cronología de migración y normalización
[23](#_Toc199209704)](#_Toc199209704)

[3.6.4. Incidencias y acciones correctivas principales
[23](#_Toc199209705)](#_Toc199209705)

[3.6.5. Lecciones aprendidas y recomendaciones
[24](#_Toc199209706)](#_Toc199209706)

[4. Arquitectura funcional del flujo F100
[25](#_Toc199209707)](#_Toc199209707)

[4.1. Origen de datos [26](#_Toc199209708)](#_Toc199209708)

[4.2. Interfaces de carga principales
[26](#_Toc199209709)](#_Toc199209709)

[4.3. Reglas de negocio y transformación
[27](#_Toc199209710)](#_Toc199209710)

[4.4. Consolidación y publicación de datos
[27](#_Toc199209711)](#_Toc199209711)

[4.4.1. Integración ampliada del modelo funcional – Foran /<-/>
Windchill /<-/> SAP [28](#_Toc199209712)](#_Toc199209712)

[4.5. Validación de calidad y revisión
[29](#_Toc199209713)](#_Toc199209713)

[4.6. Escenarios operativos [29](#_Toc199209714)](#_Toc199209714)

[4.7. Supervisión operativa y alertado
[30](#_Toc199209715)](#_Toc199209715)

[4.8. Consideraciones de mejora [30](#_Toc199209716)](#_Toc199209716)

[5. Calidad y riesgos actuales [31](#_Toc199209717)](#_Toc199209717)

[6. Próximos pasos recomendados [31](#_Toc199209718)](#_Toc199209718)

[7. Referencias internas y fuentes consultadas
[33](#_Toc199209719)](#_Toc199209719)

[**I.** Instancia: MASQL20142/NECORANET
[35](#instancia-masql20142necoranet)](#instancia-masql20142necoranet)

[**II.** Instancia: MASQL20142/SQL20142
[36](#instancia-masql20142sql20142)](#instancia-masql20142sql20142)

[**III.** Instancia: MASQL20171/HOSTDB2
[37](#instancia-masql20171hostdb2)](#instancia-masql20171hostdb2)

[**I.** Instancia: MASQL20171/HOSTDB2
[39](#instancia-masql20171hostdb2-1)](#instancia-masql20171hostdb2-1)

[**II.** Instancia: MASQL20142/NECORANET
[41](#instancia-masql20142necoranet-1)](#instancia-masql20142necoranet-1)

[**III.** Instancia: MASQL20221/SQLNORWAY
[42](#instancia-masql20221sqlnorway)](#instancia-masql20221sqlnorway)

[**IV.** Instancia: MASQL20221/SQLTURK
[42](#instancia-masql20221sqlturk)](#instancia-masql20221sqlturk)

1.  <span id="_Toc199209672" class="anchor"></span>Objeto del documento

El presente documento tiene como objetivo describir el estado
tecnológico actual de la plataforma de bases de datos de Navantia. Esto
incluye un análisis detallado de componentes clave como NecoraNet, PRYC,
las instancias de SQL Server 2017-2022, los servicios IIS (MASERVF9) y
sus integraciones con SAP. Para ello, se llevará a cabo un inventario
exhaustivo que abarque servidores, instancias, bases de datos, enlaces y
flujos ETL.

La información recopilada se consolidará a partir de actas de proyecto,
tickets GLPI y seguimientos de dedicación hasta mayo de 2025,
proporcionando así una visión única, trazable y homologada que será de
utilidad para los equipos de DBA y la auditoría interna.

El resultado de este análisis servirá como línea base para el soporte
operativo diario y para la planificación de futuras optimizaciones o
migraciones, incluyendo Azure SQL MI, RISE with SAP, nuevos flujos ETL,
así como la migración progresiva a SQL Server 2022 y versiones
posteriores.

