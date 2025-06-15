---
source: EstadoActualPlataformaBBD_V0306_10_32.md
doc_source: EstadoActualPlataformaBBD_V0306_10_32.docx
created: 2025-06-15T23:09:06.948315
---
<div class="fragment-meta">source: EstadoActualPlataformaBBD_V0306_10_32.md | doc: EstadoActualPlataformaBBD_V0306_10_32.docx | created: 2025-06-15T23:09:06.948315</div>

# 3. Detalle técnico por servidor/instancia 

## 3.1. MASQL20171/HOSTDB2

La instancia MASQL20171/HOSTDB2 funciona como el **nodo central de
consolidación** tras el apagado del entorno HOST (DB2/VSAM).
Implementada sobre SQL Server 2017 CU31, concentra todas las bases de
datos migradas desde el ecosistema mainframe, así como los esquemas
técnicos heredados de instancias auxiliares como FESRV014 y MAHOST.

### 3.1.1. Características generales

**Rol:** Nodo central de consolidación tras el apagado del entorno HOST
(DB2/VSAM) **Versión:** SQL Server 2017 CU31.

**Bases de datos:** V6, V6_2, DB2T, DB2P **Conexiones entrantes:**

- MASERVF9 (vía ODBC desde IIS/WebService) o MASQL20142/NECORANET
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

MASQL20171/HOSTDB2 almacena la información consolidada desde tres
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

- Se generaron nuevas vistas /_V sobre V6_2.

- Se reemplazaron los sinónimos en V6 para que apunten a estas vistas no
  filtradas.

- Las vistas originales se renombraron como /_BKP para permitir
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
Server (MASQL20171/HOSTDB2) sin pérdida de operatividad.

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

<img src="C:/PROYECTOS_GPT/wiki_documental/wiki/assets/media/image3.jpg"
style="width:6.33819in;height:1.39583in" />

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
  /_AtributosConfig.dtsx y /_LimpiarLogs.dtsx, se asegura la integridad
  y calidad de los datos extraídos.

- **Actualización de estados en tablas funcionales:** El paquete
  /_StatusDeleted.dtsx gestiona la actualización de estados, asegurando
  que las tablas reflejen el estado actual de los registros.

- **Consolidación de documentos técnicos:** Paquetes como
  Documentos_tecnicos/_/*.dtsx consolidan documentos técnicos,
  garantizando que toda la información relevante esté centralizada y
  accesible.

- **Gestión documental completa:** Los paquetes
  Gestion_Documental/_/*.dtsx abarcan revisiones, anexos, secciones y
  ficheros, proporcionando una gestión integral de los documentos.

- **Interfaces con MEL y materiales:** Los paquetes MEL_LME/_/*.dtsx
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

## 3.2. MASQL20142/SQL20142 – (MASQL20222)

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

## La instancia alberga exclusivamente la base de datos Necor@NC, empleada por los módulos de ingeniería y aplicaciones internas como ECADAT. Su integración con SAP se limita a las operaciones de catálogo de materiales mediante HojasCatálogo. Los enlaces externos son reducidos; la transferencia principal se dirige a NECORANET para consolidación de datos.

Pese a su carácter legacy, la plataforma continúa operativa mientras
persistan las dependencias funcionales de los módulos de ingeniería. Su
retirada definitiva está condicionada a la migración completa de dichos
esquemas y rutinas a versiones superiores de SQL Server.

## 3.3. MASQL20142/NECORANET – (MASQL20222)

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
  mediante tabla log /_Audit_Changes. o Normalización de estructuras
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

## 3.4. MASQL20221/SQLTURK

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
legacy MASQL2014/SQLTURK.

## 3.5. MASQL20221/SQLNORWAY

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
instancia legacy MASQL2014/SQLNORWAY.

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
<th style="text-align: left;">ODBC fijo → MASQL20171/HOSTDB2 (puerto
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

<img src="C:/PROYECTOS_GPT/wiki_documental/wiki/assets/media/image1.jpg"
style="width:7.18472in;height:1.78403in" />

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

