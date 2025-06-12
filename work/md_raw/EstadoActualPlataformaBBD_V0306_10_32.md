ÍNDICE

# 1. Objeto del documento 

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

# 2. Descripción del sistema actual 

> <img src="media/image2.jpg" style="width:8.13681in;height:5.02083in" />

La arquitectura actual de bases de datos de Navantia, ilustrada en el
esquema proporcionado, presenta un ecosistema estructurado en instancias
de SQL Server. Estas instancias están distribuidas según su función y
ámbito geográfico, formando agrupaciones que representan entornos
lógicos orientados a servicios específicos, tales como producción,
catálogo, integración y almacenamiento histórico.

Los principales elementos son:

## 2.1. Núcleo HOSTDB2 (<sub>MASQL20171\HOSTDB2</sub>)

Esta instancia alberga las bases de datos **V6**, **V6_2** y **DB2P**,
herederas del entorno z/OS. HOSTDB2 centraliza información histórica
migrada desde el sistema HOST, actuando como fuente para múltiples
réplicas hacia otras instancias. Se alimenta mediante copias de
seguridad y mantiene relaciones directas con bases de datos de catálogo
y explotación, asegurando la integridad y disponibilidad de la
información histórica crítica.

# **2.2. Plataforma Necor@ clásica (<sub>MASQL20142\SQL20142</sub>)**

Esta plataforma agrupa la base de datos **Necor@NC**, utilizada por
aplicaciones legadas como ECADAT y para la integración con **SAP** en la
gestión de hojas de catálogo y materiales. Su función principal es
servir como punto de entrada para datos técnicos (materiales,
ingeniería), que posteriormente se redistribuyen a otras instancias,
facilitando la interoperabilidad y el flujo de información entre
sistemas.

# **2.3. Plataforma Necor@ extendida (<sub>MASQL20142\NECORANET</sub>)**

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

### **2.4. Clientes internacionales (SQL Server 2022)**

Las instancias **MASQL20221\SQLTURK** y **MASQL20221\SQLNORWAY** están
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

### **2.5. Servicios intermedios (MASERVF9)**

## El servidor IIS 10, configurado como pasarela de integración entre SAP PO y SQL Server, actúa como intermediario en la comunicación de datos. Expone **Web Services REST/SOAP** que permiten a SAP consultar datos de materiales y recibir confirmaciones de manera segura. Se comunica directamente con HOSTDB2.V6 a través de ODBC y opera en un puerto fijo (58898), controlado por un firewall y validado por el departamento de Ciberseguridad. 

## MASERVF9 es el host Windows Server 2019 (10.100.161.76) que reemplaza al antiguo **MANECNET** como punto único de integración SOAP entre SAP PO y Necor@. Desde noviembre de 2024, aloja: 

## **Web Service NecoraWebIntegrator.svc** — expuesto en IIS 10, puerto 80.

## Carpetas de intercambio **NecoraSAP\Request\|Response** con permisos NTFS equivalentes a los de 

> MANECNET.

## Cliente SQL Native 11 para conectividad con **MASQL20171\HOSTDB2**.

- Agente de monitorización Centreon (plantilla *IIS 10*).  Repositorio
  de archivos de ingeniería y producción.

## Este servidor concentra ahora los flujos M-AT (*SetInfoMateriales*) y Login, que sincronizan el material maestro entre SAP y la base **V6**. Su consolidación elimina dependencias de hardware obsoleto y simplifica la matriz del firewall corporativo, mejorando la eficiencia operativa y la seguridad de las comunicaciones. 

.

### **2.6. Flujos de carga y extracción**

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

## El modelo de datos actual se caracteriza por su arquitectura **modular, desacoplada y orientada al cliente**. Esta estructura permite la existencia de instancias dedicadas por función, país o sistema fuente, lo que garantiza una trazabilidad completa desde el origen en SAP hasta la entrega final en Necor@. Esta orientación modular no solo facilita la gestión y el mantenimiento del sistema, sino que también asegura que las necesidades específicas de cada cliente y región sean atendidas de manera eficiente y efectiva.

# 3. Detalle técnico por servidor/instancia 

## 3.1. MASQL20171\HOSTDB2

La instancia MASQL20171\HOSTDB2 funciona como el **nodo central de
consolidación** tras el apagado del entorno HOST (DB2/VSAM).
Implementada sobre SQL Server 2017 CU31, concentra todas las bases de
datos migradas desde el ecosistema mainframe, así como los esquemas
técnicos heredados de instancias auxiliares como FESRV014 y MAHOST.

### 3.1.1. Características generales

**Rol:** Nodo central de consolidación tras el apagado del entorno HOST
(DB2/VSAM) **Versión:** SQL Server 2017 CU31.

**Bases de datos:** V6, V6_2, DB2T, DB2P **Conexiones entrantes:**

- MASERVF9 (vía ODBC desde IIS/WebService) o MASQL20142\NECORANET
  (lectura cruzada) o Objeto PDB (consulta y consolidación de datos)

**Conexiones salientes:** Réplicas parciales y flujos ETL hacia
NecoraNet, SQLTURK y SQLNORWAY.

**Parámetros relevantes:**

- Puerto TCP fijo 58898 (asignado en nov. 2024, validado por
  Ciberseguridad) o Compresión de datos tipo ROW

- Collation: SQL_Latin1_General_CP1_CI_AS

**Cambios recientes:** Generación de la copia V6_2.

Esta instancia proporciona datos operativos y documentales a múltiples
servicios de negocio, incluyendo SAP, Necor@NET y reporting externo. Los
procesos de carga, validación e indexado están diseñados para garantizar
estabilidad, trazabilidad y rendimiento.

### 3.1.2. Contenido migrado

MASQL20171\HOSTDB2 almacena la información consolidada desde tres
orígenes principales:

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 31%" />
<col style="width: 56%" />
</colgroup>
<thead>
<tr>
<th style="text-align: center;"><blockquote>
<p><strong>Origen</strong></p>
</blockquote></th>
<th style="text-align: center;"><blockquote>
<p><strong>Destino en SQL Server</strong></p>
</blockquote></th>
<th style="text-align: center;"><blockquote>
<p><strong>Descripción</strong></p>
</blockquote></th>
</tr>
<tr>
<th style="text-align: left;">HOST DB2</th>
<th style="text-align: left;"><blockquote>
<p>DB2T / DB2P</p>
</blockquote></th>
<th style="text-align: left;"><blockquote>
<p>Copia exacta de tablas fuente dentro del alcance. Carga vía paquete
MoveDataDB2ToSQLServer.</p>
</blockquote></th>
</tr>
<tr>
<th style="text-align: left;">FESRV014</th>
<th><blockquote>
<p>HOSTDB2 (diversos esquemas)</p>
</blockquote></th>
<th style="text-align: left;"><blockquote>
<p>Bases de datos ControlDoc, ControlAsuntos, etc. Job:
MoveAppAuxToNewNecor@.</p>
</blockquote></th>
</tr>
<tr>
<th style="text-align: left;">MAHOST</th>
<th style="text-align: left;"><blockquote>
<p>HOSTDB2.DB2T (esquema a esquema)</p>
</blockquote></th>
<th style="text-align: left;"><blockquote>
<p>Bases DBFERR, DBCART, DBMADR, DBSFER. Job:
PackageMAHOST_a_DB2T.dtsx.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### 3.1.3. V6 y creación de V6_2

La base de datos V6 contiene los datos de **Necor@V6** tras la
migración. Durante el proceso, se detectó que algunas vistas aplicaban
filtros que impedían consultar el histórico completo desde Necor@. Para
solucionarlo:

- Se creó la base V6_2, réplica exacta de V6 sin filtros de migración.

- Se generaron nuevas vistas \_V sobre V6_2.

- Se reemplazaron los sinónimos en V6 para que apunten a estas vistas no
  filtradas.

- Las vistas originales se renombraron como \_BKP para permitir
  comparativas de rendimiento.

- Se reforzaron índices en tablas clave (BO12SQ, BO59SQ, BO80SQ, etc.) y
  se revisaron procedimientos (PR_NC_CONSULTA_OPERACIONES, etc.).

Esta estrategia permite que **Necor@V6 acceda al histórico completo sin
afectar al código existente**, manteniendo la trazabilidad y cumpliendo
requerimientos funcionales de Ingeniería y Auditoría.

.

### 3.1.4. Antecedentes del proyecto HOST

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
Server (MASQL20171\HOSTDB2) sin pérdida de operatividad.

El proyecto de migración HOST se inició el **12 de septiembre de 2019**
y se estructuró en dos fases:

- **Fase I – Migración técnica:** de septiembre de 2019 a julio de 2020.

- **Fase II – Soporte y cierre definitivo:** de julio a diciembre de
  2020.

**Objetivos del proyecto:**

