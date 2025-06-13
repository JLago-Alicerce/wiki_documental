---
source: Plan de Pruebas-v.01.00.md
doc_source: Plan de Pruebas-v.01.docx
created: 2025-06-13T05:51:57.986707
---
# <img
src="assets/media/)) when ''F2F2F4F4400000C1F0F1'' then
''2244000A01'' when ''F7F8F5F7400000C1F0F1'' then ''7857000A01'' when
''F9F0F0F3400000C1F0F1'' then ''9003000A01'' when
''F9F0F0F3400000C1F0F2'' then ''9003000A02'' else DEMANDA end as
DEMANDA</mark></p>
<p><mark>,TIPODPM,CTAALMC,PLANO,CENTRSO,CENTRDE,ZONA,BLOQUE,GRUCOSTE,PRODINT,MODULO,REDACTA,APROBAD,VISTOBN,COMPRAD,ASIGNAD,FECHDEM</mark></p>
<p><mark>,FECHNEC,FECHAPR,FECHVBN,FECHRES,FECHASG,SITAMAT,SITAOCS,SITACOM,SITAGCA,SITOFTA,DESGHOJ,DATOSEN,CTACARGO,PARTIDA,NOTAS,ANEXOS,APUNTES,TIPOPRO,PROCESS,DNI,SECUE36,REFERENCIA</mark></p>
<p><mark>FROM NEC.NC40SQ')</mark></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

