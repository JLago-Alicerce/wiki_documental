---
source: 20221130_SeguimientoTraspasoConocimientos.md
doc_source: 20221130_SeguimientoTraspasoConocimientos.docx
created: 2025-06-13T05:51:56.755173
---
# Situación actual

La vía principal de soporte es el Service Desk de Navantia, pero algunas
de las incidencias/solicitudes no quedan registradas en el sistema
debido a que en algunos casos, las herramientas como el correo o el uso
de Teams, hacen más fluida la comunicación y finalmente la resolución
del incidente, véase InterArma, solicitudes Información GD Históricos,
servicios de correo e Interfaces con SAP, además de soporte propio a la
DTI y terceros (Plexus/Accenture)

1.  **Necor@V6**

- Resolviendo SD en cuanto a la solicitud constate de nuevos accesos al
  aplicativo. El uso es mayor por la necesidad de consulta de
  documentación base para los desarrollos de programas (buques) nuevos.

- Resolución de SD relacionadas con incidencias genéricas por
  obsolescencia de componentes para VB 6.

- Resolviendo SD de problemas de accesos a documentación.

- Alta de Personal para asignación de Taquillas. Nueva petición para
  integración SAP.

  1.  **PDB**

<!-- -->

- Apoyo en la gestión de solicitudes de accesos a PDB

- Cargas a PDB de proyectos históricos

  1.  **Clientes Externos**

<!-- -->

- Colapso por modificación masivas de Materiales desde SAP. Modificado
  de característica que afectó a los servicios de SAP y Nécora.

- Carga de Hojas Catálogo y Materiales con familias no tipadas aún en
  PDB. (tipo M)

- Revisión de procesos de carga diaria y por petición de usuarios tanto
  finales como de la DTI.

# Situación actual

Atendiendo procesos de carga masiva a través de JOBs y revisión de
notificaciones automáticas.

1.  **Ecadat**

- Revisión de aplicativo, extracción, transformación y carga de
  información entre distintos sistemas JOBs y entornos (ETL).

  1.  **ETLs**

- Procesos de traspaso de información de PDB a cliente externo.
  (Australia, Noruega y Turquía)

  1.  **Procesos manuales**

- La carga de información conlleva la carga de Datos Maestros que, en
  algunos casos, requiere la intervención manual para este tipo de
  carga. Además de esto, se requiere también de un análisis para adaptar
  la información que tiene origen distinto a Necora como es el caso de
  WindChill/ProjectWise (Astillero San Fernando)

# Situación actual

1.  **InterArma**

Tras la realización de todas las tareas adquiridas y desarrolladas a día
de hoy sólo se está dando soporte.

- Resolución de incidencias debido a desincronización de comunicaciones
  Armada-Navantia.

- Resolución de incidencias propias del aplicativo.

- Peticiones solicitadas por usuarios finales, como son, nuevas tarifas.

**<span class="mark">Está previsto que InterArma deje de tener
funcionalidad en los próximos meses</span>**

### Comunicación sistema Armada – Galia

Se puede definir como un sistema de registro y notificación
complementario a InterArma para el registro automático de Presupuestos y
notificaciones a los actores, acorde al estado de estos presupuestos.

- Notificación en los cambios de estado de estos o incluso en el avance
  de los trabajos de reparaciones realizados

- Control y Monitorización en el envío/recepción.

- Resolución de incidencias en el envío/recepción. En comunicación
  constante con Navantia/Armada.

  1.  **Línea de desarrollo**

En proceso de desarrollo de mejora de funcionalidad, línea de desarrollo
Galia en la que se está realizando el traslado de toda la lógica actual
a un sistema de servicios que mejore y facilite la trazabilidad y
mantenimiento de la herramienta.

La idea actual que se está siguiendo en la línea de desarrollo es la
creación de dos servicios independientes:

- Uno de ellos se encargará de revisar el correo y guardarlo con la
  posibilidad de escalarlo a más comunicaciones, no sólo la actual.

- Otro se encargaría de procesar la información registrada, pudiendo
  tener una mejor trazabilidad y escalabilidad.