- Eliminar el sistema HOST (z/OS + DB2 + VSAM).

- Garantizar la continuidad operativa en Necor@NET y PRYC.

- Mantener los interfaces activos con clientes externos.

- Migrar la información documental y estructural a un entorno soportado
  (SQL Server 2017).

**Logros y aspectos técnicos:**

- Más de **30 tablas y 4 ficheros VSAM** migrados utilizando IBM
  DataUnload.

- Pruebas de carga realizadas en el entorno staging (FESRV053) y New
  PRYC.

- Validación funcional con la obra 7564 (Turbinas) como proyecto piloto.

- Generación de documentación de procesos y reglas de negocio aplicadas
  a interfaces AWD.  Integración de cargas documentales desde
  Windchill.

**Riesgos abordados:**

- No disponibilidad del entorno HOST de desarrollo.

- Falta de programas COBOL (por ejemplo, PE46FV).

- Ausencia de estimación de tamaños de bases de datos debido a retrasos
  con VSAM.

- Problemas de permisos y catálogo con IBM.

- Recursos técnicos limitados (servidores, estaciones de trabajo,
  permisos).

**Participantes clave:**

**Área Personal asignado**

> Migración de datos DB2 Navantia: F. Amor, A. Rodríguez · Altia: J.R.
> Tubío, D. Vega, J. Díaz
>
> Interfaces Externos Navantia: Y. Castiñeira, F. Bordello · Altia:
> mismos Obra de Turbinas Navantia: F. Bordello · Altia: D. Vega

**Fechas clave:**

- Fin de migración técnica: **15 de julio de 2020**.

- Cierre del entorno HOST: **31 de diciembre de 2020**.

- Desactivación de IBM y licencias: **Q4 2020**.

<img src="media/image3.jpg" style="width:6.33819in;height:1.39583in" />

### 3.1.5. Interfaces SSIS en entorno HOST consolidado (AWD/ALHD)

En el marco del proyecto de migración del entorno HOST, se definieron y
desplegaron múltiples paquetes SSIS bajo la codificación
INTERFACES_AWD_ALHD_SSIS. Estos paquetes están orientados a la
integración y consolidación de datos técnicos, documentos y órdenes
asociadas a los sistemas heredados, facilitando la automatización de
tareas críticas.

> **(a) Funciones de los Paquetes SSIS**

Los paquetes SSIS permiten la automatización de las siguientes tareas
críticas:

- **Extracción y limpieza de datos:** Utilizando paquetes como
  \_AtributosConfig.dtsx y \_LimpiarLogs.dtsx, se asegura la integridad
  y calidad de los datos extraídos.

- **Actualización de estados en tablas funcionales:** El paquete
  \_StatusDeleted.dtsx gestiona la actualización de estados, asegurando
  que las tablas reflejen el estado actual de los registros.

- **Consolidación de documentos técnicos:** Paquetes como
  Documentos_tecnicos\_\*.dtsx consolidan documentos técnicos,
  garantizando que toda la información relevante esté centralizada y
  accesible.

- **Gestión documental completa:** Los paquetes
  Gestion_Documental\_\*.dtsx abarcan revisiones, anexos, secciones y
  ficheros, proporcionando una gestión integral de los documentos.

- **Interfaces con MEL y materiales:** Los paquetes MEL_LME\_\*.dtsx
  facilitan la integración con sistemas de materiales, asegurando que
  los datos estén alineados con los requerimientos técnicos.

- **Interfaces con el entorno EEA5:** Paquetes como EEA5.dtsx y
  EEA5_DB2.dtsx permiten la comunicación y sincronización con el entorno
  EEA5, asegurando que los datos sean consistentes y actualizados.

> **(b) Características Técnicas**

Los scripts SSIS incluyen lógica avanzada para:

- **Detección de registros huérfanos:** Identificación y manejo de
  registros que no tienen correspondencia en otras tablas, asegurando la
  integridad referencial.

- **Actualizaciones incrementales:** Implementación de actualizaciones
  que solo afectan a los registros modificados, optimizando el
  rendimiento y reduciendo la carga del sistema.

- **Verificación de consistencia:** Uso de checksum para asegurar que
  los campos clave mantienen su consistencia, evitando discrepancias en
  los datos.

- **Limpieza de registros obsoletos:** Eliminación de registros con
  estado status = 'DELETED', asegurando que la base de datos no acumule
  información innecesaria.

Además, se emplea el objeto UpdateNotice como mecanismo de auditoría de
ejecución para los procesos de carga diarios, proporcionando un registro
detallado de las operaciones realizadas y facilitando el seguimiento y
control de las mismas.

## 3.2. MASQL20142\SQL20142 – (MASQL20222)

Instancia **SQL Server 2014 SP3** que sostiene el núcleo histórico de
*Necor@NC*. Aunque se planificó su retirada junto con el resto de
plataformas *legacy*, continúa en producción porque varios módulos de
ingeniería siguen dependiendo de esquemas y rutinas específicas que aún
no se han portado a versiones superiores.

### 3.2.1. Características generales

**Rol:** Plataforma Necor@NC (entorno legado).

**Versión:** SQL Server 2014 SP3.

**Bases de datos:** Necor@NC.

**Conexiones entrantes:** ECADAT, SAP (vía interfaces HojasCatálogo).

**Conexiones salientes:** HOSTDB2 y NECORANET para consolidación.

**Parámetros relevantes:** Puerto dinámico, sin integración AD,
collation por defecto. **Cambios recientes:** — Información no
disponible.

### 3.2.2. Contexto y dependencias

## La instancia alberga exclusivamente la base de datos Necor@NC, empleada por los módulos de ingeniería y aplicaciones internas como ECADAT. Su integración con SAP se limita a las operaciones de catálogo de materiales mediante HojasCatálogo. Los enlaces externos son reducidos; la transferencia principal se dirige a **NECORANET** para consolidación de datos.

Pese a su carácter legacy, la plataforma continúa operativa mientras
persistan las dependencias funcionales de los módulos de ingeniería. Su
retirada definitiva está condicionada a la migración completa de dichos
esquemas y rutinas a versiones superiores de SQL Server.

## 3.3. MASQL20142\NECORANET – (MASQL20222)

Instancia SQL Server 2017 CU22 que funciona como plataforma funcional
AWD y capa de informes para el ecosistema Necor@AWD. Su diseño soporta
tanto la gestión documental como los flujos técnicos y la explotación de
datos, con un modelo de trabajo dual que facilita la gestión interna y
la distribución internacional de información.

### 3.3.1. Características generales

- **Rol:** Plataforma funcional AWD y capa de informes.

- **Versión:** SQL Server 2017 CU22.

- **Bases de datos:** Necor@AWD, InterfacesAWD_PEC, NAI_InterfacesAWD,
  NecoraDocAWD.

- **Conexiones entrantes:** SQL20142, HOSTDB2, PDB, usuarios BO.

- **Conexiones salientes:** SQLTURK, SQLNORWAY, ReportServer.

- **Parámetros relevantes:** Memoria fija asignada (32 GB), estadísticas
  automáticas activadas, jobs de mantenimiento semanales.

- **Cambios recientes:** o Optimización de vistas y reestructuración de
  Interfaces PEC (junio–julio 2020). o Implantación de auditoría interna
  mediante tabla log \_Audit_Changes. o Normalización de estructuras
  para compatibilidad internacional.

### 3.3.2. Contexto y dependencias

Esta instancia se emplea principalmente para la gestión y explotación
funcional dentro del entorno Necor@AWD, cubriendo diversos ámbitos:
gestión documental (NecoraDocAWD), procesamiento de flujos técnicos
(InterfacesAWD_PEC, NAI_InterfacesAWD) y explotación de datos
(Necor@AWD).

Además, aloja el servidor de informes REPORTSERVERSNECORANET, que
facilita la publicación de dashboards y consultas externas. También
integra el objeto PDB, que centraliza y consolida información de
múltiples fuentes para su distribución a instancias internacionales.

El modelo operativo se basa en una dualidad entre la gestión interna de
datos y la preparación de flujos estructurados hacia entornos remotos
(SQLTURK y SQLNORWAY), a través del objeto PDB que actúa como puente
lógico. Este diseño asegura la coherencia estructural y minimiza el
acoplamiento entre esquemas, facilitando la interoperabilidad con
clientes internacionales.

En 2020 se llevó a cabo un proceso de optimización orientado a mejorar
el rendimiento, reorganizando vistas y creando sinónimos funcionales.
Asimismo, se implementó un sistema de auditoría a nivel de registros
para reforzar la trazabilidad.

- **InterfacesAWD_PEC:** Utilizada como puente para el traspaso de
  información entre sistemas.

- **NAI_InterfacesAWD:** Base de datos intermedia que centraliza datos
  de origen para su derivación hacia instancias externas.

## 3.4. MASQL20221\SQLTURK 

