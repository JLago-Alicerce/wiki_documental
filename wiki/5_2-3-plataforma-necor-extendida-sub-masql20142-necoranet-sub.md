---
source: EstadoActualPlataformaBBD_V0306_10_32.md
doc_source: EstadoActualPlataformaBBD_V0306_10_32.docx
created: 2025-06-14T03:51:20.847015+00:00
---
<div class="fragment-meta">source: EstadoActualPlataformaBBD_V0306_10_32.md | doc: EstadoActualPlataformaBBD_V0306_10_32.docx | created: 2025-06-14T03:51:20.847015+00:00</div>

# **2.3. Plataforma Necor@ extendida (<sub>MASQL20142/NECORANET</sub>)**

Este entorno funcional de AWD incluye bases de datos como
**NecoraDocAWD**, **InterfacesAWD_PEC**,

**Necor@AWD** y **NAI_InterfacesAWD**. Además, incorpora el servidor de
informes

**REPORTSERVERSNECORANET**, que explota datos de todas las bases
anteriores e integra herramientas como Power BI y otras soluciones
internas. Desde esta instancia, se consolidan datos provenientes de
otras instancias a través del objeto **PDB**, que actúa como origen
común para clientes satélites y operaciones cruzadas, optimizando la
gestión y análisis de datos.

### 2.4. Clientes internacionales (SQL Server 2022)

Las instancias **MASQL20221/SQLTURK** y **MASQL20221/SQLNORWAY** están
diseñadas específicamente para los contratos de Turquía y Noruega,
respectivamente, y albergan la base de datos **Necor@AWD**. Ambas
instancias consumen datos del objeto **PDB** y cuentan con procesos ETL
para la replicación, validación y extracción específica por proyecto.
Cada una de estas instancias opera de manera sincronizada gracias a
enlaces definidos, que incluyen copias de seguridad, servicios ETL y
replicaciones manuales, lo que permite mantener la consistencia y
trazabilidad de los datos. Este diseño modular refleja una arquitectura
evolutiva orientada a clientes distribuidos, aislando entornos según su
uso y país, y asegurando la adaptabilidad a requisitos locales.

### 2.5. Servicios intermedios (MASERVF9)

## El servidor IIS 10, configurado como pasarela de integración entre SAP PO y SQL Server, actúa como intermediario en la comunicación de datos. Expone Web Services REST/SOAP que permiten a SAP consultar datos de materiales y recibir confirmaciones de manera segura. Se comunica directamente con HOSTDB2.V6 a través de ODBC y opera en un puerto fijo (58898), controlado por un firewall y validado por el departamento de Ciberseguridad.

## MASERVF9 es el host Windows Server 2019 (10.100.161.76) que reemplaza al antiguo MANECNET como punto único de integración SOAP entre SAP PO y Necor@. Desde noviembre de 2024, aloja:

## Web Service NecoraWebIntegrator.svc — expuesto en IIS 10, puerto 80.

## Carpetas de intercambio NecoraSAP/Request/|Response con permisos NTFS equivalentes a los de

> MANECNET.

## Cliente SQL Native 11 para conectividad con MASQL20171/HOSTDB2 .

- Agente de monitorización Centreon (plantilla *IIS 10*).  Repositorio
  de archivos de ingeniería y producción.

## Este servidor concentra ahora los flujos M-AT (*SetInfoMateriales*) y Login, que sincronizan el material maestro entre SAP y la base V6 . Su consolidación elimina dependencias de hardware obsoleto y simplifica la matriz del firewall corporativo, mejorando la eficiencia operativa y la seguridad de las comunicaciones.

.

### 2.6. Flujos de carga y extracción

El sistema de bases de datos de Navantia incorpora una serie de
**paquetes SSIS** (SQL Server Integration Services), **planificaciones
de SQL Server Agent** y validaciones CRC (Control de Redundancia
Cíclica) que aseguran la integridad en cada operación de lectura, carga
o replicación de datos. Estos flujos están cuidadosamente definidos
según el país, cliente y uso funcional, abarcando tareas como la
generación de informes, procesos ETL nocturnos y la sincronización de
catálogos.

Cada flujo es auditado mediante registros detallados (logs) y
comprobaciones periódicas, lo que permite una supervisión continua y la
capacidad de identificar y resolver rápidamente cualquier anomalía que
pueda surgir.

## El modelo de datos actual se caracteriza por su arquitectura modular, desacoplada y orientada al cliente . Esta estructura permite la existencia de instancias dedicadas por función, país o sistema fuente, lo que garantiza una trazabilidad completa desde el origen en SAP hasta la entrega final en Necor@. Esta orientación modular no solo facilita la gestión y el mantenimiento del sistema, sino que también asegura que las necesidades específicas de cada cliente y región sean atendidas de manera eficiente y efectiva.