3)  En DPOSTO, el campo CMAPRO cambia el char(133) por char(63) para un
    caso o valor

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th><p><mark>select * from OPENQUERY(DB2P, 'SELECT distinct CMAPRO,
hex(trim(CMAPRO)) as HEXA, case when CMAPRO='''''''' or
hex(trim(CMAPRO))=''0000000000000000000000000000000000000000'' then 0
else LENGTH(hex(trim(CMAPRO)))/2 end , UNICODE(SUBSTR(CMAPRO, 5, 1)),
UNICODE(SUBSTR(CMAPRO, 6, 1)) FROM NEC.DPOSTO where CMAPRO LIKE
''0970%'' ')</mark></p>
<p><mark>SELECT distinct CMAPRO, LEN(LTRIM(RTRIM(CMAPRO))),
UNICODE(SUBSTRING(CMAPRO,5,1)), UNICODE(SUBSTRING(CMAPRO,6,1)) from
[MASQL20171/HOSTDB2].[DB2T].[dbo].[DPOSTO] where CMAPRO LIKE
'0970%'</mark></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

# <img
src="assets/media/)  En GENFI2, el campo DATOS varía en caracteres raros en estos casos,
    a revisar si lo que se recibe en DB2T para estos 555 casos se
    considera OK (es decir, da igual que un carácter no ASCII lo haya
    convertido a ¿, por ejemplo)

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th><blockquote>
<p><mark>--POR AQUI4</mark></p>
<p><mark>select B.DATOS,B.LONG, A.* from OPENQUERY(DB2P, 'SELECT
DISTINCT DATOS, hex(trim(DATOS)) as HEXTRIM,
replace(hex(DATOS),''000000'','''') as REPLACE000000,</mark></p>
<p><mark>case when DATOS='''' or hex(trim(DATOS)) LIKE ''00%0000'' then
0 else LENGTH(hex(trim(DATOS)))/2 end as LONG</mark></p>
<p><mark>FROM NEC.GENFI2</mark></p>
<p><mark>--where DATOS LIKE ''%LJ3%''</mark></p>
<p><mark>') A full join (</mark></p>
<p><mark>SELECT DISTINCT DATOS, LEN(LTRIM(RTRIM(DATOS))) as LONG from
[MASQL20171/HOSTDB2].[DB2T].[dbo].[GENFI2] --where DATOS LIKE
'%LJ3%'</mark></p>
<p><mark>) B ON A.DATOS=B.DATOS</mark></p>
<p><mark>WHERE B.DATOS IS NULL or A.DATOS IS NULL</mark></p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

En tabla PEDIDO hay 13 valores con 00s al final, pero es el mismo valor
en DB2T

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th><p><mark>SELECT DISTINCT DESCRI, LEN(LTRIM(RTRIM(DESCRI))) as LONG
from [MASQL20171/HOSTDB2].[DB2T].[dbo].[PEDIDO]</mark></p>
<p><mark>where (DESCRI='ANULADO.' or DESCRI='BARRAS DE LATON' or
DESCRI='BRAZOLAS' or DESCRI='CABO DE NYLON. ' or DESCRI='HERRAMIENTAS'
or DESCRI='HILO DE VELA '</mark></p>
<p><mark>or DESCRI='MATERIAL ELECTRICO' or DESCRI='PEDIDO ANULADO.' or
DESCRI='PEDIDO ANULADO ' or DESCRI='TAPONES ACERO INOX. '</mark></p>
<p><mark>or DESCRI='TORNILLOS Y TUERCAS' or DESCRI='VARISTOR. ' or
DESCRI='VOLANTE PARA VALVULA')</mark></p>
<p><mark>order by 1</mark></p>
<p><mark>select * from OPENQUERY(DB2P, 'SELECT DISTINCT DESCRI,
hex(trim(DESCRI)) as HEXTRIM,</mark></p>
<p><mark>case when DESCRI='''' or hex(trim(DESCRI)) LIKE ''000000%''
then 0 when hex(trim(DESCRI)) IN
(''D6D4C4F5C4F1F0F0F74000'',''F8F9F7C3C3D7F0F8F54000'') then 9 when
(DESCRI LIKE ''OMD1%'' and LENGTH(hex(trim(DESCRI)))/2=11) then 7 else
LENGTH(hex(trim(DESCRI)))/2 end as LONG</mark></p>
<p><mark>FROM NEC.PEDIDO</mark></p>
<p><mark>where (hex(DESCRI) LIKE ''C1D5E4D3C1C4D64B%00'' or hex(DESCRI)
LIKE ''C2C1D9D9C1E240C4C540D3C1E3D6D5%00'' or hex(DESCRI) LIKE
''C2D9C1E9D6D3C1E2%00'' or hex(DESCRI) LIKE
''C3C1C2D640C4C540D5E8D3D6D54B%00''</mark></p>
<p><mark>or hex(DESCRI) LIKE ''C8C5D9D9C1D4C9C5D5E3C1E2%00'' or
hex(DESCRI) LIKE ''C8C9D3D640C4C540E5C5D3C1%00'' or hex(DESCRI) LIKE
''D4C1E3C5D9C9C1D340C5D3C5C3E3D9C9C3D6%00'' or hex(DESCRI) LIKE
''D7C5C4C9C4D640C1D5E4D3C1C4D6%00''</mark></p>
<p><mark>or hex(DESCRI) LIKE ''D7C5C4C9C4D640C1D5E4D3C1C4D64B%00'' or
hex(DESCRI) LIKE ''E3C1D7D6D5C5E240C1C3C5D9D640C9D5D6E74B%00'' or
hex(DESCRI) LIKE ''E3D6D9D5C9D3D3D6E240E840E3E4C5D9C3C1E2%00'' or
hex(DESCRI) LIKE ''E5C1D9C9E2E3D6D94B%00''</mark></p>
<p><mark>or hex(DESCRI) LIKE
''E5D6D3C1D5E3C540D7C1D9C140E5C1D3E5E4D3C1%00''</mark></p>
<p><mark>) ') order by 1</mark></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

5)  En CORA221, mismos valores salvo estos 2 (casi idénticos)

<img
src="assets/media/)  En CORA223, hay 11 valores que discrepan (casi idénticos, cambia el
    char(31))

<img
src="assets/media/)</span>

<img
src="assets/media/))) from
[MASQL20171/HOSTDB2].[DB2T].[dbo].[COSAL250] A where CSC='_ ' or CSC='_
' or LEN(LTRIM(RTRIM(A.CSC)))=0</mark></p>
<p><mark>order by 2,1</mark></p>
<p><mark>select * from OPENQUERY(DB2P, 'SELECT DISTINCT CSC,
hex(trim(CSC)) as HEXTRIM, --replace(hex(CSC),''000000'','''') as
REPLACE000000,</mark></p>
<p><mark>case when CSC='''' or hex(trim(CSC)) = ''00'' then 0 else
LENGTH(hex(trim(CSC)))/2 end as LONG</mark></p>
<p><mark>FROM CORAL.COSAL250</mark></p>
<p><mark>--where CSC LIKE ''_ %'' or CSC LIKE ''_ %''</mark></p>
<p><mark>') order by 3,2,1</mark></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

En COSAL250 también, en el campo ITNAME, hay dos discrepancias en valor
por un carácter -/> consideramos valido el valor cargado en DB2T.

# <img
src="assets/media/))) as LONG
from [MASQL20171/HOSTDB2].[DB2T].[dbo].[COSAL250] where ITNAME LIKE
'PASTA SOLDAR ESTA?O%' or ITNAME LIKE 'REGLAMENTO SE?ALES N%'</mark></p>
<p><mark>select * from OPENQUERY(DB2P, 'SELECT DISTINCT ITNAME,
hex(trim(ITNAME)) as HEXTRIM,</mark></p>
<p><mark>case when ITNAME='''' or hex(trim(ITNAME)) = ''0000%'' then 0
else LENGTH(hex(trim(ITNAME)))/2 end as LONG</mark></p>
<p><mark>FROM CORAL.COSAL250</mark></p>
<p><mark>where ITNAME LIKE ''PASTA SOLDAR ESTA%'' or ITNAME LIKE
''REGLAMENTO SE%''</mark></p>
<p><mark>') order by 3,2,1</mark></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

EN FAAL04, hay 5 valores que consideramos iguales (en DB2T terminan en
espacios y 00s): BOSCH, HENGST, KNECHT, MANN, etc

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th><p><mark>SELECT DISTINCT MARCA, LEN(LTRIM(RTRIM(MARCA))) as LONG
from [MASQL20171/HOSTDB2].[DB2T].[dbo].[FAAL04] where MARCA='BOSCH ' or
MARCA='HENGST ' or MARCA='KNECHT ' or MARCA='MANN ' or MARCA='ACB LIPS
'</mark></p>
<p><mark>select * from OPENQUERY(DB2P, 'SELECT DISTINCT MARCA,
hex(trim(MARCA)) as HEXTRIM,</mark></p>
<p><mark>case when MARCA='''' or hex(trim(MARCA)) = ''0000%'' then 0
else LENGTH(hex(trim(MARCA)))/2 end as LONG</mark></p>
<p><mark>FROM CORAL.FAAL04</mark></p>
<p><mark>where (hex(MARCA) LIKE ''C2D6E2C3C8%00'' or hex(MARCA) LIKE
''C8C5D5C7E2E3%00'' or hex(MARCA) LIKE ''D2D5C5C3C8E3%00'' or MARCA LIKE
''MANN%'' or hex(MARCA) LIKE ''C1C3C240D3C9D7E2%00'' ) ') order by
3,2,1</mark></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

# <img
src="assets/media/))) as LONG
from [MASQL20171/HOSTDB2].[DB2T].[dbo].[FAAL17] where JUSNE1 LIKE '-%'
or JUSNE1 LIKE '=%' or JUSNE1 LIKE ' NOT ASSIGNED%' or JUSNE1 LIKE
'HERRAMIENTA ESPECIAL NECESARIA PARA LA REPARACION DEL ENGRANAJE
REDUCTOR RENKAS 2X125%' or JUSNE1 LIKE 'IT IS USED FOR EXTEND PRINTED
CIRCUIT BOARDS IN OU-91(V)3 CENTRAL EQUIPMENT GROUP.%' or JUSNE1 LIKE
'IT IS USED FOR EXTRACT PRINTED WIRING BOARDS IN THE AN/UYK-43C(V)
LOWBOY COMPUTER SET%' or JUSNE1 LIKE 'IT IS USED IN ADJUST PROCEDURES,
FAULT OF POWER DETECTION ACTIONS, ETC.%' or JUSNE1 LIKE 'THIS EQUIPMENT
IS NECESSARY TO CONDUCT THE THIN HULL INSPECTION DURING THE DRYDOCKS BY
THE DEPOT LEVEL OF MAINTENANCE.%'</mark></p>
<p><mark>select * from OPENQUERY(DB2P, 'SELECT DISTINCT JUSNE1,
hex(trim(JUSNE1)) as HEXTRIM,</mark></p>
<p><mark>case when JUSNE1='''' or hex(trim(JUSNE1)) = ''0000%'' then 0
else LENGTH(hex(trim(JUSNE1)))/2 end as LONG</mark></p>
<p><mark>FROM CORAL.FAAL17</mark></p>
<p><mark>--where hex(JUSNE1) = ''00C5D4F0F2D7''</mark></p>
<p><mark>where JUSNE1 LIKE ''-%'' or JUSNE1 LIKE ''=%'' or JUSNE1 LIKE
'' NOT ASSIGNED%'' or JUSNE1 LIKE ''HERRAMIENTA ESPECIAL NECESARIA PARA
LA REPARACION DEL ENGRANAJE REDUCTOR RENKAS 2X125%'' or JUSNE1 LIKE ''IT
IS USED FOR EXTEND PRINTED CIRCUIT BOARDS IN OU-91(V)3 CENTRAL EQUIPMENT
GROUP.%'' or JUSNE1 LIKE ''IT IS USED FOR EXTRACT PRINTED WIRING BOARDS
IN THE AN/UYK-43C(V) LOWBOY COMPUTER SET%'' or JUSNE1 LIKE ''IT IS USED
IN ADJUST PROCEDURES, FAULT OF POWER DETECTION ACTIONS, ETC.%'' or
JUSNE1 LIKE ''THIS EQUIPMENT IS NECESSARY TO CONDUCT THE THIN HULL
INSPECTION DURING THE DRYDOCKS BY THE DEPOT LEVEL OF
MAINTENANCE.%''</mark></p>
<p><mark>--where LENGTH(hex(trim(JUSNE1)))/2=2</mark></p>
<p><mark>') order by 3,2,1</mark></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

En FAAL17, en el campo CAREE1, hay estas cadenas parecidas.

<img
src="assets/media/))) as LONG from
[MASQL20171/HOSTDB2].[DB2T].[dbo].[FAAL17] where CAREE1 LIKE
'-%'</mark></p>
<p><mark>or CAREE1 LIKE '-%REMOVE, TEST, AND ADJUST INJECTION NOZZLES
(PROP. DIESEL ENGINE NO. 1)%' or CAREE1 LIKE '%ALIGN ENCODER.%' or
CAREE1 LIKE '%COMPROBAR ESTADO Y FUNCIONAMIENTO DEL EQUIPO%'</mark></p>
<p><mark>or CAREE1 LIKE '%INSPECT SEWATERINSPECT SEWATER MAGAZINE
SPRINKLER VALVE (1" POWERTROL); RENEW DIAPHRAGM).%' or CAREE1 LIKE
'%REMOVE AND REPLACE X2 DATA PCB.%' or CAREE1 LIKE '=%CONDUCT THIN HULL
INSPECTION.%'</mark></p>
<p><mark>or CAREE1 LIKE '20KOHMS/V%' or CAREE1 LIKE 'DE ACERO AL
CARBONO, 14-1/2 PULGADAS%' or CAREE1 LIKE 'DOS BATERIAS TAMA%' or CAREE1
LIKE 'UNDERWATER TOOL AND EQUIPMENT CORPORATION%' order by 1</mark></p>
<p><mark>select * from OPENQUERY(DB2P, 'SELECT DISTINCT CAREE1,
hex(trim(CAREE1)) as HEXTRIM,</mark></p>
<p><mark>case when CAREE1='''' or hex(trim(CAREE1)) = ''0000%'' then 0
else LENGTH(hex(trim(CAREE1)))/2 end as LONG</mark></p>
<p><mark>FROM CORAL.FAAL17</mark></p>
<p><mark>where CAREE1 LIKE ''-%REMOVE, TEST, AND ADJUST INJECTION
NOZZLES (PROP. DIESEL ENGINE NO. 1)%''</mark></p>
<p><mark>or CAREE1 LIKE ''%ALIGN ENCODER.%'' or CAREE1 LIKE ''%COMPROBAR
ESTADO Y FUNCIONAMIENTO DEL EQUIPO%''</mark></p>
<p><mark>or CAREE1 LIKE ''%INSPECT SEWATERINSPECT SEWATER MAGAZINE
SPRINKLER VALVE (1" POWERTROL); RENEW DIAPHRAGM).%'' or CAREE1 LIKE
''%REMOVE AND REPLACE X2 DATA PCB.%''</mark></p>
<p><mark>or CAREE1 LIKE ''=%CONDUCT THIN HULL INSPECTION.%'' or CAREE1
LIKE ''20KOHMS/V%'' or CAREE1 LIKE ''DE ACERO AL CARBONO, 14-1/2
PULGADAS%'' or CAREE1 LIKE ''DOS BATERIAS TAMA%''</mark></p>
<p><mark>or CAREE1 LIKE ''UNDERWATER TOOL AND EQUIPMENT
CORPORATION%''</mark></p>
<p><mark>or CAREE1 LIKE ''-%''</mark></p>
<p><mark>--where LENGTH(hex(trim(CAREE1)))/2=2</mark></p>
<p><mark>') order by 1</mark></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

1.  <span id="_Toc37230090" class="anchor"></span>Mismos datos en los
    registros de las tablas de ambas BBDD (EXCEPT)

Se descarta por ser validación muy lenta

2.  <span id="_Toc37230091" class="anchor"></span>Mismos datos en los
    registros de las tablas de ambas BBDD (Hashbytes)

No existe en DB2 la función Hashbytes

4.  <span id="_Toc37230092" class="anchor"></span>PASO2: Migración de
    MAHOST a DB2T

    1.  <span id="_Toc37230093" class="anchor"></span>Resumen de
        validaciones

Este apartado resume las validaciones para comparar las tablas cargadas
en destino (DB2T) versus las de origen (MAHOST), donde se han conservado
los mismos nombres de esquema y tablas en destino que tuvieran en
origen.

ORIGEN: MAHOST/MAHOST

> (recordar que se traen las tablas en alcance de la migración desde las
> bases de datos DBBAZAN, DBCART, DBFERR, DBLOGI, DBMADR, DBSFER a DB2T)

DESTINO: MASQL20171/HOSTDB2 (base de datos DB2T)

2.  <span id="_Toc37230094" class="anchor"></span>Mismas tablas creadas
    en ambas bases de datos

CASOS CONSIDERADOS RESULTADO de ejecutar la consulta 2.2:

1.  Las tablas en alcance de MAHOST existen en DB2T.

2.  En DB2T se han creado los mismos esquemas que tienen las tablas
    origen. No ha sido necesario añadir la BBDD como sufijo dado que son
    esquemas que no se repiten y ya queda definidos BD+esquema en el
    Excel de alcance de esta migración.

3.  DBLOGI ya fue cargado desde DB2 en el paquete PaqueteCORAL, por lo
    que no se cargarán desde MAHOST.

4.  No se cargan (fuera de alcance de la migración)

DBFERR.GESTCONF.CRUCE01, DBFERR.NOMINASQ.PCOR14, DBFERR.SR.CTINFE,
DBFERR.SR.CTINMS, DBFERR.SR.PEDIDO

5.  No se cargan (fuera de alcance de la migración) DBMADR.NTS.NTE01V,
    DBMADR.NTS.NTS01V, DBMADR.NTS.NTS01XV, DBMADR.NTS.NTS10V

6.  Cambian de esquema:

    1.  DBBAZAN_SCP.P38AA y DBBAZAN_SCP.P39AA se cargan desde
        DBBAZAN.dbo

    2.  DBFERR_NOMINASQ.ABENFACC y DBFERR_NOMINASQ.PREIMPRESOS se cargan
        desde DBFERR.dbo

    3.  DBSFER_SFUSER.GF_CABDEM, DBSFER_SFUSER.GF_EDITOR,
        DBSFER_SFUSER.GF_LINDEM, DBSFER_SFUSER.GF_LINDEM_AUD,
        DBSFER_SFUSER.TEST2 se cargan desde DBSFER_dbo

7.  DBFERR.NOMINASQ.PCOR01A y DBFERR.NOMINASQ.PCOR02 fueron cargadas ya
    desde DB2 (porque hay más en DB2 que en DBFERR.NOMINASQ) -/> no se
    traen desde MAHOST. Solo se excluyen estas 2 tablas desde
    DBFERR.NOMINASQ en la carga desde MAHOST.

RESULTADO

Se usa la consulta 2.1 y 2.2 de ‘queryCheckDataMAHOST_DB2T.txt’

- Como se ha comentado en el punto 6, las siguientes tablas se han
  cargado en Destino, con un esquema distinto a dbo -/> OK.

- Como se comenta en el punto 7, PCOR01A y PCOR02 se cargaron de BD2 vía
  openquery y no se vuelven a cargar desde MAHOST. En la consulta, se
  muestra que están en esquema dbo de DB2T.

Todas las tablas en destino.

<img
src="assets/media/).

CONCLUSIÓN

Todo OK.

4.  <span id="_Toc37230102" class="anchor"></span>Mismos datos en los
    registros de las tablas de ambas BBDD (Hashbytes)

CASOS CONSIDERADOS

En la comparación, se consideran todas las tablas, excepto las
comentadas

RESULTADO de ejecutar la consulta 2.6:

No se observan discrepancias entre origen MAHOST y destino DB2T (mismos
valores cargados, usando la función hashbytes de todos los campos.).

CONCLUSIÓN

Todo OK. Ha tardado 49 minutos en validar todas las tablas con hashbytes
y ha dado vacio.

OK. Todos los valores son idénticos

Podemos usar la comparación de BBDD que sean SQL Server de Visual Studio

<img
src="assets/media/) versus las de origen (FESRV014)

ORIGEN: FESRV014 (bases de datos AlmacenesIntermedios, ControlAsuntos ,
ControlDoc , GestionHerramental , Necor@ , Ordenes, SubContratas)

DESTINO: MASQL20171/HOSTDB2 (esas mismas 7 bases de datos)

2.  <span id="_Toc37230105" class="anchor"></span>Mismas tablas creadas
    en ambas bases de datos

CASOS CONSIDERADOS

1.  Se han creado las mismas bases de datos, mismos esquemas y mismas
    tablas en MASQL20171/HOSTDB2.

2.  En la comparación, se consideran todas las tablas, excepto las
    siguientes:

- '/_LOGCARGA': tabla auxiliar para registrar tiempos y registros al
  cargar cada tabla. Hay un /_LOGCARGA en cada base de datos destino,
  que no existe en origen.

RESULTADO de ejecutar la consulta 3.2:

Las tablas de FESRV014 de todas las BBDD existen en MASQL20171/HOSTDB2

OK.

NOTA: No hay acceso de select a
/[SubContratas/]./[dbo/]./[tcProveedores_Documentos/]

SELECT permission denied on object 'tcProveedores_Documentos', database
'SubContratas', owner 'dbo'.

<span class="mark">Pero el paquete sí tiene acceso y hace la
carga-/>OK.</span>

<span class="mark">La validación usa sp_MSforeachtable que tiene acceso
al número de fila -/> OK</span>

CONCLUSIÓN:

Todo OK.

1.  <span id="_Toc37230106" class="anchor"></span>Mismas columnas en las
    tablas de ambas bases de datos

CASOS CONSIDERADOS

En la comparación, se consideran todas las tablas, excepto las
comentadas en el apartado anterior:

- <span class="mark">‘/_LOGCARGA’</span> en cada base de datos

> <span class="mark"> </span>

RESULTADO de ejecutar la consulta 3.3:

Todas las columnas de FESRV014 de todas las BBDD existen en
MASQL20171/HOSTDB2.

CONCLUSIÓN

Todo OK.

1.  <span id="_Toc37230107" class="anchor"></span>Mismo tipo de datos en
    columnas de ambas BBDD

CASOS CONSIDERADOS

En la comparación, se consideran todas las tablas, excepto las
siguientes (que son tablas auxiliares usadas en el proyecto):

- '/_LOGCARGA' en cada Base de datos.

RESULTADO de ejecutar la consulta 3.4:

- No hay discrepancias entre origen y destino en cuanto a tipo /longitud
  de datos.

CONCLUSIÓN

Todo OK.

1.  <span id="_Toc37230108" class="anchor"></span>Misma cantidad de
    registros en tablas de ambas BBDD

CASOS CONSIDERADOS

En la comparación, se consideran todas las tablas, excepto las
siguientes (que son tablas auxiliares usadas en el proyecto):

- '/_LOGCARGA'

RESULTADO de ejecutar la consulta 3.6:

- No se observan discrepancias en número de registros entre origen y
  destino (mismos registros cargados).

CONCLUSIÓN

- Todo OK.

  1.  Mismos valores en campos numéricos en tablas de ambas BBDD

CASOS CONSIDERADOS

En la comparación, se consideran todas las tablas, excepto las
siguientes (que son tablas auxiliares usadas en el proyecto o internas):

- '/_LOGCARGA' ,'dtproperties','sysconstraints','syssegments'

RESULTADO de ejecutar la consulta 3.5:

- No se observan discrepancias en la suma de todos los valores de cada
  campo.

CONCLUSIÓN

- Todo OK.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th><p>En SQLServer 2000, no existe TRIM, ni <mark>CONCAT_WS</mark>, ni
HASHBYTES.</p>
<p>Tampoco podemos usar la comparación de BBDD que sean SQL Server de
Visual Studio</p>
<p><img
src="assets/media/) de la
comparación.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

1.  Mismos valores en campos fecha en tablas de ambas BBDD

CASOS CONSIDERADOS

En la comparación, se consideran todas las tablas, excepto las
siguientes (que son tablas auxiliares usadas en el proyecto o internas):

- '/_LOGCARGA' ,'dtproperties','sysconstraints','syssegments'

RESULTADO de ejecutar la consulta 3.7:

- No se observan discrepancias en la suma de todos los valores fecha
  (formato ISO) de cada campo.

CONCLUSIÓN

- Todo OK.

  1.  Mismos valores en campos texto en tablas de ambas BBDD

CASOS CONSIDERADOS

En la comparación, se consideran todas las tablas, excepto las
siguientes (que son tablas auxiliares usadas en el proyecto o internas):

- '/_LOGCARGA' ,'dtproperties','sysconstraints','syssegments'

RESULTADO de ejecutar la consulta 3.8:

- No se observan discrepancias en la suma de todos los valores fecha
  (formato ISO) de cada campo. 🡪 <span class="mark">esperando a lanzar
  de nuevo paquete de proyecto 7.</span>

CONCLUSIÓN

- Todo OK.

<span id="_Toc37230109" class="anchor"></span>

6.  PASO4: Migración de NECOR@NC a NEWPRYC

    1.  <span id="_Toc37230110" class="anchor"></span>Resumen de
        validaciones

Este apartado resume las validaciones para comparar las tablas cargadas
en destino (NEWPRYC) versus las de origen (NECOR@NC)

ORIGEN: MASQL20142/SQL20142 (base de datos /[Necor@NC/])

User: Necor@Altia

Password: necora

DESTINO: MASQL20171/HOSTDB2 (base de datos NEWPRYC)

User: necor@altia

Password: 4LW4Y54LT14

2.  <span id="_Toc37230111" class="anchor"></span>Mismas tablas creadas
    en ambas bases de datos

CASOS CONSIDERADOS

En la comparación, se consideran todas las tablas, excepto las
siguientes:

-- Tablas de Pruebas

- '/_ControlErrorLog', 'ENLACES_BKP_20141127',
  'ENLACES_BKP_20141201','NC08SQ_20170608',

'NC08SQ_20170913', 'NC08SQ_20170913_NO_BORRADOS', 'NC08SQ_ANALIZE',
'NC08SQ_ANALIZE_20170509',

'NC08SQ_DIFF', 'NC08SQ_DIFF_DEL', 'NC08SQ_IMPORT', 'NC08SQ_TMP',
'SCHEMA_PRYC','SIZE_PRYC', 'filterTables', 'sysssislog',

--Tablas sin Uso

- 'ZERP00_DATCTRL', 'PROVCL1', 'PROVCL2', 'PROVCL3', 'PROVCL4',
  'PROVCL5', 'NC37SQ_DESCR_OLD',

'NC38SQ_DESCR_OLD', 'FV02SQ_DB2', 'NC08SQ_N', 'NC08SQ_NOINSERT',
'NC11SQ_DESCR', 'NC11SQ_TEXTOS', 'NC17SQ_TEXTOS',

-- Tablas que copiamos a modo de BackUp

- 'NC20SQ_DESCR_NOBORRAR', 'NC20SQ_NOBORRAR', 'NC23SQ_DESCR_NOBORRAR',
  'NC23SQ_NOBORRAR', 'NC25SQ_DESCR_NOBORRAR',

'NC25SQ_NOBORRAR', 'PROVCL_NOBORRAR', 'TACTIVIDAD_DESCR_NOBORRAR',
'TACTIVIDAD_NOBORRAR',

'TCARGOS_DESCR_NOBORRAR', 'TCARGOS_NOBORRAR', 'TCENTROS_DESCR_NOBORRAR',
'TCENTROS_NOBORRAR',

'TDESPRO_DESCR_NOBORRAR', 'TOBRAS_DESCR_NOBORRAR', 'TOBRAS_NC',
'TOBRAS_NOBORRAR','TPARTIDA_DESCR_NOBORRAR',

'TPARTIDA_NOBORRAR', 'TDESPRO_NOBORRAR', 'TFASES_DESCR_NOBORRAR',
'TFASES_NOBORRAR',

> -- Pendiente revisar

- 'MATERIAL_INT', 'MATERIALES_INT',

> -- origen DB2 más actual

- 'PCOR01A', 'PCOR02'

> --no encontradas

- ,'MARCA','NC10SQ_DESCR','NC12SQ_DESCR','NC13SQ_DESCR','NC15SQ_DESCR','NC17SQ_DESCR','NC18SQ_DESCR','NC20SQ_DESCR','NC23SQ_DESCR','NC25SQ_DESCR','NC30SQ_DESCR','NC32SQ_DESCR','NC33SQ_DESCR','NC35SQ_DESCR','TACTIVIDAD_DESCR','TCARGOS_DESCR','TCENTROS_DESCR','TDESPRO_DESCR','TFASES_DESCR','TOBRAS_DESCR','TPARTIDA_DESCR'

RESULTADO de ejecutar la consulta 6.2:

Las tablas en alcance de NECOR@NC existen en DB2T

OK.

NOTA: Las tablas dentro de alcance son las marcadas con columna M (1)=Y
en el Excel “DTI-MIGRACION-HOST_AnexoTablas-R00.xlsx”

CONCLUSIÓN:

Todo OK.

1.  <span id="_Toc37230112" class="anchor"></span>Mismas columnas en las
    tablas de ambas bases de datos

CASOS CONSIDERADOS

En la comparación, se consideran todas las tablas, excepto las
comentadas en el apartado anterior fuera del alcance de la migración:

- <span class="mark">Tablas de Pruebas</span>

> <span class="mark">'/_ControlErrorLog', 'ENLACES_BKP_20141127',
> 'ENLACES_BKP_20141201','NC08SQ_20170608',</span>
>
> <span class="mark">'NC08SQ_20170913', 'NC08SQ_20170913_NO_BORRADOS',
> 'NC08SQ_ANALIZE', 'NC08SQ_ANALIZE_20170509',</span>
>
> <span class="mark">'NC08SQ_DIFF', 'NC08SQ_DIFF_DEL', 'NC08SQ_IMPORT',
> 'NC08SQ_TMP', 'SCHEMA_PRYC','SIZE_PRYC', 'filterTables',
> 'sysssislog',</span>

- <span class="mark">Tablas sin Uso</span>

> <span class="mark">'ZERP00_DATCTRL', 'PROVCL1', 'PROVCL2', 'PROVCL3',
> 'PROVCL4', 'PROVCL5', 'NC37SQ_DESCR_OLD',</span>
>
> <span class="mark">'NC38SQ_DESCR_OLD', 'FV02SQ_DB2', 'NC08SQ_N',
> 'NC08SQ_NOINSERT', 'NC11SQ_DESCR', 'NC11SQ_TEXTOS',
> 'NC17SQ_TEXTOS',</span>

- <span class="mark">Tablas que copiamos a modo de BackUp</span>

> <span class="mark">'NC20SQ_DESCR_NOBORRAR', 'NC20SQ_NOBORRAR',
> 'NC23SQ_DESCR_NOBORRAR', 'NC23SQ_NOBORRAR',
> 'NC25SQ_DESCR_NOBORRAR',</span>
>
> <span class="mark">'NC25SQ_NOBORRAR', 'PROVCL_NOBORRAR',
> 'TACTIVIDAD_DESCR_NOBORRAR', 'TACTIVIDAD_NOBORRAR',</span>
>
> <span class="mark">'TCARGOS_DESCR_NOBORRAR', 'TCARGOS_NOBORRAR',
> 'TCENTROS_DESCR_NOBORRAR', 'TCENTROS_NOBORRAR',</span>
>
> <span class="mark">'TDESPRO_DESCR_NOBORRAR', 'TOBRAS_DESCR_NOBORRAR',
> 'TOBRAS_NC', 'TOBRAS_NOBORRAR','TPARTIDA_DESCR_NOBORRAR',</span>
>
> <span class="mark">'TPARTIDA_NOBORRAR', 'TDESPRO_NOBORRAR',
> 'TFASES_DESCR_NOBORRAR', 'TFASES_NOBORRAR',</span>

- <span class="mark">Pendiente revisar</span>

> <span class="mark">'MATERIAL_INT', 'MATERIALES_INT',</span>

- <span class="mark">Origen DB2 más actual</span>

> <span class="mark">'PCOR01A', 'PCOR02'</span>

- <span class="mark">No encontradas</span>

> <span class="mark">'MARCA','NC10SQ_DESCR','NC12SQ_DESCR','NC13SQ_DESCR','NC15SQ_DESCR','NC17SQ_DESCR','NC18SQ_DESCR','NC20SQ_DESCR','NC23SQ_DESCR','NC25SQ_DESCR','NC30SQ_DESCR','NC32SQ_DESCR','NC33SQ_DESCR','NC35SQ_DESCR','TACTIVIDAD_DESCR','TCARGOS_DESCR','TCENTROS_DESCR','TDESPRO_DESCR','TFASES_DESCR','TOBRAS_DESCR','TPARTIDA_DESCR'</span>

RESULTADO de ejecutar la consulta 6.3:

Todas las columnas en NECOR@NC existen en NEWPRYC, excepto en estas
tablas/vistas.

| TABLE_NAME | <NAME_NECOR@NC> |
|------------|-----------------|
| BO18SQ     | FECREAC         |
| NC12SQ     | DESCR           |
| NC13SQ     | DESCR           |
| NC15SQ     | DESCR           |
| NC17SQ     | DESCR           |
| NC18SQ     | DESCR           |
| NC30SQ     | DESPLAL         |
| NC30SQ     | DESPLAC         |
| NC38SQ     | DESCR           |
| NC74SQ     | DESCRIPCION     |
| NC75SQ     | DESCRIPCION     |

Todas las columnas en NEWPRYC existen en NECOR@NC, excepto en estas
tablas/vistas

| TABLE_NAME | NAME_NEWPRYC |
|------------|--------------|
| NC11SQ     | FECHSAP      |
| NC11SQ     | FRESSAP      |
| NC11SQ     | HORASAP      |
| NC11SQ     | HRESSAP      |
| NC11SQ     | PROCSAP      |
| NC11SQ     | SITUSAP      |
| NC11SQ     | USUSAP       |
| NC17SQ     | FECHSAP      |
| NC17SQ     | FRESSAP      |
| NC17SQ     | HORASAP      |
| NC17SQ     | HRESSAP      |
| NC17SQ     | PROCSAP      |
| NC17SQ     | SITUSAP      |
| NC17SQ     | USUSAP       |
| NC18SQ     | FECHSAP      |
| NC18SQ     | FRESSAP      |
| NC18SQ     | HORASAP      |
| NC18SQ     | HRESSAP      |
| NC18SQ     | PROCSAP      |
| NC18SQ     | SITUSAP      |
| NC18SQ     | USUSAP       |
| NC32SQ     | SITAMAT      |

CONCLUSIÓN

<span class="mark">Revisar si las columnas deben ser iguales en ambas
BBDD para estas tablas</span>.

1.  <span id="_Toc37230113" class="anchor"></span>Mismo tipo de datos en
    columnas de ambas BBDD

CASOS CONSIDERADOS

1.  En la comparación, se consideran todas las tablas, excepto las
    siguientes (que son tablas auxiliares usadas en el proyecto):

- '/_LOGCARGA', 'filterTables', 'sysssislog'

RESULTADO de ejecutar la consulta 6.4:

- Se observan discrepancias entre origen y destino

CONCLUSIÓN

<span class="mark">Revisar solapa 6.4 TiposDatos del Excel ‘4.Plan de
Pruebas NECORANC-NEWPRYC.xlsx</span>

1.  <span id="_Toc37230114" class="anchor"></span>Misma cantidad de
    registros en tablas de ambas BBDD

CASOS CONSIDERADOS

En la comparación, se consideran todas las tablas, excepto las
siguientes (que son tablas auxiliares usadas en el proyecto):

- '/_LOGCARGA', 'filterTables', 'sysssislog'

En NEWPRYC se cargan registros desde NECOR@NC y desde DB2T,por lo que en
la validación se descuentan los que provienen de DB2T.

RESULTADO de ejecutar la consulta 6.5:

- No se observan discrepancias entre origen NECOR@NC y destino NEWPRYC
  (mismos registros cargados).

- <span class="mark">Actualmente los datos en NEWPRYC son los que
  provienen de DB2T (donde ESTABL/</>’7’), por lo que habrá que repetir
  esta prueba, vaciando las tablas en NEWPRYC y cargando desde
  NECOR@NC</span>

CONCLUSIÓN

- Todo OK.

  1.  <span id="_Toc37230115" class="anchor"></span>Mismos valores en
      los registros de las tablas de ambas BBDD (EXCEPT)

EXCEPT compara el resultado de dos consultas y devuelve las filas
distintas existentes en la primera consulta que no aparecen en la
segunda. Es decir, EXCEPT resta el resultado de una consulta a la otra.

<span class="mark">--OJO a los campos tipo char: EXCEPT considera
prodint = 'BLQ 114 ' y prodint = 'BLQ 114' el mismo valor. 'BLQ 114' y '
BLQ 114' si los detecta</span>

INTERSECT devuelve las diferencias entre ambas tablas.

CASOS CONSIDERADOS

En la comparación, se consideran todas las tablas, excepto las
siguientes (que son tablas auxiliares usadas en el proyecto):

- '/_LOGCARGA', 'filterTables', 'sysssislog'

RESULTADO de ejecutar la consulta 6.6:

- No se observan estas discrepancias entre origen y destino NEWPRYC.

  1.  <span id="_Toc37230116" class="anchor"></span>Mismos datos en los
      registros de las tablas de ambas BBDD (Hashbytes)

Al comparar filas podríamos usar las funciones STUFF o CONCAT para unir
cadenas.

- STUFF(cast(a./[Account_No/] as varchar) + cast(a./[Transaction_Id/] as
  varchar) + ... , 1, 1, '')

> /</>
>
> STUFF(cast(b./[Account_No/] as varchar) + cast(b./[Transaction_Id/] as
> varchar) + ... , 1, 1, '')

- CONCAT(a./[account_no/],a./[transaction_id/], ...)

> /</>
>
> CONCAT(b./[account_no/],b./[transaction_id/], ...)

Para comparar muchas filas una a una, podemos añadir una función has,
como checksum o

binary_checksum para obtener un número único.

Tanto [CHECKSUM](httpassets/media/) como [BINARY_CHECKSUM](httpassets/media/) calculan
un checksum para una fila o lista de valores. La idea es obtener un
único valor fácil de comparar. Si dos conjuntos o filas tienen distinto
checksum, es que son diferentes.

No es totalmente fiable para detectar cambios en filas:

- cambiar el signo de un número con decimales, da el mismo checksum

> <img
> src="assets/media/).

En SQL Server 2017, **<u>HASBYTES no tiene ya limitación a 8000 bytes y
es la alternativa a usar</u>**. Se puede usar CONCAT_WS (concatenar con
separador), pero ignora valores NULL (lo que supone manejarlos con
ISNULL o COALESCE al concatenar). Y usar un separador que sepamos que no
existe en todos los campos. Si usamos CONCAT para combinar números y
fechas, es críticos formatearlos como cadenas para controlar nosotros el
formato usado (y evitar problemas con diferentes idiomas o
configuraciones regionales).

- HASHBYTES ('SHA2_256', CONCAT_WS('/|/|', ISNULL(Campo1, ''),
  ISNULL(Campo2, ''), ... ,ISNULL(CampoN, ''))

- Opciones en Hashbytes: MD5 = 16 bytes, SHA1 = 20, SHA2_256 = 32, and
  SHA2_512 = 64

- El inconveniente surge en encontrar la fila con el cambio. Si
  existiese un campo fijo en la tabla con una columna Hash, que fuese
  actualizada cuando los valores de las coumnas cambian, sería ideal
  para detectar cambio de datos. Se puede convertir HASHBYTES a VARCHAR
  y crear un índice sobre esa columna resultado.

SELECT CONVERT(NVARCHAR(32),HashBytes('SHA2_256', CONTENT),2)

NOTA: Usar trim porque el hashbytes difiere por el GRUCOSTE que es
char(3) en DB2T y char(6) en NEWPRYC. El valor en NEWPRYC tiene 3
espacios al final que no lleva el otro. Con TRIm se soluciona.

(<httpassets/media/)

CASOS CONSIDERADOS

En la comparación, se consideran todas las tablas, excepto las
siguientes (que son tablas auxiliares usadas en el proyecto):

- '/_LOGCARGA', 'filterTables', 'sysssislog'

RESULTADO de ejecutar la consulta 6.7:

7.  <span id="_Toc37230117" class="anchor"></span>PASO5: Migración de
    DB2T a NEWPRYC

    1.  <span id="_Toc37230118" class="anchor"></span>Resumen de
        validaciones

Este apartado resume las validaciones para comparar las tablas cargadas
en destino (NEWPRYC y CORAL) versus las de origen (DB2T)

ORIGEN: MASQL20171/HOSTDB2 (base de datos DB2T)

User: necor@altia

Password: 4LW4Y54LT14

DESTINO: MASQL20171/HOSTDB2 (base de datos NEWPRYC y CORAL)

User: necor@altia

Password: 4LW4Y54LT14

2.  <span id="_Toc37230119" class="anchor"></span>Mismas tablas creadas
    en ambas bases de datos

CASOS CONSIDERADOS

3.  En la comparación, se consideran todas las tablas, excepto las
    siguientes (que son tablas auxiliares usadas en el proyecto):

- '/_LOGCARGA', 'filterTables', 'sysssislog'

RESULTADO de ejecutar la consulta 7.2:

1.  Todas las tablas en DB2T existen en NEWPRYC

OK.

2.  Hay tablas en NEWPRYC que no existen en DB2T,

· porque se cargan desde NECORANC

> · porque son tablas de descricpiones que se han creado desde BO06DES,
> NC06DES, NC36DES, PE46DES

CONCLUSIÓN:

Todo OK.

1.  <span id="_Toc37230120" class="anchor"></span>Mismas columnas en las
    tablas de ambas bases de datos

CASOS CONSIDERADOS

En la comparación, se consideran todas las tablas, excepto las
siguientes (que son tablas auxiliares usadas en el proyecto):

- '/_LOGCARGA', 'filterTables', 'sysssislog'

RESULTADO de ejecutar la consulta 7.3:

7.3.a Todas las columnas en DB2T existen en NEWPRYC, excepto las
siguientes

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th><ul>
<li><p>SECUE</p></li>
<li><p>SECUE06</p></li>
<li><p>SECUE36</p></li>
<li><p>SECUE41</p></li>
<li><p>SECUE46</p></li>
</ul></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

En NEWPRYC no se requiere el campo de Secuencia que permite obtener la
clave compuesta (tupla de varios campos, distintos en cada tabla, que
hace único a cada registro) a partir del número de secuencia. Este
número de secuencia permite ir a las tablas de descripciones BO06DES,
NC06DES, NC36DES, PE46DES y obtener las descripciones /índices /textos
(en varios idiomas ESPAÑA, INGLES) asociados a cada registro de las
tablas generales.

- Estas dos cols (DTI, USUARIOSO) no existen en DB2T y existen en
  NEWPRYC. Se hace el insert fuera del bucle.

CONCLUSIÓN

Todo OK.

7.3b Coinciden todas las columnas entre DB2T y CORAL

1.  <span id="_Toc37230121" class="anchor"></span>Mismo tipo de datos en
    columnas de ambas BBDD

CASOS CONSIDERADOS

En la comparación, se consideran todas las tablas, excepto las
siguientes (que son tablas auxiliares usadas en el proyecto):

- '/_LOGCARGA', 'filterTables', 'sysssislog'

> Y todas las columnas excepto las siguientes (que no han sido creadas
> en NEWPRYC)

- 'SECUE06','SECUE36','SECUE41','SECUE46','SECUE'

RESULTADO de ejecutar la consulta 7.4:

7.4.a Se observan estas discrepancias entre origen y destino (Ver solapa
5.4aTiposDatosNEWPRYC en Excel).

Se considera

- GRUCOSTE char(6) en vez de char(3), como existe en DB2T, por
  uniformizar con siguientes pasos de la migración.

7.4b Coinciden todas las columnas entre DB2T y CORAL

CONCLUSIÓN

Todo OK.

1.  <span id="_Toc37230122" class="anchor"></span>Misma cantidad de
    registros en tablas de ambas BBDD

CASOS CONSIDERADOS

En la comparación, se consideran todas las tablas, excepto las
siguientes (que son tablas auxiliares usadas en el proyecto):

- '/_LOGCARGA', 'filterTables', 'sysssislog'

BO49SQ,ENLACESGENFI2,NC20SQA,PCOR01A,PCOR02 son tablas sin ESTABL.
Existen en DB2T y NECOR@NC. Se cargan solo los de NECOR@NC. ¿Se ignoran
los de Db2T?

RESULTADO de ejecutar la consulta 7.5:

- 7.5a NumRegistrosNEWPRYC

- Es correcto porque en NEWPRYC solo se cargan registros donde
  ESTABL/</>’7

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th><table>
<colgroup>
<col style="width: 17%" />
<col style="width: 15%" />
<col style="width: 66%" />
</colgroup>
<thead>
<tr>
<th>TABLE_NAME</th>
<th style="text-align: right;">FILAS</th>
<th style="text-align: right;">FILAS_NEWPRYC</th>
</tr>
</thead>
<tbody>
<tr>
<td>BL01SQ</td>
<td style="text-align: right;">19</td>
<td style="text-align: right;">0</td>
</tr>
<tr>
<td>BLNCSQ</td>
<td style="text-align: right;">14277</td>
<td style="text-align: right;">0</td>
</tr>
<tr>
<td>BO06DES</td>
<td style="text-align: right;">16974305</td>
<td style="text-align: right;">0</td>
</tr>
<tr>
<td>BO09SQ</td>
<td style="text-align: right;">806100</td>
<td style="text-align: right;">723282</td>
</tr>
<tr>
<td>BO10SQ</td>
<td style="text-align: right;">425310</td>
<td style="text-align: right;">383901</td>
</tr>
<tr>
<td>BO11SQ</td>
<td style="text-align: right;">1022799</td>
<td style="text-align: right;">949897</td>
</tr>
<tr>
<td>BO12SQ</td>
<td style="text-align: right;">6162109</td>
<td style="text-align: right;">5726714</td>
</tr>
<tr>
<td>BO13SQ</td>
<td style="text-align: right;">992126</td>
<td style="text-align: right;">913411</td>
</tr>
<tr>
<td>BO14SQ</td>
<td style="text-align: right;">1040446</td>
<td style="text-align: right;">961314</td>
</tr>
<tr>
<td>BO15SQ</td>
<td style="text-align: right;">3998151</td>
<td style="text-align: right;">3943073</td>
</tr>
<tr>
<td>BO16SQ</td>
<td style="text-align: right;">5595488</td>
<td style="text-align: right;">5153043</td>
</tr>
<tr>
<td>BO20SQ</td>
<td style="text-align: right;">758905</td>
<td style="text-align: right;">730039</td>
</tr>
<tr>
<td>BO21SQ</td>
<td style="text-align: right;">1065117</td>
<td style="text-align: right;">1033545</td>
</tr>
<tr>
<td>BO22SQ</td>
<td style="text-align: right;">1141718</td>
<td style="text-align: right;">1133311</td>
</tr>
<tr>
<td>BO29SQ</td>
<td style="text-align: right;">4136</td>
<td style="text-align: right;">4116</td>
</tr>
<tr>
<td>BO40SQ</td>
<td style="text-align: right;">947465</td>
<td style="text-align: right;">796511</td>
</tr>
<tr>
<td>BO41SQ</td>
<td style="text-align: right;">945408</td>
<td style="text-align: right;">793875</td>
</tr>
<tr>
<td>BO43SQ</td>
<td style="text-align: right;">933988</td>
<td style="text-align: right;">786124</td>
</tr>
<tr>
<td>BO46SQ</td>
<td style="text-align: right;">9831634</td>
<td style="text-align: right;">9193405</td>
</tr>
<tr>
<td>BO47SQ</td>
<td style="text-align: right;">1907251</td>
<td style="text-align: right;">1836059</td>
</tr>
<tr>
<td>BO49SQ</td>
<td style="text-align: right;">4578633</td>
<td style="text-align: right;">0</td>
</tr>
<tr>
<td>BO58SQ</td>
<td style="text-align: right;">17235</td>
<td style="text-align: right;">17222</td>
</tr>
<tr>
<td>BO59SQ</td>
<td style="text-align: right;">697445</td>
<td style="text-align: right;">697399</td>
</tr>
<tr>
<td>BO61SQ</td>
<td style="text-align: right;">2536598</td>
<td style="text-align: right;">2536585</td>
</tr>
<tr>
<td>BO67SQ</td>
<td style="text-align: right;">124384</td>
<td style="text-align: right;">119886</td>
</tr>
<tr>
<td>ENLACES</td>
<td style="text-align: right;">82064</td>
<td style="text-align: right;">0</td>
</tr>
<tr>
<td>FV02SQ</td>
<td style="text-align: right;">4660619</td>
<td style="text-align: right;">0</td>
</tr>
<tr>
<td>GENFI2</td>
<td style="text-align: right;">71836</td>
<td style="text-align: right;">0</td>
</tr>
<tr>
<td>NC06DES</td>
<td style="text-align: right;">17965613</td>
<td style="text-align: right;">0</td>
</tr>
<tr>
<td>NC36DES</td>
<td style="text-align: right;">48502260</td>
<td style="text-align: right;">0</td>
</tr>
<tr>
<td>NCUSSQ</td>
<td style="text-align: right;">8917</td>
<td style="text-align: right;">0</td>
</tr>
<tr>
<td>PCOR01A</td>
<td style="text-align: right;">14142</td>
<td style="text-align: right;">0</td>
</tr>
<tr>
<td>PCOR02</td>
<td style="text-align: right;">13742</td>
<td style="text-align: right;">0</td>
</tr>
<tr>
<td>PE10SQ</td>
<td style="text-align: right;">469810</td>
<td style="text-align: right;">47850</td>
</tr>
<tr>
<td>PE11SQ</td>
<td style="text-align: right;">527869</td>
<td style="text-align: right;">53955</td>
</tr>
<tr>
<td>PE12SQ</td>
<td style="text-align: right;">3421166</td>
<td style="text-align: right;">309234</td>
</tr>
<tr>
<td>PE13SQ</td>
<td style="text-align: right;">7330</td>
<td style="text-align: right;">6504</td>
</tr>
<tr>
<td>PE14SQ</td>
<td style="text-align: right;">833721</td>
<td style="text-align: right;">103080</td>
</tr>
<tr>
<td>PE15SQ</td>
<td style="text-align: right;">27</td>
<td style="text-align: right;">2</td>
</tr>
<tr>
<td>PE16SQ</td>
<td style="text-align: right;">325818</td>
<td style="text-align: right;">28217</td>
</tr>
<tr>
<td>PE19SQ</td>
<td style="text-align: right;">79633</td>
<td style="text-align: right;">7874</td>
</tr>
<tr>
<td>PE24SQ</td>
<td style="text-align: right;">18818</td>
<td style="text-align: right;">0</td>
</tr>
<tr>
<td>PE25SQ</td>
<td style="text-align: right;">112959</td>
<td style="text-align: right;">5002</td>
</tr>
<tr>
<td>PE26SQ</td>
<td style="text-align: right;">13</td>
<td style="text-align: right;">1</td>
</tr>
<tr>
<td>PE46DES</td>
<td style="text-align: right;">7424445</td>
<td style="text-align: right;">0</td>
</tr>
<tr>
<td>TPRESUP</td>
<td style="text-align: right;">4962</td>
<td style="text-align: right;">0</td>
</tr>
</tbody>
</table></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

1.  <span id="_Toc37230123" class="anchor"></span>Mismos valores en los
    registros de las tablas de ambas BBDD (EXCEPT)

EXCEPT compara el resultado de dos consultas y devuelve las filas
distintas existentes en la primera consulta que no aparecen en la
segunda. Es decir, EXCEPT resta el resultado de una consulta a la otra.

INTERSECT devuelve las diferencias entre ambas tablas.

CASOS CONSIDERADOS

- En la comparación, se consideran todas las tablas, excepto las
  siguientes (que son tablas auxiliares usadas en el proyecto):
  '/_LOGCARGA', 'filterTables', 'sysssislog'

- Las tablas EQUIPOX, ITEMX, MARCAFX, PIDAX se insertanen BBDD
  /[MASQL20171/HOSTDB2/]./[CORAL/]

RESULTADO de ejecutar la consulta 7.6:

- Se observan estas discrepancias entre origen y destino NEWPRYC.

- Es correcto porque en NEWPRYC solo se cargan registros donde
  ESTABL/</>’7

- No se observan discrepancias entre origen DB2T y destino CORAL (son
  tablas idénticas).

  1.  <span id="_Toc37230124" class="anchor"></span>Mismos datos en los
      registros de las tablas de ambas BBDD (Hasbytes)

Al comparar filas podríamos usar las funciones STUFF o CONCAT para unir
cadenas.

- STUFF(cast(a./[Account_No/] as varchar) + cast(a./[Transaction_Id/] as
  varchar) + ... , 1, 1, '')

> /</>
>
> STUFF(cast(b./[Account_No/] as varchar) + cast(b./[Transaction_Id/] as
> varchar) + ... , 1, 1, '')

- CONCAT(a./[account_no/],a./[transaction_id/], ...)

> /</>
>
> CONCAT(b./[account_no/],b./[transaction_id/], ...)

Y comparar muchas filas una a una, añadiendo una función hash, como
checksum o

binary_checksum para obtener un número único.

Tanto [CHECKSUM](httpassets/media/) como [BINARY_CHECKSUM](httpassets/media/) calculan
un checksum para una fila o lista de valores. La idea es obtener un
único valor fácil de comparar. Si dos conjuntos o filas tienen distinto
checksum, es que son diferentes.

No es totalmente fiable para detectar cambios en filas:

- cambiar el signo de un número con decimales, da el mismo checksum

> <img
> src="assets/media/).

En SQL Server 2017, **<u>HASBYTES no tiene ya limitación a 8000 bytes y
es la alternativa a usar</u>**. Se puede usar CONCAT_WS (concatenar con
separador), pero ignora valores NULL (lo que supone manejarlos con
ISNULL o COALESCE al concatenar). Y usar un separador que sepamos que no
existe en todos los campos. Si usamos CONCAT para combinar números y
fechas, es críticos formatearlos como cadenas para controlar nosotros el
formato usado (y evitar problemas con diferentes idiomas o
configuraciones regionales).

- HASHBYTES ('SHA2_256', CONCAT_WS('/|/|', ISNULL(Campo1, ''),
  ISNULL(Campo2, ''), ... ,ISNULL(CampoN, '')))

- Opciones en Hashbytes: MD5 = 16 bytes, SHA1 = 20, SHA2_256 = 32, and
  SHA2_512 = 64

- El inconveniente surge en encontrar la fila con el cambio. Si
  existiese un campo fijo en la tabla con una columna Hash, que fuese
  actualizada cuando los valores de las columnas cambian, sería ideal
  para detectar cambio de datos. Se puede convertir HASHBYTES a VARCHAR
  y crear un índice sobre esa columna resultado.

SELECT CONVERT(NVARCHAR(32),HashBytes('SHA2_256', CONTENT),2)

(<httpassets/media/)

CASOS CONSIDERADOS

En la comparación, se consideran todas las tablas, excepto las
siguientes (que son tablas auxiliares usadas en el proyecto):

- '/_LOGCARGA', 'filterTables', 'sysssislog'

RESULTADO de ejecutar la consulta 7.7:

CARGA 10.04.2020

<img
src="assets/media/)  Tras actualizar el paquete 3.NEC para incluir la condición Where
    para los paquetes históricos cuando se hace el conteo en origen y se
    inserta en /_LOGCARGA,

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th><p>Paso expCondicionWhere</p>
<p>@[User::CondicionWhere] =(FINDSTRING(@[User::tableSource], "BH", 1)
== 1) ?</p>
<p>" WHERE (( ESTABL = ''A'' ) OR ( ESTABL = ''2'' AND CODOBRA BETWEEN
''0206'' AND ''0216'' ) OR ( ESTABL = ''4'' AND CODOBRA BETWEEN ''0516''
AND ''0527'' )) ' )), 0"</p>
<p>: (FINDSTRING(@[User::tableSource], "NH", 1) == 1) ?</p>
<p>" WHERE (( ESTABL = ''A'' ) OR ( ESTABL = ''2'' AND CODOBRA BETWEEN
''0206'' AND ''0216'' ) OR ( ESTABL = ''4'' AND CODOBRA BETWEEN ''0516''
AND ''0527'' )) ' )), 0"</p>
<p>: (FINDSTRING(@[User::tableSource], "PH", 1) == 1) ?</p>
<p>" WHERE (( ESTABL = ''A'' ) OR ( ESTABL = ''2'' AND CODOBRA BETWEEN
''0206'' AND ''0216'' ) OR ( ESTABL = ''4'' AND CODOBRA BETWEEN ''0516''
AND ''0527'' )) ' )), 0"</p>
<p>: "')), 0"</p>
<p>Paso expInsertLog</p>
<p>@[User::insertLogCarga] = "INSERT INTO
[MASQL20171//HOSTDB2].DB2T.dbo._LOGCARGA</p>
<p>SELECT '" + @[User::tableSource] + "', CURRENT_TIMESTAMP,
CURRENT_TIMESTAMP, (select * from OPENQUERY(DB2P, 'select count(*) from
NEC." + @[User::tableSource] + @[User::CondicionWhere]</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

quedan como tablas donde falló la carga (distinto número de registros en
origen y destino)

<img
src="assets/media/)  En el caso de FAAL041 y FAAL081 tenían una versión antigua del
    paquete. Se pone FAAL041 y FAAL081 en la consulta y funcionan.
    Quedan ya cargadas

3)  En el caso de NH10SQ, PH10SQ y PH10SQ tendían conexiones antiguas en
    Connection manager (aparte de las conexiones (Proyecto)DB2 y
    (Proyecto)PRUEBA). Se borran y pasa la validación. Quedan ya
    cargadas

> NOTA: Borrar en el código /<DTS:LogProviders/> y
> /<DTS:SelectedLogProviders/> porque al borrar las conexiones que no se
> usan, no borra estos apartados.

4)  NH12SQ falló la carga del fichero. 🡪 Cannot open the datafile
    "/Maserv5/sap/$/Ficheros Db2 Host//
    DBZNEC0.DB2P.DBNEC0.TNH12SQ.UNLDS.txt".

> Se copia desde "/Maserv5/sap/$/Ficheros Db2 Host/20200101//
> DBZNEC0.DB2P.DBNEC0.TNH12SQ.UNLDS.txt" a ese directorio que usa el
> paquete y ya funciona.

5)  FV02SQ va lentísima (aunque son solo 4663919 registros).
    “Communication Link Failure” -/> debió dar Timeout

CONCLUSION: Todo OK para los paquetes 1,2,3 de 2.MoveDataDB2ToSQLServer
-/>

<span class="mark">Revisar solamente la carga de FV02SQ</span>