Instancia SQL Server 2022 CU8 dedicada a la gestión de contratos
específicos para Turquía, operando de forma autónoma dentro del
ecosistema Necor@AWD para garantizar segregación funcional y geográfica.

### 3.4.1. Características generales

- **Rol:** Instancia internacional dedicada a contratos Turquía.

- **Versión:** SQL Server 2022 CU8.

- **Bases de datos:** Necor@AWD.

- **Conexiones entrantes:** Réplicas desde PDB (NECORANET).

- **Conexiones salientes:** Flujos ETL hacia cliente, reporting
  específico.

- **Parámetros relevantes:** Compresión de columnas, alertas
  personalizadas SQL Agent.

- **Cambios recientes:** o Despliegue inicial y validación funcional
  completada (2025Q1). o Implementación de ETL segregado por región. o
  Control de errores y lógica de CRC en flujos nocturnos.

### 3.4.2. Contexto y dependencias

Esta instancia está destinada exclusivamente a la gestión y explotación
de datos relacionados con contratos de Turquía, integrando su propia
copia de Necor@AWD para operar con independencia y garantizar la
seguridad y el aislamiento requerido.

La alimentación de datos se realiza mediante flujos ETL diarios que
replican información desde el objeto PDB alojado en NECORANET. Los
procesos incorporan validaciones de integridad basadas en CRC (Control
de Redundancia Cíclica), junto con mecanismos personalizados de
trazabilidad y notificación para la detección y gestión de errores.

El diseño de esta instancia persigue asegurar la segregación funcional y
geográfica, respondiendo a los requerimientos contractuales en materia
de aislamiento de datos, soporte técnico y control de accesos.

Actualmente, la base de datos que alimenta el PDB de Turquía está en
fase de migración, con vistas al apagado progresivo de la instancia
legacy MASQL2014\SQLTURK.

## 3.5. MASQL20221\SQLNORWAY

Instancia SQL Server 2022 CU8 orientada a la gestión y soporte de
proyectos en Noruega, diseñada para operar con independencia mediante
réplicas desde el PDB general.

### 3.5.1. Características generales

- **Rol:** Instancia internacional para proyectos Noruega.

- **Versión:** SQL Server 2022 CU8.

- **Bases de datos:** Necor@AWD.

- **Conexiones entrantes:** Réplicas desde PDB.

- **Conexiones salientes:** Power BI Service, validación en Azure VDI.

- **Parámetros relevantes:** Configuración híbrida con prevalidación CRC
  y staging.

- **Cambios recientes:**

  - Flujo ETL activo desde abril 2024, con carga de 2.1 millones de
    registros en 35 minutos.

  - Estrategia de validación cruzada de claves y agrupadores desde
    Coral. o Consola de trazabilidad de cargas entregada a
    Reporting/Navantia en mayo 2025.

### 3.5.2. Contexto y dependencias

Esta instancia, basada en SQL Server 2022, da soporte a proyectos
desplegados en Noruega y contiene su propia versión de Necor@AWD.
Replica los datos de forma independiente desde el PDB general,
asegurando autonomía y seguridad en la gestión de información.

El flujo ETL, pionero en validación completa, incorpora trazabilidad
end-to-end desde las fuentes Coral hasta la explotación en Power BI,
pasando por etapas de staging, validación y carga incremental.

Los procesos diarios están optimizados para manejar grandes volúmenes de
datos —más de 2 millones de registros por carga— con tiempos inferiores
a 40 minutos. El entorno dispone de alertas y logs que permiten
monitorizar el estado de sincronización, errores y métricas clave.

Esta instancia es un referente técnico para futuros despliegues en
entornos similares, demostrando la viabilidad de operaciones con
réplicas distribuidas, controladas y auditables.

Actualmente, la base de datos que alimenta el PDB de Noruega está en
fase de migración, en preparación para el apagado gradual de la
instancia legacy MASQL2014\SQLNORWAY.

## 3.6. MASERVF9 – (Antiguo MANECNET)

Servidor Windows Server 2019 con IIS 10 y .NET Framework 4.8 que cumple
una doble función crítica dentro del ecosistema Necor@: actúa como
pasarela de integración entre SAP PO y las bases de datos de Navantia, y
como servidor documental que almacena los ficheros físicos del sistema
de Gestión Documental.

### 3.6.1. Características generales

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;"><blockquote>
<p><strong>Elemento</strong></p>
</blockquote></th>
<th style="text-align: center;"><blockquote>
<p><strong>Valor</strong></p>
</blockquote></th>
</tr>
<tr>
<th style="text-align: left;"><blockquote>
<p><strong>FQDN / IP</strong></p>
</blockquote></th>
<th style="text-align: left;">maservf9.izar.es / 10.100.161.76</th>
</tr>
<tr>
<th style="text-align: left;"><blockquote>
<p><strong>OS / Build</strong></p>
</blockquote></th>
<th style="text-align: left;">Windows Server 2019 Std 10.0.17763</th>
</tr>
<tr>
<th style="text-align: left;"><blockquote>
<p><strong>IIS / .NET</strong></p>
</blockquote></th>
<th style="text-align: left;">IIS 10 + .NET Framework 4.8</th>
</tr>
<tr>
<th style="text-align: left;"><blockquote>
<p><strong>Aplicación</strong></p>
</blockquote></th>
<th style="text-align: left;">NecoraWebIntegrator.svc (SOAP 1.2 &amp;
REST: Login + SetInfoMateriales)</th>
</tr>
<tr>
<th style="text-align: left;"><blockquote>
<p><strong>Entrantes</strong></p>
</blockquote></th>
<th style="text-align: left;">SAP PO → HTTPS + BasicAuth</th>
</tr>
<tr>
<th style="text-align: left;"><blockquote>
<p><strong>Salientes</strong></p>
</blockquote></th>
<th style="text-align: left;">ODBC fijo → MASQL20171\HOSTDB2 (puerto
1452)</th>
</tr>
<tr>
<th style="text-align: left;"><blockquote>
<p><strong>Seguridad</strong></p>
</blockquote></th>
<th style="text-align: left;">TLS 1.2 activo · Certificado Let’s Encrypt
· Token BasicAuth anual</th>
</tr>
<tr>
<th style="text-align: left;"><blockquote>
<p><strong>Timeouts</strong></p>
</blockquote></th>
<th style="text-align: left;">HTTP 90 s · ODBC 30 s</th>
</tr>
<tr>
<th style="text-align: left;"><blockquote>
<p><strong>Backups</strong></p>
</blockquote></th>
<th style="text-align: left;">Veeam Agent diarios (02:30 UTC) →
NAS-P9</th>
</tr>
<tr>
<th style="text-align: left;"><blockquote>
<p><strong>Migración</strong></p>
</blockquote></th>
<th style="text-align: left;">Clonado MANECNET → go-live
08-ene-2025</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### 3.6.2. Funciones y contexto

- **Integración:** Hospeda el WebService NecoraMQ
  (NecoraWebIntegrator.svc), que expone operaciones SOAP y REST para
  consulta y validación de materiales, órdenes y hojas de catálogo. Las
  peticiones se comunican con HOSTDB2 vía ODBC configurado con puerto
  TCP fijo 1452, garantizando seguridad mediante TLS 1.2 y autenticación
  por token renovable anualmente.

- **Gestión documental:** Mantiene el almacén físico de documentos
  digitales (PDFs, hojas técnicas, planos) usados por aplicaciones
  Necor@AWD, Necor@NC y otras, compartidos vía SMB para acceso interno.

- **Migración:** Resultado de la migración parcial desde el antiguo
  servidor MANECNET, apagado en octubre de 2024. Se trasladaron
  únicamente componentes documentales y servicios de integración,
  descartando la migración completa de Necor@V6.

3.6.3. Cronología de migración y normalización

<img src="media/image1.jpg" style="width:7.18472in;height:1.78403in" />

Figura 3.6-2 presenta la cronología del proceso de migración desde
MANECNET a MASERVF9 y la estabilización del flujo de materiales, que se
desarrolló entre el 23 de octubre de 2024 y el 8 de enero de 2025.