# Situación actual

- Asegurar la comunicación de la información entre sistemas SAP y
  Necora/PDB.

- En comunicación con Navantia/Accenture para asegurar la confirmación
  de Integración y resolución a errores.

- Posibilidad de añadir a corto plazo más sistemas a la comunicación
  (Gopyp)

- Actualmente Gopyp requiere información concerniente a los
  Proyectos/Grafos por lo que se requiere de nuevos mantenimientos.

- Añadir más datos maestros de SAP como son las Hojas de Catálogo o
  Personal (Empleados)

- El uso de Datos Maestros en PDB y Gopyp hace necesario que cada vez se
  tenga más entidades actualizadas.

  1.  **Línea de desarrollo**

Para mejorar los mantenimientos, pruebas, resolución de errores; el
código actual de T-SQL (procedures) será migrado a C# para mantener una
única fuente de codificación, por lo que se migrará código de .Net FK
4.8 a .Net 6 en diversos servicios.

Estos servicios que se dividirán por entidad (Materiales, Proveedores y
Proyecto) posibilitan la traza de errores, depuración de código y
despliegues con menor impacto, además integrarán la mensajería abriendo
la posibilidad de añadir un gestor de colas para que se consuma a través
de NecoraNet (sistema actual), GOPYP 4.0 u otros aplicativos que lo
requieran.

Este planteamiento de arquitectura sería un siguiente paso en la mejora
de trazabilidad y escalabilidad de la aplicación, con esto queremos
decir que, si existen nuevas entidades para integrar en SAP, como
Empleados y Hojas de Catálogo, se podría dar una rápida respuesta y
además facilitaría el integrar otras aplicaciones que consuman esta
información.

# Situación actual

Con el fin de unificar en una única app la gestión de procesos se está
realizando un análisis de esta arquitectura Radar para la posibilidad de
nuevos desarrollos. Actualmente PDB y EOLO están en uso de este tipo de
arquitectura.

Elaboración y mantenimiento de un manual y guía rápida para la creación
de proyectos en PDB usando Radar.  
Esta guía contiene una explicación para poder crear y ejecutar proyectos
en Radar, así como pasos a seguir para integrar, depurar y testear.

Contribuir a dar un mejor soporte a usuarios finales y DTI en cuanto a
resolución de problemas tanto técnicos como lógicos (pe: ciclos de vida
de un plano)

Se están manteniendo reuniones frecuentes con DTI Navantia para la
presentación de proyecto en Test, pendiente de feedback por Navantia y
usuarios finales para mejora de procesos

1.  **Línea de desarrollo**

Se está trasladando las funcionalidades más activas de Necor@V6 al
aplicativo NecoraNet con arquitectura Radar. Este traslado exige también
un modelo de datos nuevos y la migración de la información a
NecoraNet.  
  
Actualizando para Radar 3.0 con Entity Framework 6 y guía de despliegue
de aplicaciones, Script de BBDD y carga de información

A día de hoy se está en fase de entrega de Gestión de Taquillas y
Vestuarios y a futuro se pretende migrar las funcionalidades de Pases de
vehículo y Gestión Herramental

Junto a los puntos anteriores se actualizará la documentación ya
existente para que esté disponible tanto para Navantia como terceros.

# Situación actual

1.  **Migración de Bases de Datos SQL Server**  
    Reducir el número de Motores SQL Server obsoletos o con riesgos de
    seguridad.  
    Mínima versión SQL Server />= 2012.  
    Base de datos de test para Proyectos con Clientes Externos
    (Australia, Noruega y Turquía).  
    Base de datos de Producción para aplicativos como InterArma o Gestor
    de Notificaciones Galia.

2.  **Migración de aplicaciones para ejecutar en W10**  
    Evitar uso de SO con obsolescencia o sin soporte estableciendo
    versiones mínimas como son Windows 10 y Windows Server 2008.  
    En proceso de migración de código existente en VSS (Visual Source
    Safe) a TFS y posibilidad de ejecutar aplicaciones desarrolladas en
    VB6 en equipos W10. Pendiente InterArma.

