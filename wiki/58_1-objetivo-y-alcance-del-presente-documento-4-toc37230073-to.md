---
source: Plan de Pruebas-v.01.00.md
doc_source: Plan de Pruebas-v.01.docx
created: 2025-06-13T05:51:57.978668
---
# [1 OBJETIVO Y ALCANCE DEL PRESENTE DOCUMENTO. [4](#_Toc37230073)](#_Toc37230073)

[2 Pasos de la migración [5](#_Toc37230074)](#_Toc37230074)

[3 Documentos relacionados [6](#_Toc37230075)](#_Toc37230075)

[3.1 Plan de pruebas (/*.docx). [6](#_Toc37230076)](#_Toc37230076)

[3.2 Scripts de Plan de pruebas (/*.sql).
[6](#_Toc37230077)](#_Toc37230077)

[3.3 Resultado de Plan de pruebas (/*.xlsx).
[6](#_Toc37230078)](#_Toc37230078)

[3.4 Documentos adicionales [6](#_Toc37230079)](#_Toc37230079)

[4 PASO1: Migración de DB2 a STAGING (DB2T)
[7](#_Toc37230080)](#_Toc37230080)

[4.1 Resumen de validaciones [7](#_Toc37230081)](#_Toc37230081)

[4.2 Mismas tablas en D2T y en alcance
[7](#_Toc37230082)](#_Toc37230082)

[4.3 Creación de tablas [7](#_Toc37230083)](#_Toc37230083)

[4.4 Mismas columnas en las tablas de ambas bases de datos
[8](#_Toc37230084)](#_Toc37230084)

[4.5 Mismo tipo de datos en columnas de ambas BBDD
[9](#_Toc37230085)](#_Toc37230085)

[4.6 Misma cantidad de registros en tablas de ambas BBDD
[11](#_Toc37230086)](#_Toc37230086)

[4.7 Mismos datos numéricos en los registros de las tablas de ambas BBDD
[12](#_Toc37230087)](#_Toc37230087)

[4.8 Mismos datos de fechas en los registros de las tablas de ambas BBDD
[13](#_Toc37230088)](#_Toc37230088)

[4.9 Mismos datos de tipo texto en los registros de las tablas de ambas
BBDD [14](#_Toc37230089)](#_Toc37230089)

[4.10 Mismos datos en los registros de las tablas de ambas BBDD (EXCEPT)
[20](#_Toc37230090)](#_Toc37230090)

[4.11 Mismos datos en los registros de las tablas de ambas BBDD
(Hashbytes) [20](#_Toc37230091)](#_Toc37230091)

[5 PASO2: Migración de MAHOST a DB2T [21](#_Toc37230092)](#_Toc37230092)

[5.1 Resumen de validaciones [21](#_Toc37230093)](#_Toc37230093)

[5.2 Mismas tablas creadas en ambas bases de datos
[21](#_Toc37230094)](#_Toc37230094)

[5.3 Mismas columnas en las tablas de ambas bases de datos
[22](#_Toc37230095)](#_Toc37230095)

[5.4 Mismo tipo de datos en columnas de ambas BBDD
[22](#_Toc37230096)](#_Toc37230096)

[5.5 Misma cantidad de registros en tablas de ambas BBDD
[22](#_Toc37230097)](#_Toc37230097)

[5.6 Mismos datos en los campos numéricos
[23](#_Toc37230098)](#_Toc37230098)

[5.7 Mismos datos en los campos fecha
[23](#_Toc37230099)](#_Toc37230099)

[5.8 Mismos datos en los campos texto
[23](#_Toc37230100)](#_Toc37230100)

[5.9 Mismos datos en los registros de las tablas de ambas BBDD (EXCEPT)
[23](#_Toc37230101)](#_Toc37230101)

[5.10 Mismos datos en los registros de las tablas de ambas BBDD
(Hashbytes) [23](#_Toc37230102)](#_Toc37230102)

[6 PASO3: Migración de FESRV014 a MASQL20171
[24](#_Toc37230103)](#_Toc37230103)

[6.1 Resumen de validaciones [24](#_Toc37230104)](#_Toc37230104)

[6.2 Mismas tablas creadas en ambas bases de datos
[24](#_Toc37230105)](#_Toc37230105)

[6.3 Mismas columnas en las tablas de ambas bases de datos
[24](#_Toc37230106)](#_Toc37230106)

[6.4 Mismo tipo de datos en columnas de ambas BBDD
[25](#_Toc37230107)](#_Toc37230107)

[6.5 Misma cantidad de registros en tablas de ambas BBDD
[25](#_Toc37230108)](#_Toc37230108)

[7 PASO4: Migración de NECOR@NC a NEWPRYC
[26](#_Toc37230109)](#_Toc37230109)

[7.1 Resumen de validaciones [26](#_Toc37230110)](#_Toc37230110)

[7.2 Mismas tablas creadas en ambas bases de datos
[26](#_Toc37230111)](#_Toc37230111)

[7.3 Mismas columnas en las tablas de ambas bases de datos
[27](#_Toc37230112)](#_Toc37230112)

[7.4 Mismo tipo de datos en columnas de ambas BBDD
[28](#_Toc37230113)](#_Toc37230113)

[7.5 Misma cantidad de registros en tablas de ambas BBDD
[29](#_Toc37230114)](#_Toc37230114)

[7.6 Mismos valores en los registros de las tablas de ambas BBDD
(EXCEPT) [29](#_Toc37230115)](#_Toc37230115)

[7.7 Mismos datos en los registros de las tablas de ambas BBDD
(Hashbytes) [30](#_Toc37230116)](#_Toc37230116)

[8 PASO5: Migración de DB2T a NEWPRYC
[32](#_Toc37230117)](#_Toc37230117)

[8.1 Resumen de validaciones [32](#_Toc37230118)](#_Toc37230118)

[8.2 Mismas tablas creadas en ambas bases de datos
[32](#_Toc37230119)](#_Toc37230119)

[8.3 Mismas columnas en las tablas de ambas bases de datos
[32](#_Toc37230120)](#_Toc37230120)

[8.4 Mismo tipo de datos en columnas de ambas BBDD
[33](#_Toc37230121)](#_Toc37230121)

[8.5 Misma cantidad de registros en tablas de ambas BBDD
[33](#_Toc37230122)](#_Toc37230122)

[8.6 Mismos valores en los registros de las tablas de ambas BBDD
(EXCEPT) [35](#_Toc37230123)](#_Toc37230123)

[8.7 Mismos datos en los registros de las tablas de ambas BBDD
(Hasbytes) [35](#_Toc37230124)](#_Toc37230124)

1.  <span id="_Toc37230073" class="anchor"></span>OBJETIVO Y ALCANCE DEL
    PRESENTE DOCUMENTO.

En el presente documento se pretende analizar un Plan de Pruebas que
valide las cargas de tablas desde DB2 a PRYC y aporte evidencia de que
las tablas en origen y destino son iguales (o que contienen los mismos
registros que hayan sido filtrados; p.ej ESTABL/</>’7’) en el proyecto
Migración Host.  
  
El objetivo es tener preparado el Plan de Pruebas para repetirlo el día
en que se congele el acceso al Host, se impidan nuevas
inserciones/cambios/borrados y se vuelque el contenido en Alcance a la
base de datos de Staging en el servidor de SQL Server 2017.

En cada apartado se detallan los ficheros con las consultas a lanzar
para repetir cada validación, casos que quedan excluidos (filtrados) y
el resultado esperado.

1.  <span id="_Toc37230074" class="anchor"></span>Pasos de la migración

Se han considerado tres pasos en la migración:

- Paso 1: de host DB2 -/> al servidor SQLServer MASQL20171/HOSTDB2, base
  de datos DB2T (es una copia exacta de las tablas origen dentro de
  alcance). Incluye paquetes que cargan desde ficheros.

  - Se ejecuta en SSMS /> SQl Server Agent /> Jobs /> el job
    ‘2.MoveDataDB2ToSQLServer’

> Contiene

- PackageNEC.dtsx

- PackageCORAL.dtsx

- PackageNOMINASQ.dtsx

- PackageREPU.dtsx

- PackageDES.dtsx,

<!-- -->

- Paso 2: carga de MAHOST a /[MASQL20171/HOSTDB2/], esquema a esquema,
  de todas las tablas que haya en {DBFERR,DBCART,DBMADR,DBSFER} a DB2T.

> Contiene

- PackageMAHOST_a_DB2T.dtsx

<!-- -->

- Paso 3: de FESRV014 a /[MASQL20171/HOSTDB2/]

  - Se ejecuta en SSMS /> SQL Server Agent /> Jobs /> el job
    ‘6.MoveAppAuxToNewNecor@’

> Contiene

- PackageAlmacenesIntermedios.dtsx

- PackageControlAsuntos.dtsx

- PackageControlDoc.dtsx

- PackageGestionHerramental.dtsx

- PackageNecor@.dtsx

- PackageNecor@.dtsx

- PackageSubContratas.dtsx

<!-- -->

- Paso 4: del servidor SQLServer MASQL20142/SQL20142, base de datos PRYC
  -/> servidor SQLServer MASQL20171/HOSTDB2, bases de datos NEWPRYC

  - Se ejecuta job ‘3.MoveDataPrycToNewPryc’

> Contiene

- PRYC_a_NEWPRYC.dtsx

<!-- -->

- Paso 5: del servidor SQLServer MASQL20171/HOSTDB2, base de datos
  intermedia DB2T -/> servidor SQLServer MASQL20171/HOSTDB2, bases de
  datos NEWPRYC

  - Se ejecuta job ‘4.MoveDataMirrorDB2ToNewPryc’

> Contiene

- 1.CORAL.dtsx

- 2.ORDENES.dtsx

- 3.DEMANDAS.dtsx

- 4.PEDIDOS.dtsx

- 5.HISTORICOS.dtsx

- 6.OTROS.dtsx

- 7.DESCRIPCIONES.dtsx

2.  <span id="_Toc37230075" class="anchor"></span>Documentos
    relacionados

En cada paso se han creado tres ficheros:

1.  <span id="_Toc37230076" class="anchor"></span>Plan de pruebas
    (/*.docx).

Por comodidad, es un único documento (este documento) donde se definen
las validaciones realizadas y conclusión de cada una de ellas, con un
capítulo por cada paso mencionado arriba.

2.  <span id="_Toc37230077" class="anchor"></span>Scripts de Plan de
    pruebas (/*.sql).

Consultas utilizadas en cada una de las validaciones.

PASO1: queryCheckDataDB2_DB2T.sql

PASO2: queryCheckDataMAHOST_DB2T. sql

PASO3: queryCheckDataFESRV014_MASQL0271.sql

PASO4: queryCheckDataNecor@NC_NEWPRYC.sql

> queries_ExceptQueries_NecoraNC_NEWPRYC. sql

PASO5: queryCheckDataDB2T_NEWPRYC.sql

> queries_ExceptQueries_DB2T_NEWPRYC. sql
>
> queries_Hashbytes_DB2T_NEWPRYC. sql

3.  <span id="_Toc37230078" class="anchor"></span>Resultado de Plan de
    pruebas (/*.xlsx).

- 1.Plan de Pruebas DB2-DB2T.xlsx

- 2.Plan de Pruebas MAHOST-DB2T.xlsx

- 3.Plan de Pruebas FESRV014_MASQL0271.xlsx

- 4.Plan de Pruebas NECOR@NC-NEWPRYC.xlsx

- 5.Plan de Pruebas DB2T vs NEWPRYC.xlsx

> Cada solapa es el resultado devuelto por las distintas consultas
> empleadas.

1.  <span id="_Toc37230079" class="anchor"></span>Documentos adicionales

DTI-MIGRACION-HOST_AnexoTablas-R00.xlsx define las tablas en DB2 dentro
de alcance en la migración.

3.  <span id="_Toc37230080" class="anchor"></span>PASO1: Migración de
    DB2 a STAGING (DB2T)

    1.  <span id="_Toc37230081" class="anchor"></span>Resumen de
        validaciones

Este apartado resume las validaciones para comparar las tablas cargadas
en destino (DB2T) versus las de origen (DB2)

ORIGEN: FESRV053 (base de datos Prueba)

> Que accede al HOST (DB2) usando sentencias OPENQUERY

DESTINO: MASQL20171/HOSTDB2 (base de datos DB2T)

En cada capítulo se resumen las validaciones realizadas y su resultado.

2.  <span id="_Toc37230082" class="anchor"></span>Mismas tablas en D2T y
    en alcance

CASOS CONSIDERADOS  
Caso de Uso

- Las tablas dentro de alcance son las marcadas con columna

· M(1)=S

· M(1)=N con ¿Migrar?=S

en el Excel “DTI-MIGRACION-HOST_AnexoTablas-R00.xlsx”.

- Tampoco se consideran las siguientes tablas auxiliares:

  - '/_filterTables' : Tabla para parametrizar consultas

  - '/_/_LOGCARGA': Tabla con log de las tablas cargadas y registros en
    origen y destino

  - 'sysssislog': Log interno de SQLServer

  - '/_REGISTROS_DB2_DB2T': Tabla que se usa en la validación de tipos
    de datos

  - '/_BO06DES_EXCLUDE','/_NC06DES_EXCLUDE','/_NC36DES_EXCLUDE','/_PE46DES_EXCLUDE'
    : Tablas donde se conservan los registros duplicados de las
    correspondientes tablas VSAM.

EJECUCIÓN DE LA VALIDACIÓN

Consulta 1.1 del fichero ‘queryCheckDataDB2_DB2T.txt’

- Compara las tablas obtenidas en DB2T con las del alcance del Excel.

RESULTADO de consulta 1.1

Todas existen en DB2T.

Son 1113 tablas las que se migran desde DB2, segun
‘DTI-MIGRACION-HOST_AnexoTablas-R00.xlsx ‘

CONCLUSIÓN

Todo OK

1.  <span id="_Toc37230083" class="anchor"></span>Creación de tablas

CASOS CONSIDERADOS  
Caso de Uso

- Las tablas dentro de alcance son las marcadas con columna

· M(1)=S

· M(1)=N con ¿Migrar?=S

en el Excel “DTI-MIGRACION-HOST_AnexoTablas-R00.xlsx”.

- Tampoco se consideran las siguientes tablas auxiliares:

  - '/_filterTables' : Tabla para parametrizar consultas

  - '/_/_LOGCARGA': Tabla con log de las tablas cargadas y registros en
    origen y destino

  - 'sysssislog': Log interno de SQLServer

  - '/_REGISTROS_DB2_DB2T': Tabla que se usa en la validación de tipos
    de datos

  - '/_BO06DES_EXCLUDE','/_NC06DES_EXCLUDE','/_NC36DES_EXCLUDE','/_PE46DES_EXCLUDE'
    : Tablas donde se conservan los registros duplicados de las
    correspondientes tablas VSAM.

EJECUCIÓN DE LA VALIDACIÓN

Consulta 1.2a del fichero ‘queryCheckDataDB2_DB2T.txt’

- Obtiene el nombre de las tablas en la base de datos sistema destino

- Obtiene el nombre de las tablas en DB2

- Compara ambos listados

RESULTADO de ejecutar la consulta 1.2:

Se obtienen 1113 en DB2 y 1113 en DB2T. Incluye las tablas CORAL y
FAAL020, que son 2 ficheros VSAM por crear la estructura en DB2T.

1.  <span id="_Toc37230084" class="anchor"></span>Mismas columnas en las
    tablas de ambas bases de datos

CASOS CONSIDERADOS

Las tablas que no son auxiliares, comentadas en los puntos anteriores.

EJECUCIÓN DE LA VALIDACIÓN

Consulta 1.3 del fichero ‘queryCheckDataDB2_DB2T.txt’

- Obtiene el nombre de las tablas en la base de datos sistema destino

- Obtiene el nombre de las tablas en DB2

- Compara ambos listados

RESULTADO de ejecutar la consulta 1.3:

<img src="assets/media/) 🡪OK

2.  La columna PD05.PEDIDOS.PEDIDO tiene posición 1. Y existe en la
    misma posición en PD05.PEDIDOS.PEDIDO (fila 1 del resultado a la
    derecha) -/> Ok

NOTA: en Excel de alcance de la migración, cargamos la tabla PEDIDOS
desde DBLOGI.CORAL a DB2T.dbo.PEDIDOS y desde DBSFER.PD05 a
DB2T.PD05.PEDIDOS. Como la consulta no cruza por esquema, le aparecen 2
líneas con COLNO distinto.

<img src="assets/media/) y no en DB2T. En
    ‘DTI-MIGRACION-HOST_AnexoTablas-R00.xlsx’ se indica que PLAN_TABLE
    no se carga desde NEC sino desde CTUSER (En CTUSER.PLAN_TABLE no
    existen esos 2 campos del final) -/> Todo OK.

CONCLUSIÓN

Todo OK.

1.  <span id="_Toc37230085" class="anchor"></span>Mismo tipo de datos en
    columnas de ambas BBDD

CASOS CONSIDERADOS

Las tablas que no son auxiliares, comentadas en los puntos anteriores.

> NOTA: ‘PROVCL’ no existe en DB2. Es un fichero VSAM

1.  Se ha establecido la correspondencia de tipo de dato en DB2 y DB2T
    indicada en la tabla de abajo. Aunque en
    DB2T.<span class="mark">sysibm.syscolumns</span> y
    <span class="mark">INFORMATION_SCHEMA.COLUMNS</span>, los campos
    tienen definido distinto tipo, longitud, escala -/> se trata de
    tipos equivalentes para guardar el valor de origen en destino. No se
    pierde información (es un tipo homólogo o de mayor longitud) y
    veremos en las siguientes validaciones que los datos cargados son
    idénticos a origen (es correcto el tipo de dato y longitud con el
    que se ha definido el campo en destino).

<table style="width:100%;">
<colgroup>
<col style="width: 33%" />
<col style="width: 9%" />
<col style="width: 14%" />
<col style="width: 10%" />
<col style="width: 10%" />
<col style="width: 11%" />
<col style="width: 9%" />
</colgroup>
<thead>
<tr>
<th colspan="4" style="text-align: center;"><strong>En DB2 aparece este
tipo y longitud</strong></th>
<th colspan="3" style="text-align: center;"><strong>En DB2T
veremos</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td><strong><mark>TABLAS</mark></strong></td>
<td><strong><mark>COLTYPE</mark></strong></td>
<td><strong><mark>LENGTH</mark></strong></td>
<td><strong><mark>SCALE</mark></strong></td>
<td><strong><mark>DATA_TYPE</mark></strong></td>
<td><strong><mark>CHARACTER_ MAXIMUM_ LENGTH/ NUMERIC_
PRECISION</mark></strong></td>
<td><strong><mark>NUMERIC_ SCALE</mark></strong></td>
</tr>
<tr>
<td></td>
<td>CHAR</td>
<td>n</td>
<td>0</td>
<td>nchar</td>
<td>n</td>
<td>0</td>
</tr>
<tr>
<td></td>
<td>INTEGER</td>
<td>4</td>
<td>0</td>
<td>int</td>
<td>10</td>
<td>0</td>
</tr>
<tr>
<td></td>
<td>SMALLINT</td>
<td>2</td>
<td>0</td>
<td>smallint</td>
<td>5</td>
<td>0</td>
</tr>
<tr>
<td></td>
<td>DECIMAL</td>
<td>x</td>
<td>y</td>
<td>numeric</td>
<td>x</td>
<td>y</td>
</tr>
<tr>
<td></td>
<td>LONGVAR</td>
<td></td>
<td></td>
<td>NTEXT</td>
<td></td>
<td></td>
</tr>
<tr>
<td>Tablas donde TBCREATOR='NEC' (porque se lee desde fichero que no
permite cargar a ntext)</td>
<td>LONGVAR</td>
<td><table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th>32648</th>
</tr>
</thead>
<tbody>
<tr>
<td>32676</td>
</tr>
<tr>
<td>32678</td>
</tr>
<tr>
<td>32684</td>
</tr>
</tbody>
</table></td>
<td>0</td>
<td>text</td>
<td>2147483647</td>
<td>0</td>
</tr>
<tr>
<td></td>
<td>TIMESTMP</td>
<td>10</td>
<td>6</td>
<td>datetime</td>
<td>null</td>
<td>null</td>
</tr>
<tr>
<td><p>'GB_AUDITOR',</p>
<p>'GC_AUDITOR',</p>
<p>'MAT_SOL_DESP',</p>
<p>'MPF_AUDITOR',</p>
<p>'MPF_GC_AUDITOR',</p>
<p>'PER_DAT_AUDI',</p>
<p>'PLAN_TABLE'</p></td>
<td>TIMESTMP</td>
<td>10</td>
<td>6</td>
<td>datetime2</td>
<td>null</td>
<td>null</td>
</tr>
<tr>
<td><p>'PPF_CCAL_PROV','PPF_CONS_CAB',</p>
<p>'PPF_CONS_OFER','PPF_CONS_PAR',</p>
<p>'PPF_CONS_PLENV','PPF_CONS_PROV',</p>
<p>'PPF_MAT_ACOMP','PPF_MAT_ACOMPB',</p>
<p>'PPF_MAT_CCONC','PPF_MAT_COD_SUS',</p>
<p>'PPF_MAT_DIS_NEG','PPF_MAT_MOV',</p>
<p>'PPF_MAT_PED_ENT','PPF_MAT_SIT',</p>
<p>'PPF_MODELOS','PPF_OBC_CAR',</p>
<p>'PPF_OBC_FALTAS','PPF_OBC_PZAS',</p>
<p>'PPF_OBS_COMP','PPF_PIDA',</p>
<p>'PPF_PRECAL_ENV','PPF_VAL_CAR','PCOR02'</p></td>
<td>DATE</td>
<td>4</td>
<td>0</td>
<td>datetime</td>
<td>null</td>
<td>null</td>
</tr>
<tr>
<td>'PED_DAT_AUX', 'PPF_CONS_OFER', 'PPF_CONS_PAR', 'PPF_CONS_PLENV',
'PPF_EST_CFU_COM', 'PPF_EST_MON_CAB', 'PPF_EST_PSU_COM',
'PPF_MAT_ACOMP', 'PPF_MAT_ACOMPB', 'PPF_MAT_CAR2', 'PPF_MAT_CAR2',
'PPF_MAT_CAR3', 'PPF_MAT_CAR3', 'PPF_MAT_CAR3', 'PPF_MAT_CAR3',
'PPF_MAT_PAR', 'PPF_MAT_PED', 'PPF_MAT_PED', 'PPF_MAT_PED',
'PPF_MAT_PED_ENT', 'PPF_MAT_PED_ENT', 'PPF_MAT_PED_MOD', 'PPF_MAT_SUM',
'PPF_MAT_TRAB', 'PPF_MAT_TRAB', 'PPF_MODELOS', 'PPF_NOT_ENV',
'PPF_OBC_CAR', 'PPF_OBS_COMP'</td>
<td>VARCHAR</td>
<td>z</td>
<td>0</td>
<td>nvarchar</td>
<td>z</td>
<td>0</td>
</tr>
<tr>
<td>'BO06DES','NC06DES','NC36DES','PE46DES'</td>
<td>VARCHAR</td>
<td>32672</td>
<td>0</td>
<td>text</td>
<td>2147483647</td>
<td></td>
</tr>
</tbody>
</table>

En el caso de DATE el valor contiene fecha+hora (21/12/2018
00:00:00.000) por lo que se ha conservado datetime como tipo destino.

RESULTADO de ejecutar la consulta 1.4:

Se observan estas diferencias entre las BBDD origen y destino.

<img src="assets/media/), encuentra que el campo PEDIDO tiene COLNO 1 y
> 2, y le aparece como posible discrepancia.
>
> <img src="assets/media/) y en DB2T
  con TIME(10)

> <img src="assets/media/). En DB2, TIME tiene longitud (3). En SQLServer le asigna por
> defecto longitud(10). Los valores se conservan idénticos, por lo
> podemos hacer asignar length(10) en la consulta.

<img src="assets/media/), no se carga
  desde NEC de DB2. Por tanto, los 2 campos extra que aparecen en NEC no
  tienen que estar en destino DB2T-/> OK, no son 2 campos de
  discrepancia, porque NEC.PLAN_TABLE no está en alcance.

- Normalmente el tipo TIMESTMP se define en destino como datetime. En
  las tablas indicadas arriba aparecen campos de fecha (con TIMESTMP)
  con valores en formato datetime2. En esas tablas, es correcto definir
  datetime2 como tipo en destino.

<img src="assets/media/)

- <span class="mark">‘PROVCL’ no existe en DB2. Es un fichero VSAM a
  pedir actualizado</span>

- Estas 4 tablas de NEC ('BO06DES','NC06DES','/_NC36DES','PE46DES') se
  cargan desde fichero.

- Recordar que PCOR01 se carga desde MAHOST

- Recordar que ALTAMA,BO11SQ,BO16SQ,BO21SQ,BO22SQ,BO40SQ,BO61SQ,
  BRIONTXT,NC39SQ,NC41SQ,PE11SQ,PECENT,TTEXTOS se cargan por OPENQUERY
  (inicialmente desde fichero)

RESULTADO de ejecutar la consulta 1.5:

- No se observan discrepancias en el número de registros entre origen
  DB2 y destino DB2T. El número de registros distintos en la siguiente
  tabla auxiliar

<span class="mark">select /* from dbo.REGISTROS_DB2_DB2T</span>

son tablas cuyo origen es fichero.

<img src="assets/media/)

> Se indican a continuación tablas que siguen creciendo o con fichero
> desactualizado, que pueden requerir una recarga cuando se vuelvan a
> comprobar el número de filas.

| **TABLE_NAME** | **Razón**              |
|----------------|------------------------|
| BH12SQ         | Fichero desactualizado |
| BH15SQ         | Fichero desactualizado |
| BH18SQ         | Siguen creciendo       |
| BH40SQ         | Fichero desactualizado |
| BO11SQ         | Siguen creciendo       |
| BO12SQ         | Fichero desactualizado |
| ENLACES        | Siguen creciendo       |
| GENFI2         | Siguen creciendo       |
| NC08SQ         | Fichero desactualizado |
| NC10SQ         | Siguen creciendo       |
| NC11SQ         | Siguen creciendo       |
| NC12SQ         | Fichero desactualizado |
| NC13SQ         | Siguen creciendo       |
| NC14SQ         | Siguen creciendo       |
| NC15SQ         | Siguen creciendo       |
| NC16SQ         | Fichero desactualizado |
| NC18SQ         | Siguen creciendo       |
| NC31SQ         | Siguen creciendo       |
| NC32SQ         | Fichero desactualizado |
| NC36SQ         | Fichero desactualizado |
| NC37SQ         | Siguen creciendo       |
| NC38SQ         | Siguen creciendo       |
| NH12SQ         | Fichero desactualizado |
| NH18SQ         | Siguen creciendo       |
| PE12SQ         | Fichero desactualizado |
| TACTIVIDAD     | Siguen creciendo       |
| TCARGOS        | Siguen creciendo       |
| TOBRAS         | Siguen creciendo       |
| TTEXTOS        | Siguen creciendo       |

CONCLUSION:

Todo OK (Las tablas desde fichero se validan en otro apartado).

1.  <span id="_Toc37230087" class="anchor"></span>Mismos datos numéricos
    en los registros de las tablas de ambas BBDD

Realizamos una suma en cada campo de todas las filas existentes en la
tabla DB2 y en la tabla DB2T (hay mismo número de registros). Y
comparamos el valor devuelto en cada campo (comparamos sumas en cada
columna) de las tablas de ''NEC'',''CORAL'',''REPU'',''NOMINASQ' cuyo
tipo de datos es ''DECIMAL'',''SMALLINT'',''INTEGER''.

CASOS CONSIDERADOS

Se revisan tablas con campos numéricos en DB2 vs DB2T

- ''BH12SQ'',''BH15SQ'',''BH40SQ'',''NH12SQ'' , ''BO12SQ'', ''NC08SQ'',
  ''NC12SQ'', ''NC16SQ'', ''NC32SQ'', ''NC36SQ'' vienen desde fichero.
  Los validamos en otro apartado, porque hoy están desactualizados.

- Se excluyen en la comparación entre DB2 y DB2T las tablas BO06_DES,
  NC06DES, NC36DES, PE46DES <span class="mark">(Aunque tenemos acceso
  openquery 🡪se carga desde fichero)</span>

RESULTADO de ejecutar la consulta 1.6:

Nota1: Utilizar decimal(31, 6) porque hay campos que son decimal con 5 o
6 decimales de precisión

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th><p>[dbo].[CORA200L], campo AI</p>
<p>[dbo].[CORA222T] , campo TRFA</p>
<p>[dbo].[CORA223] ], campo TRFA</p>
<p>[dbo].[CORAL101], campos VLIMCB y FIACOS</p>
<p>[dbo].[CORFUA] , campo AI</p>
<p>[dbo].[COSAL2] , campo TRFA</p>
<p>[dbo].[COSAL250] , campo ATRF</p>
<p>[dbo].[COSAL300], campo CUBE</p>
<p>[dbo].[BO63SQ], campo CANCTAPM y CANCTAP</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Nota2: En NC20SQ y NC75SQ, aunque tengan las mismas filas, pueden haber
cambiado valores. Cargando de nuevo con datos de hoy, ya no hay
discrepancias

CONCLUSION:

Todo OK (Las tablas desde fichero se validan en otro apartado, al no
estar actualizadas).

1.  <span id="_Toc37230088" class="anchor"></span>Mismos datos de fechas
    en los registros de las tablas de ambas BBDD

CASOS CONSIDERADOS

Se revisan tablas con campos fechas en DB2T

1)  ''BH12SQ'',''BH15SQ'',''BH40SQ'', ''NH12SQ'' tienen fechas pero
    vienen desde fichero. Los validamos en otro apartado, al no estar
    actualizados sus registros.

2)  Estas otras tablas tiene fechas pero vienen de MAHOST
    <span class="mark">''FA18SQ'',''NH08SQ'',''PCOR02'',''PLAN_TABLE'',''DSN_STATEMNT_TABLE'',''EVENTMDU'',''MAT_AUD_NEC'',</span>''ASRED03'',''ASREDE3'',''PCOR03'',''PCOR04'',''PCOR09'',''PCOR10'',''PCOR12'',''PCOR13'',''PCOR14'',''TSRED03'',''TSRED04'',''TSRED0E''.
    Se validan en el capítulo ‘MAHOST versus DB2T’.

3)  Se validan resto de tablas con fechas, 7 a validar:
    ''BH10SQ'',''BH18SQ'',''NH10SQ'', ''NH15SQ'', ''NH17SQ'',
    ''NH18SQ'', ''PE18SQ''

Recordar que en las tablas históricas solo se cargan los registros donde
( ( ESTABL = 'A') OR ESTABL = '2' AND CODOBRA BETWEEN '0206' AND '0216'
) OR ( ESTABL = '4' AND CODOBRA BETWEEN '0516' AND '0527' ))

Se convierten las fechas a formato ISO (yyyymmdd) entero y se realiza la
suma en cada columna fecha. Se compara la suma total en cada columna
entre DB2T y DB2.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th><p>No es posible hacer una diferencia entre cada fecha y 1970-01-01,
por ejemplo, porque DB2 no devuelve los mismos días de diferencia que en
SQLServer.</p>
<p>Ejemplo: Si restas 31.01.2016 de 01.01.2016 da 30 en Db2 y
SQLServer</p>
<p>select * from OPENQUERY(DB2P, 'select timestampdiff(16</p>
<p>, char(timestamp(''2016-02-01 00:00:00.000000'')</p>
<p>- timestamp(''2016-01-31 00:00:00.000000'')</p>
<p>)</p>
<p>) from sysibm.sysdummy1')</p>
<p>select datediff(day,cast('2016-01-31 00:00:00.000' as datetime)
,cast('2016-02-01 00:00:00.000' as datetime))</p>
<p>Pero esto ya no da el mismo valor</p>
<p>select * from OPENQUERY(DB2P, 'select timestampdiff(16</p>
<p>, char(timestamp(''2016-02-01 00:00:00.000000'')</p>
<p>- timestamp(''2016-01-01 00:00:00.000000'')</p>
<p>)</p>
<p>) from sysibm.sysdummy1') --da 30</p>
<p>select datediff(day,cast('2016-01-01 00:00:00.000' as datetime)
,cast('2016-02-01 00:00:00.000' as datetime)) --da 31<img
src="assets/media/). Two reasons - 1) The output
of TIMESTAMPDIFF() is limited to 'INTEGER', which automatically limits
the size it can be (for <em>seconds</em> this means the end of the epoch
is 2038). 2) The output of the difference of the two timestamps is an
imprecise <strong>interval</strong>, which is why the function can only
return an <strong>ESTIMATE</strong> (I mean, seriously, IBM?) - this is
because interval is divorced from information that would help it
determine needed information, like daylight savings time, or leap
years. </p>
<p>I don't think
(TimeZone.CurrentTimeZone.ToUniversalTime(sqlLocalDate.Value)) will work
for ALL historical dates "The ToUniversalTime method recognizes only the
current daylight saving time adjustment rule for the local time zone. As
a result, it is guaranteed to accurately return the Coordinated
Universal Time (UTC) corresponding to a particular local time only
during the period in which the latest adjustment rule is in effect. It
may return inaccurate results if time is a historic date and time value
that was subject to a previous adjustment rule.</p></td>
</tr>
</tbody>
</table>

RESULTADO de ejecutar la consulta 1.7:

No se encuentran discrepancias en los valores de fechas cargados en DB2T
respecto a origen DB2

en
''BH10SQ'',''BH18SQ'',''NH10SQ'',''NH15SQ'',''NH17SQ'',''NH18SQ'',''PE18SQ''

1.  <span id="_Toc37230089" class="anchor"></span>Mismos datos de tipo
    texto en los registros de las tablas de ambas BBDD

CASOS CONSIDERADOS

Se revisan tablas con campos fechas en DB2T

1)  Recordar que ALTAMA, BO11SQ, BO16SQ, BO21SQ, BO22SQ, BO40SQ, BO61SQ,
    BRIONTXT,NC39SQ,NC41SQ,PE11SQ,PECENT,TTEXTOS se cargan por OPENQUERY
    (inicialmente desde fichero)

2)  ''PROVCL'', ''AUXVAL'', ''BH12SQ'', ''BH15SQ'', ''BH40SQ'',
    ''BO06DES'', ''BO12SQ'', ''BO15SQ'', ''BO46SQ'', ''BO49SQ'',
    ''FA46SQ'', ''NC06DES'', ''NC36DES'', ''PE46DES'', ''NC08SQ'',
    ''NC12SQ'', ''NC16SQ'', ''NC32SQ'', ''NC36SQ'', ''NH12SQ'',
    ''PE12SQ'', ''VALES'' vienen desde fichero. Los validamos en otro
    apartado, por estar desactualizados.

3)  Estas otras tablas vienen de MAHOST
    ''ASRED03'',''ASREDE3'',''PCOR03'',''PCOR04'',''PCOR09'',''PCOR10'',''PCOR12'',''PCOR13'',''PCOR14'',''TSRED03'',''TSRED04'',''TSRED0E''.
    Se validan en el capítulo ‘MAHOST versus DB2T’

4)  Resto se validan. Encontramos que hay campos que contienen el
    carácter hexadecimal 00 en DB2. Esos valores dan longitud/>0 cuando
    en realidad openquery lo converite a valor vacío en DB2T -/> se
    asigna longitud 0 a dicho caracter.

5)  Idem cuando existe una cadena seguida de espacios o caracteres ‘00’.
    Se consideran estos ‘00’ como espacios a los que se hace el trim y
    se da por válida la longitud del resto de la cadena (tras el trim,
    la longitud y valor coincide con lo que se ha cargado en DB2T).

6)  <span class="mark">Se observa que openquery elimina todos los
    caracteres que siguen a un carácter ‘00’, por lo que solo se carga
    en DB2T el principio de la cadena hasta ese carácter. En Db2 pueden
    existir casos donde haya caracteres tras ese/esos ‘00s’ (se ven si
    usamos la función hexadecimal de DB2), pero nunca podremos
    conocerlos usando openquery. La</span>

    1.  En NC43SQ.DESGLOSE openquery devuelve valores ‘vacíos’ desde
        DB2, cuyo hexadecimal en DB2 no son solo 00s. Hemos decidido
        suponer que su longitud es cero, por empezar por 00s. Y dejo la
        consulta por si decidimos otra cosa.

| <span class="mark">select /* from OPENQUERY(DB2P, 'SELECT DISTINCT DESGLOSE, hex(trim(DESGLOSE)) as HEXTRIM, replace(hex(DESGLOSE),''000000'','''') as REPLACE000000, case when DESGLOSE='''' or hex(trim(DESGLOSE)) LIKE ''00%0000'' then 0 else LENGTH(hex(trim(DESGLOSE)))/2 end as LONG FROM NEC.NC43SQ ') order by 2,1</span> |
|----|

<img
src="assets/media/)  En NC43SQ, hay 3 casos también con 00 por medio, con distinta
    longitud a DB2T. Openquery elimina los caracteres que sigan a un
    ‘00’

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th><p><mark>select * from OPENQUERY(DB2P, 'SELECT DISTINCT DESGLOSE,
hex(trim(DESGLOSE)) as HEXTRIM, replace(hex(DESGLOSE),''000000'','''')
as REPLACE000000, case when DESGLOSE='''' or hex(trim(DESGLOSE)) LIKE
''00%0000'' then 0 else LENGTH(hex(trim(DESGLOSE)))/2 end as LONG FROM
NEC.NC43SQ</mark></p>
<p><mark>where DESGLOSE LIKE ''9 INGLES%'' or DESGLOSE LIKE ''¯‰OBSEC99
INGLE%'' or DESGLOSE LIKE ''4z JŠö%'' or DESGLOSE LIKE ''7¯%'' or
DESGLOSE LIKE ''â%''</mark></p>
<p><mark>') order by 2,1</mark></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<img
src="assets/media/)  En NC40SQ hay estos 4 valores en DB2, con 000000 en hexadecimal que
    podrían ser cambiados por F0F0F0 . Es decir 2244 -/> 2244000A01,
    7857-/>7857000A01, 9003 -/> 9003000A01, 9003 -/> 9003000A02