### 3.6.4. Incidencias y acciones correctivas principales

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 29%" />
<col style="width: 26%" />
<col style="width: 23%" />
</colgroup>
<thead>
<tr>
<th style="text-align: center;"><blockquote>
<p><strong>Ticket / Fecha</strong></p>
</blockquote></th>
<th style="text-align: center;"><blockquote>
<p><strong>Descripción</strong></p>
</blockquote></th>
<th style="text-align: center;"><blockquote>
<p><strong>Acción ejecutada</strong></p>
</blockquote></th>
<th style="text-align: center;"><blockquote>
<p><strong>Resultado</strong></p>
</blockquote></th>
</tr>
<tr>
<th style="text-align: left;">GLPI #849716 – 08nov-2024</th>
<th style="text-align: left;"><blockquote>
<p>SAP deja de notificar cambios de materiales</p>
</blockquote></th>
<th style="text-align: left;"><p>Análisis raíz: parada de</p>
<p>MANECNET</p></th>
<th style="text-align: left;"><blockquote>
<p>Migración decidida a</p>
<p>MASERVF9</p>
</blockquote></th>
</tr>
<tr>
<th style="text-align: center;"><blockquote>
<p><strong>Ticket / Fecha</strong></p>
</blockquote></th>
<th style="text-align: center;"><blockquote>
<p><strong>Descripción</strong></p>
</blockquote></th>
<th style="text-align: center;"><blockquote>
<p><strong>Acción ejecutada</strong></p>
</blockquote></th>
<th style="text-align: center;"><blockquote>
<p><strong>Resultado</strong></p>
</blockquote></th>
</tr>
<tr>
<th style="text-align: left;">GLPI #856409 – 26nov-2024</th>
<th style="text-align: left;"><blockquote>
<p>Timeout MASERVF9 →</p>
<p>HOSTDB2</p>
</blockquote></th>
<th style="text-align: left;">Fijar puerto SQL en 1452 y reiniciar
DSN</th>
<th style="text-align: left;"><blockquote>
<p>Conectividad restablecida 27-nov</p>
</blockquote></th>
</tr>
<tr>
<th style="text-align: left;">GLPI #857752 – 29nov-2024</th>
<th style="text-align: left;"><blockquote>
<p>Access Denied desde SAP PO</p>
<p>(P9P)</p>
</blockquote></th>
<th style="text-align: left;">Apertura reglas FW y validación
SOAP-UI</th>
<th style="text-align: left;"><blockquote>
<p>Error 500 resuelto 13dic</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### 3.6.5. Lecciones aprendidas y recomendaciones

- Documentar exhaustivamente las dependencias de puertos SQL, evitando
  asignaciones dinámicas.

- Validar cambios en entornos espejo o pre-producción antes de
  desactivar sistemas legados.

- Automatizar pruebas E2E (SOAP-UI CLI + SQL ping) tras cada
  modificación infraestructural.

- Configurar alertas Centreon para códigos HTTP 5xx en el servicio
  NecoraWebIntegrator.

# 4. Arquitectura funcional del flujo F100 

<img src="media/image5.jpg" style="width:9.39375in;height:4.075in" />

El flujo funcional denominado **F100** constituye el núcleo del proceso
de **carga estructurada de datos de obras** en el ecosistema de bases de
datos de Navantia. Esta arquitectura permite la integración coordinada
de información procedente de **SAP, ECADAT y sistemas legados
(DB2/VSAM)** hacia las bases de datos funcionales del entorno AWD,
aplicando reglas de negocio, validaciones y consolidación por país o
cliente final.

El esquema general de F100 está compuesto por las siguientes fases y
componentes:

## 4.1. Origen de datos

Los datos de obra se generan en distintos sistemas fuente:

- **SAP**: estructura técnica y materiales asociados.

- **ECADAT**: catálogos de elementos constructivos.

- **DB2/VSAM** y **Necora Negro**: datos heredados, consolidados en
  Mirror DB2/SAM para compatibilidad.

Estos datos se integran inicialmente en bases intermedias como New PRYC,
PRYC, GDoc o Necor@ECADAT.

## 4.2. Interfaces de carga principales

Las dos cargas operativas clave son:

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 44%" />
<col style="width: 41%" />
</colgroup>
<thead>
<tr>
<th style="text-align: center;"><blockquote>
<p><strong>Job</strong></p>
</blockquote></th>
<th style="text-align: center;"><blockquote>
<p><strong>Instancia</strong></p>
</blockquote></th>
<th style="text-align: center;"><blockquote>
<p><strong>Descripción</strong></p>
</blockquote></th>
</tr>
<tr>
<th><blockquote>
<p><strong>Job 21: Carga</strong></p>
</blockquote></th>
<th><blockquote>
<p>MASQL20142\NECORANET.InterfacesAWD_PEC</p>
</blockquote></th>
<th><blockquote>
<p>Integra información desde SAP, ECADAT y PRYC. Aplica validaciones
iniciales.</p>
</blockquote></th>
</tr>
<tr>
<th><blockquote>
<p><strong>Job 22: Carga</strong></p>
</blockquote></th>
<th style="text-align: left;">NAILInterfacesAWD</th>
<th><blockquote>
<p>Permite mantener consistencia en el modelo</p>
</blockquote></th>
</tr>
<tr>
<th style="text-align: center;"><blockquote>
<p><strong>Job</strong></p>
</blockquote></th>
<th style="text-align: center;"><blockquote>
<p><strong>Instancia</strong></p>
</blockquote></th>
<th style="text-align: center;"><blockquote>
<p><strong>Descripción</strong></p>
</blockquote></th>
</tr>
<tr>
<th style="text-align: left;"><strong>Nail PEC</strong></th>
<th style="text-align: left;"></th>
<th style="text-align: left;"><blockquote>
<p>PEC, especializado para entornos AWD.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Ambos jobs están planificados como procesos automáticos, bajo SQL Agent,
con control de errores y trazabilidad mediante logs.

## 4.3. Reglas de negocio y transformación

Previo al volcado en bases finales, los datos pasan por un proceso de
validación y enriquecimiento definido como “**MD. Aplica Reglas de
Negocio**”, que se ejecuta en:

- MASQL2014\SQLTURK (Turquía)

- NORUEGAS (Noruega)

- AWD V 1.0 y AWD V 2.0 (clientes internos y externos)

Estas reglas comprueban la consistencia estructural, claves maestras,
relaciones válidas y codificación de campos técnicos. En el esquema se
identifican claramente los puntos donde se aplican dichas reglas en rojo
(“Aplica Reglas de Negocio AWD”).

## 4.4. Consolidación y publicación de datos

El objeto **PDB** actúa como **centro de consolidación lógico**,
recogiendo la información filtrada y estructurada desde Interfaces
HOST_AWD_PEC y Necor@Net. Desde este punto, se redistribuye a los
entornos de destino:

- InterfacesAWD

- InterfacesAWD.EEA5

- FESRVAD02.ESS

- MA SQL20221\SQLTURK y \SQLNORWAY

Estas instancias están diseñadas para soportar entornos funcionales,
pruebas, publicaciones a clientes externos o acceso desde plataformas
como Power BI.

### 4.4.1. Integración ampliada del modelo funcional – Foran \<-\> Windchill \<-\> SAP

Dentro del modelo operativo ampliado para entornos de Ingeniería, se ha
establecido una arquitectura de integración funcional entre los sistemas
Foran, Windchill y SAP. Esta arquitectura automatiza la conversión,
vinculación y sincronización de las estructuras de producto (EBOM/MBOM),
documentos técnicos y órdenes planificadas, facilitando la trazabilidad
y coherencia en todo el ciclo de vida del producto.

El flujo se articula en torno a los siguientes conceptos clave:

- **EBOM (Design View) y MBOM (Manufacturing View):** Generadas desde
  los módulos de Foran (FBUILDS, FDESIGN, FSYSD, FNEST), representan
  respectivamente la estructura de diseño y fabricación del producto.

- **Documentos IDD/IP:** Creación, gestión y aprobación dentro de
  Windchill, con trazabilidad detallada de revisiones y estados.

- **Publicación y vinculación automática:** Los materiales y documentos
  se publican desde Foran hacia Windchill, y posteriormente se
  sincronizan con SAP, garantizando la consistencia de la información.

- **Estructuras de planificación y órdenes previsionales:** Se
  transfieren a SAP (etapas OPrev1, OPrev2, OP1–OP6) para su ejecución y
  control en planta.

Además, el modelo incluye:

- **Reglas de conversión:** Adaptadas a cada producto y tipo documental,
  para asegurar la correcta transformación y mapeo entre sistemas.

- **Mecanismos de verificación:** Procesos ESI y MRP integrados en el
  momento de la sincronización con SAP, que validan la viabilidad
  técnica y de planificación.

- **Integración avanzada:** Control económico, subcontratación y gestión
  del cambio gestionados desde Windchill mediante ProjectLink, que
  asegura la coherencia administrativa y técnica.

Este flujo representa el marco general para la automatización documental
y de ingeniería, y es fundamental para comprender los orígenes, destinos
y relaciones de la información técnica que alimenta el ecosistema de
bases de datos y reporting.

<img src="media/image4.jpg" style="width:7.18472in;height:2.86667in" />

## 4.5. Validación de calidad y revisión

La arquitectura incorpora mecanismos explícitos de revisión, como el
nodo “**Revisar calidad de datos**” que opera tras las primeras
interfaces (HOST_AWD_PEC). Esto incluye:

- Comparaciones CRC (control de redundancia cíclica)

