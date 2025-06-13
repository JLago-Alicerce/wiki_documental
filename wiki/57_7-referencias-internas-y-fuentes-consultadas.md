---
source: EstadoActualPlataformaBBD_V0306_10_32.md
doc_source: EstadoActualPlataformaBBD_V0306_10_32.docx
created: 2025-06-13T05:51:57.814354
---
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

1.  **Instancia: MASQL20142/NECORANET**

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

2.  **Instancia: MASQL20142/SQL20142**

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

3.  **Instancia: MASQL20171/HOSTDB2**

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

Nota: en el caso de la instancia MASQL20171/HOSTDB2 no se han incluido
las bases que comienzan por 'T/_' al considerarse entornos de prueba
(TEST) de las anteriores.

## Anexo – Inventario de Jobs por instancia

Este anexo recoge el inventario de trabajos (SQL Server Agent Jobs)
habilitados en distintas instancias SQL de Navantia, tal como aparecen
configurados en el Job Activity Monitor. Para cada job se indica si está
activo y la frecuencia estimada de ejecución-

1.  **Instancia: MASQL20171/HOSTDB2**

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

2.  **Instancia: MASQL20142/NECORANET**

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

3.  **Instancia: MASQL20221/SQLNORWAY**

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

4.  **Instancia: MASQL20221/SQLTURK**

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
