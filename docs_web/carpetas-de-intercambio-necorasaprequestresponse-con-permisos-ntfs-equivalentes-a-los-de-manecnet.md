<!--
---
source: EstadoActualPlataformaBBD_V27_3_42.md
doc_source: EstadoActualPlataformaBBD_V27_3_42.docx
inserted: 2025-06-19T08:07:59.874907
---
-->

<div class="fragment-meta">source: EstadoActualPlataformaBBD_V27_3_42.md | doc: EstadoActualPlataformaBBD_V27_3_42.docx | inserted: 2025-06-19T08:07:59.874907</div>

# Carpetas de intercambio NecoraSAP/Request/|Response con permisos NTFS equivalentes a los de MANECNET.

## Cliente SQL Native 11 para conectividad con MASQL20171/HOSTDB2 .

- Agente de monitorización Centreon (plantilla *IIS 10*).

- Repositorio de archivos de ingeniería y producción.

Este servidor concentra ahora los flujos M-AT (*SetInfoMateriales*) y
Login, que sincronizan el material maestro entre SAP y la base **V6**.
Su consolidación elimina dependencias de hardware obsoleto y simplifica
la matriz del firewall corporativo, mejorando la eficiencia operativa y
la seguridad de las comunicaciones.

.

1.  <span id="_Toc199209679" class="anchor"></span>Flujos de carga y
    extracción

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

El modelo de datos actual se caracteriza por su arquitectura **modular,
desacoplada y orientada al cliente**. Esta estructura permite la
existencia de instancias dedicadas por función, país o sistema fuente,
lo que garantiza una trazabilidad completa desde el origen en SAP hasta
la entrega final en Necor@. Esta orientación modular no solo facilita la
gestión y el mantenimiento del sistema, sino que también asegura que las
necesidades específicas de cada cliente y región sean atendidas de
manera eficiente y efectiva.

3.  <span id="_Toc199209680" class="anchor"></span>Detalle técnico por
    servidor/instancia

    1.  <span id="_Toc199209681"
        class="anchor"></span>MASQL20171/HOSTDB2

La instancia MASQL20171/HOSTDB2 funciona como el **nodo central de
consolidación** tras el apagado del entorno HOST (DB2/VSAM).
Implementada sobre SQL Server 2017 CU31, concentra todas las bases de
datos migradas desde el ecosistema mainframe, así como los esquemas
técnicos heredados de instancias auxiliares como FESRV014 y MAHOST.

1.  <span id="_Toc199209682" class="anchor"></span>Características
    generales

- **Rol:** Nodo central de consolidación tras el apagado del entorno
  HOST (DB2/VSAM)  
  **Versión:** SQL Server 2017 CU31.  
  **Bases de datos:** V6, V6_2, DB2T, DB2P  
  **Conexiones entrantes:**

- MASERVF9 (vía ODBC desde IIS/WebService)

- MASQL20142/NECORANET (lectura cruzada)

- Objeto PDB (consulta y consolidación de datos)

- **Conexiones salientes:** Réplicas parciales y flujos ETL hacia
  NecoraNet, SQLTURK y SQLNORWAY.  
  **Parámetros relevantes:**

- Puerto TCP fijo 58898 (asignado en nov. 2024, validado por
  Ciberseguridad)

- Compresión de datos tipo ROW

- Collation: SQL_Latin1_General_CP1_CI_AS

- **Cambios recientes:** Generación de la copia V6_2.

Esta instancia proporciona datos operativos y documentales a múltiples
servicios de negocio, incluyendo SAP, Necor@NET y reporting externo. Los
procesos de carga, validación e indexado están diseñados para garantizar
estabilidad, trazabilidad y rendimiento.

MASQL20171/HOSTDB2 almacena la información consolidada desde tres
orígenes principales:

| **Origen** | **Destino en SQL Server** | **Descripción** |
|:---|:---|:---|
| HOST DB2 | DB2T / DB2P | Copia exacta de tablas fuente dentro del alcance. Carga vía paquete MoveDataDB2ToSQLServer. |
| FESRV014 | HOSTDB2 (diversos esquemas) | Bases de datos ControlDoc, ControlAsuntos, etc. Job: MoveAppAuxToNewNecor@. |
| MAHOST | HOSTDB2.DB2T (esquema a esquema) | Bases DBFERR, DBCART, DBMADR, DBSFER. Job: PackageMAHOST_a_DB2T.dtsx. |

1.  <span id="_Toc199209684" class="anchor"></span>V6 y creación de V6_2

La base de datos V6 contiene los datos de **Necor@V6** tras la
migración. Durante el proceso, se detectó que algunas vistas aplicaban
filtros que impedían consultar el histórico completo desde Necor@. Para
solucionarlo:

- Se creó la base V6_2, réplica exacta de V6 sin filtros de migración.

- Se generaron nuevas vistas /_V sobre V6_2.

- Se reemplazaron los sinónimos en V6 para que apunten a estas vistas no
  filtradas.

- Las vistas originales se renombraron como /_BKP para permitir
  comparativas de rendimiento.

Esta estrategia permite que **Necor@V6 acceda al histórico completo sin
afectar al código existente**, manteniendo la trazabilidad y cumpliendo
requerimientos funcionales de Ingeniería y Auditoría.

.

1.  <span id="_Toc199209685" class="anchor"></span>Antecedentes del
    proyecto HOST

El proyecto HOST se concibió como una iniciativa de migración y
mantenimiento de los sistemas legacy (DB2/VSAM), gestionándose bajo un
modelo mixto que combina soporte y transferencia de conocimiento. En
colaboración con Altia Consultores, se llevaron a cabo tareas de
mantenimiento correctivo y adaptativo, así como procesos de migración
escalonada.

Esta colaboración se alineó con las prácticas ITIL y los estándares
ISO/IEC 20000, estableciendo una infraestructura de servicio que incluyó
indicadores de calidad (SLA), herramientas de gestión, dedicación de
recursos y mecanismos de seguimiento tanto semanal como mensual. Además,
se garantizó una cobertura integral sobre aplicaciones críticas (Necora,
Coral, ControlDoc, Brion, entre otras) mediante soporte de tercer nivel
y supervisión de procesos en explotación.

El acuerdo contemplaba una planificación detallada de proyectos,
atención 24x7 para casos críticos y controles de calidad periódicos. Se
documentaron procedimientos para el análisis y resolución de incidentes,
gestión de problemas y planificación de desarrollos, lo que permitió
asegurar la continuidad del servicio durante la migración al entorno SQL
Server (MASQL20171/HOSTDB2) sin pérdida de operatividad.

El proyecto de migración HOST se inició el **12 de septiembre de 2019**
y se estructuró en dos fases:

- **Fase I – Migración técnica:** de septiembre de 2019 a julio de 2020.

- **Fase II – Soporte y cierre definitivo:** de julio a diciembre de
  2020.