- Revisión de integridad relacional

- Chequeo de campos obligatorios y reglas específicas por cliente

- Logs de control y excepciones

## 4.6. Escenarios operativos

Se contemplan dos tipos de ejecución:

- **Carga completa**: aplicada en escenarios iniciales o de
  reestructuración completa de obras.

- **Carga incremental**: basada en cambios detectados (timestamp, flags
  lógicos, triggers en origen), activando solo las rutas necesarias.

## 4.7. Supervisión operativa y alertado

En este entorno se ha establecido un modelo de trabajo dual: por un
lado, la gestión y explotación interna de los datos AWD; y por otro, la
preparación de flujos estructurados hacia instancias remotas (SQLTURK y
SQLNORWAY) a través del objeto **PDB**. Este objeto actúa como “puente
lógico” entre los entornos locales y los clientes internacionales,
asegurando la consistencia estructural y minimizando el acoplamiento
entre esquemas.

## 4.8. Consideraciones de mejora

La arquitectura actual ha demostrado ser robusta y funcional, pero
pueden abordarse mejoras para simplificar la trazabilidad y
mantenimiento:

- Consolidar los puntos de aplicación de reglas de negocio en un único
  motor o repositorio.

- Unificar nomenclatura de interfaces y vistas entre instancias.

- Automatizar validaciones en origen antes de ejecutar cargas (previa a
  Job 21).

- Documentar un protocolo de fallback ante errores en fases críticas del
  flujo (job fallido, validación fallida).

# 5. Calidad y riesgos actuales 

El sistema actual presenta un estado de operación estable, con mejoras
sustanciales de rendimiento tras la consolidación de datos en instancias
SQL Server modernas (2017–2022) y la reestructuración de vistas e
índices. No obstante, existen **riesgos operativos y técnicos** que
deben ser considerados:

- **Heterogeneidad tecnológica**: conviven versiones desde SQL Server
  2008 R2 hasta 2022, lo que dificulta la unificación de estrategias de
  mantenimiento, backup y seguridad.

- **Instancias con soporte expirado** (MAHOST, SQL20142): aunque en modo
  sólo-lectura, siguen presentes en el entorno y requieren control hasta
  su decommission.

- **Riesgos de obsolescencia funcional**: ciertas dependencias en
  Necor@V6, ECADA o interfaces PEC siguen ancladas a estructuras
  heredadas, dificultando la modernización.

- **Puntos críticos sin HA (alta disponibilidad)**: algunas instancias
  claves no disponen de réplica o failover automático, lo que incrementa
  la exposición ante caídas no planificadas.

- **Dependencias manuales en flujos ETL**: aunque automatizados, los
  flujos de Turquía y Noruega aún dependen de comprobaciones visuales en
  ciertas etapas.

En cuanto a calidad, las mejoras en índices, sinónimos y vistas
funcionales han permitido reducir los tiempos de respuesta entre un
**30 % y 50 %** en procedimientos críticos. Se han implantado controles
CRC y logs que aseguran trazabilidad, pero aún no existe una cobertura
total de pruebas automatizadas ni de alertas proactivas de rendimiento.
Se recomienda avanzar en esas áreas como parte del plan de evolución
técnica.

# 6. Próximos pasos recomendados 

El principal hito pendiente identificado a corto-medio plazo es la
**migración completa de las instancias actuales en MA SQL20142 (tanto
SQL20142 como NECORANET) hacia una nueva instancia consolidada MA
SQL20222 basada en SQL Server 2022**. Esta acción, alineada con las
políticas de modernización tecnológica y soporte de plataforma,
implicará una revisión exhaustiva de todo el entorno actual.

Dicha revisión debe incluir:

- **Análisis y validación de compatibilidad** de procedimientos
  almacenados, funciones, vistas y sinónimos actualmente en uso.

- **Revisión de flujos ETL, enlaces de servidor y servicios asociados**
  (como Reporting Services y Power BI).

- **Evaluación de vistas funcionales y refactorización de estructuras
  heredadas**, con el objetivo de simplificar lógicas innecesarias y
  mejorar el rendimiento global.

- **Homologación de estándares técnicos**: nombres de objetos,
  collation, agrupación de esquemas por rol funcional, etc.

- **Prueba completa de rendimiento comparado**, para asegurar que la
  nueva instancia mantiene o mejora los tiempos actuales, especialmente
  en vistas \_V, índices aplicados y llamadas desde Necor@.

Este proceso no solo permitirá abandonar entornos sin soporte y reducir
riesgos operativos, sino que abrirá la puerta a **implementar buenas
prácticas y optimizaciones** que en el estado actual están condicionadas
por la necesidad de mantener compatibilidad hacia atrás.

Adicionalmente, se recomienda:

- Consolidar backups y planes de mantenimiento en entornos más robustos
  (Azure SQL Managed Instance en el medio plazo).

- Ampliar los mecanismos de alertas y trazabilidad, especialmente en
  entornos internacionales.

Estas acciones permitirán avanzar hacia una **plataforma unificada,
segura y preparada para integraciones futuras**, cumpliendo con los
requisitos operativos internos y externos de Navantia.

# 7. Referencias internas y fuentes consultadas 

A continuación se relacionan las principales fuentes documentales y
registros corporativos consultados para la elaboración de este documento
técnico. Estas referencias aportan el soporte técnico y funcional
necesario para la trazabilidad y justificación de las decisiones
reflejadas.

<table>
<colgroup>
<col style="width: 4%" />
<col style="width: 28%" />
<col style="width: 20%" />
<col style="width: 46%" />
</colgroup>
<thead>
<tr>
<th><blockquote>
<p><strong>Nº</strong></p>
</blockquote></th>
<th style="text-align: center;"><strong>Fuente interna</strong></th>
<th colspan="2" style="text-align: center;"><strong>Descripción y
aportación</strong></th>
</tr>
<tr>
<th>R.1</th>
<th style="text-align: left;"><p>Informe de dedicación –</p>
<p>Integración Materiales (Altia)</p></th>
<th colspan="2" style="text-align: left;">Seguimiento detallado del
proceso de sustitución de MANECNET por MASERVF9. Incluye cronograma,
validaciones técnicas y coordinación con SAP PO.</th>
</tr>
<tr>
<th>R.2</th>
<th style="text-align: left;"><p>GLPI #0849716 /</p>
<p>#0856409 / SD 857752</p></th>
<th colspan="2" style="text-align: left;">Incidencias técnicas
registradas durante la migración de servicios y validación de
conectividad entre MASERVF9 y HOSTDB2.</th>
</tr>
<tr>
<th>R.3</th>
<th style="text-align: left;">Actas TEAMS – Integración materiales
SAP</th>
<th colspan="2" style="text-align: left;">Validación funcional conjunta
con SAP y definición del modelo operativo post-migración.</th>
</tr>
<tr>
<th>R.4</th>
<th style="text-align: left;">Reunión 30/04/2024 – Seguimiento activos
históricos</th>
<th colspan="2" style="text-align: left;">Avance del piloto ETL Noruega
y confirmación de la viabilidad del modelo de carga a Power BI.</th>
</tr>
<tr>
<th>R.5</th>
<th><p>Optimización V6 – Tarea GLPI</p>
<p>#431672</p></th>
<th colspan="2" style="text-align: left;"><p>Reestructuración de vistas,
sinónimos e índices en V6 y V6_2.</p>
<p>Justificación técnica validada por Ingeniería.</p></th>
</tr>
<tr>
<th>R.6</th>
<th><p>Diseño técnico ETL Noruega y</p>
<p>Turquía</p></th>
<th colspan="2" style="text-align: left;">Documento funcional sobre
flujos de carga diarios, validaciones CRC y segmentación por país.</th>
</tr>
<tr>
<th>R.7</th>
<th style="text-align: left;">Extracción GLPI (csv)</th>
<th colspan="2" style="text-align: left;">Registro de tickets y acciones
históricas sobre migraciones, refactors y soporte asociado.</th>
</tr>
<tr>
<th>R.8</th>
<th style="text-align: left;">Plantilla Base – Documento</th>
<th colspan="2" style="text-align: left;">Estructura corporativa
empleada para estandarizar el presente</th>
</tr>
<tr>
<th><blockquote>
<p><strong>Nº</strong></p>
</blockquote></th>
<th style="text-align: center;"><blockquote>
<p><strong>Fuente interna</strong></p>
</blockquote></th>
<th style="text-align: left;"></th>
<th style="text-align: left;"><strong>Descripción y
aportación</strong></th>
</tr>
<tr>
<th style="text-align: left;"></th>
<th style="text-align: left;"><blockquote>
<p>Técnico Navantia</p>
</blockquote></th>
<th style="text-align: left;"><blockquote>
<p>documento.</p>
</blockquote></th>
<th style="text-align: left;"></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Todas las fuentes están almacenadas en sistemas internos (Teams, GLPI,
correo corporativo) y disponibles bajo petición para auditoría técnica o
trazabilidad interna.

**Referencias documentales utilizadas en este informe:**

- Propuesta Técnica: «Mantenimiento de Sistemas Legacy de Navantia»,
  Altia Consultores.

- Documentos de planificación y ejecución del proyecto HOST (2019–2021).

- Herramientas de gestión de servicio empleadas durante el mantenimiento
  y migración (Helpdesk Navantia).

- Acuerdos de Nivel de Servicio (SLA) establecidos con indicadores de
  tiempo de respuesta y resolución.

- Metodologías empleadas: ITIL, ISO/IEC 20000, Métrica v3.

## Anexo técnico – Inventario actual de bases de datos por instancia

A continuación se documenta el inventario actualizado de bases de datos
existentes en las principales instancias activas de la plataforma, según
revisión interna a fecha de actualización (última revisión: hace 3
días). Se incluyen observaciones de revisión o validación pendiente para
facilitar su trazabilidad operativa.

1.  **Instancia: MASQL20142\NECORANET**

<table>
<colgroup>
<col style="width: 37%" />
<col style="width: 62%" />
</colgroup>
<thead>
<tr>
<th style="text-align: center;"><blockquote>
<p><strong>Base de datos</strong></p>
</blockquote></th>
<th style="text-align: center;"><blockquote>
<p><strong>Estado / Observación</strong></p>
</blockquote></th>
</tr>
<tr>
<th style="text-align: left;">BD_Auxiliar</th>
<th style="text-align: left;"><blockquote>
<p><strong>Obsoleta</strong> – tablas VB6; exportar y eliminar Q4-2025
(plan obsolescencia) 0adce6d2-706d-4681-8949…</p>
</blockquote></th>
</tr>
<tr>
<th style="text-align: left;">Coral</th>
<th style="text-align: left;"><blockquote>
<p><strong>Activa</strong> – módulo Corales PDB; migrar a SQL 2022 junto
con</p>
<p>Necora*</p>
</blockquote></th>
</tr>
<tr>
<th style="text-align: left;">InterfacesAWD</th>
<th><blockquote>
<p><strong>Activa</strong> – staging de cargas AWD; revisar tamaño de
log (&gt; 45</p>
<p>GB)</p>
</blockquote></th>
</tr>
<tr>
<th style="text-align: left;">InterfacesAWD_PEC</th>
<th style="text-align: left;"><blockquote>
<p><strong>Activa</strong> – mismo esquema que InterfacesAWD; consolidar
en una sola BD</p>
</blockquote></th>
</tr>
<tr>
<th style="text-align: left;">InterfacesDWH</th>
<th style="text-align: left;"><blockquote>
<p><strong>Sólo-lectura</strong> – origen Power BI; última actualización
17may-2025</p>
</blockquote></th>
</tr>
<tr>
<th style="text-align: left;">NAILInterfacesAWD</th>
<th><blockquote>
<p><strong>Pendiente validación</strong> – sin conexiones registradas en
90 días</p>
</blockquote></th>
</tr>
<tr>
<th style="text-align: left;">Nautilus</th>
<th style="text-align: left;"><blockquote>
<p><strong>Obsoleta</strong> – sustituida por módulo RADAR Nautilus;</p>
</blockquote></th>
</tr>
<tr>
<th style="text-align: left;">NecoraAWD</th>
<th style="text-align: left;"><blockquote>
<p><strong>Producción</strong> – núcleo histórico Necor@</p>
</blockquote></th>
</tr>
<tr>
<th style="text-align: left;">NecoraDocAWD</th>
<th><blockquote>
<p><strong>Activa</strong> – documentos DWG; alto growth de FILESTREAM
(4,3</p>
</blockquote></th>
</tr>
<tr>
<th style="text-align: center;"><blockquote>
<p><strong>Base de datos</strong></p>
</blockquote></th>
<th style="text-align: center;"><blockquote>
<p><strong>Estado / Observación</strong></p>
</blockquote></th>
</tr>
<tr>
<th style="text-align: left;"></th>
<th style="text-align: left;"><blockquote>
<p>TB)</p>
</blockquote></th>
</tr>
<tr>
<th style="text-align: left;">NecoraHistoric</th>
<th style="text-align: left;"><blockquote>
<p><strong>Archivada</strong> – modo READ_ONLY desde 01-mar-2025 (ahorro
backup)</p>
</blockquote></th>
</tr>
<tr>
<th style="text-align: left;">NecoraNet_BI</th>
<th style="text-align: left;"><blockquote>
<p><strong>Sólo-lectura</strong> – cubos SSAS; refresco nocturno 03:00
h</p>
</blockquote></th>
</tr>
<tr>
<th style="text-align: left;">NecoraReplicationControlAWD</th>
<th style="text-align: left;"><blockquote>
<p><strong>Sistema</strong> – metadatos de réplica Merge; no tocar</p>
</blockquote></th>
</tr>
<tr>
<th style="text-align: left;">RADAR</th>
<th><blockquote>
<p><strong>Pre-producción</strong> – módulo Taquillas 75 % completado;
pilotaje sept-2025 0adce6d2-706d-4681-8949…</p>
</blockquote></th>
</tr>
<tr>
<th style="text-align: left;">ReportServer$NECORANET</th>
<th><blockquote>
<p><strong>Sistema Reporting</strong> – SSRS; plan migración a nuevo
servidor BI</p>
</blockquote></th>
</tr>
<tr>
<th style="text-align: left;">ReportServer$NECORANETTempDB</th>
<th style="text-align: left;"><blockquote>
<p><strong>Sistema Reporting</strong> – temp de SSRS</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

2.  **Instancia: MASQL20142\SQL20142**

<table>
<colgroup>
<col style="width: 36%" />
<col style="width: 63%" />
</colgroup>
<thead>
<tr>
<th style="text-align: center;"><strong>Base de datos</strong></th>
<th style="text-align: center;"><strong>Estado /
Observación</strong></th>
</tr>
<tr>
<th style="text-align: left;">Necor@NC</th>
<th><blockquote>
<p><strong>Producción (cliente Noruega)</strong> – backups diarios;
migración a</p>
<p>MASQL20222 en octubre-2025</p>
</blockquote></th>
</tr>
<tr>
<th style="text-align: left;">NecoraAWD</th>
<th style="text-align: left;"><blockquote>
<p><strong>Vacía</strong> – se creó para pruebas; eliminar tras validar
que no hay jobs dependientes</p>
</blockquote></th>
</tr>
<tr>
<th style="text-align: left;">ReportServer_ReportingTest</th>
<th style="text-align: left;"><blockquote>
<p><strong>Entorno TEST</strong> – migrar o eliminar con el nuevo portal
BI</p>
</blockquote></th>
</tr>
<tr>
<th>ReportServer_ReportingTestTempDB</th>
<th style="text-align: left;"><blockquote>
<p><strong>Entorno TEST</strong> – idem anterior</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

3.  **Instancia: MASQL20171\HOSTDB2**

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 74%" />
</colgroup>
<thead>
<tr>
<th style="text-align: center;"><strong>Base de datos</strong></th>
<th style="text-align: center;"><strong>Estado /
Observación</strong></th>
</tr>
<tr>
<th style="text-align: left;">Aceros</th>
<th style="text-align: left;"><strong>Producción baja
frecuencia</strong> – consulta puntual por Programa F110</th>
</tr>
<tr>
<th style="text-align: left;">AcerosMPGS</th>
<th style="text-align: left;"><strong>Pendiente migrar</strong> –
move-group lote 2 (plan WS 2012R2)</th>
</tr>
<tr>
<th style="text-align: left;">AlmacenesIntermedios</th>
<th style="text-align: left;"><strong>Activa</strong> – interfaz SAP;
índice IDX_AlmTrans con fragmentación 68 %</th>
</tr>
<tr>
<th style="text-align: left;">BQ 206</th>
<th style="text-align: left;"><strong>Obsoleta</strong> – sin escrituras
desde 2018; archivar</th>
</tr>
<tr>
<th style="text-align: left;">ControlAsuntos</th>
<th style="text-align: left;"><strong>Activa</strong> – workflow VB6;
riesgo .NET 3.5 legacy 345e8c4b-ef01-4600-9dd7…</th>
</tr>
<tr>
<th style="text-align: left;">ControlDoc</th>
<th style="text-align: left;"><strong>Producción</strong> – repositorio
documentos internos</th>
</tr>
<tr>
<th style="text-align: left;">CoralTest</th>
<th style="text-align: left;"><strong>Desarrollo</strong> – sandbox de
Coral; limpiar cada trimestre</th>
</tr>
<tr>
<th style="text-align: left;">DB2P</th>
<th style="text-align: left;"><strong>Producción</strong> – dados de
Newport; requiere puerto estático 1456</th>
</tr>
<tr>
<th style="text-align: left;">DB2T</th>
<th style="text-align: left;"><strong>Test</strong> – restauración
diaria de DB2P</th>
</tr>
<tr>
<th style="text-align: left;">GestionHerramental</th>
<th style="text-align: left;"><strong>Producción</strong> – migrar a
RADAR (nov-2025) 0adce6d2-706d-4681-8949…</th>
</tr>
<tr>
<th style="text-align: left;">LowCodeWorkOrders</th>
<th style="text-align: left;"><strong>PoC</strong> – app Power Apps;
validar modelo de seguridad</th>
</tr>
<tr>
<th style="text-align: left;">Necor@</th>
<th><strong>Producción</strong> – núcleo HOST; integrado con MASERVF9
TEAMS - Integración mat…</th>
</tr>
<tr>
<th style="text-align: left;">Ordenes</th>
<th style="text-align: left;"><strong>Producción</strong> – integración
MES; alto I/O nocturno</th>
</tr>
<tr>
<th style="text-align: left;">ReportServer_SI2</th>
<th style="text-align: left;"><strong>Sistema Reporting</strong> –
activo; pendiente renombrar estándar</th>
</tr>
<tr>
<th>ReportServer_SI2TempDB</th>
<th style="text-align: left;"><strong>Sistema Reporting</strong> –
activo</th>
</tr>
<tr>
<th style="text-align: center;"><strong>Base de datos</strong></th>
<th style="text-align: center;"><strong>Estado /
Observación</strong></th>
</tr>
<tr>
<th style="text-align: left;"></th>
<th style="text-align: left;"></th>
</tr>
<tr>
<th style="text-align: left;">SSISDB</th>
<th style="text-align: left;"><strong>Sistema</strong> – cat. SSIS;
backup FULL semanal</th>
</tr>
<tr>
<th style="text-align: left;">SubContratas</th>
<th style="text-align: left;"><strong>Producción</strong> – módulo
contratos; revisar FK inconsistentes</th>
</tr>
<tr>
<th style="text-align: left;">V6</th>
<th><p><strong>Producción</strong> – destino flujo F100_MAT_SAP;
monitorización proactiva pendiente</p>
<p>TEAMS - Integración mat…</p></th>
</tr>
<tr>
<th style="text-align: left;">V6_2</th>
<th style="text-align: left;"><strong>Calidad / pruebas</strong> – copia
de V6;</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Nota: en el caso de la instancia MASQL20171\HOSTDB2 no se han incluido
las bases que comienzan por 'T\_' al considerarse entornos de prueba
(TEST) de las anteriores.

## Anexo – Inventario de Jobs por instancia

Este anexo recoge el inventario de trabajos (SQL Server Agent Jobs)
habilitados en distintas instancias SQL de Navantia, tal como aparecen
configurados en el Job Activity Monitor. Para cada job se indica si está
activo y la frecuencia estimada de ejecución-

1.  **Instancia: MASQL20171\HOSTDB2**

<table>
<colgroup>
<col style="width: 58%" />
<col style="width: 11%" />
<col style="width: 29%" />
</colgroup>
<thead>
<tr>
<th style="text-align: center;"><blockquote>
<p>Nombre del Job</p>
</blockquote></th>
<th style="text-align: left;"><blockquote>
<p>Activo</p>
</blockquote></th>
<th style="text-align: left;"><blockquote>
<p>Frecuencia estimada</p>
</blockquote></th>
</tr>
<tr>
<th style="text-align: left;">SAPInterfaces</th>
<th style="text-align: left;"><blockquote>
<p>Sí</p>
</blockquote></th>
<th style="text-align: left;">Diario</th>
</tr>
<tr>
<th style="text-align: left;">Replication agents checkup</th>
<th style="text-align: left;"><blockquote>
<p>Sí</p>
</blockquote></th>
<th style="text-align: left;">Diario</th>
</tr>
<tr>
<th style="text-align: left;">INTERFACES_NET_CARGA_MATERIAL</th>
<th style="text-align: left;"><blockquote>
<p>Sí</p>
</blockquote></th>
<th style="text-align: left;">Diario</th>
</tr>
<tr>
<th style="text-align: left;">MaintenancePlan - Backup Full and Log</th>
<th style="text-align: left;"><blockquote>
<p>Sí</p>
</blockquote></th>
<th style="text-align: left;">Diario</th>
</tr>
<tr>
<th style="text-align: left;">BATCH_NECORANET_BRAVOERI_AR</th>
<th style="text-align: left;"><blockquote>
<p>Sí</p>
</blockquote></th>
<th style="text-align: left;">No programado</th>
</tr>
<tr>
<th style="text-align: left;">BATCH_NECORANET_BRAVROPE_PROD</th>
<th style="text-align: left;"><blockquote>
<p>Sí</p>
</blockquote></th>
<th style="text-align: left;">No programado</th>
</tr>
<tr>
<th style="text-align: left;">syspolicy_purge_history</th>
<th style="text-align: left;"><blockquote>
<p>Sí</p>
</blockquote></th>
<th style="text-align: left;">Diario</th>
</tr>
<tr>
<th style="text-align: left;">INTERFACES_SAP_AUTOMATICOS</th>
<th style="text-align: left;"><blockquote>
<p>Sí</p>
</blockquote></th>
<th style="text-align: left;">Diario</th>
</tr>
<tr>
<th style="text-align: left;">ShrinkLogDBProduction</th>
<th style="text-align: left;"><blockquote>
<p>Sí</p>
</blockquote></th>
<th style="text-align: left;">Diario</th>
</tr>
<tr>
<th style="text-align: left;">SSIS Server Maintenance Job</th>
<th style="text-align: left;"><blockquote>
<p>Sí</p>
</blockquote></th>
<th style="text-align: left;">Diario</th>
</tr>
<tr>
<th style="text-align: left;">MaintenancePlan - Shrink
shrinkDataBase</th>
<th style="text-align: left;"><blockquote>
<p>Sí</p>
</blockquote></th>
<th style="text-align: left;">Diario</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 58%" />
<col style="width: 11%" />
<col style="width: 29%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Borrado-planes-mantenimiento
Subplan_8</th>
<th style="text-align: left;"><blockquote>
<p>Sí</p>
</blockquote></th>
<th style="text-align: left;">Diario</th>
</tr>
<tr>
<th style="text-align: left;">MaintenancePlan - Clean History
Subplan_1</th>
<th style="text-align: left;"><blockquote>
<p>Sí</p>
</blockquote></th>
<th style="text-align: left;">Diario</th>
</tr>
<tr>
<th style="text-align: left;">ShrinkLogDBTest</th>
<th style="text-align: left;"><blockquote>
<p>Sí</p>
</blockquote></th>
<th style="text-align: left;">Diario</th>
</tr>
<tr>
<th style="text-align: left;">DiarioDorado-BK Dorado-backups</th>
<th style="text-align: left;"><blockquote>
<p>Sí</p>
</blockquote></th>
<th style="text-align: left;">Diario</th>
</tr>
<tr>
<th style="text-align: left;">_ShrinkBKTTest</th>
<th style="text-align: left;"><blockquote>
<p>Sí</p>
</blockquote></th>
<th style="text-align: left;">Diario</th>
</tr>
<tr>
<th style="text-align: left;">TestingActiveScripting</th>
<th style="text-align: left;"><blockquote>
<p>Sí</p>
</blockquote></th>
<th style="text-align: left;">Diario</th>
</tr>
<tr>
<th style="text-align: left;">Diario-Subplan_3</th>
<th style="text-align: left;"><blockquote>
<p>Sí</p>
</blockquote></th>
<th style="text-align: left;">Semanal</th>
</tr>
<tr>
<th style="text-align: left;">MaintenancePlan - Rebuild Index And
Stats</th>
<th style="text-align: left;"><blockquote>
<p>Sí</p>
</blockquote></th>
<th style="text-align: left;">Semanal</th>
</tr>
<tr>
<th style="text-align: left;">INTERFACES_NET_CARGA_CABECERAS</th>
<th style="text-align: left;"><blockquote>
<p>Sí</p>
</blockquote></th>
<th style="text-align: left;">No programado</th>
</tr>
<tr>
<th style="text-align: left;">INTERFACES_NET_CARGA_CABECERAS_2</th>
<th style="text-align: left;"><blockquote>
<p>Sí</p>
</blockquote></th>
<th style="text-align: left;">No programado</th>
</tr>
<tr>
<th style="text-align: left;">BATCH_FICHEROS_PCACNEX_CARGA</th>
<th style="text-align: left;"><blockquote>
<p>Sí</p>
</blockquote></th>
<th style="text-align: left;">No programado</th>
</tr>
<tr>
<th style="text-align: left;">SAPcompressionHistoryFiles</th>
<th style="text-align: left;"><blockquote>
<p>Sí</p>
</blockquote></th>
<th style="text-align: left;">Mensual</th>
</tr>
<tr>
<th style="text-align: left;">Z_InformeGD_AWD</th>
<th style="text-align: left;"><blockquote>
<p>Sí</p>
</blockquote></th>
<th style="text-align: left;">No programado</th>
</tr>
<tr>
<th style="text-align: left;">BATCH_FICHEROS_HOJAS</th>
<th style="text-align: left;"><blockquote>
<p>No</p>
</blockquote></th>
<th style="text-align: left;">No programado</th>
</tr>
<tr>
<th style="text-align: left;">BATCH_FICHEROS_SI2_NO_INMEDIATO</th>
<th style="text-align: left;"><blockquote>
<p>Sí</p>
</blockquote></th>
<th style="text-align: left;">No programado</th>
</tr>
<tr>
<th style="text-align: left;">BATCH_FICHEROS_SI2_INMEDIATO</th>
<th style="text-align: left;"><blockquote>
<p>Sí</p>
</blockquote></th>
<th style="text-align: left;">Ejecución reciente</th>
</tr>
<tr>
<th style="text-align: left;">MaintenancePlan - Check DB Subplan_1</th>
<th style="text-align: left;"><blockquote>
<p>Sí</p>
</blockquote></th>
<th style="text-align: left;">Diario</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

2.  **Instancia: MASQL20142\NECORANET**

<table>
<colgroup>
<col style="width: 62%" />
<col style="width: 10%" />
<col style="width: 27%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;"><blockquote>
<p>Nombre del Job</p>
</blockquote></th>
<th style="text-align: left;"><blockquote>
<p>Activo</p>
</blockquote></th>
<th style="text-align: left;">Frecuencia estimada</th>
</tr>
<tr>
<th style="text-align: left;"><blockquote>
<p>Nautilus</p>
</blockquote></th>
<th style="text-align: left;"><blockquote>
<p>Sí</p>
</blockquote></th>
<th style="text-align: left;">Diario</th>
</tr>
<tr>
<th style="text-align: left;"><blockquote>
<p>Z7_Carga NAIL NC1XSQ</p>
</blockquote></th>
<th style="text-align: left;"><blockquote>
<p>Sí</p>
</blockquote></th>
<th style="text-align: left;">Diario</th>
</tr>
<tr>
<th style="text-align: left;"><blockquote>
<p>ActualizarEstadoCasillas</p>
</blockquote></th>
<th style="text-align: left;"><blockquote>
<p>Sí</p>
</blockquote></th>
<th style="text-align: left;">Diario</th>
</tr>
<tr>
<th style="text-align: left;"><blockquote>
<p>99_Correccion Codigo TDRevision</p>
</blockquote></th>
<th style="text-align: left;"><blockquote>
<p>Sí</p>
</blockquote></th>
<th style="text-align: left;">Diario</th>
</tr>
<tr>
<th style="text-align: left;"><blockquote>
<p>Agent history clean up: distribution</p>
</blockquote></th>
<th style="text-align: left;"><blockquote>
<p>Sí</p>
</blockquote></th>
<th style="text-align: left;">Diario</th>
</tr>
<tr>
<th style="text-align: left;"><blockquote>
<p>Replication agents checkup</p>
</blockquote></th>
<th style="text-align: left;"><blockquote>
<p>Sí</p>
</blockquote></th>
<th style="text-align: left;">Diario</th>
</tr>
<tr>
<th style="text-align: left;"><blockquote>
<p>MaintenancePlan - Backup Full And TLogs</p>
</blockquote></th>
<th style="text-align: left;"><blockquote>
<p>Sí</p>
</blockquote></th>
<th style="text-align: left;">Diario</th>
</tr>
<tr>
<th style="text-align: left;"><blockquote>
<p>25_Carga NecoraNET - Materiales</p>
</blockquote></th>
<th style="text-align: left;"><blockquote>
<p>Sí</p>
</blockquote></th>
<th style="text-align: left;">Diario</th>
</tr>
<tr>
<th style="text-align: left;"><blockquote>
<p>Distribucion delta</p>
</blockquote></th>
<th style="text-align: left;"><blockquote>
<p>Sí</p>
</blockquote></th>
<th style="text-align: left;">Diario</th>
</tr>
<tr>
<th style="text-align: left;"><blockquote>
<p>30_Carga NecoraNET - Carga completa + reglas</p>
</blockquote></th>
<th style="text-align: left;"><blockquote>
<p>Sí</p>
</blockquote></th>
<th style="text-align: left;">Diario</th>
</tr>
<tr>
<th style="text-align: left;"><blockquote>
<p>Plan CheckDB Subplan_1</p>
</blockquote></th>
<th style="text-align: left;"><blockquote>
<p>Sí</p>
</blockquote></th>
<th style="text-align: left;">Diario</th>
</tr>
<tr>
<th style="text-align: left;"><blockquote>
<p>Plan_Indices Reorganiza Subplan_1</p>
</blockquote></th>
<th style="text-align: left;"><blockquote>
<p>Sí</p>
</blockquote></th>
<th style="text-align: left;">Semanal</th>
</tr>
<tr>
<th style="text-align: left;"><blockquote>
<p>22_Carga NAIL PEC - Carga Asuntos y Tareas</p>
</blockquote></th>
<th style="text-align: left;"><blockquote>
<p>Sí</p>
</blockquote></th>
<th style="text-align: left;">Diario</th>
</tr>
<tr>
<th style="text-align: left;"><blockquote>
<p>22_Carga NAIL PEC - Carga completa + materiales</p>
</blockquote></th>
<th style="text-align: left;"><blockquote>
<p>Sí</p>
</blockquote></th>
<th style="text-align: left;">Diario</th>
</tr>
<tr>
<th style="text-align: left;"><blockquote>
<p>99_Correccion extensiones</p>
</blockquote></th>
<th style="text-align: left;"><blockquote>
<p>Sí</p>
</blockquote></th>
<th style="text-align: left;">Diario</th>
</tr>
<tr>
<th style="text-align: left;"><blockquote>
<p>MaintenancePlan - Clean History Subplan_1</p>
</blockquote></th>
<th style="text-align: left;"><blockquote>
<p>Sí</p>
</blockquote></th>
<th style="text-align: left;">Diario</th>
</tr>
<tr>
<th style="text-align: left;"><blockquote>
<p>25_Carga NecoraNET - HojasCatalogo</p>
</blockquote></th>
<th style="text-align: left;"><blockquote>
<p>Sí</p>
</blockquote></th>
<th style="text-align: left;">Diario</th>
</tr>
<tr>
<th style="text-align: left;"></th>
<th style="text-align: left;"></th>
<th style="text-align: left;"></th>
</tr>
<tr>
<th style="text-align: left;"><blockquote>
<p>Z_Alerta deDocumento</p>
</blockquote></th>
<th style="text-align: left;"><blockquote>
<p>Sí</p>
</blockquote></th>
<th style="text-align: left;">Diario</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

3.  **Instancia: MASQL20221\SQLNORWAY**

<table>
<colgroup>
<col style="width: 56%" />
<col style="width: 11%" />
<col style="width: 32%" />
</colgroup>
<thead>
<tr>
<th style="text-align: center;"><blockquote>
<p>Nombre del Job</p>
</blockquote></th>
<th style="text-align: left;"><blockquote>
<p>Activo</p>
</blockquote></th>
<th style="text-align: left;"><blockquote>
<p>Frecuencia estimada</p>
</blockquote></th>
</tr>
<tr>
<th style="text-align: left;">MaintenancePlan - BackupFull And Log</th>
<th style="text-align: left;">Sí</th>
<th style="text-align: left;">Diario</th>
</tr>
<tr>
<th style="text-align: left;">01_Carga NORWAY</th>
<th style="text-align: left;">No</th>
<th style="text-align: left;">Diario</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

4.  **Instancia: MASQL20221\SQLTURK**

<table>
<colgroup>
<col style="width: 56%" />
<col style="width: 11%" />
<col style="width: 31%" />
</colgroup>
<thead>
<tr>
<th style="text-align: center;"><blockquote>
<p>Nombre del Job</p>
</blockquote></th>
<th style="text-align: left;"><blockquote>
<p>Activo</p>
</blockquote></th>
<th style="text-align: left;"><blockquote>
<p>Frecuencia estimada</p>
</blockquote></th>
</tr>
<tr>
<th style="text-align: left;">MaintenancePlan - Backup Full And Log</th>
<th style="text-align: left;">Sí</th>
<th style="text-align: left;">Diario</th>
</tr>
<tr>
<th style="text-align: left;">MaintenancePlan - Rebuild Index</th>
<th style="text-align: left;">Sí</th>
<th style="text-align: left;">Semanal</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
