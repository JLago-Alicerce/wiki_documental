<!--
---
source: NAVANTIA-Interfaces_AWD_ALHD.md
doc_source: NAVANTIA-Interfaces_AWD_ALHD.docx
inserted: 2025-06-19T08:08:00.017064
---
-->

<div class="fragment-meta">source: NAVANTIA-Interfaces_AWD_ALHD.md | doc: NAVANTIA-Interfaces_AWD_ALHD.docx | inserted: 2025-06-19T08:08:00.017064</div>

# PAQUETES 2005 - INTERFACES_AWD_ALHD_SSIS

<img src="assets/media/image1.png"
style="width:3.33333in;height:2.64583in" /><img src="assets/media/image2.png"
style="width:2.57292in;height:2.27083in" />

## Paquetes comunes

### /_AtributosConfig.dtsx

Llama a /_LimpiarCamposBO.dtsx

### /_CompAtributosConfig.dtsx

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">User::V_SQL_ATRIB -&gt; User::V_RESULT
&gt; ForEachLoop &gt; User::V_SQL -&gt; User::V_CONTADOR</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><strong>-- contador de estado a
fin</strong></p>
<p><strong>select count(*) from _ejecucion</strong></p>
<p><strong>where codobra =(select _codobra from _obras</strong></p>
<p><strong>where id = (select max(id) from _obras</strong></p>
<p><strong>where _proyecto = User::GLOBAL_PROYECTO ))</strong></p>
<p><strong>AND TABLA = 'TABLAS' AND ESTADO = 'FIN'</strong></p></td>
</tr>
<tr>
<td style="text-align: left;"><p>UPDATE UpdateNotice set Finish_Date =
getdate() where Id = (select max(id) from UpdateNotice )</p>
<p>Disable si @[User::V_ESCRIBR_LOG] == TRUE</p></td>
</tr>
</tbody>
</table>

### /_LimpiarLogs.dtsx

| Borra todos los /*.log y los LOGERROR//.txt |
|---------------------------------------------|

### /_LimpiarLogs_EEA5.dtsx

| Boora todos los @/[User::GLOBAL_PATH_LOG/]//.log |
|--------------------------------------------------|

### /_StatusDeleted.dtsx

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th>User::V_Update_NC08SQ</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>update nc08sq</p>
<p>set _tstamp = getdate(),</p>
<p>_status = 'DELETED'</p>
<p>from nc08sq a</p>
<p>where _status &lt;&gt; 'DELETED'</p>
<p>And not exists (</p>
<p>select * from interfacesDWH.dbo.copic_referencia b</p>
<p>where a.copic = b.copic</p>
<p>and a.referencia = b.referencia</p>
<p>)</p></td>
</tr>
<tr>
<td><p>update nc13sq</p>
<p>set _tstamp = getdate(),</p>
<p>_status = 'DELETED'</p>
<p>from NC13SQ R</p>
<p>WHERE _STATUS &lt;&gt; 'DELETED'</p>
<p>AND NOT EXISTS</p>
<p>(SELECT * FROM NC11SQ RV</p>
<p>WHERE RV.ESTABL=R.ESTABL AND RV.CODOBRA=R.CODOBRA</p>
<p>AND RV.PLANO=R.PLANO AND RV.REVISION=R.REVISION</p>
<p>AND RV._STATUS &lt;&gt; 'DELETED')</p></td>
</tr>
<tr>
<td><p>update nc13sq</p>
<p>set _tstamp = getdate(),</p>
<p>_status = 'DELETED'</p>
<p>from NC13SQ R</p>
<p>WHERE _STATUS &lt;&gt; 'DELETED'</p>
<p>AND NOT EXISTS</p>
<p>(SELECT * FROM NC11SQ RV</p>
<p>WHERE RV.ESTABL=R.ESTABL AND RV.CODOBRA=R.CODOBRA</p>
<p>AND RV.PLANO=R.PLANO AND RV.REVISION=R.REVISION</p>
<p>AND RV._STATUS &lt;&gt; 'DELETED')</p></td>
</tr>
<tr>
<td><p>update NC14SQ</p>
<p>set _tstamp = getdate(),</p>
<p>_status = 'DELETED'</p>
<p>from nc14sq n14</p>
<p>where n14._status &lt;&gt; 'DELETED'</p>
<p>and not exists</p>
<p>(select * from nc13sq n13</p>
<p>where n13.ESTABL = n14.ESTABL</p>
<p>and n13.CODOBRA = n14.CODOBRA</p>
<p>and n13.PLANO = n14.PLANO</p>
<p>AND n13.TIPOREF = n14.TIPOREF</p>
<p>and n13.NUMREF = n14.NUMREF</p>
<p>and n13._status &lt;&gt; 'DELETED')</p></td>
</tr>
<tr>
<td><p>update NC14SQ</p>
<p>set _STATUS='DELETED',</p>
<p>_tstamp = getdate()</p>
<p>WHERE _ID IN (</p>
<p>SELECT R._ID</p>
<p>FROM NC14SQ R</p>
<p>INNER JOIN NC13SQ R2</p>
<p>ON R.ESTABL=R2.ESTABL AND R.CODOBRA=R2.CODOBRA</p>
<p>AND R.PLANO=R2.PLANO AND R.TIPOREF=R2.TIPOREF</p>
<p>AND R.NUMREF=R2.NUMREF</p>
<p>LEFT JOIN NC12SQ LM</p>
<p>ON LM.ESTABL=R.ESTABL AND LM.CODOBRA=R.CODOBRA</p>
<p>AND LM.PLANO=R.PLANO AND LM.LINEA=R.LINEIN</p>
<p>WHERE (R.TIPOREF='B' OR R.TIPOREF='S')</p>
<p>AND (R2.TIPIND='OB' OR R2.TIPIND='NG' OR (R2.TIPIND='' AND
R.LINEFI=R.LINEIN))</p>
<p>AND (R._STATUS&lt;&gt;'DELETED')</p>
<p>AND (LM._STATUS='DELETED' OR LM._STATUS IS NULL))</p></td>
</tr>
<tr>
<td><p>update NC33SQ</p>
<p>set _tstamp = getdate (),</p>
<p>_status = 'DELETED'</p>
<p>from nc33sq n33</p>
<p>where not exists</p>
<p>(select * from nc34sq n34</p>
<p>where n33.establ = n34.establ</p>
<p>and n33.codobra = n34.codobra</p>
<p>and n33.plano = n34.plano</p>
<p>and n33.numref = n34.numref</p>
<p>and n33.tiporef = n34.tiporef</p>
<p>and n34._status &lt;&gt; 'DELETED')</p>
<p>and n33._status &lt;&gt; 'DELETED'</p></td>
</tr>
<tr>
<td><p>update DBO.INCopic_HojasCatalogoAplicabilidadCopics</p>
<p>set _tstamp = getdate(), _status = 'DELETED'</p>
<p>where DBO.INCopic_HojasCatalogoAplicabilidadCopics.copic</p>
<p>not in</p>
<p>(select distinct n8.copic collate Modern_Spanish_CI_AS</p>
<p>from nc08sq n8</p>
<p>where n8._status &lt;&gt;'DELETED' )</p>
<p>and DBO.INCopic_HojasCatalogoAplicabilidadCopics._status &lt;&gt;
'DELETED'</p></td>
</tr>
<tr>
<td><p>update DBO.INCopic_HojasCatalogoAplicabilidadCopics</p>
<p>set _tstamp = getdate(), _status = 'DELETED'</p>
<p>from DBO.INCopic_HojasCatalogoAplicabilidadCopics a</p>
<p>where not exists</p>
<p>(select * from dbo.INCopic_HojasCatalogo b</p>
<p>where a.codigohoja = b.codigohoja</p>
<p>and b._status &lt;&gt; 'DELETED')</p>
<p>and a._status &lt;&gt; 'DELETED'</p></td>
</tr>
<tr>
<td>User::V_Update_tcCodigos</td>
</tr>
<tr>
<td><p>update tchojascatalogo_documentos</p>
<p>set _status = 'DELETED',</p>
<p>_tstamp = getdate()</p>
<p>where _status &lt;&gt; 'DELETED'</p>
<p>and cdgentidad not in</p>
<p>(select codigohoja from INCopic_HojasCatalogoAplicabilidadObras</p>
<p>where _status &lt;&gt; 'Deleted' )</p></td>
</tr>
<tr>
<td>User::V_Update_SeccionesDocumento con parámetros 0 y 1 =
User::GLOBAL_PROYECTO y User::GLOBAL_PROYECTO</td>
</tr>
<tr>
<td>User::V_Update_Documentos con entradas User::GLOBAL_PROYECTO y
System::VersionMinor</td>
</tr>
<tr>
<td>User::V_Update_trRevisionDocRevisionSec con User::GLOBAL_PROYECTO y
User::GLOBAL_PROYECTO</td>
</tr>
<tr>
<td><p>update trRevisionDocRevisionSec</p>
<p>set _Status = 'DELETED', _Tstamp = getdate()</p>
<p>FROM trRevisionDocRevisionSec A</p>
<p>WHERE A.cdgDocumento is not null</p>
<p>AND A.RevisionDoc is not null</p>
<p>AND A._Status &lt;&gt; 'DELETED'</p>
<p>AND Not EXISTS</p>
<p>(SELECT * FROM RevisionesDocumento B</p>
<p>WHERE A.cdgDocumento = B.cdgDocumento</p>
<p>AND A.RevisionDoc = B.RevisionDoc</p>
<p>AND B._Status &lt;&gt; 'DELETED')</p>
<p>and A.Revisionsec &gt;</p>
<p>coalesce ( (select max( C.Revisionsec)</p>
<p>FROM trRevisionDocRevisionSec C</p>
<p>WHERE C.cdgDocumento is not null</p>
<p>AND C.RevisionDoc is not null</p>
<p>AND A.cdgdocumento = C.cdgDocumento</p>
<p>AND A.REVISIONDOC = C.REVISIONDOC</p>
<p>AND A.CDGSECCION = C.CDGSECCION</p>
<p>AND C._Status &lt;&gt; 'DELETED'</p>
<p>AND EXISTS</p>
<p>(SELECT * FROM RevisionesDocumento D</p>
<p>WHERE C.cdgDocumento = D.cdgDocumento</p>
<p>AND C.RevisionDoc = D.RevisionDoc</p>
<p>AND D._Status &lt;&gt; 'DELETED')</p>
<p>) , ' ')</p>
<p>Con User::GLOBAL_PROYECTO y User::GLOBAL_PROYECTO</p></td>
</tr>
<tr>
<td><p>Update trrevisiondocrevisionsec</p>
<p>set trrevisiondocrevisionsec._STATUS = 'DELETED',</p>
<p>trrevisiondocrevisionsec._TSTAMP = getdate()</p>
<p>where not exists</p>
<p>(select * from fesrv014.controldoc.dbo.trrevisiondocrevisionsec
t14</p>
<p>where trrevisiondocrevisionsec.cdgdocumento = t14.cdgdocumento
collate Modern_Spanish_CI_AS</p>
<p>and trrevisiondocrevisionsec.Revisiondoc = t14.revisiondoc collate
Modern_Spanish_CI_AS</p>
<p>and trrevisiondocrevisionsec.Revisionsec = t14.revisionsec collate
Modern_Spanish_CI_AS</p>
<p>and trrevisiondocrevisionsec.cdgseccion = t14.cdgseccion collate
Modern_Spanish_CI_AS)</p>
<p>and trrevisiondocrevisionsec._status &lt;&gt; 'DELETED'</p></td>
</tr>
<tr>
<td>User::V_Update_SeccionesDocumento con User::GLOBAL_PROYECTO y
User::GLOBAL_PROYECTO</td>
</tr>
<tr>
<td><p>Update RevisionesSeccion</p>
<p>set RevisionesSeccion._STATUS = 'DELETED',</p>
<p>RevisionesSeccion._TSTAMP = getdate()</p>
<p>where RevisionesSeccion._STATUS &lt;&gt; 'DELETED'</p>
<p>and (RevisionesSeccion.cdgSeccion not in</p>
<p>(select SeccionesDocumento.cdgSeccion</p>
<p>from SeccionesDocumento</p>
<p>where SeccionesDocumento._STATUS &lt;&gt; 'DELETED'</p>
<p>)</p>
<p>or not exists</p>
<p>(select * from trRevisiondocrevisionsec tr</p>
<p>where RevisionesSeccion.cdgseccion = tr.cdgseccion</p>
<p>and RevisionesSeccion.revisionSec = tr.revisionSec</p>
<p>and RevisionesSeccion._STATUS &lt;&gt; 'DELETED'</p>
<p>))</p></td>
</tr>
<tr>
<td><p>Update trRevisionSecFichero</p>
<p>set trRevisionSecFichero._STATUS = 'DELETED',</p>
<p>trRevisionSecFichero._TSTAMP = getdate()</p>
<p>from trRevisionSecFichero tr</p>
<p>where tr._STATUS &lt;&gt; 'DELETED'</p>
<p>and not exists</p>
<p>(select *</p>
<p>from RevisionesSeccion r</p>
<p>where r._STATUS &lt;&gt; 'DELETED'</p>
<p>and r.cdgseccion = tr.cdgseccion</p>
<p>and r.revisionsec = tr.revisionsec</p>
<p>)</p></td>
</tr>
<tr>
<td><p>Update trRevisionSecFichero</p>
<p>set trRevisionSecFichero._STATUS = 'DELETED',</p>
<p>trRevisionSecFichero._TSTAMP = getdate()</p>
<p>where trRevisionSecFichero._STATUS &lt;&gt; 'DELETED'</p>
<p>and (trRevisionSecFichero.cdgSeccion not in</p>
<p>(select SeccionesDocumento.cdgSeccion</p>
<p>from SeccionesDocumento</p>
<p>where SeccionesDocumento._STATUS &lt;&gt; 'DELETED'</p>
<p>)</p>
<p>)</p></td>
</tr>
<tr>
<td><p>Update trRevisionSecFichero</p>
<p>set trRevisionSecFichero._STATUS = 'DELETED',</p>
<p>trRevisionSecFichero._TSTAMP = getdate()</p>
<p>where not exists</p>
<p>(select * from fesrv014.controldoc.dbo.trrevisionsecfichero t14</p>
<p>where trrevisionSEcfichero.cdgseccion = t14.cdgseccion collate
Modern_Spanish_CI_AS</p>
<p>and trrevisionSEcfichero.Revisionsec = t14.revisionsec collate
Modern_Spanish_CI_AS</p>
<p>and trrevisionSEcfichero.cdgfichero = t14.cdgfichero collate
Modern_Spanish_CI_AS)</p>
<p>and trrevisionSEcfichero._status &lt;&gt; 'DELETED'</p></td>
</tr>
<tr>
<td>User::V_Update_trRevisionDocFichero con User::GLOBAL_PROYECTO</td>
</tr>
<tr>
<td><p>Update trRevisionDocFichero</p>
<p>set trRevisionDocFichero._STATUS = 'DELETED',</p>
<p>trRevisionDocFichero._TSTAMP = getdate()</p>
<p>where trRevisionDocFichero._STATUS &lt;&gt; 'DELETED'</p>
<p>and not exists</p>
<p>(select *</p>
<p>from fesrv014.controldoc.dbo.trrevisiondocfichero t14</p>
<p>where trrevisiondocfichero.cdgdocumento = t14.cdgdocumento collate
Modern_Spanish_CI_AS</p>
<p>and trrevisiondocfichero.revisiondoc = t14.revisiondoc collate
Modern_Spanish_CI_AS</p>
<p>and trrevisiondocfichero.cdgfichero = t14.cdgfichero collate
Modern_Spanish_CI_AS)</p></td>
</tr>
<tr>
<td>User::V_Update_ficheros</td>
</tr>
<tr>
<td>User::V_Update_ficheros_tr</td>
</tr>
<tr>
<td><p>Update Ubicaciones</p>
<p>set Ubicaciones._STATUS = 'DELETED',</p>
<p>Ubicaciones._TSTAMP = getdate()</p>
<p>where Ubicaciones._STATUS &lt;&gt; 'DELETED'</p>
<p>and Ubicaciones.cdgUbicacion not in</p>
<p>(select ficheros.cdgUbicacion</p>
<p>from ficheros</p>
<p>where ficheros._STATUS &lt;&gt; 'DELETED'</p>
<p>)</p></td>
</tr>
<tr>
<td><p>update situacionesRevisionDocumento</p>
<p>set _status = 'DELETED'</p>
<p>from SituacionesRevisionDocumento a</p>
<p>WHERE a.cdgdocumento not in</p>
<p>(select T.cdgDocumento</p>
<p>from (</p>
<p>(Select DISTINCT tcDocsOT_Documentos.cdgDocumento as
cdgDocumento,</p>
<p>tcDocsOT_Documentos.RevisionDoc as RevisionDoc,</p>
<p>tcDocsOT_Documentos.Establecimiento as Establecimiento,</p>
<p>tcDocsOT_Documentos.Obra as Obra,</p>
<p>tcDocsOT_Documentos._STATUS COLLATE Modern_Spanish_CI_AS as
STATUS</p>
<p>FROM tcDocsOT_Documentos)</p>
<p>UNION</p>
<p>(Select DISTINCT tcOOTT_Documentos.cdgDocumento as cdgDocumento,</p>
<p>tcOOTT_Documentos.RevisionDoc as RevisionDoc,</p>
<p>tcOOTT_Documentos.Establecimiento as Establecimiento,</p>
<p>tcOOTT_Documentos.Obra as Obra,</p>
<p>tcOOTT_Documentos._STATUS COLLATE Modern_Spanish_CI_AS as STATUS</p>
<p>FROM tcOOTT_Documentos)</p>
<p>UNION</p>
<p>(Select DISTINCT tcAvisosRevision_Documentos.cdgDocumento</p>
<p>COLLATE Modern_Spanish_CI_AS as cdgDocumento,</p>
<p>tcAvisosRevision_Documentos.RevisionDoc</p>
<p>COLLATE Modern_Spanish_CI_AS as RevisionDoc,</p>
<p>tcAvisosRevision_Documentos.Establecimiento</p>
<p>COLLATE Modern_Spanish_CI_AS as Establecimiento,</p>
<p>tcAvisosRevision_Documentos.Obra</p>
<p>COLLATE Modern_Spanish_CI_AS as Obra,</p>
<p>tcAvisosRevision_Documentos._STATUS</p>
<p>COLLATE Modern_Spanish_CI_AS as STATUS</p>
<p>FROM tcAvisosRevision_Documentos)</p>
<p>UNION</p>
<p>(Select DISTINCT tcHojasCatalogo_Documentos.cdgDocumento</p>
<p>COLLATE Modern_Spanish_CI_AS as cdgDocumento,</p>
<p>tcHojasCatalogo_Documentos.RevisionDoc COLLATE Modern_Spanish_CI_AS
as RevisionDoc,</p>
<p>INCopic_HojasCatalogoAplicabilidadObras.establecimiento</p>
<p>COLLATE Modern_Spanish_CI_AS as Establecimiento,</p>
<p>INCopic_HojasCatalogoAplicabilidadObras.obra COLLATE
Modern_Spanish_CI_AS as Obra,</p>
<p>tcHojasCatalogo_Documentos._STATUS COLLATE Modern_Spanish_CI_AS as
STATUS</p>
<p>FROM tcHojasCatalogo_Documentos</p>
<p>left join INCopic_HojasCatalogoAplicabilidadObras</p>
<p>on INCopic_HojasCatalogoAplicabilidadObras.codigohoja</p>
<p>COLLATE Modern_Spanish_CI_AS =
tcHojasCatalogo_Documentos.cdgentidad)</p>
<p>UNION</p>
<p>(Select tcCodigos_Documentos.cdgDocumento COLLATE
Modern_Spanish_CI_AS as cdgDocumento,</p>
<p>tcCodigos_Documentos.RevisionDoc</p>
<p>COLLATE Modern_Spanish_CI_AS as RevisionDoc,</p>
<p>NC32.Establ COLLATE Modern_Spanish_CI_AS as Establecimiento,</p>
<p>NC32.Codobra COLLATE Modern_Spanish_CI_AS as Obra,</p>
<p>tcCodigos_Documentos._STATUS COLLATE Modern_Spanish_CI_AS as
STATUS</p>
<p>From tcCodigos_Documentos</p>
<p>left join NC12SQ as NC32</p>
<p>on nc32.planoo COLLATE Modern_Spanish_CI_AS =
tcCodigos_Documentos.cdgEntidad )</p>
<p>) as T</p>
<p>where T.cdgDocumento = a.cdgDocumento</p>
<p>and T.STATUS &lt;&gt; 'DELETED')</p></td>
</tr>
<tr>
<td><p>update situacionesRevisionDocumento</p>
<p>set _status = 'DELETED'</p>
<p>from SituacionesRevisionDocumento a</p>
<p>WHERE a._status &lt;&gt; 'DELETED'</p>
<p>and NOT EXISTS(</p>
<p>select * from FESRV014.CONTROLDOC.DBO.SituacionesRevisionDocumento
S</p>
<p>where S.cdgdocumento = a.cdgdocumento collate
Modern_Spanish_CI_AS</p>
<p>and S.RevisionDoc = a.RevisionDoc collate Modern_Spanish_CI_AS</p>
<p>and S.cdgTipoSitDoc = a.cdgTipoSitDoc collate
Modern_Spanish_CI_AS)</p></td>
</tr>
<tr>
<td><p>update situacionesRevisionSeccion</p>
<p>set _status = 'DELETED'</p>
<p>from SituacionesRevisionSeccion a</p>
<p>WHERE a._status &lt;&gt; 'DELETED'</p>
<p>and NOT EXISTS(</p>
<p>select * from FESRV014.CONTROLDOC.DBO.SituacionesRevisionSeccion
S</p>
<p>where S.cdgSeccion = a.cdgSeccion collate Modern_Spanish_CI_AS</p>
<p>and S.RevisionSec = a.RevisionSec collate Modern_Spanish_CI_AS</p>
<p>and S.cdgTipoSitSec = a.cdgTipoSitSec collate
Modern_Spanish_CI_AS)</p></td>
</tr>
<tr>
<td><p>update situacionesRevisionSeccion</p>
<p>set _status = 'DELETED',</p>
<p>_tstamp = getdate()</p>
<p>from situacionesRevisionSeccion s</p>
<p>where not exists</p>
<p>(select * from dbo.revisionesSeccion r</p>
<p>where s.cdgseccion = r.cdgseccion</p>
<p>and s.revisionsec = r.revisionsec</p>
<p>and r._status &lt;&gt; 'DELETED')</p>
<p>and s._status &lt;&gt; 'DELETED'</p></td>
</tr>
<tr>
<td><p>update situacionesRevisionSeccion</p>
<p>set _status = 'DELETED',</p>
<p>_tstamp = getdate()</p>
<p>from situacionesRevisionSeccion s</p>
<p>where not exists</p>
<p>(select * from dbo.revisionesSeccion r</p>
<p>where s.cdgseccion = r.cdgseccion</p>
<p>and s.revisionsec = r.revisionsec</p>
<p>and r._status &lt;&gt; 'DELETED')</p>
<p>and s._status &lt;&gt; 'DELETED'</p></td>
</tr>
<tr>
<td>User::V_Update_Cora223</td>
</tr>
<tr>
<td>User::V_Update_Cora225</td>
</tr>
<tr>
<td><p>Update trRevisionSecFichero</p>
<p>set trRevisionSecFichero._STATUS = 'DELETED',</p>
<p>trRevisionSecFichero._TSTAMP = getdate()</p>
<p>where trRevisionSecFichero._STATUS &lt;&gt; 'DELETED'</p>
<p>and (trRevisionSecFichero.cdgFichero not in</p>
<p>(select Ficheros.cdgFichero</p>
<p>from Ficheros</p>
<p>where Ficheros._STATUS &lt;&gt; 'DELETED'</p>
<p>)</p>
<p>)</p></td>
</tr>
</tbody>
</table>

## Anexos

### Anexos.dtsx

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th><p><strong>--EXTRACT PREVIO a NC17SQ_ANEXOS</strong></p>
<p><strong>(SELECT ESTABL AS ESTABL, CODOBRA AS CODOBRA, DOCUREV as
docurev, 'ANEXO01' as numero, cast(BZNC.NCUDF06('NC06FV', 'NC17SQ'
,SECUE06, 'ANEXO01' ,'INGLES') as varchar(4000)) as anexo FROM
NEC.NC17SQ WHERE ESTABL = 'A' AND CODOBRA = 'AWD1' AND ANEXOS = 'SI')
UNION (SELECT ESTABL AS ESTABL, CODOBRA AS CODOBRA, DOCUREV as docurev,
'ANEXO02' as numero , cast(BZNC.NCUDF06('NC06FV', 'NC17SQ' ,SECUE06,
'ANEXO02' ,'INGLES') as varchar(4000)) as anexo FROM NEC.NC17SQ WHERE
ESTABL = 'A' AND CODOBRA = 'AWD1' AND ANEXOS = 'SI')</strong></p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><strong>delete nc17sq_anexos</strong></p>
<p><strong>from NC17SQ_anexos DWH</strong></p>
<p><strong>WHERE dwh.anexo = ''</strong></p>
<p><strong>or docurev not in</strong></p>
<p><strong>(select docurev from nc17sq)</strong></p></td>
</tr>
<tr>
<td><p>select distinct docurev from dbo.nc17sq_anexos where numeroanexo
&gt; 'anexo01'</p>
<p>- &gt;User::OBJECT_DOCUREV y un bucle por cada docurev</p></td>
</tr>
<tr>
<td><p>Bucle mientras @V_CONT_ANEXOS &lt; 99 &amp;&amp; @V_ANEXO != ""
ejecuta</p>
<p>{User::V_CONSULTAANEXOS -&gt; User::V_ANEXO (resultado) y
User::V_INSERT_ANEXOS}</p></td>
</tr>
<tr>
<td></td>
</tr>
</tbody>
</table>

## Avisos

### Avisos_Rev_BO18SQ.dtsx

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th><p><strong>SELECT ESTABL ,CODOBRA ,ORDEN ,REVISION ,DOCUREV ,FEREVIS
,SITREVIS</strong></p>
<p><strong>,CTRPREV ,CTRAVISO ,CTRAEJEC ,DNIREV ,DNIAPR ,TIPDOCU
,SECUE06</strong></p>
<p><strong>,REVPLA ,FEAPR,</strong></p>
<p><strong>CAST(BZNC.NCUDF06('BO06FV ','BO18SQ'
,SECUE06,'DESREV','INGLES') AS CHAR(100)) AS DESCR</strong></p>
<p><strong>FROM NEC.BO18SQ WHERE establ= ? and codobra =?</strong></p>
<p><strong>(Lee de Db2 y carga en BO18SQ)</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### Avisos_Rev_NC17SQ.dtsx

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th><p><strong>SELECT</strong></p>
<p><strong>ESTABL,CODOBRA,DOCUREV,DOCUREF,FECDOCU,FEFINAL,</strong></p>
<p><strong>NOTAS,ANEXOS,DNIRDOC,TIPDOCU,SECUE06,CENTEMI,ORIGIN,GDEFECT,DECISION,CDEFECT,CAUSAPR,FECHRESO,GIMPORT,IMPACTOE,TRANSARM,IMPRVING,IMPRVMAT,IMPRVPRO,IMPRVVAR,IMPREING,IMPREMAT,IMPREPRO,IMPREVAR,IMPRRING,IMPRRMAT,IMPRRPRO,IMPRRVAR,MONEDA,
SITING,SITAPROV,SITPRO,SITGESCAL,SITOTROS,DNISITING,DNISITAPRO,DNISITPRO,DNISITCAL,DNISITOTR,GRUCOSTE,BLOQUE,FECSITING,FECSITAPRO,FECSITPRO,FECSITCAL,FECSITOTR,MARFUNC,</strong></p>
<p><strong>cast(BZNC.NCUDF06('NC06FV ','NC17SQ'
,SECUE06,'DESDOC','INGLES') as varchar(8000)) AS DESCR</strong></p>
<p><strong>FROM NEC.NC17SQ</strong></p>
<p><strong>WHERE CODOBRA=? AND ESTABL=?</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### Avisos_Rev_NC18SQ.dtsx

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;"><p><strong>SELECT</strong></p>
<p><strong>ESTABL,CODOBRA,PLANO,REVISION,DOCUREV,FEREVIS,SITREVIS,CTRPREV,CTRAVISO,CTRAEJEC,DNIREV,DNIAPR,TIPDOCU,SECUE06,REVPLA,FEAPR,</strong></p>
<p><strong>cast(BZNC.NCUDF06('NC06FV ','NC18SQ'
,SECUE06,'DESREV','INGLES') as varchar(4000)) AS DESCR</strong></p>
<p><strong>FROM NEC.NC18SQ WHERE CODOBRA=? AND
ESTABL=?</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### AWD1.TareasNuevosCOPIC.dtsx

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th><p>Con la conexion InterfacesADW, crea fichero AWD001.txt</p>
<p><strong>SELECT DISTINCT NC08SQ.COPIC,
Convert(Char(14),NC08SQ.REFERENCIA) REFERENCIA, Convert(Char(82),
replace(NC08SQ.VALOR,'</strong></p>
<p><strong>',' ')) VALOR, NC08SQ._TSTAMP AS fecha</strong></p>
<p><strong>FROM NC08SQ</strong></p>
<p><strong>inner join NC12SQ</strong></p>
<p><strong>on NC08SQ.COPIC = nc12SQ.PLANOO</strong></p>
<p><strong>and nc12sq.codobra = 'AWD1'</strong></p>
<p><strong>WHERE (NC08SQ._STATUS = 'NEW')</strong></p>
<p><strong>and (NC08SQ.REFERENCIA = 'INGLES') AND (NC08SQ._TSTAMP
BETWEEN GETDATE() - 2 AND GETDATE());</strong></p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p>Executable</p>
<p>@[User::GLOBAL_PATH_LOGPLAN] + @[User::GLOBAL_PROYECTO] +
"/Asuntos_Y_Tareas/Carga.exe"</p>
<p>WorkingDirectory</p>
<p>@[User::GLOBAL_PATH_LOGPLAN] + @[User::GLOBAL_PROYECTO] +
"/Asuntos_Y_Tareas"</p>
<p>Argumentos</p>
<p>"A _ AWD0000001 " + @[User::GLOBAL_PATH_LOG] + "AWD001.txt " +
@[User::GLOBAL_PATH_LOG] + "AsuntosYTareas.exe.log"</p></td>
</tr>
</tbody>
</table>

### Deshabilitar_Index.dtsx

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;"><p><strong>SELECT NAME FROM SYSOBJECTS
WHERE XTYPE = 'U' AND CATEGORY &lt;&gt; 2</strong></p>
<p><strong>Con User::GLOBAL_CATEGORY. Los guarda en User::Tabla_object y
recorre cada objeto del bucle User::GLOBAL_CATEGORY para hacer
User::V_Alter</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## Documentos_tecnicos

### Documentos_tecnicos_NC10SQ.dtsx

<img src="assets/media/image3.png"
style="width:6.53125in;height:4.82292in" />

<img src="assets/media/image4.png"
style="width:6.53125in;height:2.95833in" />

<img src="assets/media/image5.png"
style="width:4.44792in;height:2.10417in" />

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">TRUNCATE TABLE DBO.NC10SQ</th>
</tr>
</thead>
<tbody>
<tr>
<td
style="text-align: left;"><p><strong>--DocTec_NC10SQ_Extract</strong></p>
<p><strong>SELECT
N10.ESTABL,N10.CODOBRA,N10.PLANO,N10.TIPOPLA,N10.TAREA,N10.CENDESA,N10.CENCOST,</strong></p>
<p><strong>N10.ZONA,N10.BLOQUE,N10.MODULO,N10.SECCION,N10.GRUCOSTE,N10.PRODINT,N11.SITOFTEC,</strong></p>
<p><strong>N10.SITINPRO,N10.SITAPROV,N10.SITCONFI,N10.SITINTEG,N10.SITLOGIS,N10.URREALZ,</strong></p>
<p><strong>N10.URAPROB,N10.URCIRCU,N10.URINPRO,N10.URINTEG,N10.URAPROV,N10.URCONFI,</strong></p>
<p><strong>N10.AVISOREV,N10.DNI,N10.CLASIFI,N10.SECUE06,N10.FECREAC,</strong></p>
<p><strong>cast(BZNC.NCUDF06('NC06FV ','NC10SQ'
,N10.SECUE06,'DESPLAC','INGLES') as char(100)) AS DESPLAC,</strong></p>
<p><strong>cast(BZNC.NCUDF06('NC06FV ','NC10SQ'
,N10.SECUE06,'DESPLAL','INGLES') as char(100)) AS DESPLAL</strong></p>
<p><strong>FROM NEC.NC10SQ N10</strong></p>
<p><strong>INNER JOIN NEC.NC11SQ N11</strong></p>
<p><strong>ON N10.ESTABL = N11.ESTABL</strong></p>
<p><strong>AND N10.CODOBRA = N11.CODOBRA</strong></p>
<p><strong>AND N10.PLANO = N11.PLANO</strong></p>
<p><strong>AND N11.REVISION = (SELECT MAX(N11A.REVISION)</strong></p>
<p><strong>FROM NEC.NC11SQ N11A</strong></p>
<p><strong>WHERE N11A.ESTABL = N10.ESTABL</strong></p>
<p><strong>AND N11A.CODOBRA = N10.CODOBRA</strong></p>
<p><strong>AND N11A.PLANO = N10.PLANO)</strong></p>
<p><strong>WHERE</strong></p>
<p><strong>(N10.SITLOGIS = 'A' OR N10.SITLOGIS = 'I') AND N10.CODOBRA=?
AND N10.ESTABL=?</strong></p></td>
</tr>
</tbody>
</table>

Donde las variables son

| V_BARRA | // |  |
|----|----|----|
| V_CODOBRA | STNA |  |
| V_CONTADOR | 0 |  |
| V_ESTABL | A |  |
| V_ID_EJECUCION | 0 |  |
| V_INSERT_ERROR | INSERT INTO /[dbo/]./[/_EJECUCION/] (/[Tabla/],/[Estado/],/[Codobra/],/[Proyecto/]) VALUES ('NC10SQ','ERROR','STNA', 'AWD') | "INSERT INTO /[dbo/]./[/_EJECUCION/] (/[Tabla/],/[Estado/],/[Codobra/],/[Proyecto/]) VALUES ('NC10SQ','ERROR','" + @V_CODOBRA + "','" + @V_PROYECTO + "')" |
| V_JOB_NAME |  |  |
| V_PROYECTO | AWD |  |
| V_RUTA_ERRORLOG | LOGERROR// | @GLOBAL_PATH_LOG + @V_SUBCARPETA |
| V_STOP_JOB | exec msdb.dbo.sp_stop_job '' | "exec msdb.dbo.sp_stop_job '" + @V_JOB_NAME + "'" |
| V_SUBCARPETA | LOGERROR// |  |
| V_TABLA | NC10SQ |  |
| VLINEASERROR |  |  |

### Documentos_tecnicos_NC11SQ.dtsx

<img src="assets/media/image6.png"
style="width:3.17687in;height:3.90625in" /><img src="assets/media/image7.png"
style="width:3.3125in;height:2.71359in" />

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;"><p><strong>SELECT
ESTABL,CODOBRA,PLANO,REVISION,DNIDIB,DNICOM,DNIAPR,</strong></p>
<p><strong>FEINREA,FEAPROB,FEFIREA,FEENARM,FEINPRE,FEFIPRE,FEENPRO,</strong></p>
<p><strong>FEPRPRE,FEPRREA,FEINSPE,FECLASI,CENDESA,CENCOST,SECINPRO,</strong></p>
<p><strong>SITOFTEC,SITINPRO,SECOFTEC,FECINPRO,HORINPRO,DOCUREV,</strong></p>
<p><strong>CODENVIO,DOCLIC,REVDIB,DOCCLI,REVLIC,REVCLI,PADRE,SECUE06,CAST(BZNC.NCUDF06('NC06FV
','NC11SQ' ,SECUE06,'DESPLAC','INGLES') AS CHAR(100)) AS DESPLAC
,</strong></p>
<p><strong>CAST(BZNC.NCUDF06('NC06FV ','NC11SQ'
,SECUE06,'DESPLAL','INGLES') AS CHAR(100)) AS DESPLAL</strong></p>
<p><strong>FROM NEC.NC11SQ A</strong></p>
<p><strong>WHERE A.CODOBRA=? AND A.ESTABL=? AND EXISTS</strong></p>
<p><strong>(SELECT * FROM NEC.NC10SQ B WHERE A.ESTABL= B.ESTABL AND
A.CODOBRA = B.CODOBRA AND A.PLANO = B.PLANO AND (B.SITLOGIS='A' OR
B.SITLOGIS='I'))</strong></p>
<p><strong>--Convierte los campos a STR y los carga en dbo.NC11SQ en
FESRV053.InterfacesDWH</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### Documentos_tecnicos_NC12SQ.dtsx

<img src="assets/media/image8.png"
style="width:2.88731in;height:3.66667in" /><img src="assets/media/image9.png"
style="width:3.53954in;height:2.34375in" />

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;"><p><strong>SELECT
ESTABL,CODOBRA,PLANO,LINEA,TIPOACO,REVISION,GRUCOSTE,</strong></p>
<p><strong>PLANOO,LINEAO,CANCONT,UNIDCON,CANPROD,UNIDPRO,PESO,CANDEMN,</strong></p>
<p><strong>NORMAD,DIMENS,TANOMI,ACABADO,NORMAC,PARTIC,RESIST,INSPEC,</strong></p>
<p><strong>PRESION,MARPLAN,NUMELE,DESGMAR,BLOQUE,DESGBLO,SOLACO,DESGACO,</strong></p>
<p><strong>MODULO,DESGMOD,LOCAL,DESGLOC,DETALLE,NOTAS,MODDEMN,SNREF,</strong></p>
<p><strong>PROCESS,DNI,OBSERV,SECUE06,</strong></p>
<p><strong>CAST(BZNC.NCUDF06('NC06FV ','NC12SQ'
,SECUE06,'DESLINE','INGLES') AS CHAR(100)) AS DESCR</strong></p>
<p><strong>FROM NEC.NC12SQ A</strong></p>
<p><strong>WHERE A.CODOBRA=? AND A.ESTABL=? AND EXISTS</strong></p>
<p><strong>(SELECT * FROM NEC.NC10SQ B WHERE A.ESTABL= B.ESTABL AND
A.CODOBRA = B.CODOBRA AND A.PLANO = B.PLANO AND (B.SITLOGIS='A' OR
B.SITLOGIS='I'))</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### Documentos_tecnicos_NC13SQ.dtsx

<img src="assets/media/image10.png"
style="width:3.88387in;height:4.46875in" />

<img src="assets/media/image11.png"
style="width:4.08966in;height:2.79167in" />

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">TRUNCATE TABLE DBO.NC13SQ</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;">Dts.TaskResult =
(int)ScriptResults.Success;</td>
</tr>
<tr>
<td style="text-align: left;"><p><strong>SELECT
ESTABL,CODOBRA,PLANO,TIPOREF,NUMREF,TIPIND,INDREF,</strong></p>
<p><strong>FEREFER,SECUE06,REVISION,CAST(BZNC.NCUDF06('NC06FV ','NC13SQ'
,SECUE06,'DESREF','INGLES') AS VARCHAR(7000)) AS DESCR</strong></p>
<p><strong>FROM NEC.NC13SQ A</strong></p>
<p><strong>WHERE A.CODOBRA=? AND A.ESTABL=? AND EXISTS</strong></p>
<p><strong>(SELECT * FROM NEC.NC10SQ B WHERE A.ESTABL= B.ESTABL AND
A.CODOBRA = B.CODOBRA AND A.PLANO = B.PLANO AND (B.SITLOGIS='A' OR
B.SITLOGIS='I'))</strong></p>
<p>--Luego DESCR lo pasa a DT_TEXT. Resto a DT_STR. Concatenar salto de
linea en DESCR (en un script). Y los carga en dbo.NC13SQ en
FESRV053.InterfacesDWH</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>delete nc13sq</p>
<p>from nc13sq n13</p>
<p>where not exists</p>
<p>(select * from nc11sq n11</p>
<p>where n13.establ = n11.establ collate Modern_Spanish_CI_AS</p>
<p>and n13.codobra = n11.codobra collate Modern_Spanish_CI_AS</p>
<p>and n13.plano = n11.plano collate Modern_Spanish_CI_AS</p>
<p>and n13.revision = n11.revision collate
Modern_Spanish_CI_AS)</p></td>
</tr>
<tr>
<td style="text-align: left;">Lanza _AtributosConfig.dtsx</td>
</tr>
<tr>
<td style="text-align: left;">Dts.TaskResult =
(int)ScriptResults.Success;</td>
</tr>
<tr>
<td style="text-align: left;"><p>UPDATE [dbo].[NC13SQ]</p>
<p>SET TIPIND = DWH.TIPIND</p>
<p>,INDREF = DWH.INDREF</p>
<p>,FEREFER = DWH.FEREFER</p>
<p>,SECUE06 = DWH.SECUE06</p>
<p>,REVISION = DWH.REVISION</p>
<p>,DESCR = DWH.DESCR</p>
<p>,_TSTAMP = getdate()</p>
<p>,_CHECKSUM = checksum(DWH.ESTABL, DWH.CODOBRA, DWH.PLANO,
DWH.TIPOREF,</p>
<p>DWH.NUMREF, DWH.TIPIND, DWH.INDREF, DWH.FEREFER,</p>
<p>DWH.SECUE06, DWH.REVISION, DWH.DESCR)</p>
<p>,_STATUS = 'UPDATED'</p>
<p>FROM [dbo].[NC13SQ] AWD</p>
<p>INNER JOIN INTERFACESDWH.dbo.NC13SQ DWH</p>
<p>ON AWD.ESTABL = DWH.ESTABL</p>
<p>AND AWD.CODOBRA = DWH.CODOBRA</p>
<p>AND AWD.PLANO = DWH.PLANO</p>
<p>AND AWD.TIPOREF = DWH.TIPOREF</p>
<p>AND AWD.NUMREF = DWH.NUMREF</p>
<p>WHERE checksum(DWH.ESTABL, DWH.CODOBRA, DWH.PLANO, DWH.TIPOREF,</p>
<p>DWH.NUMREF, DWH.TIPIND, DWH.INDREF, DWH.FEREFER,</p>
<p>DWH.SECUE06, DWH.REVISION, DWH.DESCR) &lt;&gt; AWD._CHECKSUM</p>
<p>and AWD.establ = ? and AWD.Codobra = ?</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>UPDATE NC13SQ</p>
<p>SET _STATUS='NEW',</p>
<p>_TSTAMP=GETDATE()</p>
<p>FROM NC13SQ AWD</p>
<p>INNER JOIN INTERFACESDWH.DBO.NC13SQ DWH</p>
<p>ON DWH.ESTABL = AWD.ESTABL</p>
<p>AND DWH.CODOBRA = AWD.CODOBRA</p>
<p>AND DWH.PLANO = AWD.PLANO</p>
<p>AND DWH.TIPOREF = AWD.TIPOREF</p>
<p>AND DWH.NUMREF = AWD.NUMREF</p>
<p>WHERE CHECKSUM(DWH.ESTABL, DWH.CODOBRA, DWH.PLANO, DWH.TIPOREF,</p>
<p>DWH.NUMREF, DWH.TIPIND, DWH.INDREF, DWH.FEREFER,</p>
<p>DWH.SECUE06, DWH.REVISION, DWH.DESCR) = AWD._CHECKSUM</p>
<p>AND AWD._STATUS = 'DELETED'</p>
<p>and AWD.establ = ? and AWD.Codobra = ?</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>INSERT INTO [dbo].[NC13SQ]</p>
<p>(ESTABL ,CODOBRA ,PLANO ,TIPOREF ,NUMREF ,TIPIND ,INDREF ,FEREFER
,SECUE06</p>
<p>,REVISION ,DESCR ,_TSTAMP ,_CHECKSUM ,_STATUS)</p>
<p>select ESTABL, CODOBRA, PLANO, TIPOREF, NUMREF, TIPIND, INDREF,
FEREFER, SECUE06,</p>
<p>REVISION, DESCR, getdate() as_TSTAMP,</p>
<p>checksum (DWH.ESTABL, DWH.CODOBRA, DWH.PLANO, DWH.TIPOREF,</p>
<p>DWH.NUMREF, DWH.TIPIND, DWH.INDREF, DWH.FEREFER,</p>
<p>DWH.SECUE06, DWH.REVISION, DWH.DESCR) as _CHECKSUM,</p>
<p>'NEW' as _STATUS</p>
<p>FROM INTERFACESDWH.DBO.NC13SQ DWH</p>
<p>WHERE NOT EXISTS</p>
<p>(SELECT *</p>
<p>FROM NC13SQ AWD</p>
<p>WHERE DWH.ESTABL = AWD.ESTABL</p>
<p>AND DWH.CODOBRA = AWD.CODOBRA</p>
<p>AND DWH.PLANO = AWD.PLANO</p>
<p>AND DWH.TIPOREF = AWD.TIPOREF</p>
<p>AND DWH.NUMREF = AWD.NUMREF)</p></td>
</tr>
<tr>
<td style="text-align: left;">Dts.TaskResult =
(int)ScriptResults.Success;</td>
</tr>
<tr>
<td style="text-align: left;"><p>UPDATE NC13SQ</p>
<p>SET _STATUS='DELETED',</p>
<p>_TSTAMP=GETDATE()</p>
<p>from nc13sq AWD</p>
<p>WHERE AWD._STATUS &lt;&gt; 'DELETED'</p>
<p>AND AWD.ESTABL = ? AND AWD.CODOBRA = ?</p>
<p>AND NOT EXISTS</p>
<p>(SELECT DWH.*</p>
<p>FROM INTERFACESDWH.DBO.NC13SQ DWH</p>
<p>WHERE DWH.ESTABL = AWD.ESTABL</p>
<p>AND DWH.CODOBRA = AWD.CODOBRA</p>
<p>AND DWH.PLANO = AWD.PLANO</p>
<p>AND DWH.TIPOREF = AWD.TIPOREF</p>
<p>AND DWH.NUMREF = AWD.NUMREF</p>
<p>)</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>INSERT INTO [_EJECUCION]</p>
<p>([Tabla]</p>
<p>,[Estado]</p>
<p>,[Codobra]</p>
<p>,[Proyecto])</p>
<p>VALUES</p>
<p>('NC13SQ'</p>
<p>,'FIN'</p>
<p>,?</p>
<p>,?)</p></td>
</tr>
<tr>
<td style="text-align: left;">Dts.TaskResult =
(int)ScriptResults.Success;</td>
</tr>
</tbody>
</table>

### Documentos_tecnicos_NC14SQ.dtsx (origen es FESRV030)

<img src="assets/media/image12.png"
style="width:3.01042in;height:3.47917in" /><img src="assets/media/image13.png"
style="width:2.875in;height:2.96875in" />

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;"><p><strong>SELECT * FROM NEC.NC14SQ
A</strong></p>
<p><strong>WHERE A.CODOBRA=? AND A.ESTABL=? AND EXISTS</strong></p>
<p><strong>(SELECT * FROM NEC.NC10SQ B WHERE A.ESTABL= B.ESTABL AND
A.CODOBRA = B.CODOBRA AND A.PLANO = B.PLANO AND (B.SITLOGIS='A' OR
B.SITLOGIS='I'))</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### Documentos_tecnicos_NC15SQ.dtsx

<img src="assets/media/image14.png"
style="width:3.3125in;height:3.06834in" />
<img src="assets/media/image15.png"
style="width:3.04167in;height:3.04902in" />

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;"><p><strong>SELECT
ESTABL,CODOBRA,PLANO,LINEA,CANPROD,UNIDPRO,CANRESE,PESO,NORMAD,NORMAC,DIMENS,TANOMI,ACABADO,PARTIC,OBSERV,MAREQUI,MARFUNC,DNI,PROCESS,MARBORR,REVISION,SECUE06,CAST(BZNC.NCUDF06('NC06FV
','NC15SQ' ,SECUE06,'DESLINE','INGLES') AS CHAR(100)) AS
DESCR</strong></p>
<p><strong>FROM NEC.NC15SQ A</strong></p>
<p><strong>WHERE A.CODOBRA=? AND A.ESTABL=? AND EXISTS</strong></p>
<p><strong>(SELECT * FROM NEC.NC10SQ B WHERE A.ESTABL= B.ESTABL AND
A.CODOBRA = B.CODOBRA AND A.PLANO = B.PLANO AND (B.SITLOGIS='A' OR
B.SITLOGIS='I'))</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### Documentos_tecnicos_NC16SQ.dtsx

<img src="assets/media/image16.png"
style="width:3.09375in;height:3.34527in" /><img src="assets/media/image17.png"
style="width:3.21875in;height:3.30128in" />

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;"><p><strong>SELECT A.ESTABL, A.CODOBRA,
A.PLANO, A.LINEA, A.TIPODES, A.ELEMEN, A.CANPROD, B.UNIDPRO, A.CANCONT,
B.UNIDCON, A.NUMELE</strong></p>
<p><strong>FROM NEC.NC16SQ A</strong></p>
<p><strong>INNER JOIN NEC.NC12SQ B</strong></p>
<p><strong>ON A.ESTABL = B.ESTABL</strong></p>
<p><strong>AND A.CODOBRA = B.CODOBRA</strong></p>
<p><strong>AND A.PLANO = B.PLANO</strong></p>
<p><strong>AND A.LINEA = B.LINEA</strong></p>
<p><strong>WHERE (A.CODOBRA =?) AND (A.ESTABL =?) AND
EXISTS</strong></p>
<p><strong>(SELECT ESTABL, CODOBRA, PLANO, TIPOPLA, TAREA, CENDESA,
CENCOST, ZONA, BLOQUE, MODULO, SECCION, GRUCOSTE, PRODINT,</strong></p>
<p><strong>SITOFTEC, SITINPRO, SITAPROV, SITCONFI, SITINTEG, SITLOGIS,
URREALZ, URAPROB, URCIRCU, URINPRO, URINTEG, URAPROV,</strong></p>
<p><strong>URCONFI, AVISOREV, DNI, CLASIFI, SECUE06,
FECREAC</strong></p>
<p><strong>FROM NEC.NC10SQ B</strong></p>
<p><strong>WHERE (A.ESTABL = ESTABL) AND (A.CODOBRA = CODOBRA) AND
(A.PLANO = PLANO) AND (SITLOGIS = 'A' OR SITLOGIS =
'I'))</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### Documentos_tecnicos_NC68SQ.dtsx (apunta a FESRV030)

<img src="assets/media/image18.png"
style="width:3.5in;height:3.82292in" /><img src="assets/media/image19.png"
style="width:2.94792in;height:2.97917in" />

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;"><p><strong>SELECT * FROM NEC.NC68SQ
A</strong></p>
<p><strong>WHERE A.CODOBRA=? AND A.ESTABL=? AND EXISTS</strong></p>
<p><strong>(SELECT * FROM NEC.NC10SQ B WHERE A.ESTABL= B.ESTABL AND
A.CODOBRA = B.CODOBRA AND A.PLANO = B.PLANO AND (B.SITLOGIS='A' OR
B.SITLOGIS='I'))</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## Documentos_tecnicos_Prod

### Documentos_tecnicos_Prod_NC30SQ.dtsx

<img src="assets/media/image20.png"
style="width:3.32292in;height:4.68317in" /><img src="assets/media/image21.png"
style="width:3.06165in;height:3.58333in" />

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;"><p><strong>SELECT</strong></p>
<p><strong>N30.ESTABL, N30.CODOBRA, N30.PLANO, N30.TIPOPLA,
N30.TAREA,</strong></p>
<p><strong>N30.CENDESA, N30.CENCOST, N30.ZONA, N30.BLOQUE, N30.MODULO,
N30.SECCION,</strong></p>
<p><strong>N30.GRUCOSTE, N30.PRODINT, N31.SITOFTEC, N30.SITINPRO,
N30.SITCONFI,</strong></p>
<p><strong>N30.SITAPROV, N30.SITINTEG, N30.SITLOGIS, N30.SITAMAT,
N30.URREALZ,</strong></p>
<p><strong>N30.URAPROB, N30.URCIRCU, N30.URINPRO, N30.URINTEG,
N30.URAPROV,</strong></p>
<p><strong>N30.URCONFI, N30.AVISOREV, N30.DNI, N30.CLASIFI, N30.SECUE36,
N30.FECREAC,</strong></p>
<p><strong>CAST(BZNC.NCUDF06('NC36FV ','NC30SQ'
,N30.SECUE36,'DESPLAC','INGLES') AS CHAR(30)) AS DESPLAC,</strong></p>
<p><strong>CAST(BZNC.NCUDF06('NC36FV ','NC30SQ'
,N30.SECUE36,'DESPLAL','INGLES') AS CHAR(100)) AS DESPLAL</strong></p>
<p><strong>FROM NEC.NC30SQ N30</strong></p>
<p><strong>INNER JOIN NEC.NC31SQ N31</strong></p>
<p><strong>ON N30.ESTABL = N31.ESTABL</strong></p>
<p><strong>AND N30.CODOBRA = N31.CODOBRA</strong></p>
<p><strong>AND N30.PLANO = N31.PLANO</strong></p>
<p><strong>AND N31.REVISION = (SELECT MAX(N31A.REVISION)</strong></p>
<p><strong>FROM NEC.NC31SQ N31A</strong></p>
<p><strong>WHERE N31A.ESTABL = N30.ESTABL</strong></p>
<p><strong>AND N31A.CODOBRA = N30.CODOBRA</strong></p>
<p><strong>AND N31A.PLANO = N30.PLANO)</strong></p>
<p><strong>WHERE N30.CODOBRA =? AND N30.ESTABL = ? AND (N30.SITLOGIS =
'A' OR N30.SITLOGIS = 'I');</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### Documentos_tecnicos_Prod_NC31SQ.dtsx

<img src="assets/media/image22.png"
style="width:2.90625in;height:3.14971in" /><img src="assets/media/image23.png"
style="width:3.50689in;height:3.55208in" />

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;"><p><strong>SELECT</strong></p>
<p><strong>ESTABL,CODOBRA,PLANO,REVISION,DNIDIB,DNICOM,</strong></p>
<p><strong>DNIAPR,FEINPRE,FEFIPRE,FEINREA,FEAPROB,FEFIREA,</strong></p>
<p><strong>FEENARM,FEENPRO,FEPRPRE,FEPRREA,FEINSPE,</strong></p>
<p><strong>FECLASI,CENDESA,CENCOST,SECOFTEC,SECINPRO,</strong></p>
<p><strong>SITOFTEC,SITINPRO,FECINPRO,HORINPRO,SITAMAT,</strong></p>
<p><strong>DOCUREV,CODENVIO,DOCLIC,DOCCLI,REVDIB,REVLIC,</strong></p>
<p><strong>REVCLI,PADRE,SECUE36,</strong></p>
<p><strong>cast(BZNC.NCUDF06('NC36FV ','NC31SQ'
,SECUE36,'OBSAR01','INGLES') as char(100)) AS OBSAR01,</strong></p>
<p><strong>cast(BZNC.NCUDF06('NC36FV ','NC31SQ'
,SECUE36,'OBSAR02','INGLES') as char(100)) AS OBSAR02</strong></p>
<p><strong>FROM NEC.NC31SQ A</strong></p>
<p><strong>WHERE A.CODOBRA=? AND A.ESTABL=? AND EXISTS</strong></p>
<p><strong>(SELECT * FROM NEC.NC30SQ B WHERE A.ESTABL= B.ESTABL AND
A.CODOBRA = B.CODOBRA AND A.PLANO = B.PLANO AND (B.SITLOGIS='A' OR
B.SITLOGIS='I'))</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### Documentos_tecnicos_Prod_NC32SQ.dtsx

<img src="assets/media/image24.png"
style="width:3.0766in;height:4.11458in" /><img src="assets/media/image25.png"
style="width:3.40625in;height:4.01632in" />

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;"><p><strong>SELECT
ACABADO,BLOQUE,CANCONT,CANDEMN,CANPROD,</strong></p>
<p><strong>CODOBRA, DESGACO,DESGBLO,DESGLOC,DESGMAR,</strong></p>
<p><strong>DESGMOD,DETALLE,DIMENS,DNI,ESTABL,GRUCOSTE,INSPEC,</strong></p>
<p><strong>LINEA,LINEAO,LOCAL,MARPLAN,MODDEMN,MODULO,NORMAC,</strong></p>
<p><strong>NORMAD,NOTAS,NUMELE,OBSERV,PARTIC,PESO,PLANO,</strong></p>
<p><strong>PLANOO,PRESION,PROCESS,RESIST,REVISION,SECUE36,</strong></p>
<p><strong>SITAMAT,SNREF,SOLACO,TANOMI,TIPOACO,UNIDCON,UNIDPRO,</strong></p>
<p><strong>cast(BZNC.NCUDF06('NC36FV','NC32SQ',SECUE36,'DESLINE','INGLES')
as char(100)) AS DESCR</strong></p>
<p><strong>FROM NEC.NC32SQ A</strong></p>
<p><strong>WHERE A.CODOBRA=? AND A.ESTABL=? AND EXISTS</strong></p>
<p><strong>(SELECT * FROM NEC.NC30SQ B WHERE A.ESTABL= B.ESTABL AND
A.CODOBRA = B.CODOBRA AND A.PLANO = B.PLANO AND (B.SITLOGIS='A' OR
B.SITLOGIS='I'))</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### Documentos_tecnicos_Prod_NC33SQ.dtsx

<img src="assets/media/image26.png"
style="width:3.07064in;height:4.55208in" />

<img src="assets/media/image27.png"
style="width:4.96723in;height:3.57292in" />

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;"><p><strong>SELECT ESTABL, CODOBRA, PLANO,
TIPOREF, NUMREF,</strong></p>
<p><strong>TIPIND, INDREF, FEREFER, SECUE36, REVISION,</strong></p>
<p><strong>cast(BZNC.NCUDF06('NC36FV','NC33SQ',SECUE36,'DESREF','INGLES')
as VARCHAR(7000)) AS DESCR</strong></p>
<p><strong>FROM NEC.NC33SQ A</strong></p>
<p><strong>WHERE A.CODOBRA=? AND A.ESTABL=? AND EXISTS</strong></p>
<p><strong>(SELECT * FROM NEC.NC30SQ B WHERE A.ESTABL= B.ESTABL AND
A.CODOBRA = B.CODOBRA AND A.PLANO = B.PLANO AND (B.SITLOGIS='A' OR
B.SITLOGIS='I'))</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### Documentos_tecnicos_Prod_NC34SQ.dtsx

(<span class="mark">desde FESRV030, ¿a InterfacesAWD o a
InterfacesAWD_DES?</span>)

<img src="assets/media/image28.png"
style="width:2.72917in;height:4.27083in" /><img src="assets/media/image29.png"
style="width:3.08333in;height:3.10417in" />

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;"><p><strong>SELECT A.ESTABL, A.CODOBRA,
A.PLANO, A.TIPOREF, A.NUMREF, A.LINEIN, A.LINEFI</strong></p>
<p><strong>FROM NEC.NC34SQ A</strong></p>
<p><strong>WHERE A.CODOBRA=? AND A.ESTABL=? AND EXISTS</strong></p>
<p><strong>(SELECT * FROM NEC.NC10SQ B WHERE A.ESTABL= B.ESTABL AND
A.CODOBRA = B.CODOBRA AND A.PLANO = B.PLANO AND (B.SITLOGIS='A' OR
B.SITLOGIS='I'))</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### Documentos_tecnicos_Prod_NC35SQ.dtsx

<img src="assets/media/image30.png"
style="width:1.78309in;height:3.88542in" /><img src="assets/media/image31.png"
style="width:3.09375in;height:2.98958in" />

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;"><p><strong>SELECT ESTABL, CODOBRA, PLANO,
LINEA, CANPROD,</strong></p>
<p><strong>UNIDPRO, CANRESE, PESO, NORMAD, NORMAC, DIMENS,</strong></p>
<p><strong>TANOMI, ACABADO, PARTIC, OBSERV, MAREQUI,
MARFUNC,</strong></p>
<p><strong>DNI, PROCESS, MARBORR, REVISION, SECUE36,</strong></p>
<p><strong>cast(BZNC.NCUDF06('NC36FV','NC35SQ',SECUE36,'DESLINE','INGLES')
AS CHAR(100)) AS DESCR</strong></p>
<p><strong>FROM NEC.NC35SQ A</strong></p>
<p><strong>WHERE A.CODOBRA=? AND A.ESTABL=? AND EXISTS</strong></p>
<p><strong>(SELECT * FROM NEC.NC30SQ B WHERE A.ESTABL= B.ESTABL AND
A.CODOBRA = B.CODOBRA AND A.PLANO = B.PLANO AND (B.SITLOGIS='A' OR
B.SITLOGIS='I'))</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### Documentos_tecnicos_Prod_NC36SQ.dtsx

<img src="assets/media/image32.png"
style="width:3.47917in;height:4.02996in" /><img src="assets/media/image33.png"
style="width:3.02083in;height:3.42649in" />

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;"><p><strong>SELECT A.ESTABL, A.CODOBRA,
A.PLANO, A.LINEA, A.TIPODES,</strong></p>
<p><strong>A.ELEMEN, A.CANPROD, B.UNIDPRO, A.CANCONT, B.UNIDCON,
A.NUMELE</strong></p>
<p><strong>FROM NEC.NC36SQ A</strong></p>
<p><strong>INNER JOIN NEC.NC32SQ B</strong></p>
<p><strong>ON A.ESTABL = B.ESTABL</strong></p>
<p><strong>AND A.CODOBRA = B.CODOBRA</strong></p>
<p><strong>AND A.PLANO = B.PLANO</strong></p>
<p><strong>AND A.LINEA = B.LINEA</strong></p>
<p><strong>WHERE A.CODOBRA=? AND A.ESTABL=? AND EXISTS</strong></p>
<p><strong>(SELECT * FROM NEC.NC30SQ B WHERE A.ESTABL= B.ESTABL AND
A.CODOBRA = B.CODOBRA</strong></p>
<p><strong>AND A.PLANO = B.PLANO AND (B.SITLOGIS='A' OR
B.SITLOGIS='I'))</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### Documentos_tecnicos_Prod_NC37SQ.dtsx

<img src="assets/media/image34.png"
style="width:3.22917in;height:4.32393in" /><img src="assets/media/image35.png"
style="width:3.06968in;height:3.57232in" />

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;"><p><strong>SELECT ESTABL, CODOBRA,
DOCUREV, DOCUREF,</strong></p>
<p><strong>FECDOCU, FEFINAL, NOTAS, DNIRDOC, TIPDOCU,
SECUE36,cast(</strong></p>
<p><strong>BZNC.NCUDF06('NC36FV','NC32SQ',SECUE36,'DESDOC','INGLES') as
varchar(4000)) AS DESCR</strong></p>
<p><strong>FROM NEC.NC37SQ A</strong></p>
<p><strong>WHERE A.CODOBRA=? AND A.ESTABL=? AND EXISTS</strong></p>
<p><strong>(SELECT * FROM NEC.NC38SQ B WHERE A.ESTABL= B.ESTABL AND
A.CODOBRA = B.CODOBRA AND A.DOCUREV = B.DOCUREV)</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### Documentos_tecnicos_Prod_NC38SQ.dtsx

<img src="assets/media/image36.png"
style="width:2.86458in;height:3.48339in" />

<img src="assets/media/image37.png"
style="width:6.53125in;height:4.26042in" />

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;"><p><strong>SELECT ESTABL, CODOBRA, PLANO,
REVISION,</strong></p>
<p><strong>DOCUREV, FEREVIS, SITREVIS, CTRPREV, CTRAEJEC,</strong></p>
<p><strong>CTRAVISO, DNIREV, DNIAPR, TIPDOCU, SECUE36,</strong></p>
<p><strong>REVPLA,</strong></p>
<p><strong>cast(BZNC.NCUDF06('NC36FV','NC38SQ',SECUE36,'DESREV','INGLES')
AS VARCHAR(4000)) AS DESCR</strong></p>
<p><strong>FROM NEC.NC38SQ A</strong></p>
<p><strong>WHERE A.CODOBRA=? AND A.ESTABL=? AND EXISTS</strong></p>
<p><strong>(SELECT * FROM NEC.NC30SQ B WHERE A.ESTABL= B.ESTABL AND
A.CODOBRA = B.CODOBRA AND A.PLANO = B.PLANO AND (B.SITLOGIS='A' OR
B.SITLOGIS='I'))</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### Documentos_tecnicos_Prod_NC74SQ.dtsx

<img src="assets/media/image38.png"
style="width:3.95833in;height:2.13453in" /><img src="assets/media/image39.png"
style="width:3.9142in;height:2.98958in" />

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;"><p><strong>SELECT</strong></p>
<p><strong>NC.ESTABL, NC.CODOBRA, NC.PLANO, NC.LINEA,NC.
REVISION,</strong></p>
<p><strong>NC.HOJAINI, NC.HOJAFIN, NC.NUMHOJAS, NC.SECUE06,</strong></p>
<p><strong>cast(TT.descri as char(100)) AS DESCRIPCION</strong></p>
<p><strong>FROM nec.nc74sq as NC</strong></p>
<p><strong>LEFT JOIN NEC.ttextos AS TT</strong></p>
<p><strong>ON NC.secue06 = TT.secue</strong></p>
<p><strong>AND TT.tablfich = 'NC74SQ' AND
TT.IDIOMA='INGLES'</strong></p>
<p><strong>WHERE CODOBRA =? AND ESTABL= ? and exists (SELECT * FROM
NEC.NC10SQ B WHERE NC.ESTABL= B.ESTABL AND NC.CODOBRA = B.CODOBRA AND
NC.PLANO = B.PLANO AND (B.SITLOGIS='A' OR
B.SITLOGIS='I'))</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### Documentos_tecnicos_Prod_NC75SQ.dtsx

<img src="assets/media/image40.png"
style="width:3.11458in;height:2.27604in" /><img src="assets/media/image41.png"
style="width:3.3125in;height:2.67732in" />

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;"><p><strong>SELECT</strong></p>
<p><strong>NC.ESTABL, NC.CODOBRA, NC.PLANO, NC.LINEA,NC.
REVISION,</strong></p>
<p><strong>NC.HOJAINI, NC.HOJAFIN, NC.NUMHOJAS, NC.SECUE06,</strong></p>
<p><strong>cast(TT.descri as char(100)) AS DESCRIPCION</strong></p>
<p><strong>FROM nec.nc75sq as NC</strong></p>
<p><strong>LEFT JOIN NEC.ttextos AS TT</strong></p>
<p><strong>ON NC.secue06 = TT.secue AND TT.IDIOMA='INGLES'</strong></p>
<p><strong>AND TT.tablfich = 'NC75SQ'</strong></p>
<p><strong>WHERE CODOBRA=? AND ESTABL=? and exists (SELECT * FROM
NEC.NC30SQ B WHERE NC.ESTABL= B.ESTABL</strong></p>
<p><strong>AND NC.CODOBRA = B.CODOBRA AND NC.PLANO = B.PLANO AND
(B.SITLOGIS='A' OR B.SITLOGIS='I'))</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## Paquetes E

### EEA5.dtsx

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Dias Ejecutados (Script)</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>Ejecuta estos paquetes</p>
<p>T_DB_C_E_CabAdd</p>
<p>T_DB_C_E_CabDel</p>
<p>T_DB_C_E_Cables</p>
<p>T_DB_C_E_Connections</p>
<p>T_DB_C_E_Notes</p>
<p>T_DB_C_E_Equipment</p>
<p>T_DB_C_SC_CabAdd</p>
<p>T_DB_C_SC_CabDel</p>
<p>T_DB_C_SC_Cables</p>
<p>T_DB_C_SC_Connections</p>
<p>T_DB_C_SC_Equipment</p>
<p>T_DB_C_SC_Notes</p>
<p>T_DB_R_E_CabAdd</p>
<p>T_DB_R_E_CabDel</p>
<p>T_DB_R_E_Cables</p>
<p>T_DB_R_E_Equipment</p>
<p>T_DB_R_E_Route</p>
<p>T_DB_R_E_ROUTEBLOCK</p>
<p>T_DB_R_SC_CabAdd</p>
<p>T_DB_R_SC_CabDel</p>
<p>T_DB_R_SC_Cables</p>
<p>T_DB_R_SC_Equipment</p>
<p>T_DB_R_SC_Route</p>
<p>T_DB_R_SC_ROUTEBLOCK</p>
<p>T_DBCatal</p>
<p>T_DBDesign</p>
<p>T_DBLme</p>
<p>T_DBPcontrol</p>
<p>T_DBLocal</p></td>
</tr>
<tr>
<td style="text-align: left;">Fecha maxiima de UpdateNotice con
User::Select_MasUnDia</td>
</tr>
</tbody>
</table>

### EEA5_DB2.dtsx

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;"><p>Ejecuta los paquetes</p>
<p>EEA5_NC30SQ.dtsx</p>
<p>EEA5_NC68SQ.dtsx</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### Eliminar_deleted.dtsx

|     |
|-----|

### EXTRACT_ARBOL_MARCAS.dtsx

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;"><p><strong>select ma.marcah, ma.marcap,
ma.repere, dg.codenat as mpmi</strong></p>
<p><strong>from coral.marca ma</strong></p>
<p><strong>left outer join coral.cora200a as dg</strong></p>
<p><strong>on ma.buque = dg.buque</strong></p>
<p><strong>and ma.marcah = dg.marca200</strong></p>
<p><strong>where ma.buque = ?</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### EXTRACT_CI_MF.dtsx

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;"><p><strong>select c201.buque, c221.pedirp
as CI, c201.marca200, mf.repere, C201.TIPAGR, c201.pedido,
c201.nseq</strong></p>
<p><strong>from coral.cora201 c201</strong></p>
<p><strong>inner join coral.cora221 c221</strong></p>
<p><strong>on c221.buque = c201.buque</strong></p>
<p><strong>and c221.pedido = c201.pedido</strong></p>
<p><strong>and c221.nseq = c201.nseq</strong></p>
<p><strong>inner join coral.marca mf on</strong></p>
<p><strong>c201.buque = mf.buque and</strong></p>
<p><strong>c201.marca200 = mf.marcah</strong></p>
<p><strong>where c201.buque = ?</strong></p>
<p><strong>and c221.pedirp &lt;&gt; '' and
c201.tipagr='A';</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### FinUpdatenotice.dtsx

| UPDATE UpdateNotice set Finish_Date = getdate() where Id = (select max(id) from UpdateNotice ) |
|----|

## Gestion_Documental

### Gestion_Documental_Documentos.dtsx

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">TRUNCATE TABLE Documentos</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><strong>--GD_Documentos_Extract
1</strong></p>
<p><strong>SELECT DISTINCT</strong></p>
<p><strong>Documentos.cdgDocumento,</strong></p>
<p><strong>Documentos.cdgTipoDoc,</strong></p>
<p><strong>Documentos.DescripcionDoc,</strong></p>
<p><strong>Documentos.Establecimiento,</strong></p>
<p><strong>Documentos.Division,</strong></p>
<p><strong>Documentos.cdgOrigen,</strong></p>
<p><strong>Documentos.ReferenciaOrigen,</strong></p>
<p><strong>Documentos.Obsoleto,</strong></p>
<p><strong>Documentos.fchObsoleto,</strong></p>
<p><strong>Documentos.horaObsoleto,</strong></p>
<p><strong>Documentos.AutorObsoleto,</strong></p>
<p><strong>Documentos.NotasObsoleto,</strong></p>
<p><strong>Documentos.cdgTipoEntidad</strong></p>
<p><strong>FROM Documentos</strong></p>
<p><strong>Where Documentos.cdgDocumento in</strong></p>
<p><strong>(select cdgDocumento from
tcCodigos_Documentos)</strong></p></td>
</tr>
<tr>
<td style="text-align: left;"><p>--GD_Documentos_Extract</p>
<p><strong>SELECT DISTINCT Documentos.cdgDocumento,
Documentos.cdgTipoDoc, Documentos.DescripcionDoc,
Documentos.Establecimiento, Documentos.Division, Documentos.cdgOrigen,
Documentos.ReferenciaOrigen, Documentos.Obsoleto,
Documentos.fchObsoleto, Documentos.horaObsoleto,
Documentos.AutorObsoleto, Documentos.NotasObsoleto,
Documentos.cdgTipoEntidad FROM Documentos INNER JOIN ((Select DISTINCT
tcDocsOT_Documentos.cdgDocumento as cdgDocumento,
tcDocsOT_Documentos.Establecimiento as Establecimiento,
tcDocsOT_Documentos.Obra as Obra FROM tcDocsOT_Documentos) UNION (Select
DISTINCT tcOOTT_Documentos.cdgDocumento as cdgDocumento,
tcOOTT_Documentos.Establecimiento as Establecimiento,
tcOOTT_Documentos.Obra as Obra FROM tcOOTT_Documentos where 'ALHD' =
'AWD') UNION (Select DISTINCT tcAvisosRevision_Documentos.cdgDocumento
COLLATE Modern_Spanish_CI_AS as cdgDocumento,
tcAvisosRevision_Documentos.Establecimiento COLLATE Modern_Spanish_CI_AS
as Establecimiento, tcAvisosRevision_Documentos.Obra COLLATE
Modern_Spanish_CI_AS as Obra FROM tcAvisosRevision_Documentos) UNION
(Select DISTINCT tcHojasCatalogo_Documentos.cdgdocumento COLLATE
Modern_Spanish_CI_AS as cdgdocumento,
Vista_Necora@INCopic_HojasCatalogoAplicabilidadObras.establecimiento
COLLATE Modern_Spanish_CI_AS as Establecimiento,
Vista_Necora@INCopic_HojasCatalogoAplicabilidadObras.obra COLLATE
Modern_Spanish_CI_AS as Obra FROM tcHojasCatalogo_Documentos left join
Vista_Necora@INCopic_HojasCatalogoAplicabilidadObras on
Vista_Necora@INCopic_HojasCatalogoAplicabilidadObras.codigohoja =
tcHojasCatalogo_Documentos.cdgentidad) ) as T ON T.cdgDocumento =
Documentos.cdgDocumento WHERE T.Establecimiento ='A' And T.Obra
='AWD1'</strong></p></td>
</tr>
<tr>
<td style="text-align: left;">VARIABLE LIMPIEZA (script)</td>
</tr>
<tr>
<td style="text-align: left;"><p>--Limpieza GD</p>
<p>User::V_SQL_LIMPIEZA con User::V_OBRA y User::V_ESTABL</p></td>
</tr>
<tr>
<td style="text-align: left;">GD_Documentos_Update
(GD_Documentos_Delete, deshabilitado)</td>
</tr>
</tbody>
</table>

### Gestion_Documental_Ficheros.dtsx

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;"><p>--En GD, Extracto Previo 1</p>
<p><strong>SELECT DISTINCT</strong></p>
<p><strong>dbo.Ficheros.cdgFichero,</strong></p>
<p><strong>dbo.Ficheros.cdgTipoFichero,</strong></p>
<p><strong>dbo.Ficheros.DescripcionFichero,</strong></p>
<p><strong>dbo.Ficheros.AutorRegistro,</strong></p>
<p><strong>dbo.Ficheros.NombreAutorRegistro,</strong></p>
<p><strong>dbo.Ficheros.fchRegistro,</strong></p>
<p><strong>dbo.Ficheros.cdgOrigenFichero,</strong></p>
<p><strong>dbo.Ficheros.AutorFicheroOrig,</strong></p>
<p><strong>dbo.Ficheros.UbicacionFicheroOrig,</strong></p>
<p><strong>dbo.Ficheros.NombreFicheroOrig,</strong></p>
<p><strong>dbo.Ficheros.Extensionfichero,</strong></p>
<p><strong>dbo.Ficheros.fchFicheroOrig,</strong></p>
<p><strong>'R' + substring(</strong></p>
<p><strong>dbo.Ficheros.cdgUbicacion,2,7</strong></p>
<p><strong>) as cdgUbicacion,</strong></p>
<p><strong>dbo.Ficheros.SubCarpeta,</strong></p>
<p><strong>dbo.Ficheros.cdgIdioma,</strong></p>
<p><strong>dbo.Ficheros.Centro,</strong></p>
<p><strong>dbo.Ficheros.NumEquipo,</strong></p>
<p><strong>dbo.Ficheros.NivelConfidencial,</strong></p>
<p><strong>dbo.Ficheros.Protegido,</strong></p>
<p><strong>dbo.Ficheros.TamañoKb,</strong></p>
<p><strong>dbo.Ficheros.TamañoMB,</strong></p>
<p><strong>dbo.Ficheros.Procesado,</strong></p>
<p><strong>dbo.Ficheros.fch</strong></p>
<p><strong>FROM Ficheros</strong></p>
<p><strong>LEFT JOIN trRevisionDocFichero</strong></p>
<p><strong>on Ficheros.cdgFichero =
trRevisionDocFichero.cdgFichero</strong></p>
<p><strong>where trRevisionDocFichero.cdgDocumento in</strong></p>
<p><strong>(select cdgDocumento from
tcCodigos_documentos)</strong></p></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>--En GD, Extracto Previo 2</p>
<p><strong>SELECT DISTINCT</strong></p>
<p><strong>dbo.Ficheros.cdgFichero,</strong></p>
<p><strong>dbo.Ficheros.cdgTipoFichero,</strong></p>
<p><strong>dbo.Ficheros.DescripcionFichero,</strong></p>
<p><strong>dbo.Ficheros.AutorRegistro,</strong></p>
<p><strong>dbo.Ficheros.NombreAutorRegistro,</strong></p>
<p><strong>dbo.Ficheros.fchRegistro,</strong></p>
<p><strong>dbo.Ficheros.cdgOrigenFichero,</strong></p>
<p><strong>dbo.Ficheros.AutorFicheroOrig,</strong></p>
<p><strong>dbo.Ficheros.UbicacionFicheroOrig,</strong></p>
<p><strong>dbo.Ficheros.NombreFicheroOrig,</strong></p>
<p><strong>dbo.Ficheros.Extensionfichero,</strong></p>
<p><strong>dbo.Ficheros.fchFicheroOrig,</strong></p>
<p><strong>'R' + substring(</strong></p>
<p><strong>dbo.Ficheros.cdgUbicacion,2,7</strong></p>
<p><strong>) as cdgUbicacion,</strong></p>
<p><strong>dbo.Ficheros.SubCarpeta,</strong></p>
<p><strong>dbo.Ficheros.cdgIdioma,</strong></p>
<p><strong>dbo.Ficheros.Centro,</strong></p>
<p><strong>dbo.Ficheros.NumEquipo,</strong></p>
<p><strong>dbo.Ficheros.NivelConfidencial,</strong></p>
<p><strong>dbo.Ficheros.Protegido,</strong></p>
<p><strong>dbo.Ficheros.TamañoKb,</strong></p>
<p><strong>dbo.Ficheros.TamañoMB,</strong></p>
<p><strong>dbo.Ficheros.Procesado,</strong></p>
<p><strong>dbo.Ficheros.fch</strong></p>
<p><strong>FROM Ficheros</strong></p>
<p><strong>LEFT JOIN trRevisionSecFichero</strong></p>
<p><strong>on Ficheros.cdgFichero =
trRevisionSecFichero.cdgFichero</strong></p>
<p><strong>LEFT JOIN SeccionesDocumento</strong></p>
<p><strong>on SeccionesDocumento.cdgSeccion =
trRevisionSecFichero.cdgSeccion</strong></p>
<p><strong>WHERE SeccionesDocumento.cdgDocumento in</strong></p>
<p>(select cdgDocumento from tcCodigos_documentos)</p></td>
</tr>
<tr>
<td
style="text-align: left;"><p>--GD_Ficheros_Extract_trRevisionDocFichero</p>
<p>--User::V_EXTRACT_FICH_TR</p>
<p><strong>SELECT DISTINCT dbo.Ficheros.cdgFichero,
dbo.Ficheros.cdgTipoFichero, dbo.Ficheros.DescripcionFichero,
dbo.Ficheros.AutorRegistro, dbo.Ficheros.NombreAutorRegistro,
dbo.Ficheros.fchRegistro, dbo.Ficheros.cdgOrigenFichero,
dbo.Ficheros.AutorFicheroOrig, dbo.Ficheros.UbicacionFicheroOrig,
dbo.Ficheros.NombreFicheroOrig, dbo.Ficheros.Extensionfichero,
dbo.Ficheros.fchFicheroOrig, 'R' +
substring(dbo.Ficheros.cdgUbicacion,2,7) as cdgUbicacion,
dbo.Ficheros.SubCarpeta, dbo.Ficheros.cdgIdioma, dbo.Ficheros.Centro,
dbo.Ficheros.NumEquipo, dbo.Ficheros.NivelConfidencial,
dbo.Ficheros.Protegido, dbo.Ficheros.TamañoKb, dbo.Ficheros.TamañoMB,
dbo.Ficheros.Procesado, dbo.Ficheros.fch FROM Ficheros LEFT JOIN
trRevisionDocFichero on Ficheros.cdgFichero =
trRevisionDocFichero.cdgFichero INNER JOIN ((Select DISTINCT
tcDocsOT_Documentos.cdgDocumento as cdgDocumento,
tcDocsOT_Documentos.RevisionDoc as RevisionDoc,
tcDocsOT_Documentos.Establecimiento as Establecimiento,
tcDocsOT_Documentos.Obra as Obra FROM tcDocsOT_Documentos) UNION (Select
DISTINCT tcOOTT_Documentos.cdgDocumento as cdgDocumento,
tcOOTT_Documentos.RevisionDoc as RevisionDoc,
tcOOTT_Documentos.Establecimiento as Establecimiento,
tcOOTT_Documentos.Obra as Obra FROM tcOOTT_Documentos WHERE 'ALHD' =
'ALHD' ) UNION (Select DISTINCT tcAvisosRevision_Documentos.cdgDocumento
COLLATE Modern_Spanish_CI_AS as cdgDocumento,
tcAvisosRevision_Documentos.RevisionDoc as RevisionDoc,
tcAvisosRevision_Documentos.Establecimiento COLLATE Modern_Spanish_CI_AS
as Establecimiento, tcAvisosRevision_Documentos.Obra COLLATE
Modern_Spanish_CI_AS as Obra FROM tcAvisosRevision_Documentos) UNION
(Select DISTINCT tcHojasCatalogo_Documentos.cdgdocumento COLLATE
Modern_Spanish_CI_AS as cdgdocumento,
tcHojasCatalogo_Documentos.RevisionDoc as
RevisionDoc,Vista_Necora@INCopic_HojasCatalogoAplicabilidadObras.establecimiento
COLLATE Modern_Spanish_CI_AS as Establecimiento,
Vista_Necora@INCopic_HojasCatalogoAplicabilidadObras.obra COLLATE
Modern_Spanish_CI_AS as Obra FROM tcHojasCatalogo_Documentos left join
Vista_Necora@INCopic_HojasCatalogoAplicabilidadObras on
Vista_Necora@INCopic_HojasCatalogoAplicabilidadObras.codigohoja =
tcHojasCatalogo_Documentos.cdgentidad) ) as T ON T.cdgDocumento =
trRevisionDocFichero.cdgDocumento and T.RevisionDoc &gt;=
trRevisionDocFichero.RevisionDoc where T.Establecimiento = '.' And
T.Obra = '....'</strong></p></td>
</tr>
<tr>
<td style="text-align: left;"><p>-­-GD_Ficheros_Extract_Secciones</p>
<p>--User::V_EXTRACT_FICH_SEC</p>
<p><strong>SELECT DISTINCT dbo.Ficheros.cdgFichero,
dbo.Ficheros.cdgTipoFichero, dbo.Ficheros.DescripcionFichero,
dbo.Ficheros.AutorRegistro, dbo.Ficheros.NombreAutorRegistro,
dbo.Ficheros.fchRegistro, dbo.Ficheros.cdgOrigenFichero,
dbo.Ficheros.AutorFicheroOrig, dbo.Ficheros.UbicacionFicheroOrig,
dbo.Ficheros.NombreFicheroOrig, dbo.Ficheros.Extensionfichero,
dbo.Ficheros.fchFicheroOrig, 'R' +
substring(dbo.Ficheros.cdgUbicacion,2,7) as cdgUbicacion,
dbo.Ficheros.SubCarpeta, dbo.Ficheros.cdgIdioma, dbo.Ficheros.Centro,
dbo.Ficheros.NumEquipo, dbo.Ficheros.NivelConfidencial,
dbo.Ficheros.Protegido, dbo.Ficheros.TamañoKb, dbo.Ficheros.TamañoMB,
dbo.Ficheros.Procesado, dbo.Ficheros.fch FROM Ficheros LEFT JOIN
trRevisionSecFichero on Ficheros.cdgFichero =
trRevisionSecFichero.cdgFichero LEFT JOIN SeccionesDocumento on
SeccionesDocumento.cdgSeccion = trRevisionSecFichero.cdgSeccion INNER
JOIN ((Select DISTINCT tcDocsOT_Documentos.cdgDocumento as cdgDocumento,
tcDocsOT_Documentos.Establecimiento as Establecimiento,
tcDocsOT_Documentos.Obra as Obra FROM tcDocsOT_Documentos) UNION (Select
DISTINCT tcOOTT_Documentos.cdgDocumento as cdgDocumento,
tcOOTT_Documentos.Establecimiento as Establecimiento,
tcOOTT_Documentos.Obra as Obra FROM tcOOTT_Documentos where 'ALHD' =
'ALHD') union (Select DISTINCT tcAvisosRevision_Documentos.cdgDocumento
as cdgDocumento, tcAvisosRevision_Documentos.Establecimiento as
Establecimiento, tcAvisosRevision_Documentos.Obra as Obra FROM
tcAvisosRevision_Documentos) UNION (Select DISTINCT
tcHojasCatalogo_Documentos.cdgdocumento COLLATE Modern_Spanish_CI_AS as
cdgdocumento,
Vista_Necora@INCopic_HojasCatalogoAplicabilidadObras.establecimiento
COLLATE Modern_Spanish_CI_AS as Establecimiento,
Vista_Necora@INCopic_HojasCatalogoAplicabilidadObras.obra COLLATE
Modern_Spanish_CI_AS as Obra FROM tcHojasCatalogo_Documentos left join
Vista_Necora@INCopic_HojasCatalogoAplicabilidadObras on
Vista_Necora@INCopic_HojasCatalogoAplicabilidadObras.codigohoja =
tcHojasCatalogo_Documentos.cdgentidad) ) as T ON T.cdgDocumento =
SeccionesDocumento.cdgDocumento where T.Establecimiento = '.' And T.Obra
= '....'</strong></p></td>
</tr>
<tr>
<td style="text-align: left;"><p>--Limpieza huérfanos</p>
<p><strong>delete from ficheros where ficheros.cdgfichero not
in</strong></p>
<p><strong>(select P.cdgfichero from</strong></p>
<p><strong>((select tr.cdgfichero</strong></p>
<p><strong>from trrevisiondocfichero tr</strong></p>
<p><strong>inner join RevisionesDocumento Rd</strong></p>
<p><strong>on tr.cdgDocumento = rd.cdgDocumento and tr.revisionDoc =
rd.revisionDoc)</strong></p>
<p><strong>UNION (select SEC.cdgfichero</strong></p>
<p><strong>from trrevisionsecfichero SEC inner join (select
RVSEC.*</strong></p>
<p><strong>from RevisionesSeccion RVSEC</strong></p>
<p><strong>inner join Trrevisiondocrevisionsec DocSec</strong></p>
<p><strong>on RVSEC.cdgseccion = DocSec.cdgseccion</strong></p>
<p><strong>) as c</strong></p>
<p><strong>on SEC.cdgseccion = c.cdgseccion</strong></p>
<p><strong>and SEC.revisionSec = c.revisionSec)) P</strong></p>
<p><strong>where P.cdgfichero = cdgfichero)</strong></p></td>
</tr>
<tr>
<td style="text-align: left;"><p>--Limpieza de campos</p>
<p>Ejecuta paquete _AtributosConfig.dtsx</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>--Paso Updated</p>
<p>UPDATE FICHEROS</p>
<p>SET cdgTipoFichero = DWH.cdgTipoFichero</p>
<p>,DescripcionFichero = DWH.DescripcionFichero</p>
<p>,AutorRegistro = DWH.AutorRegistro</p>
<p>,NombreAutorRegistro = DWH.NombreAutorRegistro</p>
<p>,fchRegistro = DWH.fchRegistro</p>
<p>,cdgOrigenFichero = DWH.cdgOrigenFichero</p>
<p>,AutorFicheroOrig = DWH.AutorFicheroOrig</p>
<p>,UbicacionFicheroOrig = DWH.UbicacionFicheroOrig</p>
<p>,NombreFicheroOrig = DWH.NombreFicheroOrig</p>
<p>,Extensionfichero = DWH.Extensionfichero</p>
<p>,fchFicheroOrig = DWH.fchFicheroOrig</p>
<p>,cdgUbicacion = DWH.cdgUbicacion</p>
<p>,SubCarpeta = DWH.SubCarpeta</p>
<p>,cdgIdioma = DWH.cdgIdioma</p>
<p>,Centro = DWH.Centro</p>
<p>,NumEquipo = DWH.NumEquipo</p>
<p>,NivelConfidencial = DWH.NivelConfidencial</p>
<p>,Protegido = DWH.Protegido</p>
<p>,TamañoKb = DWH.TamañoKb</p>
<p>,TamañoMB = DWH.TamañoMB</p>
<p>,Procesado = DWH.Procesado</p>
<p>,fch = DWH.fch</p>
<p>,_TSTAMP = getdate()</p>
<p>,_CHECKSUM = CHECKSUM</p>
<p>(DWH.cdgFichero ,DWH.cdgTipoFichero ,DWH.DescripcionFichero</p>
<p>,DWH.AutorRegistro ,DWH.NombreAutorRegistro ,DWH.fchRegistro</p>
<p>,DWH.cdgOrigenFichero ,DWH.AutorFicheroOrig
,DWH.UbicacionFicheroOrig</p>
<p>,DWH.NombreFicheroOrig ,DWH.Extensionfichero ,DWH.fchFicheroOrig</p>
<p>,DWH.cdgUbicacion ,DWH.SubCarpeta ,DWH.cdgIdioma</p>
<p>,DWH.Centro ,DWH.NumEquipo ,DWH.NivelConfidencial</p>
<p>,DWH.Protegido ,DWH.TamañoKb ,DWH.TamañoMB</p>
<p>,DWH.Procesado ,DWH.fch)</p>
<p>,_STATUS = 'UPDATED'</p>
<p>FROM FICHEROS AWD</p>
<p>INNER JOIN INTERFACESDWH.DBO.FICHEROS DWH</p>
<p>ON DWH.CDGFICHERO = AWD.CDGFICHERO</p>
<p>WHERE AWD._CHECKSUM &lt;&gt; CHECKSUM</p>
<p>(DWH.cdgFichero ,DWH.cdgTipoFichero ,DWH.DescripcionFichero</p>
<p>,DWH.AutorRegistro ,DWH.NombreAutorRegistro ,DWH.fchRegistro</p>
<p>,DWH.cdgOrigenFichero ,DWH.AutorFicheroOrig
,DWH.UbicacionFicheroOrig</p>
<p>,DWH.NombreFicheroOrig ,DWH.Extensionfichero ,DWH.fchFicheroOrig</p>
<p>,DWH.cdgUbicacion ,DWH.SubCarpeta ,DWH.cdgIdioma</p>
<p>,DWH.Centro ,DWH.NumEquipo ,DWH.NivelConfidencial</p>
<p>,DWH.Protegido ,DWH.TamañoKb ,DWH.TamañoMB</p>
<p>,DWH.Procesado ,DWH.fch)</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>--Actualiza estado a NEW</p>
<p>UPDATE FICHEROS</p>
<p>SET _STATUS = 'NEW'</p>
<p>, _TSTAMP = GETDATE()</p>
<p>FROM FICHEROS AWD</p>
<p>INNER JOIN INTERFACESDWH.DBO.FICHEROS DWH</p>
<p>ON DWH.CDGFICHERO = AWD.CDGFICHERO</p>
<p>WHERE AWD._STATUS = 'DELETED'</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>--Inserta nuevos</p>
<p>INSERT INTO FICHEROS</p>
<p>(cdgFichero ,cdgTipoFichero ,DescripcionFichero</p>
<p>,AutorRegistro ,NombreAutorRegistro ,fchRegistro</p>
<p>,cdgOrigenFichero ,AutorFicheroOrig ,UbicacionFicheroOrig</p>
<p>,NombreFicheroOrig ,Extensionfichero ,fchFicheroOrig</p>
<p>,cdgUbicacion ,SubCarpeta ,cdgIdioma</p>
<p>,Centro ,NumEquipo ,NivelConfidencial</p>
<p>,Protegido ,TamañoKb ,TamañoMB</p>
<p>,Procesado ,fch ,_TSTAMP</p>
<p>,_CHECKSUM ,_STATUS)</p>
<p>SELECT DWH.cdgFichero ,DWH.cdgTipoFichero ,DWH.DescripcionFichero</p>
<p>,DWH.AutorRegistro ,DWH.NombreAutorRegistro ,DWH.fchRegistro</p>
<p>,DWH.cdgOrigenFichero ,DWH.AutorFicheroOrig
,DWH.UbicacionFicheroOrig</p>
<p>,DWH.NombreFicheroOrig ,DWH.Extensionfichero ,DWH.fchFicheroOrig</p>
<p>,DWH.cdgUbicacion ,DWH.SubCarpeta ,DWH.cdgIdioma</p>
<p>,DWH.Centro ,DWH.NumEquipo ,DWH.NivelConfidencial</p>
<p>,DWH.Protegido ,DWH.TamañoKb ,DWH.TamañoMB</p>
<p>,DWH.Procesado ,DWH.fch ,GETDATE() AS _TSTAMP</p>
<p>,CHECKSUM</p>
<p>(DWH.cdgFichero ,DWH.cdgTipoFichero ,DWH.DescripcionFichero</p>
<p>,DWH.AutorRegistro ,DWH.NombreAutorRegistro ,DWH.fchRegistro</p>
<p>,DWH.cdgOrigenFichero ,DWH.AutorFicheroOrig
,DWH.UbicacionFicheroOrig</p>
<p>,DWH.NombreFicheroOrig ,DWH.Extensionfichero ,DWH.fchFicheroOrig</p>
<p>,DWH.cdgUbicacion ,DWH.SubCarpeta ,DWH.cdgIdioma</p>
<p>,DWH.Centro ,DWH.NumEquipo ,DWH.NivelConfidencial</p>
<p>,DWH.Protegido ,DWH.TamañoKb ,DWH.TamañoMB</p>
<p>,DWH.Procesado ,DWH.fch) AS _CHECKSUM</p>
<p>,'NEW' AS _STATUS</p>
<p>FROM INTERFACESDWH.DBO.FICHEROS DWH</p>
<p>WHERE NOT EXISTS</p>
<p>(SELECT AWD.* FROM FICHEROS AWD WHERE AWD.CDGFICHERO =
DWH.CDGFICHERO)</p></td>
</tr>
</tbody>
</table>

### Gestion_Documental_RevisionesDocumento.dtsx

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th>TRUNCATE TABLE RevisionesDocumento</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>--GD_RevDocumento_Extract</p>
<p>--User::V_SQL_EXTRACT_REVDOC</p>
<p><strong>select distinct * from((SELECT distinct RevisionesDocumento.*
FROM RevisionesDocumento INNER JOIN ((Select DISTINCT
tcDocsOT_Documentos.cdgDocumento as cdgDocumento,
tcDocsOT_Documentos.RevisionDoc as RevisionDoc,
tcDocsOT_Documentos.Establecimiento as Establecimiento,
tcDocsOT_Documentos.Obra as Obra FROM tcDocsOT_Documentos) UNION (Select
DISTINCT tcOOTT_Documentos.cdgDocumento as cdgDocumento,
tcOOTT_Documentos.RevisionDoc as RevisionDoc,
tcOOTT_Documentos.Establecimiento as Establecimiento,
tcOOTT_Documentos.Obra as Obra FROM tcOOTT_Documentos where 'ALHD' =
'AWD') UNION (Select DISTINCT tcAvisosRevision_Documentos.cdgDocumento
COLLATE Modern_Spanish_CI_AS as cdgDocumento,
tcAvisosRevision_Documentos.RevisionDoc as RevisionDoc,
tcAvisosRevision_Documentos.Establecimiento COLLATE Modern_Spanish_CI_AS
as Establecimiento, tcAvisosRevision_Documentos.Obra COLLATE
Modern_Spanish_CI_AS as Obra FROM tcAvisosRevision_Documentos) UNION
(Select DISTINCT tcHojasCatalogo_Documentos.cdgdocumento COLLATE
Modern_Spanish_CI_AS as cdgdocumento,
tcHojasCatalogo_Documentos.RevisionDoc as RevisionDoc,
Vista_Necora@INCopic_HojasCatalogoAplicabilidadObras.establecimiento
COLLATE Modern_Spanish_CI_AS as Establecimiento,
Vista_Necora@INCopic_HojasCatalogoAplicabilidadObras.obra COLLATE
Modern_Spanish_CI_AS as Obra FROM tcHojasCatalogo_Documentos left join
Vista_Necora@INCopic_HojasCatalogoAplicabilidadObras on
Vista_Necora@INCopic_HojasCatalogoAplicabilidadObras.codigohoja =
tcHojasCatalogo_Documentos.cdgentidad) ) as T on T.cdgDocumento =
RevisionesDocumento.cdgDocumento and Revisionesdocumento.RevisionDoc
&lt;= T.RevisionDoc WHERE T.Establecimiento ='A' and T.Obra = 'AWD1')
union (SELECT RD.* from RevisionesDocumento RD inner join
tcCodigos_documentos tc on tc.cdgdocumento = RD.cdgdocumento collate
Modern_Spanish_CI_AS and RD.revisiondoc &lt;= tc.revisiondoc collate
Modern_Spanish_CI_AS) ) REV</strong></p></td>
</tr>
<tr>
<td><p>--Limpieza</p>
<p><strong>DELETE RevisionesDocumento</strong></p>
<p><strong>FROM RevisionesDocumento</strong></p>
<p><strong>LEFT JOIN tcDocsOT_Documentos</strong></p>
<p><strong>on tcDocsOT_Documentos.cdgDocumento =
RevisionesDocumento.cdgDocumento</strong></p>
<p><strong>and tcDocsOT_Documentos.RevisionDoc &gt;=
RevisionesDocumento.RevisionDoc</strong></p>
<p><strong>LEFT JOIN tcOOTT_Documentos</strong></p>
<p><strong>on tcOOTT_Documentos .cdgDocumento =
RevisionesDocumento.cdgDocumento</strong></p>
<p><strong>and tcOOTT_Documentos.RevisionDoc &gt;=
RevisionesDocumento.RevisionDoc</strong></p>
<p><strong>LEFT JOIN tcAvisosRevision_Documentos</strong></p>
<p><strong>ON tcAvisosRevision_Documentos.cdgDocumento COLLATE
Modern_Spanish_CI_AS = RevisionesDocumento.cdgDocumento</strong></p>
<p><strong>and tcAvisosRevision_Documentos.RevisionDoc COLLATE
Modern_Spanish_CI_AS &gt;= RevisionesDocumento.RevisionDoc</strong></p>
<p><strong>LEFT JOIN tcCodigos_Documentos</strong></p>
<p><strong>on tcCodigos_Documentos.cdgDocumento COLLATE
Modern_Spanish_CI_AS = RevisionesDocumento.cdgDocumento</strong></p>
<p><strong>and tcCodigos_Documentos.RevisionDoc COLLATE
Modern_Spanish_CI_AS &gt;= RevisionesDocumento.RevisionDoc</strong></p>
<p><strong>LEFT JOIN tcHojasCatalogo_Documentos</strong></p>
<p><strong>ON tcHojasCatalogo_Documentos.cdgDocumento COLLATE
Modern_Spanish_CI_AS = RevisionesDocumento.cdgDocumento</strong></p>
<p><strong>and tcHojasCatalogo_Documentos.RevisionDoc COLLATE
Modern_Spanish_CI_AS &gt;= RevisionesDocumento.RevisionDoc</strong></p>
<p><strong>WHERE tcDocsOT_Documentos.cdgDocumento IS NULL</strong></p>
<p><strong>AND tcOOTT_Documentos.cdgDocumento IS NULL</strong></p>
<p><strong>AND tcAvisosRevision_Documentos.cdgDocumento IS
NULL</strong></p>
<p><strong>AND tcCodigos_Documentos.cdgDocumento IS NULL</strong></p>
<p><strong>AND tcHojasCatalogo_Documentos.cdgDocumento IS
NULL</strong></p></td>
</tr>
<tr>
<td>GD_Documentos_Update (GD_RevDocumento_Delete deshabilitada)</td>
</tr>
</tbody>
</table>

### Gestion_Documental_RevisionesSeccion.dtsx

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th>TRUNCATE TABLE RevisionesSeccion</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>--GD_RevisionesSeccion_Extract 1</p>
<p><strong>SELECT DISTINCT RevisionesSeccion.cdgSeccion,</strong></p>
<p><strong>RevisionesSeccion.DescripcionRevisionSec,</strong></p>
<p><strong>RevisionesSeccion.RevisionOrigen,</strong></p>
<p><strong>RevisionesSeccion.RevisionSec</strong></p>
<p><strong>FROM RevisionesSeccion WITH(NOLOCK)</strong></p>
<p><strong>INNER JOIN SeccionesDocumento WITH(NOLOCK)</strong></p>
<p><strong>ON RevisionesSeccion.cdgSeccion =
SeccionesDocumento.cdgSeccion</strong></p>
<p><strong>Where SeccionesDocumento.cdgDocumento in</strong></p>
<p><strong>(select cdgDocumento from tcCodigos_Documentos WITH(NOLOCK)
)</strong></p></td>
</tr>
<tr>
<td><p>--GD_RevisionesSeccion_Extract</p>
<p>----User::V_SQL_EXTRACT_REVSECC</p>
<p><strong>SELECT DISTINCT RevisionesSeccion.cdgSeccion,
RevisionesSeccion.DescripcionRevisionSec,
RevisionesSeccion.RevisionOrigen, RevisionesSeccion.RevisionSec FROM
RevisionesSeccion WITH(NOLOCK) INNER JOIN SeccionesDocumento
WITH(NOLOCK)</strong></p>
<p><strong>ON RevisionesSeccion.cdgSeccion =
SeccionesDocumento.cdgSeccion INNER JOIN ((Select DISTINCT
tcDocsOT_Documentos.cdgDocumento as cdgDocumento,
tcDocsOT_Documentos.Establecimiento as Establecimiento,
tcDocsOT_Documentos.Obra as Obra FROM tcDocsOT_Documentos WITH(NOLOCK) )
UNION (Select DISTINCT tcOOTT_Documentos.cdgDocumento as cdgDocumento,
tcOOTT_Documentos.Establecimiento as Establecimiento,
tcOOTT_Documentos.Obra as Obra FROM tcOOTT_Documentos WITH(NOLOCK) where
'ALHD' = 'AWD') UNION (Select DISTINCT
tcAvisosRevision_Documentos.cdgDocumento COLLATE Modern_Spanish_CI_AS as
cdgDocumento, tcAvisosRevision_Documentos.Establecimiento COLLATE
Modern_Spanish_CI_AS as Establecimiento,
tcAvisosRevision_Documentos.Obra COLLATE Modern_Spanish_CI_AS as Obra
FROM tcAvisosRevision_Documentos WITH(NOLOCK) ) UNION (Select DISTINCT
tcHojasCatalogo_Documentos.cdgdocumento COLLATE Modern_Spanish_CI_AS as
cdgdocumento,
Vista_Necora@INCopic_HojasCatalogoAplicabilidadObras.establecimiento
COLLATE Modern_Spanish_CI_AS as Establecimiento,
Vista_Necora@INCopic_HojasCatalogoAplicabilidadObras.obra COLLATE
Modern_Spanish_CI_AS as Obra</strong></p>
<p><strong>FROM tcHojasCatalogo_Documentos WITH(NOLOCK) left join
Vista_Necora@INCopic_HojasCatalogoAplicabilidadObras
WITH(NOLOCK)</strong></p>
<p><strong>on
Vista_Necora@INCopic_HojasCatalogoAplicabilidadObras.codigohoja =
tcHojasCatalogo_Documentos.cdgentidad) ) as T ON
SeccionesDocumento.cdgDocumento = T.cdgDocumento WHERE T.Establecimiento
= 'A' And T.Obra = 'AWD1'</strong></p></td>
</tr>
<tr>
<td><p>--Limpieza GD</p>
<p>delete RevisionesSeccion</p>
<p>FROM RevisionesSeccion</p>
<p>left JOIN SeccionesDocumento</p>
<p>ON RevisionesSeccion.cdgSeccion = SeccionesDocumento.cdgSeccion</p>
<p>left join TrRevisionDocRevisionSec tr</p>
<p>on RevisionesSeccion.cdgseccion = tr.cdgseccion</p>
<p>WHERE SeccionesDocumento.cdgSeccion IS NULL</p>
<p>OR tr.cdgseccion IS NULL</p></td>
</tr>
<tr>
<td>GD_RevisionesSeccion_Update</td>
</tr>
</tbody>
</table>

### Gestion_Documental_SeccionesDocumento.dtsx

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th>TRUNCATE TABLE SeccionesDocumento</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>--Extract previo</p>
<p><strong>SELECT DISTINCT</strong></p>
<p><strong>dbo.SeccionesDocumento.cdgSeccion,</strong></p>
<p><strong>dbo.SeccionesDocumento.cdgTipoSec,</strong></p>
<p><strong>dbo.SeccionesDocumento.DescripcionSec,</strong></p>
<p><strong>dbo.SeccionesDocumento.cdgDocumento,</strong></p>
<p><strong>dbo.SeccionesDocumento.ReferenciaOrigenSec</strong></p>
<p><strong>FROM SeccionesDocumento</strong></p>
<p><strong>LEFT JOIN trRevisionDocFichero</strong></p>
<p><strong>on SeccionesDocumento.cdgDocumento =
trRevisionDocFichero.cdgDocumento</strong></p>
<p><strong>where trRevisionDocFichero.cdgDocumento in</strong></p>
<p><strong>(select cdgDocumento from
tcCodigos_Documentos)</strong></p></td>
</tr>
<tr>
<td><p>--GD_SeccionesDocumento_Extract</p>
<p>--User::V_EXTRACT_SECC_DOC</p>
<p><strong>SELECT DISTINCT SeccionesDocumento.* FROM SeccionesDocumento
INNER JOIN ((Select DISTINCT tcDocsOT_Documentos.cdgDocumento as
cdgDocumento, tcDocsOT_Documentos.Establecimiento as Establecimiento,
tcDocsOT_Documentos.Obra as Obra FROM tcDocsOT_Documentos) UNION (Select
DISTINCT tcOOTT_Documentos.cdgDocumento as cdgDocumento,
tcOOTT_Documentos.Establecimiento as Establecimiento,
tcOOTT_Documentos.Obra as Obra FROM tcOOTT_Documentos WHERE 'ALHD' =
'AWD') UNION (Select DISTINCT tcAvisosRevision_Documentos.cdgDocumento
COLLATE Modern_Spanish_CI_AS as cdgDocumento,
tcAvisosRevision_Documentos.Establecimiento COLLATE Modern_Spanish_CI_AS
as Establecimiento, tcAvisosRevision_Documentos.Obra COLLATE
Modern_Spanish_CI_AS as Obra FROM tcAvisosRevision_Documentos) UNION
(Select DISTINCT tcHojasCatalogo_Documentos.cdgdocumento COLLATE
Modern_Spanish_CI_AS as cdgdocumento,
Vista_Necora@INCopic_HojasCatalogoAplicabilidadObras.establecimiento
COLLATE Modern_Spanish_CI_AS as Establecimiento,
Vista_Necora@INCopic_HojasCatalogoAplicabilidadObras.obra COLLATE
Modern_Spanish_CI_AS as Obra FROM tcHojasCatalogo_Documentos left join
Vista_Necora@INCopic_HojasCatalogoAplicabilidadObras on
Vista_Necora@INCopic_HojasCatalogoAplicabilidadObras.codigohoja =
tcHojasCatalogo_Documentos.cdgentidad) ) as T ON T.cdgDocumento =
SeccionesDocumento.cdgDocumento WHERE T.Establecimiento ='A' And T.Obra
= 'AWD1'</strong></p></td>
</tr>
<tr>
<td><p>--Limpieza</p>
<p>User::V_SQL_LIMPIEZA</p></td>
</tr>
<tr>
<td>GD_SeccionesDocumento_Update</td>
</tr>
</tbody>
</table>

### Gestion_Documental_tcAvisosRevision_Documentos.dtsx

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th>TRUNCATE TABLE tcAvisosRevision_Documentos</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>--GD_AvisosRevision_Extract</p>
<p><strong>SELECT *</strong></p>
<p><strong>FROM tcAvisosRevision_Documentos</strong></p>
<p><strong>WHERE (Establecimiento = ? AND Obra = ?)</strong></p></td>
</tr>
<tr>
<td><p>--Limpieza GD</p>
<p>DELETE tcAvisosRevision_Documentos</p>
<p>FROM tcAvisosRevision_Documentos</p>
<p>WHERE Establecimiento = ? AND Obra = ?</p>
<p>AND not exists</p>
<p>(SELECT * FROM NC17SQ B WHERE
tcAvisosRevision_Documentos.ESTABLECIMIENTO= B.ESTABL AND
tcAvisosRevision_Documentos.OBRA = B.CODOBRA AND
tcAvisosRevision_Documentos.CDGENTIDAD = B.DOCUREV)</p></td>
</tr>
<tr>
<td>GD_AvisosRevision_Update y GD_AvisosRevision_Delete</td>
</tr>
</tbody>
</table>

### Gestion_Documental_tcCodigos_Documentos.dtsx

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th>TRUNCATE TABLE tcCodigos_Documentos</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>-- GD_tcCodigos_Documentos Extract</p>
<p><strong>De GD.dbo.tcCodigosDocumentos 🡪
InterfacesDWH.dbo.tcCodigosDocumentos</strong></p></td>
</tr>
<tr>
<td><p>--LimpiezaGD</p>
<p>User::V_LIMPIEZA</p></td>
</tr>
<tr>
<td>--Limpiear campos: llama al paquete _AtributosConfig.dtsx</td>
</tr>
<tr>
<td>GD_tcCodigos_Documentos Update y GD_tcCodigos_Documentos Delete</td>
</tr>
</tbody>
</table>

### Gestion_Documental_tcDocsOT_Documentos.dtsx

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th>TRUNCATE TABLE tcDocsOT_Documentos</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>--­ GD_tcDocsOT_Documentos_Extract</p>
<p><strong>SELECT Establecimiento, Obra, cdgEntidad,
RevisionEntidad,</strong></p>
<p><strong>cdgDocumento, RevisionDoc, Pertenencia, Ultima, Usuario,
fchAsoc,</strong></p>
<p><strong>horaAsoc, Centro, NumEquipo, SitEntidad,
Aplicable</strong></p>
<p><strong>FROM tcDocsOT_Documentos WITH(NOLOCK)</strong></p>
<p><strong>WHERE (Establecimiento = ? AND Obra = ?)</strong></p></td>
</tr>
<tr>
<td><p>--Limpieza GD</p>
<p><strong>DELETE tcDocsOT_Documentos</strong></p>
<p><strong>FROM tcDocsOT_Documentos tc</strong></p>
<p><strong>WHERE tc.Establecimiento = ? AND tc.Obra = ?</strong></p>
<p><strong>and not exists</strong></p>
<p><strong>(select nc.establ, nc.codobra, nc.plano, nc.revision from
nc31sq nc</strong></p>
<p><strong>where tc.obra = nc.codobra</strong></p>
<p><strong>and tc.cdgentidad = nc.plano</strong></p>
<p><strong>and tc.revisionentidad = nc.revision</strong></p>
<p><strong>)</strong></p></td>
</tr>
<tr>
<td>GD_tcDocsOT_Documentos_Update y GD_tcDocsOT_Documentos_Delete</td>
</tr>
</tbody>
</table>

### Gestion_Documental_tcOOTT_Documentos.dtsx

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th>truncate table tcOOTT_Documentos</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>--extract tcOOTT_Documentos</p>
<p><strong>SELECT Establecimiento, Obra, cdgEntidad,
RevisionEntidad,</strong></p>
<p><strong>cdgDocumento, RevisionDoc, Pertenencia, Ultima, Usuario,
fchAsoc,</strong></p>
<p><strong>horaAsoc, Centro, NumEquipo, SitEntidad,
Aplicable</strong></p>
<p><strong>FROM tcOOTT_Documentos</strong></p>
<p><strong>WHERE (Establecimiento = ? AND Obra = ?)</strong></p></td>
</tr>
<tr>
<td><p>--limpieza de proveedores que no son BAE</p>
<p><strong>delete TCOOTT_DOCUMENTOS</strong></p>
<p><strong>from tcoott_documentos A</strong></p>
<p><strong>WHERE A.ESTABLECIMIENTO = ?</strong></p>
<p><strong>AND A.OBRA = ?</strong></p>
<p><strong>AND NOT EXISTS</strong></p>
<p><strong>(select * FROM BO11SQ B</strong></p>
<p><strong>INNER JOIN BO10SQ C</strong></p>
<p><strong>ON B.ESTABL = C.ESTABL COLLATE
Modern_Spanish_CI_AS</strong></p>
<p><strong>AND B.CODOBRA = C.CODOBRA COLLATE
Modern_Spanish_CI_AS</strong></p>
<p><strong>AND B.ORDEN = C.ORDEN COLLATE
Modern_Spanish_CI_AS</strong></p>
<p><strong>WHERE C.COPROV = '118Q'</strong></p>
<p><strong>AND B.ESTABL = A.ESTABLECIMIENTO COLLATE
Modern_Spanish_CI_AS</strong></p>
<p><strong>AND B.CODOBRA = A.OBRA COLLATE
Modern_Spanish_CI_AS</strong></p>
<p><strong>AND B.ORDEN = A.CDGENTIDAD COLLATE
Modern_Spanish_CI_AS</strong></p>
<p><strong>AND B.REVISION = A.REVISIONENTIDAD COLLATE
Modern_Spanish_CI_AS )</strong></p></td>
</tr>
<tr>
<td>--Limpieza de campos que llama al paquete _AtributosConfig.dtsx</td>
</tr>
<tr>
<td>Update tcOOTT_Documentos y Delete tcOOTT_Documentos</td>
</tr>
</tbody>
</table>

### Gestion_Documental_trRevisionDocFichero.dtsx

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th>TRUNCATE TABLE trRevisionDocFichero</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>--GD_trRevisionDocFichero_Extract</p>
<p>--User::V_EXTRACT</p>
<p><strong>(SELECT DISTINCT trRevisionDocFichero.cdgDocumento,
trRevisionDocFichero.cdgFichero, trRevisionDocFichero.Pertenencia,
trRevisionDocFichero.RevisionDoc FROM trRevisionDocFichero INNER JOIN
((Select DISTINCT tcDocsOT_Documentos.cdgDocumento as cdgDocumento,
tcDocsOT_Documentos.RevisionDoc as RevisionDoc,
tcDocsOT_Documentos.Establecimiento as Establecimiento,
tcDocsOT_Documentos.Obra as Obra FROM tcDocsOT_Documentos) UNION (Select
DISTINCT tcOOTT_Documentos.cdgDocumento as cdgDocumento,
tcOOTT_Documentos.RevisionDoc as RevisionDoc,
tcOOTT_Documentos.Establecimiento as Establecimiento,
tcOOTT_Documentos.Obra as Obra FROM tcOOTT_Documentos where 'ALHD' =
'AWD') UNION (Select DISTINCT tcAvisosRevision_Documentos.cdgDocumento
COLLATE Modern_Spanish_CI_AS as cdgDocumento,
tcAvisosRevision_Documentos.RevisionDoc as RevisionDoc,
tcAvisosRevision_Documentos.Establecimiento COLLATE Modern_Spanish_CI_AS
as Establecimiento, tcAvisosRevision_Documentos.Obra COLLATE
Modern_Spanish_CI_AS as Obra FROM tcAvisosRevision_Documentos) UNION
(Select DISTINCT tcHojasCatalogo_Documentos.cdgdocumento COLLATE
Modern_Spanish_CI_AS as cdgdocumento,
tcHojasCatalogo_Documentos.RevisionDoc as RevisionDoc,
Vista_Necora@INCopic_HojasCatalogoAplicabilidadObras.establecimiento
COLLATE Modern_Spanish_CI_AS as Establecimiento,
Vista_Necora@INCopic_HojasCatalogoAplicabilidadObras.obra COLLATE
Modern_Spanish_CI_AS as Obra FROM tcHojasCatalogo_Documentos left join
Vista_Necora@INCopic_HojasCatalogoAplicabilidadObras on
Vista_Necora@INCopic_HojasCatalogoAplicabilidadObras.codigohoja =
tcHojasCatalogo_Documentos.cdgentidad)) as T ON T.cdgDocumento =
trRevisionDocFichero.cdgDocumento and trRevisionDocFichero.revisionDoc
&lt;= T.RevisionDoc WHERE T.Establecimiento = 'A' And T.Obra = 'AWD1')
UNION (SELECT DISTINCT dbo.trRevisionDocFichero.cdgDocumento,
dbo.trRevisionDocFichero.cdgFichero,
dbo.trRevisionDocFichero.Pertenencia,
dbo.trRevisionDocFichero.RevisionDoc FROM trRevisionDocFichero inner
join tcCodigos_Documentos on trRevisionDocFichero.cdgDocumento =
tcCodigos_Documentos.cdgDocumento COLLATE Modern_Spanish_CI_AS and
trRevisionDocFichero.RevisionDoc = tcCodigos_Documentos.RevisionDoc
COLLATE Modern_Spanish_CI_AS)</strong></p></td>
</tr>
<tr>
<td><p>--Limpieza</p>
<p>User::V_SQL_LIMPIEZA</p></td>
</tr>
<tr>
<td>GD_trRevisionDocFichero_Update</td>
</tr>
</tbody>
</table>

### Gestion_Documental_trRevisionDocRevisionSec.dtsx

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th>TRUNCATE TABLE trRevisionDocRevisionSec</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>--­GD_RevDocRevSec_Extract</p>
<p>--User::V_EXTRAC</p>
<p>(<strong>SELECT distinct trRevisionDocRevisionSec.* FROM
trRevisionDocRevisionSec WITH(NOLOCK) INNER JOIN ((Select DISTINCT
tcDocsOT_Documentos.cdgDocumento as cdgDocumento,
tcDocsOT_Documentos.Establecimiento as Establecimiento,
tcDocsOT_Documentos.Obra as Obra FROM tcDocsOT_Documentos WITH(NOLOCK) )
UNION (Select DISTINCT tcOOTT_Documentos.cdgDocumento as cdgDocumento,
tcOOTT_Documentos.Establecimiento as Establecimiento,
tcOOTT_Documentos.Obra as Obra</strong></p>
<p><strong>FROM tcOOTT_Documentos WITH(NOLOCK) where 'ALHD' = 'AWD')
UNION (Select DISTINCT tcAvisosRevision_Documentos.cdgDocumento COLLATE
Modern_Spanish_CI_AS as cdgDocumento,
tcAvisosRevision_Documentos.Establecimiento COLLATE Modern_Spanish_CI_AS
as Establecimiento, tcAvisosRevision_Documentos.Obra COLLATE
Modern_Spanish_CI_AS as Obra</strong></p>
<p><strong>FROM tcAvisosRevision_Documentos WITH(NOLOCK) ) UNION (Select
DISTINCT tcHojasCatalogo_Documentos.cdgdocumento COLLATE
Modern_Spanish_CI_AS as cdgdocumento,
Vista_Necora@INCopic_HojasCatalogoAplicabilidadObras.establecimiento
COLLATE Modern_Spanish_CI_AS as Establecimiento,
Vista_Necora@INCopic_HojasCatalogoAplicabilidadObras.obra COLLATE
Modern_Spanish_CI_AS as Obra FROM tcHojasCatalogo_Documentos
WITH(NOLOCK) left join
Vista_Necora@INCopic_HojasCatalogoAplicabilidadObras
WITH(NOLOCK)</strong></p>
<p><strong>on
Vista_Necora@INCopic_HojasCatalogoAplicabilidadObras.codigohoja =
tcHojasCatalogo_Documentos.cdgentidad)) as T on T.cdgDocumento =
trRevisionDocRevisionSec.cdgDocumento WHERE T.Establecimiento = 'A' and
T.Obra ='AWD1') UNION (SELECT DISTINCT
dbo.trRevisionDocRevisionSec.cdgDocumento,
dbo.trRevisionDocRevisionSec.RevisionDoc,
dbo.trRevisionDocRevisionSec.cdgSeccion,
dbo.trRevisionDocRevisionSec.RevisionSec,
dbo.trRevisionDocRevisionSec.Pertenencia</strong></p>
<p><strong>FROM trRevisionDocRevisionSec WITH(NOLOCK) left JOIN (select
distinct trRevisionDocFichero.cdgDocumento,
trRevisionDocFichero.RevisionDoc,
trRevisionDocFichero.Pertenencia</strong></p>
<p><strong>from trRevisionDocFichero WITH(NOLOCK) inner join
tcCodigos_Documentos WITH(NOLOCK) on trRevisionDocFichero.cdgDocumento =
tcCodigos_Documentos.cdgDocumento COLLATE Modern_Spanish_CI_AS and
trRevisionDocFichero.RevisionDoc = tcCodigos_Documentos.RevisionDoc
COLLATE Modern_Spanish_CI_AS ) as T on
trRevisionDocRevisionSec.cdgDocumento = T.cdgDocumento and
trRevisionDocRevisionSec.RevisionDoc = T.RevisionDoc)</strong></p></td>
</tr>
<tr>
<td><p>--DELETE REVISIONESDOCUMENTO</p>
<p><strong>delete trRevisionDocRevisionSec</strong></p>
<p><strong>FROM trRevisionDocRevisionSec A</strong></p>
<p><strong>WHERE A.cdgDocumento is not null</strong></p>
<p><strong>AND A.RevisionDoc is not null</strong></p>
<p><strong>AND Not EXISTS</strong></p>
<p><strong>(SELECT * FROM RevisionesDocumento B</strong></p>
<p><strong>WHERE A.cdgDocumento = B.cdgDocumento</strong></p>
<p><strong>AND A.RevisionDoc = B.RevisionDoc)</strong></p>
<p><strong>and A.Revisionsec &gt;</strong></p>
<p><strong>coalesce ( (select max( C.Revisionsec)</strong></p>
<p><strong>FROM trRevisionDocRevisionSec C</strong></p>
<p><strong>WHERE C.cdgDocumento is not null</strong></p>
<p><strong>AND C.RevisionDoc is not null</strong></p>
<p><strong>AND A.cdgdocumento = C.cdgDocumento</strong></p>
<p><strong>AND A.REVISIONDOC = C.REVISIONDOC</strong></p>
<p><strong>AND A.CDGSECCION = C.CDGSECCION</strong></p>
<p><strong>AND EXISTS</strong></p>
<p><strong>(SELECT * FROM RevisionesDocumento D</strong></p>
<p><strong>WHERE C.cdgDocumento = D.cdgDocumento</strong></p>
<p><strong>AND C.RevisionDoc = D.RevisionDoc)</strong></p>
<p><strong>) , ' ')</strong></p></td>
</tr>
<tr>
<td>GD_RevDocRevSec_Update</td>
</tr>
</tbody>
</table>

### Gestion_Documental_trRevisionSecFichero.dtsx

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th>TRUNCATE TABLE trRevisionSecFichero</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>--GD_trRevisionSecFichero_Extract 1</p>
<p><strong>SELECT DISTINCT trRevisionSecFichero.cdgFichero,</strong></p>
<p><strong>trRevisionSecFichero.cdgSeccion,
trRevisionSecFichero.Pertenencia,</strong></p>
<p><strong>trRevisionSecFichero.RevisionSec</strong></p>
<p><strong>FROM trRevisionSecFichero WITH(NOLOCK)</strong></p>
<p><strong>INNER JOIN SeccionesDocumento WITH(NOLOCK)</strong></p>
<p><strong>ON trRevisionSecFichero.cdgSeccion =
SeccionesDocumento.cdgSeccion</strong></p>
<p><strong>Where SeccionesDocumento.cdgDocumento in</strong></p>
<p><strong>(select cdgDocumento from tcCodigos_Documentos WITH(NOLOCK)
)</strong></p></td>
</tr>
<tr>
<td><p>--GD_trRevisionSecFichero_Extract1</p>
<p><strong>SELECT DISTINCT trRevisionSecFichero.cdgFichero,</strong></p>
<p><strong>trRevisionSecFichero.cdgSeccion,
trRevisionSecFichero.Pertenencia,</strong></p>
<p><strong>trRevisionSecFichero.RevisionSec</strong></p>
<p><strong>FROM trRevisionSecFichero WITH(NOLOCK)</strong></p>
<p><strong>INNER JOIN SeccionesDocumento WITH(NOLOCK)</strong></p>
<p><strong>ON trRevisionSecFichero.cdgSeccion =
SeccionesDocumento.cdgSeccion</strong></p>
<p><strong>Where SeccionesDocumento.cdgDocumento in</strong></p>
<p><strong>(select cdgDocumento from tcCodigos_Documentos WITH(NOLOCK)
)</strong></p></td>
</tr>
<tr>
<td><p>--GD_trRevisionSecFichero_Extract</p>
<p>--User::V_EXTRACT_SECFICHERO</p>
<p><strong>SELECT DISTINCT trRevisionSecFichero.cdgFichero,
trRevisionSecFichero.cdgSeccion, trRevisionSecFichero.Pertenencia,
trRevisionSecFichero.RevisionSec FROM trRevisionSecFichero WITH(NOLOCK)
INNER JOIN SeccionesDocumento WITH(NOLOCK)</strong></p>
<p><strong>ON trRevisionSecFichero.cdgSeccion =
SeccionesDocumento.cdgSeccion INNER JOIN ((Select DISTINCT
tcDocsOT_Documentos.cdgDocumento as cdgDocumento,
tcDocsOT_Documentos.Establecimiento as Establecimiento,
tcDocsOT_Documentos.Obra as Obra FROM tcDocsOT_Documentos WITH(NOLOCK) )
UNION (Select DISTINCT tcOOTT_Documentos.cdgDocumento as cdgDocumento,
tcOOTT_Documentos.Establecimiento as Establecimiento,
tcOOTT_Documentos.Obra as Obra FROM tcOOTT_Documentos WITH(NOLOCK) WHERE
'ALHD' = 'AWD') UNION (Select DISTINCT
tcAvisosRevision_Documentos.cdgDocumento COLLATE Modern_Spanish_CI_AS as
cdgDocumento, tcAvisosRevision_Documentos.Establecimiento COLLATE
Modern_Spanish_CI_AS as Establecimiento,
tcAvisosRevision_Documentos.Obra COLLATE Modern_Spanish_CI_AS as Obra
FROM tcAvisosRevision_Documentos WITH(NOLOCK) ) UNION (Select DISTINCT
tcHojasCatalogo_Documentos.cdgdocumento COLLATE Modern_Spanish_CI_AS as
cdgdocumento,
Vista_Necora@INCopic_HojasCatalogoAplicabilidadObras.establecimiento
COLLATE Modern_Spanish_CI_AS as Establecimiento,
Vista_Necora@INCopic_HojasCatalogoAplicabilidadObras.obra COLLATE
Modern_Spanish_CI_AS as Obra FROM tcHojasCatalogo_Documentos
WITH(NOLOCK) left join
Vista_Necora@INCopic_HojasCatalogoAplicabilidadObras WITH(NOLOCK) on
Vista_Necora@INCopic_HojasCatalogoAplicabilidadObras.codigohoja =
tcHojasCatalogo_Documentos.cdgentidad) ) as T ON
SeccionesDocumento.cdgDocumento = T.cdgDocumento WHERE T.Establecimiento
= 'A' And T.Obra = 'AWD1'</strong></p></td>
</tr>
<tr>
<td><p>--Limpieza contra RevisionesSeccion</p>
<p><strong>delete trRevisionSecFichero</strong></p>
<p><strong>FROM trRevisionSecFichero A</strong></p>
<p><strong>WHERE A.cdgSeccion is not null</strong></p>
<p><strong>AND A.RevisionSec is not null</strong></p>
<p><strong>AND Not EXISTS</strong></p>
<p><strong>(SELECT * FROM RevisionesSeccion B</strong></p>
<p><strong>WHERE A.cdgSeccion = B.cdgSeccion AND A.RevisionSec =
B.RevisionSec)</strong></p></td>
</tr>
<tr>
<td>GD_trRevisionSecFichero_Update</td>
</tr>
</tbody>
</table>

### Gestion_Documental_Ubicaciones.dtsx

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th>TRUNCATE TABLE Ubicaciones</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>--Extract previo</p>
<p><strong>SELECT DISTINCT</strong></p>
<p><strong>dbo.Ubicaciones.cdgUbicacion,</strong></p>
<p><strong>dbo.Ubicaciones.Tipo,</strong></p>
<p><strong>dbo.Ubicaciones.Servidor,</strong></p>
<p><strong>dbo.Ubicaciones.Recurso,</strong></p>
<p><strong>dbo.Ubicaciones.ruta,</strong></p>
<p><strong>dbo.Ubicaciones.UltimaScarpeta</strong></p>
<p><strong>FROM Ubicaciones</strong></p>
<p><strong>LEFT JOIN trRevisionDocFichero</strong></p>
<p><strong>on Ubicaciones.cdgUbicacion =
trRevisionDocFichero.cdgDocumento</strong></p>
<p><strong>WHERE trRevisionDocFichero.cdgDocumento in</strong></p>
<p><strong>(select cdgDocumento from
tcCodigos_Documentos)</strong></p></td>
</tr>
<tr>
<td><p>--GD_Ubicaciones_Extract</p>
<p>--User::V_EXTRACT_UBIC</p>
<p><strong>SELECT DISTINCT Ubicaciones.cdgUbicacion, Ubicaciones.Tipo,
Ubicaciones.Servidor, Ubicaciones.Recurso, Ubicaciones.ruta,
Ubicaciones.UltimaScarpeta FROM ubicaciones INNER JOIN Ficheros ON
Ubicaciones.cdgUbicacion = 'R'+substring(Ficheros.cdgUbicacion,2,7)
INNER JOIN trRevisionDocFichero ON Ficheros.cdgFichero =
trRevisionDocFichero.cdgFichero INNER JOIN ((Select DISTINCT
tcDocsOT_Documentos.cdgDocumento as cdgDocumento,
tcDocsOT_Documentos.Establecimiento as Establecimiento,
tcDocsOT_Documentos.Obra as Obra FROM tcDocsOT_Documentos) UNION (Select
DISTINCT tcOOTT_Documentos.cdgDocumento as cdgDocumento,
tcOOTT_Documentos.Establecimiento as Establecimiento,
tcOOTT_Documentos.Obra as Obra FROM tcOOTT_Documentos WHERE 'ALHD' =
'AWD') UNION (Select DISTINCT tcAvisosRevision_Documentos.cdgDocumento
COLLATE Modern_Spanish_CI_AS as cdgDocumento,
tcAvisosRevision_Documentos.Establecimiento COLLATE Modern_Spanish_CI_AS
as Establecimiento, tcAvisosRevision_Documentos.Obra COLLATE
Modern_Spanish_CI_AS as Obra FROM tcAvisosRevision_Documentos) UNION
(Select DISTINCT tcHojasCatalogo_Documentos.cdgentidad COLLATE
Modern_Spanish_CI_AS as cdgentidad,
Vista_Necora@INCopic_HojasCatalogoAplicabilidadObras.establecimiento
COLLATE Modern_Spanish_CI_AS as Establecimiento,
Vista_Necora@INCopic_HojasCatalogoAplicabilidadObras.obra COLLATE
Modern_Spanish_CI_AS as Obra FROM tcHojasCatalogo_Documentos left join
Vista_Necora@INCopic_HojasCatalogoAplicabilidadObras on
Vista_Necora@INCopic_HojasCatalogoAplicabilidadObras.codigohoja =
tcHojasCatalogo_Documentos.cdgentidad) ) as T ON T.cdgDocumento =
trRevisionDocFichero.cdgDocumento WHERE T.Establecimiento = '' And
T.Obra = ''</strong></p></td>
</tr>
<tr>
<td><p>--Limpieza</p>
<p>delete Ubicaciones</p>
<p>where not exists (select * from Ficheros where</p>
<p>Ubicaciones.cdgUbicacion COLLATE Modern_Spanish_CI_AS =
Ficheros.cdgUbicacion)</p></td>
</tr>
<tr>
<td>GD_Ubicaciones_Update</td>
</tr>
</tbody>
</table>

### GestionDocumental_SituacionesRevisionDocumento.dtsx

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th>TRUNCATE TABLE SituacionesRevisionDocumento</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>-- Extract SituacionesRevisionDocumento</p>
<p>--User::V_SQL_EXTARCT_GD</p>
<p><strong>select distinct a.* from dbo.situacionesRevisionDocumento a
inner join ((SELECT distinct RevisionesDocumento.* FROM
RevisionesDocumento inner join((Select DISTINCT
tcDocsOT_Documentos.cdgDocumento as cdgDocumento,
tcDocsOT_Documentos.Establecimiento as Establecimiento,
tcDocsOT_Documentos.Obra as Obra FROM tcDocsOT_Documentos) UNION (Select
DISTINCT tcOOTT_Documentos.cdgDocumento as cdgDocumento,
tcOOTT_Documentos.Establecimiento as Establecimiento,
tcOOTT_Documentos.Obra as Obra FROM tcOOTT_Documentos ) UNION (Select
DISTINCT tcAvisosRevision_Documentos.cdgDocumento COLLATE
Modern_Spanish_CI_AS as cdgDocumento,
tcAvisosRevision_Documentos.Establecimiento COLLATE Modern_Spanish_CI_AS
as Establecimiento, tcAvisosRevision_Documentos.Obra COLLATE
Modern_Spanish_CI_AS as Obra FROM tcAvisosRevision_Documentos)
UNION</strong></p>
<p><strong>(Select DISTINCT tcHojasCatalogo_Documentos.cdgdocumento
COLLATE Modern_Spanish_CI_AS as cdgdocumento,</strong></p>
<p><strong>Vista_Necora@INCopic_HojasCatalogoAplicabilidadOBras.establecimiento
COLLATE Modern_Spanish_CI_AS as Establecimiento,
Vista_Necora@INCopic_HojasCatalogoAplicabilidadObras.obra COLLATE
Modern_Spanish_CI_AS as Obra FROM tcHojasCatalogo_Documentos left join
Vista_Necora@INCopic_HojasCatalogoAplicabilidadObras on
Vista_Necora@INCopic_HojasCatalogoAplicabilidadObras.codigohoja =
tcHojasCatalogo_Documentos.cdgentidad)) as T on T.cdgDocumento =
RevisionesDocumento.cdgDocumento WHERE T.Establecimiento ='' and T.Obra
= '' ) UNION (SELECT distinct RD.* FROM RevisionesDocumento RD inner
join tcCodigos_Documentos tc on RD.cdgdocumento = tc.cdgdocumento and
RD.revisiondoc = tc.revisiondoc)) as p on p.cdgdocumento =
a.cdgdocumento collate Modern_Spanish_CI_AS and p.revisiondoc =
a.revisiondoc collate Modern_Spanish_CI_AS</strong></p></td>
</tr>
<tr>
<td><p>-- Limpieza de registros situacionesRevisionDocumento</p>
<p><strong>delete
interfacesDWH.dbo.SituacionesRevisionDocumento</strong></p>
<p><strong>from dbo.SituacionesRevisionDocumento Srd</strong></p>
<p><strong>where not exists</strong></p>
<p><strong>(select * from Dbo.RevisionesDocumento Rd</strong></p>
<p><strong>where Rd.cdgdocumento = Srd.cdgdocumento</strong></p>
<p><strong>and Rd.revisionDoc = Srd.revisionDoc)</strong></p></td>
</tr>
<tr>
<td>Update SituacionesRevisionDocumento</td>
</tr>
</tbody>
</table>

### GestionDocumental_SituacionesRevisionSeccion.dtsx

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th>Truncate table SituacionesRevisionSeccion</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>--Extract previo</p>
<p><strong>select SrS.* from dbo.SituacionesRevisionSeccion
SrS</strong></p>
<p><strong>inner join</strong></p>
<p><strong>(SELECT DISTINCT RevisionesSeccion.cdgSeccion,</strong></p>
<p><strong>RevisionesSeccion.DescripcionRevisionSec,</strong></p>
<p><strong>RevisionesSeccion.RevisionOrigen,</strong></p>
<p><strong>RevisionesSeccion.RevisionSec</strong></p>
<p><strong>FROM RevisionesSeccion</strong></p>
<p><strong>INNER JOIN SeccionesDocumento</strong></p>
<p><strong>ON RevisionesSeccion.cdgSeccion =
SeccionesDocumento.cdgSeccion</strong></p>
<p><strong>Where SeccionesDocumento.cdgDocumento in</strong></p>
<p><strong>(select cdgDocumento collate Modern_Spanish_CI_AS from
tcCodigos_Documentos)) as T1</strong></p>
<p><strong>on T1.cdgseccion = SrS.cdgSeccion</strong></p>
<p><strong>and T1.revisionSec = SrS.revisionSec</strong></p></td>
</tr>
<tr>
<td><p>-- Extract SituacionesRevisionSeccion</p>
<p>--User::V_EXTRACT_GD</p>
<p><strong>select a.* from situacionesRevisionSeccion a inner join
(SELECT DISTINCT RevisionesSeccion.cdgSeccion,
RevisionesSeccion.DescripcionRevisionSec,
RevisionesSeccion.RevisionOrigen, RevisionesSeccion.RevisionSec FROM
RevisionesSeccion INNER JOIN SeccionesDocumento ON
RevisionesSeccion.cdgSeccion = SeccionesDocumento.cdgSeccion INNER JOIN
((Select DISTINCT tcDocsOT_Documentos.cdgDocumento as cdgDocumento,
tcDocsOT_Documentos.Establecimiento as Establecimiento,
tcDocsOT_Documentos.Obra as Obra FROM tcDocsOT_Documentos) UNION (Select
DISTINCT tcOOTT_Documentos.cdgDocumento as cdgDocumento,
tcOOTT_Documentos.Establecimiento as Establecimiento,
tcOOTT_Documentos.Obra as Obra FROM tcOOTT_Documentos) UNION (Select
DISTINCT tcAvisosRevision_Documentos.cdgDocumento COLLATE
Modern_Spanish_CI_AS as cdgDocumento,
tcAvisosRevision_Documentos.Establecimiento COLLATE Modern_Spanish_CI_AS
as Establecimiento, tcAvisosRevision_Documentos.Obra COLLATE
Modern_Spanish_CI_AS as Obra FROM tcAvisosRevision_Documentos) UNION
(Select DISTINCT tcHojasCatalogo_Documentos.cdgdocumento COLLATE
Modern_Spanish_CI_AS as cdgdocumento,
Vista_Necora@INCopic_HojasCatalogoAplicabilidadObras.establecimiento
COLLATE Modern_Spanish_CI_AS as Establecimiento,
Vista_Necora@INCopic_HojasCatalogoAplicabilidadObras.obra COLLATE
Modern_Spanish_CI_AS as Obra FROM tcHojasCatalogo_Documentos left join
Vista_Necora@INCopic_HojasCatalogoAplicabilidadObras on
Vista_Necora@INCopic_HojasCatalogoAplicabilidadObras.codigohoja =
tcHojasCatalogo_Documentos.cdgentidad) ) as T ON
SeccionesDocumento.cdgDocumento = T.cdgDocumento WHERE T.Establecimiento
= '' And T.Obra = '') as p on p.revisionSec = a.revisionSec collate
Modern_Spanish_CI_AS and p.cdgseccion = a.cdgseccion collate
Modern_Spanish_CI_AS</strong></p></td>
</tr>
<tr>
<td><p>-- Limpieza de Campos SituacionesRevisionSeccion</p>
<p><strong>delete SituacionesRevisionseccion</strong></p>
<p><strong>from SituacionesRevisionseccion Srs</strong></p>
<p><strong>where not exists</strong></p>
<p><strong>(select * from Dbo.RevisionesSeccion Rs</strong></p>
<p><strong>where Rs.cdgseccion = Srs.cdgseccion</strong></p>
<p><strong>and Rs.RevisionSec = Srs.RevisionSec)</strong></p></td>
</tr>
<tr>
<td>Update SituacionsRevisionSeccion</td>
</tr>
</tbody>
</table>

### GestionDocumental_tcHojasCatalogo_Documentos.dtsx

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th>TRUNCATE TABLE DBO.tcHojasCatalogo_Documentos</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>-- Materiales_INCopic_HojasCatalogo_Extract</p>
<p>--User::V_EXTRACT</p>
<p><strong>select * from tcHojasCatalogo_Documentos tc inner join
Vista_Necora@INCopic_HojasCatalogoAplicabilidadObras vis on
Vis.codigohoja = tc.cdgentidad and vis.establecimiento = 'A' and
vis.obra ='AWD1'</strong></p></td>
</tr>
<tr>
<td><p>-- Limpieza INCopic_HojasCatalogo</p>
<p><strong>delete</strong></p>
<p><strong>from tcHojasCatalogo_Documentos</strong></p>
<p><strong>where tcHojasCatalogo_Documentos .cdgentidad not
in</strong></p>
<p><strong>(select codigohoja</strong></p>
<p><strong>from INCopic_HojasCatalogo)</strong></p></td>
</tr>
<tr>
<td>-- Limpiar Campos que ejecuta paquete _AtributosConfig.dtsx</td>
</tr>
<tr>
<td>Materiales_INCopic_HojasCatalogo_Update y
Mat_CatalogueShee_Delete</td>
</tr>
</tbody>
</table>

### Habilitar_Index.dtsx

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th>Delete _FK_FALLIDOS where proyecto = ? con
User::GLOBAL_PROYECTO</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>SELECT NAME FROM SYSOBJECTS WHERE XTYPE = 'U' AND CATEGORY
&lt;&gt; 2</p>
<p>con User::GLOBAL_CATEGORY, dentro de User::tabla_object. Para usar en
el bucle</p></td>
</tr>
<tr>
<td><p>Bucle de tablas (cada una en User::tabla_object desde
User::tabla_object)</p>
<p>Saca sus FK</p>
<p>select Constraint_name, constraint_type from
INFORMATION_SCHEMA.TABLE_CONSTRAINTS</p>
<p>where constraint_type in ('FOREIGN KEY', 'CHECK')</p>
<p>and table_name = ?</p>
<p>con User::V_Nombre_Tabla y deja resultado en
User::V_foreign_key_OBJ</p></td>
</tr>
<tr>
<td><p>Bucle de Foreign key (usa User::V_Foreign_key y
User::V_TIPO_CONST desde User::V_foreign_key_OBJ)</p>
<p>RAMA1: {</p>
<p>Bucle de campos relacionados con User::V_TOrigen, User::V_COrigen,
User::V_TDestino, User::V_CDestino, User::V_TipoO desde
User::V_Campos_OBJ</p>
<p>Insertar tabla FALLIDOS con User::V_SQL_INSERT</p>
<p>Ejecutar Select Existe con User::V_Existe</p>
<p>Valor de V_Alter (script)</p>
<p>Habilitar INDEX con User::V_ALTER</p>
<p>}</p>
<p>RAMA2: {</p>
<p>CREA SELECT Y CONTADOR DE REGISTROS</p>
<p>Insertar tabla FALLIDOS_CHECK con User::V_INSERT_CHK</p>
<p>Ejecutar Select Existe CHECK con User::V_EXIST_CHK</p>
<p>Valor de V_Alter CHECK (script)</p>
<p>HABILITAR CHECK con User::V_ALTER_CHK</p>
<p>}</p></td>
</tr>
</tbody>
</table>

### InicioUpdatenotice.dtsx

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th><p>--insert inicio updatenotice</p>
<p>Declare @v_id int</p>
<p>set @v_id = (select isnull(max(id),0)+1 from UpdateNotice)</p>
<p>Insert into UpdateNotice (Id,Start_Date, Finish_Date)</p>
<p>Values(@v_id,getdate(),null)</p></th>
</tr>
</thead>
<tbody>
<tr>
<td>TRUNCATE TABLE COPIC_REFERENCIA</td>
</tr>
</tbody>
</table>

### INTERFACES_PRINCIPAL_EEA5.dtsx

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th><p>--Limpieza Updatenotice</p>
<p>delete updatenotice</p>
<p>where CONVERT(VARCHAR(10), Start_date, 120) = CONVERT(VARCHAR(10),
GETDATE(), 120)</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p>--Actualiza Fecha Inicial UpdateNotice</p>
<p>Declare @v_id int</p>
<p>set @v_id = (select isnull(max(id),0)+1 from UpdateNotice)</p>
<p>Insert into UpdateNotice (Id,Start_Date, Finish_Date)</p>
<p>Values(@v_id,getdate(),null)</p></td>
</tr>
<tr>
<td><p>EEA5_DB2 ejecuta el paquete EEA5_DB2.dtsx</p>
<p>Ejecuta los paquetes</p>
<p>EEA5_NC30SQ.dtsx</p>
<p>EEA5_NC68SQ.dtsx</p></td>
</tr>
<tr>
<td><p>EEA5 ejecuta el paquete EEA5.dtsx - Ejecuta estos paquetes</p>
<p>T_DB_C_E_CabAdd</p>
<p>T_DB_C_E_CabDel</p>
<p>T_DB_C_E_Cables</p>
<p>T_DB_C_E_Connections</p>
<p>T_DB_C_E_Notes</p>
<p>T_DB_C_E_Equipment</p>
<p>T_DB_C_SC_CabAdd</p>
<p>T_DB_C_SC_CabDel</p>
<p>T_DB_C_SC_Cables</p>
<p>T_DB_C_SC_Connections</p>
<p>T_DB_C_SC_Equipment</p>
<p>T_DB_C_SC_Notes</p>
<p>T_DB_R_E_CabAdd</p>
<p>T_DB_R_E_CabDel</p>
<p>T_DB_R_E_Cables</p>
<p>T_DB_R_E_Equipment</p>
<p>T_DB_R_E_Route</p>
<p>T_DB_R_E_ROUTEBLOCK</p>
<p>T_DB_R_SC_CabAdd</p>
<p>T_DB_R_SC_CabDel</p>
<p>T_DB_R_SC_Cables</p>
<p>T_DB_R_SC_Equipment</p>
<p>T_DB_R_SC_Route</p>
<p>T_DB_R_SC_ROUTEBLOCK</p>
<p>T_DBCatal</p>
<p>T_DBDesign</p>
<p>T_DBLme</p>
<p>T_DBPcontrol</p>
<p>T_DBLocal</p></td>
</tr>
<tr>
<td><p>-- Actualiza Fecha Final UpdateNotice</p>
<p>UPDATE UpdateNotice set Finish_Date = getdate() where Id = (select
max(id) from UpdateNotice )</p></td>
</tr>
</tbody>
</table>

## Interfaces MEL

### MEL_LME_CATALOGO.dtsx

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th>TRUNCATE TABLE LME_CATALOGO</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>--MEL LME_CATALOGO Extract</p>
<p><strong>Desde BAE Select * from eea213.LME_CATALOGO</strong></p></td>
</tr>
<tr>
<td>Limpieza de campos, que ejecuta _AtributosConfig.dtsx</td>
</tr>
<tr>
<td>MEL LME_CATALOGO Update y MEL LME_CATALOGO Delete</td>
</tr>
</tbody>
</table>

MEL_LME_ELECTRICA.dtsx

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th>TRUNCATE TABLE LME_ELECTRICA</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>--MEL LME_ELECTRICA Extract</p>
<p><strong>Desde BAE, select * from
eea213.LME_ELECTRICA</strong></p></td>
</tr>
<tr>
<td><p>Limpieza LME_ELECTRICA</p>
<p>DELETE FROM LME_ELECTRICA</p>
<p>WHERE PARENTID NOT IN</p>
<p>(SELECT ID</p>
<p>FROM LME_PIEZAS)</p></td>
</tr>
<tr>
<td>Limpieza de campos, que ejecuta _AtributosConfig.dtsx</td>
</tr>
<tr>
<td>MEL LME_ELECTRICA Update y MEL LME_ELECTRICA Delete</td>
</tr>
</tbody>
</table>

### MEL_LME_EQUIPO_ELECTRICO.dtsx

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th>TRUNCATE TABLE LME_EQUIPO_ELECTRICO</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>--MEL LME_EQUIPO_ELECTRICO Extract</p>
<p><strong>Desde BAE, select * from
[eea213].[LME_EQUIPO_ELECTRICO]</strong></p></td>
</tr>
<tr>
<td><p>-- Limpieza LME_EQUIPO_ELECTRICO</p>
<p>DELETE FROM LME_EQUIPO_ELECTRICO</p>
<p>WHERE PARENTID NOT IN</p>
<p>(SELECT ID</p>
<p>FROM LME_ELECTRICA)</p></td>
</tr>
<tr>
<td>Limpieza de campos, que ejecuta _AtributosConfig.dtsx</td>
</tr>
<tr>
<td>MEL LME_EQUIPO_ELECTRICO Update y MEL LME_EQUIPO_ELECTRICO
Delete</td>
</tr>
</tbody>
</table>

### MEL_LME_IDENTIFICADORES.dtsx

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th>TRUNCATE TABLE LME_IDENTIFICADORES</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>-- MEL LME_IDENTIFICADORES Extract</p>
<p><strong>Desde BAE, select * from
[eea213].[LME_IDENTIFICADORES]</strong></p></td>
</tr>
<tr>
<td><p>-- Limpieza LME_IDENTIFICADORES</p>
<p>DELETE FROM LME_IDENTIFICADORES</p>
<p>WHERE OWNERID NOT IN</p>
<p>(SELECT ID</p>
<p>FROM LME_PIEZAS)</p></td>
</tr>
<tr>
<td>Limpieza de campos, que ejecuta _AtributosConfig.dtsx</td>
</tr>
<tr>
<td>MEL LME_IDENTIFICADORES Update y MEL LME_IDENTIFICADORES Delete</td>
</tr>
</tbody>
</table>

### MEL_LME_LOCALES.dtsx

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th>TRUNCATE TABLE LME_LOCALES</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Desde BAE, select * from
[eea213].[LME_LOCALES]</strong></td>
</tr>
<tr>
<td><p>-- Limpieza LME_LOCALES</p>
<p>DELETE FROM LME_LOCALES</p>
<p>WHERE ID NOT IN</p>
<p>(SELECT ID_LOCAL</p>
<p>FROM LME_UBICACIONES)</p></td>
</tr>
<tr>
<td>MEL LME_LOCALES Update y MEL LME_LOCALES Delete</td>
</tr>
</tbody>
</table>

### MEL_LME_PIEZAS.dtsx

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th>TRUNCATE TABLE LME_PIEZAS</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>-- MEL LME_PIEZAS Extract</p>
<p><strong>SELECT distinct id, systemid, gdc, tipo, copic, descripcion,
documento,</strong></p>
<p><strong>etc_demanda, soporte_polin, plano_situacion,
choque,</strong></p>
<p><strong>ownerid, observaciones</strong></p>
<p><strong>FROM LME_PIEZAS</strong></p></td>
</tr>
<tr>
<td><p>-- Limpieza LME_PIEZAS</p>
<p>DELETE FROM LME_PIEZAS</p>
<p>WHERE COPIC NOT IN</p>
<p>(SELECT COPIC</p>
<p>FROM LME_CATALOGO)</p></td>
</tr>
<tr>
<td>Limpieza de campos, que ejecuta _AtributosConfig.dtsx</td>
</tr>
<tr>
<td>MEL LME_PIEZAS Update y MEL LME_PIEZAS Delete</td>
</tr>
</tbody>
</table>

### MEL_LME_UBICACIONES.dtsx

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th>TRUNCATE TABLE LME_UBICACIONES</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>-- MEL LME_UBICACIONES Extract</p>
<p><strong>Desde BAE, select * from
[eea213].[LME_UBICACIONES]</strong></p></td>
</tr>
<tr>
<td><p>--Limpieza LME_UBICACIONES</p>
<p>DELETE FROM LME_UBICACIONES</p>
<p>WHERE OWNERID NOT IN</p>
<p>(SELECT ID</p>
<p>FROM LME_PIEZAS)</p></td>
</tr>
<tr>
<td>Limpieza de campos, que ejecuta _AtributosConfig.dtsx</td>
</tr>
<tr>
<td>MEL LME_UBICACIONES Update y MEL LME_UBICACIONES Delete</td>
</tr>
</tbody>
</table>

## Notas

### Notas.dtsx

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th>truncate table nc17sq_notes</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>-- Extract previo</p>
<p>-- User::V_EXTRACT_PREVIO</p>
<p><strong>(SELECT ESTABL AS ESTABL, CODOBRA AS CODOBRA, DOCUREV as
docurev, 'NOTA01' as numero, cast(BZNC.NCUDF06('NC06FV', 'NC17SQ'
,SECUE06, 'NOTA01' ,'INGLES') as varchar(4000)) as NOTA FROM NEC.NC17SQ
WHERE ESTABL = '2' AND CODOBRA = '0213' AND NOTAS = 'SI') UNION (SELECT
ESTABL AS ESTABL, CODOBRA AS CODOBRA, DOCUREV as docurev, 'NOTA02' as
numero , cast(BZNC.NCUDF06('NC06FV', 'NC17SQ' ,SECUE06, 'NOTA02'
,'INGLES') as varchar(4000)) as NOTA FROM NEC.NC17SQ WHERE ESTABL = '2'
AND CODOBRA = '0213' AND NOTAS = 'SI')</strong></p></td>
</tr>
<tr>
<td><p>-- limpieza de notas</p>
<p>delete nc17sq_notes</p>
<p>from NC17SQ_notes DWH</p>
<p>WHERE dwh.nota = ''</p>
<p>or docurev not in</p>
<p>(select docurev from nc17sq )</p></td>
</tr>
<tr>
<td><p>-- Obtener Docurev de NC17SQ</p>
<p><strong>select distinct docurev from dbo.nc17sq_notes where
numeronota &gt; 'nota01'</strong></p>
<p><strong>en User::OBJECT_DOCUREV, para usar en el
bucle</strong></p></td>
</tr>
<tr>
<td><p>Bucle ‘Notas por cada docurev ‘ usando cada User::OBJECT_DOCUREV
desde User::OBJECT_DOCUREV {</p>
<p>INICIALIZA V_CONT_NOTAS (script)</p>
<p>Bucle ‘Consulta d enotas’ evaluando @V_CONT_NOTAS &lt; 99 &amp;&amp;
@V_NOTA != ""</p>
<p>{ NOTA CONSULTA (script)</p>
<p>Consulta la nota con User::V_CONSULTANOTAS y vuelca a
User::V_NOTA</p>
<p>Concatenar salto de línea (script)</p>
<p>insertar en NC17SQ_NOTES con User::V_INSERT_NOTA</p>
<p>Contador de notas (script)</p>
<p>}</p>
<p>}</p></td>
</tr>
<tr>
<td>Update NOTAS y Delete NOTAS</td>
</tr>
</tbody>
</table>

## Ordenes

### Ordenes_BO10SQ.dtsx

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th>Truncate table dbo.BO10SQ</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>--Ordenes_BO10SQ_Extract</p>
<p><strong>SELECT a.ESTABL, a.CODOBRA, a.ORDEN, a.TIPORDN,</strong></p>
<p><strong>a.TAREA, a.FASE, a.CENDESA, a.CENTREM, a.CENTREJ,
a.ZONA,</strong></p>
<p><strong>a.BLOQUE, a.MODULO, a.SECCION, a.GRUCOSTE,
a.PRODINT,</strong></p>
<p><strong>a.ETAPA, a.AREAWK , a.GREMIO, a.AVANCE, a.SITUAIPA,
a.SITUAPRO,</strong></p>
<p><strong>a.SITUAMAT, a.SITCONFI, a.PLANOORI, a.URREALZ,
a.URAPROB,</strong></p>
<p><strong>a.URLANZA, a.URCONFI, a.AVISOREV, a.DNI,
a.CTACARGO,</strong></p>
<p><strong>a.PARTIDA, a.SECUE06, a.GHSPROB, a.GHSPREV,
a.GHSLANZ,</strong></p>
<p><strong>a.GHSCONS, a.GHSIMPU, a.HORASINV,</strong></p>
<p><strong>case a.COPROV</strong></p>
<p><strong>when '118Q' then '118Q'</strong></p>
<p><strong>else</strong></p>
<p><strong>case coalesce ( b.coprov, '' )</strong></p>
<p><strong>when '118Q' then '118Q'</strong></p>
<p><strong>else ''</strong></p>
<p><strong>end</strong></p>
<p><strong>end as Coprov,</strong></p>
<p><strong>a.GESTMAT, a.GESTCOM,</strong></p>
<p><strong>a.ACTIVIDAD, a.FECREAC, a.AVAPROB, a.GHSPROBSUB,</strong></p>
<p><strong>cast(BZNC.NCUDF06('BO06FV ','BO10SQ'
,a.SECUE06,'DESORDC','INGLES') as char(100)) AS DESORDC ,</strong></p>
<p><strong>cast(BZNC.NCUDF06('BO06FV ','BO10SQ'
,a.SECUE06,'DESORDL','INGLES') as char(100)) AS DESORDL</strong></p>
<p><strong>FROM NEC.BO10SQ a</strong></p>
<p><strong>left join</strong></p>
<p><strong>(Select distinct establ , codobra, orden, coprov from
nec.bo41sq b</strong></p>
<p><strong>where coprov = '118Q'</strong></p>
<p><strong>) b</strong></p>
<p><strong>on b.establ = a.establ</strong></p>
<p><strong>and b.codobra = a.codobra</strong></p>
<p><strong>and b.orden = a.orden</strong></p>
<p><strong>WHERE (a.CODOBRA =? AND a.ESTABL=?)</strong></p>
<p><strong>Or a.orden in</strong></p>
<p><strong>(select b.orden</strong></p>
<p><strong>from nec.bo41sq b</strong></p>
<p><strong>where b.establ = ?</strong></p>
<p><strong>and a.establ = b.establ</strong></p>
<p><strong>and b.codobra = ?</strong></p>
<p><strong>and a.codobra = b.codobra</strong></p>
<p><strong>and a.orden = b.orden</strong></p>
<p><strong>and b.coprov = '118Q')</strong></p></td>
</tr>
<tr>
<td><p>--update</p>
<p>update bo10sq</p>
<p>set coprov = ''</p>
<p>where tarea = 'CT'</p></td>
</tr>
<tr>
<td>Grupo de limpiza No Proceed (script)</td>
</tr>
<tr>
<td>Limpieza_Campos No Proceed que ejecuta paquete
_LimpiarCamposBO.dtsx</td>
</tr>
<tr>
<td>Grupo de limpieza IIAA</td>
</tr>
<tr>
<td>Limpieza_Campos IIAA que ejecuta paquete _LimpiarCamposBO.dtsx</td>
</tr>
<tr>
<td>Grupo de limpieza Navantia</td>
</tr>
<tr>
<td>Limpieza_Campos Navantia que ejecuta paquete
_LimpiarCamposBO.dtsx</td>
</tr>
<tr>
<td>Ordenes_BO10SQ_Update y Ordenes_BO10SQ_Delete y INSERTA REG EN
_EJECUCION (script)</td>
</tr>
</tbody>
</table>

### Ordenes_BO11SQ.dtsx

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th>TRUNCATE TABLE BO11SQ</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>-- Ordenes_BO11SQ_Extract</p>
<p>--User::V_SQL</p>
<p><strong>SELECT a.*,</strong></p>
<p><strong>cast(BZNC.NCUDF06('BO06FV ','BO10SQ'
,b.SECUE06,'DESORDC','INGLES') as char(100)) AS DESORDC ,</strong></p>
<p><strong>cast(BZNC.NCUDF06('BO06FV ','BO10SQ'
,b.SECUE06,'DESORDL','INGLES') as char(100)) AS DESORDL</strong></p>
<p><strong>FROM NEC.BO11SQ a</strong></p>
<p><strong>inner join nec.bo10sq b</strong></p>
<p><strong>on a.establ = b.establ</strong></p>
<p><strong>and a.codobra = b.codobra</strong></p>
<p><strong>and a.orden = b.orden</strong></p>
<p><strong>WHERE a.establ= '2' and b.codobra = '0213'</strong></p></td>
</tr>
<tr>
<td>Grupo de limpiza No Proceed y Limpieza_Campos No Proceed (Paquete
_LimpiarCamposBO.dtsx)</td>
</tr>
<tr>
<td>Grupo de limpieza IIAA (script) y Limpieza_Campos IIAA
(_LimpiarCamposBO.dtsx)</td>
</tr>
<tr>
<td>Grupo de limpieza Navantia (script) y Limpieza_Campos Navantia
(_LimpiarCamposBO.dtsx)</td>
</tr>
<tr>
<td>Ordenes_BO11SQ_Update y Ordenes_BO11SQ_Delete y INSERTA REG EN
_EJECUCION (Script)</td>
</tr>
</tbody>
</table>

### Ordenes_BO12SQ.dtsx

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th>Truncate table dbo.BO12SQ</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>--Ordenes_BO12SQ_Extract</p>
<p>-- User::V_SQL</p>
<p><strong>SELECT establ, codobra, orden, linea, tipoaco, revision,
grucoste, acopio, lineao, cantnec, cantres, cantsol, cantdes, unidcon,
cantnep, unidpro, peso, candemn, normad, normac, dimens, tanomi,
acabado, partic, resist, inspec, presion, marplan, numele, desgmar,
bloque, desgblo, solaco, desgaco, modulo, desgmod, local, desgloc,
situamat, snref, detalle, notas, observ, dni, process, ctacargo,
partida, secue06, entorno, cast(BZNC.NCUDF06('BO06FV ','BO12SQ'
,SECUE06,'DESLINE','INGLES') as char(100)) AS DESCR FROM NEC.BO12SQ nc12
WHERE establ= '2' and codobra = '0213' AND (establ= '2' and EXISTS
(select 1 from nec.bo10sq a left join nec.bo41sq b on b.establ =
a.establ and b.codobra = a.codobra and b.orden = a.orden where a.establ
= nc12.establ and a.codobra = nc12.codobra and a.orden = nc12.orden and
a.tarea &lt;&gt; 'CT' and (a.coprov = '118Q' ) ) or establ =
'T')</strong></p></td>
</tr>
<tr>
<td>Limpieza de Registros que ejecuta _LimpiezaRegistros.dtsx</td>
</tr>
<tr>
<td>Grupo de limpiza No Proceed y Limpieza_Campos No Proceed (Paquete
_LimpiarCamposBO.dtsx)</td>
</tr>
<tr>
<td>Grupo de limpieza IIAA (script) y Limpieza_Campos IIAA
(_LimpiarCamposBO.dtsx)</td>
</tr>
<tr>
<td>Grupo de limpieza Navantia (script) y Limpieza_Campos Navantia
(_LimpiarCamposBO.dtsx)</td>
</tr>
<tr>
<td>Ordenes_BO12SQ_Update y Ordenes_BO12SQ_Delete y INSERTA REG EN
_EJECUCION (Script)</td>
</tr>
</tbody>
</table>

### Ordenes_BO13SQ.dtsx

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th>TRUNCATE TABLE BO13SQ</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>--Ordenes_BO13SQ_Extract</p>
<p>-- User::V_SQL</p>
<p><strong>SELECT establ, codobra, orden, tiporef, numref, tipind,
indref, ferefer, secue06, revision, cast(BZNC.NCUDF06('BO06FV ','BO13SQ'
,SECUE06,'DESREF','INGLES') AS VARCHAR(8000)) AS DESCR FROM NEC.BO13SQ
WHERE establ= 'T' and codobra = '9999'</strong></p></td>
</tr>
<tr>
<td>Limpieza de Registros que ejecuta _LimpiezaRegistros.dtsx</td>
</tr>
<tr>
<td>Grupo de limpiza No Proceed y Limpieza_Campos No Proceed (Paquete
_LimpiarCamposBO.dtsx)</td>
</tr>
<tr>
<td>Grupo de limpieza IIAA (script) y Limpieza_Campos IIAA
(_LimpiarCamposBO.dtsx)</td>
</tr>
<tr>
<td>Grupo de limpieza Navantia (script) y Limpieza_Campos Navantia
(_LimpiarCamposBO.dtsx)</td>
</tr>
<tr>
<td>Ordenes_BO12SQ_Update y Ordenes_BO12SQ_Delete y INSERTA REG EN
_EJECUCION (Script)</td>
</tr>
</tbody>
</table>

### Ordenes_BO14SQ.dtsx

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th>TRUNCATE TABLE BO14SQ</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>--Ordenes_BO14SQ_Extract</p>
<p>-- User::V_SQL</p>
<p>SELECT * FROM NEC.BO14SQ WHERE establ= '2' and codobra =
'0213'</p></td>
</tr>
<tr>
<td><p>--borra lo que no existe en BO13SQ</p>
<p>delete bo14sq</p>
<p>from bo14sq b14</p>
<p>where not exists</p>
<p>( select * from bo13sq b13</p>
<p>where b14.establ = b13.establ</p>
<p>and b14.codobra = b13.codobra</p>
<p>and b14.orden = b13.orden</p>
<p>and b14.tiporef = b13.tiporef</p>
<p>and b14.numref = b13.numref</p>
<p>)</p></td>
</tr>
<tr>
<td>Ordenes_BO14SQ_Update y Ordenes_BO14SQ_Delete y Insertar REG en
_EJECUCION (script)</td>
</tr>
</tbody>
</table>

### Ordenes_BO15SQ.dtsx

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th>TRUNCATE TABLE BO15SQ</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>--Ordenes_BO15SQ_Extract</p>
<p>-- User::V_SQL</p>
<p><strong>select establ, codobra, orden, linea, cantnep, unidpro,
cantres, cantela, cantdes, cantsol, unidcon, peso, normad, normac,
dimens, tanomi, acabado, partic, observ, marequi, marfunc, dni, process,
marborr, revision, secue06, tipoco, tipprod, tipproc, arbol, entorno,
cast(BZNC.NCUDF06('BO06FV ','BO15SQ' ,SECUE06,'DESLINE','INGLES') as
char(100)) AS DESCR from nec.bo15sq B15 where b15.establ='2' and
b15.codobra='0213' and (establ = '2' and ((( not exists (Select 1 from
nec.bo40sq b40 where B15.establ= b40.establ and B15.codobra= b40.codobra
and B15.orden= b40.orden and clavalor &lt;&gt; '20' and clavalor
&lt;&gt; '23' and establ='2' and codobra='0213' ) and exists (select 1
from nec.bo61sq b61 inner join nec.bo41sq b41 on b41.establ = b61.establ
and b41.codobra = b61.codobra and b41.orden = b61.orden and b41.linea =
b61.lineaope and b41.sublinea = b61.subliope where b61.establ =
b15.establ and b61.codobra = b15.codobra and b61.orden = b15.orden and
b61.lineacom = b15.linea and b41.coprov = '118Q' and b41.establ='2' and
b41.codobra='0213' ) ) or exists (select 1 from (select b40.establ,
b40.codobra, b40.orden, count(*) as num40 from nec.bo40sq b40 inner join
nec.bo41sq b41 on b40.establ = b41.establ and b40.codobra = b41.codobra
and b40.orden = b41.orden and b40.linea = b41.linea inner join
nec.bo10sq b10 on b10.establ = b10.establ and b10.codobra = b40.codobra
and b10.orden = b40.orden where b40.establ='2' and b40.codobra='0213'
and (b41.coprov = '118Q' or (b41.coprov = ' ' and b10.coprov = '118Q'))
group by b40.establ, b40.codobra, b40.orden) as b40 left join (select
b40.establ, b40.codobra, b40.orden, count(*) as num20 from nec.bo40sq
b40 inner join nec.bo41sq b41 on b40.establ = b41.establ and b40.codobra
= b41.codobra and b40.orden = b41.orden and b40.linea = b41.linea inner
join nec.bo10sq b10 on b10.establ = b10.establ and b10.codobra =
b40.codobra and b10.orden = b40.orden where (b40.clavalor = '20' or
b40.clavalor = '23') and b40.establ='2' and b40.codobra='0213' and
(b41.coprov = '118Q'or (b41.coprov = ' ' and b10.coprov = '118Q')) group
by b40.establ, b40.codobra, b40.orden) as b4020 on b40.establ =
b4020.establ and b40.codobra = b4020.codobra and b40.orden = b4020.orden
where b40.establ = b15.establ and b40.codobra = b15.codobra and
b40.orden = b15.orden and b40.num40 = coalesce(b4020.num20, 0) ))) or
establ = 'T')</strong></p></td>
</tr>
<tr>
<td>Limpieza de Registros que ejecuta _LimpiezaRegistros.dtsx</td>
</tr>
<tr>
<td>Grupo de limpiza No Proceed y Limpieza_Campos No Proceed (Paquete
_LimpiarCamposBO.dtsx)</td>
</tr>
<tr>
<td>Grupo de limpieza IIAA (script) y Limpieza_Campos IIAA
(_LimpiarCamposBO.dtsx)</td>
</tr>
<tr>
<td>Grupo de limpieza Navantia (script) y Limpieza_Campos Navantia
(_LimpiarCamposBO.dtsx)</td>
</tr>
<tr>
<td>Ordenes_BO15SQ_Update y Ordenes_BO15SQ_Delete y INSERTA REG EN
_EJECUCION (Script)</td>
</tr>
</tbody>
</table>

### Ordenes_BO16SQ.dtsx

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th>TRUNCATE TABLE BO16SQ</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>--Ordenes_BO16SQ_Extract</p>
<p>-- User::V_SQL</p>
<p><strong>SELECT * FROM NEC.BO16SQ WHERE establ= '2' and codobra =
'9999'</strong></p></td>
</tr>
<tr>
<td>limpieza de REGISTROS que ejecuta _LimpiezaRegistros.dtsx</td>
</tr>
<tr>
<td>Ordenes_BO16SQ_Update y Ordenes_BO16SQ_Delete y Insertar REG en
_ejecucion</td>
</tr>
</tbody>
</table>

### Ordenes_BO40SQ.dtsx

(lo llama el paquete Ordenes_BO41SQ.dtsx)

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th>TRUNCATE TABLE BO40SQ</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>--Ordenes_BO40SQ_Extract</p>
<p>-- User::V_SQL</p>
<p><strong>SELECT NEC.BO40SQ.*,cast(NEC.BO49SQ.DESCRI as varchar(8000))
as DESCR FROM NEC.BO40SQ LEFT JOIN NEC.BO49SQ on tablfich = 'BO40SQ' and
clavfich= concat(concat(concat(concat(establ , codobra) , orden) ,
linea) , sublinea) and nomcamp = 'DESLINE' and idioma = 'INGLES' WHERE
establ= 'T' and codobra = '9999'</strong></p></td>
</tr>
<tr>
<td><p>--borrar no existe en bo41sq</p>
<p>delete bo40sq</p>
<p>from bo40sq b40</p>
<p>where not exists</p>
<p>( select * from bo41sq b41</p>
<p>where b40.establ = b41.establ</p>
<p>and b40.codobra = b41.codobra</p>
<p>and b40.orden = b41.orden</p>
<p>and b40.linea = b41.linea</p>
<p>and b40.sublinea = b41.sublinea</p>
<p>)</p></td>
</tr>
<tr>
<td>Limpieza de Registros que ejecuta _LimpiezaRegistros.dtsx</td>
</tr>
<tr>
<td>Grupo de limpiza No Proceed y Limpieza_Campos No Proceed (Paquete
_LimpiarCamposBO.dtsx)</td>
</tr>
<tr>
<td>Grupo de limpieza IIAA (script) y Limpieza_Campos IIAA
(_LimpiarCamposBO.dtsx)</td>
</tr>
<tr>
<td>Grupo de limpieza Navantia (script) y Limpieza_Campos Navantia
(_LimpiarCamposBO.dtsx)</td>
</tr>
<tr>
<td>Ordenes_BO40SQ_Update y Ordenes_BO40SQ_Delete y INSERTA REG EN
_EJECUCION (Script)</td>
</tr>
</tbody>
</table>

### Ordenes_BO41SQ.dtsx

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th>TRUNCATE TABLE BO41SQ</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>--Ordenes_BO41SQ_Extract</p>
<p>-- User::V_SQL</p>
<p><strong>SELECT NEC.BO41SQ.*,cast(NEC.BO49SQ.DESCRI as varchar(8000))
as DESCR FROM NEC.BO41SQ LEFT JOIN NEC.BO49SQ on tablfich = 'BO41SQ' and
clavfich= concat(concat(concat(concat(establ , codobra) , orden) ,
linea) , sublinea) and nomcamp = 'DESLINE' and idioma = 'INGLES' WHERE
establ= 'T' and codobra = '9999'</strong></p></td>
</tr>
<tr>
<td><strong>Llamada al package bo40sq que llama al paquete
‘Ordenes_BO40SQ.dtsx’</strong></td>
</tr>
<tr>
<td><p>-- Borra lo que no exista en bo40sq</p>
<p><strong>delete bo41sq</strong></p>
<p><strong>from bo41sq b41</strong></p>
<p><strong>where not exists</strong></p>
<p><strong>( select * from bo40sq b40</strong></p>
<p><strong>where b40.establ = b41.establ</strong></p>
<p><strong>and b40.codobra = b41.codobra</strong></p>
<p><strong>and b40.orden = b41.orden</strong></p>
<p><strong>and b40.linea = b41.linea</strong></p>
<p><strong>and b40.sublinea = b41.sublinea</strong></p>
<p><strong>)</strong></p></td>
</tr>
<tr>
<td>Grupo de limpiza No Proceed y Limpieza_Campos No Proceed (Paquete
_LimpiarCamposBO.dtsx)</td>
</tr>
<tr>
<td>Grupo de limpieza IIAA (script) y Limpieza_Campos IIAA
(_LimpiarCamposBO.dtsx)</td>
</tr>
<tr>
<td>Grupo de limpieza Navantia (script) y Limpieza_Campos Navantia
(_LimpiarCamposBO.dtsx)</td>
</tr>
<tr>
<td>Ordenes_BO41SQ_Update y Ordenes_BO41SQ_Delete y INSERTA REG EN
_EJECUCION (Script)</td>
</tr>
</tbody>
</table>

### Ordenes_BO42SQ.dtsx

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th>TRUNCATE TABLE BO42SQ</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>--Ordenes_BO42SQ_Extract</p>
<p>-- User::V_SQL</p>
<p><strong>select b42.*, cast(b49.DESCRI as varchar(8000)) as
DESCR</strong></p>
<p><strong>from</strong></p>
<p><strong>(</strong></p>
<p><strong>SELECT distinct b42.establ, b42.centro, b42.taller,
b42.maquina, b42.unidpr, b42.cantcon, b42.ghsesti, b42.fecreac,
b42.usucrea, b42.notas, b42.observ, b42.unimed</strong></p>
<p><strong>FROM NEC.BO42SQ b42</strong></p>
<p><strong>INNER JOIN NEC.BO41SQ b41</strong></p>
<p><strong>ON b42.establ = b41.establ</strong></p>
<p><strong>AND b42.centro = b41.cenejec</strong></p>
<p><strong>AND b42.taller = b41.taller</strong></p>
<p><strong>AND b42.maquina = b41.maquina</strong></p>
<p><strong>WHERE b41.establ= '2' and b41.codobra = '0210' and '0210' =
'0210'</strong></p>
<p><strong>) as b42</strong></p>
<p><strong>LEFT JOIN NEC.BO49SQ B49 on B49.tablfich = 'BO42SQ' and
B49.clavfich= concat(concat(concat(concat(b42.establ , b42.centro) ,
b42.taller) , b42.maquina) , b42.unidpr) and b49.nomcamp = 'DESLINE' and
b49.idioma = 'INGLES'</strong></p></td>
</tr>
<tr>
<td>Ordenes_BO42SQ_Update y Ordenes_BO42SQ_Delete</td>
</tr>
</tbody>
</table>

### Ordenes_BO43SQ.dtsx

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th>TRUNCATE TABLE BO43SQ</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>--Ordenes_BO43SQ_Extract</p>
<p>-- User::V_SQL</p>
<p><strong>SELECT NEC.BO43SQ.* ,cast(NEC.BO49SQ.DESCRI as varchar(8000))
as DESCR FROM NEC.BO43SQ LEFT JOIN NEC.BO49SQ on tablfich = 'BO4SQ' and
clavfich= concat(concat(concat(concat(concat(establ , codobra) , orden)
, linea) , sublinea) , numtasac) and nomcamp = 'DESLINE' and idioma =
'INGLES' WHERE establ= 'T' and codobra = '9999' and '9999' =
'9999'</strong></p></td>
</tr>
<tr>
<td>Ordenes_BO43SQ_Update y Ordenes_BO43SQ_Delete</td>
</tr>
</tbody>
</table>

### Ordenes_BO47SQ.dtsx

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th>TRUNCATE TABLE BO47SQ</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>--Ordenes_BO47SQ_Extract</p>
<p><strong>SELECT * FROM NEC.BO47SQ WHERE establ= 'T' and codobra =
'9999'</strong></p></td>
</tr>
<tr>
<td><p>--borra lo que no exista en BO40sq</p>
<p><strong>delete bo47sq</strong></p>
<p><strong>from bo47sq b47</strong></p>
<p><strong>where not exists</strong></p>
<p><strong>( select * from bo40sq b40</strong></p>
<p><strong>where b47.establ = b40.establ</strong></p>
<p><strong>and b47.codobra = b40.codobra</strong></p>
<p><strong>and b47.orden = b40.orden</strong></p>
<p><strong>and b47.linea = b40.linea</strong></p>
<p><strong>and b47.sublinea = b40.sublinea</strong></p>
<p><strong>)</strong></p></td>
</tr>
<tr>
<td>Grupo de limpiza No Proceed y Limpieza_Campos No Proceed (Paquete
_LimpiarCamposBO.dtsx)</td>
</tr>
<tr>
<td>Grupo de limpieza IIAA (script) y Limpieza_Campos IIAA
(_LimpiarCamposBO.dtsx)</td>
</tr>
<tr>
<td>Grupo de limpieza Navantia (script) y Limpieza_Campos Navantia
(_LimpiarCamposBO.dtsx)</td>
</tr>
<tr>
<td>Ordenes_BO47SQ_Update y Ordenes_BO47SQ_Delete</td>
</tr>
</tbody>
</table>

### Ordenes_BO59SQ.dtsx

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th>TRUNCATE TABLE BO59SQ</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>--Ordenes_BO59SQ_Extract</p>
<p><strong>SELECT * FROM NEC.BO59SQ WHERE establ= 'T' and codobra =
'9999'</strong></p></td>
</tr>
<tr>
<td>Ordenes_BO59SQ_Update y Ordenes_BO59SQ_Delete y INSERTA REG EN
_EJECUCION (Script)</td>
</tr>
</tbody>
</table>

### Ordenes_BO61SQ.dtsx

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th>TRUNCATE TABLE BO61SQ</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>--Ordenes_BO61SQ_Extract</p>
<p><strong>SELECT * FROM NEC.BO61SQ WHERE establ= 'T' and codobra =
'9999'</strong></p></td>
</tr>
<tr>
<td><p>-- borra lo que no existe en bo41sq</p>
<p><strong>delete bo61sq</strong></p>
<p><strong>from bo61sq b61</strong></p>
<p><strong>where not exists</strong></p>
<p><strong>(select * from bo41sq b41</strong></p>
<p><strong>where b61.establ = b41.establ collate
Modern_Spanish_CI_AS</strong></p>
<p><strong>and b61.codobra = b41.codobra collate
Modern_Spanish_CI_AS</strong></p>
<p><strong>and b61.orden = b41.orden collate
Modern_Spanish_CI_AS</strong></p>
<p><strong>and b61.lineaope = b41.linea collate
Modern_Spanish_CI_AS</strong></p>
<p><strong>)</strong></p></td>
</tr>
<tr>
<td>Grupo de limpiza No Proceed y Limpieza_Campos No Proceed (Paquete
_LimpiarCamposBO.dtsx)</td>
</tr>
<tr>
<td>Grupo de limpieza IIAA (script) y Limpieza_Campos IIAA
(_LimpiarCamposBO.dtsx)</td>
</tr>
<tr>
<td>Grupo de limpieza Navantia (script) y Limpieza_Campos Navantia
(_LimpiarCamposBO.dtsx)</td>
</tr>
<tr>
<td>Ordenes_BO61SQ_Update y Ordenes_BO61SQ_Delete</td>
</tr>
</tbody>
</table>

### Ordenes_BO67SQ.dtsx

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th>TRUNCATE TABLE BO67SQ</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>--Ordenes_BO67SQ_Extract</p>
<p><strong>SELECT * FROM NEC.BO67SQ WHERE establ= 'T' and codobra =
'9999'</strong></p></td>
</tr>
<tr>
<td>Ordenes_BO67SQ_Update y Ordenes_BO67SQ_Delete</td>
</tr>
</tbody>
</table>

## Tablas_Apoyo

### Tablas_Apoyo_NC20SQ.dtsx

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th>TRUNCATE TABLE NC20SQ</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>-- Tablas_Apoyo_NC20SQ_Extract</p>
<p>SELECT CODTAB, CODELE,SECUE06,</p>
<p>cast(BZNC.NCUDF06('NC06FV ','NC20R' CONCAT CODTAB,SECUE06,'DESCR2 ','
') as char(100)) AS DESCRI,</p>
<p>cast(BZNC.NCUDF06('NC06FV ','NC20R' CONCAT CODTAB,SECUE06,'DESCR2
','INGLES') as char(100)) AS DESCRI2,</p>
<p>FORMATO</p>
<p>FROM NEC.NC20SQ</p>
<p>WHERE NOT (codtab='900' AND SECUE06=0)</p></td>
</tr>
<tr>
<td><p>-- Paso Updated</p>
<p>UPDATE NC20SQ</p>
<p>SET DESCRI = DWH.DESCRI</p>
<p>,SECUE06 = DWH.SECUE06</p>
<p>,DESCRI2 = DWH.DESCRI2</p>
<p>,FORMATO = DWH.FORMATO</p>
<p>,_TSTAMP = getdate()</p>
<p>,_CHECKSUM =
CHECKSUM(DWH.CODTAB,DWH.CODELE,DWH.DESCRI,DWH.SECUE06,DWH.DESCRI2,DWH.FORMATO)</p>
<p>,_STATUS = 'UPDATED'</p>
<p>FROM NC20SQ AWD</p>
<p>INNER JOIN INTERFACESDWH.DBO.NC20SQ DWH</p>
<p>ON DWH.CODTAB = AWD.CODTAB</p>
<p>AND DWH.CODELE = AWD.CODELE</p>
<p>WHERE
CHECKSUM(DWH.CODTAB,DWH.CODELE,DWH.DESCRI,DWH.SECUE06,DWH.DESCRI2,DWH.FORMATO)
&lt;&gt; AWD._CHECKSUM</p></td>
</tr>
<tr>
<td><p>-- Actualiza estado a NEW si habia sido borrado</p>
<p>UPDATE NC20SQ SET _STATUS='NEW', _TSTAMP=GETDATE()</p>
<p>FROM NC20SQ AWD</p>
<p>INNER JOIN</p>
<p>INTERFACESDWH.DBO.NC20SQ DWH</p>
<p>ON DWH.CODTAB = AWD.CODTAB</p>
<p>AND DWH.CODELE = AWD.CODELE</p>
<p>WHERE
CHECKSUM(DWH.CODTAB,DWH.CODELE,DWH.DESCRI,DWH.SECUE06,DWH.DESCRI2,DWH.FORMATO)
= AWD._CHECKSUM</p>
<p>AND AWD._STATUS = 'DELETED'</p></td>
</tr>
<tr>
<td><p>-- Paso_insert</p>
<p>INSERT INTO NC20SQ</p>
<p>(CODTAB,CODELE,DESCRI,SECUE06,DESCRI2,_TSTAMP,_CHECKSUM,_STATUS,FORMATO)</p>
<p>SELECT CODTAB, CODELE, DESCRI, SECUE06, DESCRI2, GETDATE()AS
_TSTAMP,</p>
<p>CHECKSUM(CODTAB,CODELE,DESCRI,SECUE06,DESCRI2,FORMATO) AS
_CHECKSUM,</p>
<p>'NEW' AS _STATUS , FORMATO</p>
<p>FROM INTERFACESDWH.DBO.NC20SQ DWH</p>
<p>WHERE NOT EXISTS</p>
<p>(SELECT *</p>
<p>FROM NC20SQ AWD</p>
<p>WHERE DWH.CODTAB = AWD.CODTAB</p>
<p>AND DWH.CODELE = AWD.CODELE)</p></td>
</tr>
<tr>
<td><p>-- Paso_deleted</p>
<p>UPDATE NC20SQ</p>
<p>SET _STATUS='DELETED',</p>
<p>_TSTAMP=GETDATE()</p>
<p>from nc20sq AWD</p>
<p>WHERE AWD._STATUS &lt;&gt; 'DELETED'</p>
<p>AND NOT EXISTS</p>
<p>(SELECT DWH.*</p>
<p>FROM INTERFACESDWH.DBO.NC20SQ DWH</p>
<p>WHERE DWH.CODTAB = AWD.CODTAB</p>
<p>AND DWH.CODELE = AWD.CODELE</p>
<p>)</p></td>
</tr>
<tr>
<td><p>-- INSERTA REG EN _EJECUCION</p>
<p>User::V_INSERT_FIN</p></td>
</tr>
</tbody>
</table>

### Tablas_Apoyo_NC20SQA.dtsx

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th>TRUNCATE TABLE dbo.NC20SQA</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>-- Tablas_Apoyo_NC20SQA_Extract</p>
<p><strong>SELECT Codigo, Tamano, Descripcion</strong></p>
<p><strong>FROM NEC.NC20SQA</strong></p>
<p><strong>WHERE Idioma = 'INGLES'</strong></p></td>
</tr>
<tr>
<td>Tablas_Apoyo_N20SQA_Update y Tablas_Apoyo_N20SQA_Delete</td>
</tr>
</tbody>
</table>

### Tablas_Apoyo_Tactividad.dtsx

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th>Truncate table dbo.Tactividad</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>-- Tablas_Apoyo_Tactividad_Extract</p>
<p><strong>SELECT
ESTABL,CODOBRA,TIPOPLA,TIPOFUN,ACTIVIDAD,TAREA,FASE,CENTREJ,ZONA,BLOQUE,MODULO,GRUCOSTE,PRODINT,ETAPA,AREAWK,FEINPRE,FEFINPRE,FEINLIM,FEFINLIM,SITING,SITAPROV,SITPRO,SITGESCAL,SITOTROS,DNISITING,DNISITAPRO,DNISITPRO,DNISITCAL,DNISITOTR,FECSITING,FECSITAPRO,FECSITPRO,FECSITCAL,FECSITOTR,SECUE</strong></p>
<p><strong>FROM NEC.TACTIVIDAD</strong></p>
<p><strong>WHERE CODOBRA=? AND ESTABL=?</strong></p></td>
</tr>
<tr>
<td>Tablas_Apoyo_Tactividad_Update y Tablas_Apoyo_Tactividad_Delete</td>
</tr>
</tbody>
</table>

### Tablas_Apoyo_taIdiomas.dtsx

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th>TRUNCATE TABLE DBO.taIdiomas</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>--Tablas_Apoyo_taIdiomas_Extract</p>
<p><strong>Select * from [dbo].[taIdiomas]</strong></p></td>
</tr>
<tr>
<td>Tablas_Apoyo_taIdiomas_Update y Tablas_Apoyo_taIdiomas_Delete</td>
</tr>
</tbody>
</table>

### Tablas_Apoyo_taOrigenes.dtsx

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th>TRUNCATE TABLE DBO.taOrigenes</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>--Tablas_Apoyo_taOrigenes_Extract</p>
<p><strong>Select * from [dbo].[taOrigenes]</strong></p></td>
</tr>
<tr>
<td>Tablas_Apoyo_taOrigenes_Update y Tablas_Apoyo_taOrigenes_Delete</td>
</tr>
</tbody>
</table>

### Tablas_Apoyo_taTiposDocumento.dtsx

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th>TRUNCATE TABLE taTiposDocumento</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>--Tablas_Apoyo_taTiposDocumentos_Extract</p>
<p><strong>Select * from [dbo].[taTiposDocumento]</strong></p></td>
</tr>
<tr>
<td>Limpiar Campos ejecuta el paquete _AtributosConfig.dtsx</td>
</tr>
<tr>
<td>Tablas_Apoyo_taTiposDocumentos_Update y
Tablas_Apoyo_taTiposDocumentos_Delete</td>
</tr>
</tbody>
</table>

### Tablas_Apoyo_taTiposEntidad.dtsx

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th>TRUNCATE TABLE taTiposEntidad</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>--Tablas_Apoyo_taTiposEntidad_Extract</p>
<p><strong>Select * from [dbo].[taTiposEntidad]</strong></p></td>
</tr>
<tr>
<td>Tablas_Apoyo_taTiposEntidad_Update y
Tablas_Apoyo_taTiposEntidad_Delete</td>
</tr>
</tbody>
</table>

### Tablas_Apoyo_taTiposSeccion.dtsx

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th>TRUNCATE TABLE taTiposSeccion</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>-- Tablas_Apoyo_taTiposSeccion_Extract</p>
<p><strong>Select * from [dbo].[taTiposSeccion]</strong></p></td>
</tr>
<tr>
<td>Tablas_Apoyo_taTiposSeccion_Update y
Tablas_Apoyo_taTiposSeccion_Delete</td>
</tr>
</tbody>
</table>

### Tablas_Apoyo_TDESPRO.dtsx

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th>TRUNCATE TABLE tdespro</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>-- Ejecutar TDESPRO Extract</p>
<p><strong>SELECT *</strong></p>
<p><strong>FROM NEC.TDESPRO</strong></p></td>
</tr>
<tr>
<td>Limpiar campos ejecuta el paquete _AtributosConfig.dtsx</td>
</tr>
<tr>
<td>Ejecutar TDESPRO Update y Ejecutar TDESPRO Delete</td>
</tr>
</tbody>
</table>

### Tablas_Apoyo_Tobras.dtsx

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th>Truncate table dbo.TObras</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>-- Tablas_Apoyo_Tobras_Extract</p>
<p><strong>SELECT CODOBRA, DIVISION, ESTABL, PROYECTO, TIPOPROD,
TIPOCONS, LINEACT,</strong></p>
<p><strong>DESTINO, TITAREA, RESPONS, SITUACO, FEINDES, FEFIDES,
FEINCON, FEFICON,</strong></p>
<p><strong>TICARGO, CTAALMC, PAGOROY, COTECNO, COCLIEN, PEDICLI,
FEPECLI, COSTADO,</strong></p>
<p><strong>CANON, DNI, SECUE06, SOCISAP, DIVISSAP, OBRASAP,</strong></p>
<p><strong>cast(BZNC.NCUDF06('NC06FV ','TOBRAS ',SECUE06,'NOMOBRA ',' ')
as char(100)) AS DESCRI,</strong></p>
<p><strong>cast(BZNC.NCUDF06('NC06FV ','TOBRAS ',SECUE06,'NOMOBRA
','INGLES') as char(100)) AS DESCRI2</strong></p>
<p><strong>FROM NEC.TOBRAS WHERE CODOBRA=? AND
ESTABL=?</strong></p></td>
</tr>
<tr>
<td>Limpiar campos ejecuta el paquete _AtributosConfig.dtsx</td>
</tr>
<tr>
<td>Tablas_Apoyo_Tobras_Update y Tablas_Apoyo_Tobras_Delete</td>
</tr>
</tbody>
</table>

## TBL

### TBL_B1_CONFIGURATION_ITEM.dtsx

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th>Truncate table TBL_B1_CONFIGURATION_ITEM</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>-- Extract B1_CONFIGURATION_ITEM</p>
<p><strong>select</strong></p>
<p><strong>case rtrim(psa.pedirp) when '' then NULL else psa.pedirp END
AS CI_NO,</strong></p>
<p><strong>CASE coalesce(RTRIM(psa.titulop),'') WHEN '' THEN 'NK' ELSE
psa.titulop END AS GENERIC_CI_DESCRIPTION,</strong></p>
<p><strong>CASE ltrim(RTRIM(psa.tipda)) WHEN '' THEN NULL ELSE
LEFT(psa.tipda, 3) END AS RI_CATEGORY,</strong></p>
<p><strong>CASE coalesce(RTRIM(psa.modefb),'') WHEN '' THEN 'NK' ELSE
psa.modefb END AS CONFIG_STATE_ID,</strong></p>
<p><strong>CASE coalesce(RTRIM(amf.marca200),'') WHEN '' THEN 'NK' ELSE
amf.marca200 END as SSI, '' AS STOCKCODE,</strong></p>
<p><strong>CASE RTRIM(left(ltrim(psa.obsdto), 2)) WHEN '' THEN NULL ELSE
left(ltrim(psa.obsdto), 2) END AS CI_TYPE,</strong></p>
<p><strong>psa.aplael AS AID_NO , psa.pedido, pida.buque,
psa.nseq</strong></p>
<p><strong>from coral.cora220 as pida</strong></p>
<p><strong>inner join coral.cora221 as psa on</strong></p>
<p><strong>pida.buque = psa.buque and</strong></p>
<p><strong>pida.pedido = psa.pedido</strong></p>
<p><strong>inner join (select buque, pedido, nseq, min(marca200) as
marca200</strong></p>
<p><strong>from coral.cora201 where tipagr='A'</strong></p>
<p><strong>group by buque, pedido, nseq) as amf on</strong></p>
<p><strong>psa.buque = amf.buque and</strong></p>
<p><strong>psa.pedido = amf.pedido and</strong></p>
<p><strong>psa.nseq = amf.nseq</strong></p>
<p><strong>inner join coral.cora200a as dgmf on</strong></p>
<p><strong>amf.buque = dgmf.buque and</strong></p>
<p><strong>amf.marca200 = dgmf.marca200</strong></p>
<p><strong>where pida.buque= ? and psa.pedirp &lt;&gt;
'';</strong></p></td>
</tr>
<tr>
<td>Update B1_CONFIGURATION_ITEM y Delete B1_CONFIGURATION_ITEM</td>
</tr>
</tbody>
</table>

### TBL_B2_CI_CI.dtsx

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th><p>Truncate table TBL_B2_CI_CI</p>
<p>Truncate table TBL_B2_CI_CI_INTERM</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p>-- Extract TBL_B2_CI_CI_INTERM</p>
<p><strong>select</strong></p>
<p><strong>case rtrim(psa.pedirp) when '' then NULL else psa.pedirp END
AS CI_NO,</strong></p>
<p><strong>'0000' AS FIND_NO,</strong></p>
<p><strong>CASE LENGth(ltrim(rtrim(mf.repere))) when 1 then
'CI89000'</strong></p>
<p><strong>else</strong></p>
<p><strong>case rtrim(mf.REPERE) when '' then 'CI89000' else mf.REPERE
END</strong></p>
<p><strong>end AS PARENT_CI_NO,</strong></p>
<p><strong>psa.cant as CI_QTY,</strong></p>
<p><strong>case when psa.cant &gt; 1 and coalesce (nmf.num, 0) = 1 then
'Y' else 'N' end AS FMMS_QUANTITY,</strong></p>
<p><strong>CASE RTRIM(left(ltrim(psa.caracte), 2)) WHEN '' THEN NULL
ELSE left(ltrim(psa.caracte), 2) END AS FACILITY_LEVEL,</strong></p>
<p><strong>CASE RTRIM(substr(ltrim(psa.caracte), 6, 2)) WHEN '' THEN
NULL ELSE substr(ltrim(psa.caracte), 6, 2) END AS
FACILITY_STATUS,</strong></p>
<p><strong>pida.buque, psa.pedido, psa.nseq</strong></p>
<p><strong>from coral.cora220 as pida</strong></p>
<p><strong>left join coral.cora221 as psa on</strong></p>
<p><strong>pida.buque = psa.buque and</strong></p>
<p><strong>pida.pedido = psa.pedido</strong></p>
<p><strong>inner join coral.cora201 as mfci on</strong></p>
<p><strong>psa.buque = mfci.buque and</strong></p>
<p><strong>psa.pedido = mfci.pedido and</strong></p>
<p><strong>psa.nseq = mfci.nseq and</strong></p>
<p><strong>mfci.tipagr = 'A'</strong></p>
<p><strong>inner join coral.marca as mf on</strong></p>
<p><strong>mfci.buque = mf.buque and</strong></p>
<p><strong>mfci.marca200 = mf.marcah</strong></p>
<p><strong>left join (</strong></p>
<p><strong>select amf.buque, amf.pedido, amf.nseq, count(*) as
num</strong></p>
<p><strong>from coral.cora201 as amf</strong></p>
<p><strong>where amf.tipagr = 'A'</strong></p>
<p><strong>group by amf.buque, amf.pedido, amf.nseq) as nmf
on</strong></p>
<p><strong>psa.buque = nmf .buque and</strong></p>
<p><strong>psa.pedido = nmf .pedido and</strong></p>
<p><strong>psa.nseq = nmf .nseq</strong></p>
<p><strong>where pida.buque = ? and psa.pedirp &lt;&gt;
'';</strong></p></td>
</tr>
<tr>
<td><p>-- Actualiza PARENT_CI_NO</p>
<p>UPDATE dbo.TBL_B2_CI_CI_INTERM</p>
<p>SET [PARENT_CI_NO] = (SELECT
DBO.ObtenerCMCBigrama([PARENT_CI_NO],'CI'))</p>
<p>where parent_ci_no &lt;&gt; 'CI89000'</p></td>
</tr>
<tr>
<td><p>-- EXTRACT B2_CI_CI (desde InterfacesDWH)</p>
<p>SELECT F.buque, f.ci_no, f.find_no, F.PARENT_CI_NO,</p>
<p>MAX(F.CI_QTY) AS CI_QTY, MAX(F.FMMS_QUANTITY) AS FMMS_QUANTITY,</p>
<p>MAX(F.FACILITY_LEVEL) AS FACILITY_LEVEL, MAX(F.FACILITY_STATUS) AS
FACILITY_STATUS</p>
<p>FROM dbo.TBL_B2_CI_CI_INTERM F</p>
<p>GROUP BY F.buque, f.ci_no, f.find_no, F.PARENT_CI_NO</p></td>
</tr>
<tr>
<td>Update TBL_B2_CI_CI y Delete TBL_B2_CI_CI</td>
</tr>
</tbody>
</table>

### TBL_B3_CI_CI_APPLICABLITY.dtsx

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th><p>Truncate table TBL_B3_CI_CI_APPLICABLITY</p>
<p>Truncate table TBL_B3_CI_CI_APPLICABLITY_INTERM</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p>-- Extract B3_CI_CI_APPLICABLITY_INTERM</p>
<p><strong>select distinct</strong></p>
<p><strong>case rtrim(psa.pedirp) when '' then NULL else psa.pedirp END
AS CI_NO,</strong></p>
<p><strong>'0000' AS FIND_NO,</strong></p>
<p><strong>CASE LENGth(ltrim(rtrim(mf.repere))) when 1 then
'CI89000'</strong></p>
<p><strong>else</strong></p>
<p><strong>case rtrim(mf.REPERE) when '' then 'CI89000' else mf.REPERE
END</strong></p>
<p><strong>end AS PARENT_CI_NO,</strong></p>
<p><strong>pida1.buque AS APPLICABILITY,</strong></p>
<p><strong>psa.pedido, pida.buque</strong></p>
<p><strong>from coral.cora220 as pida</strong></p>
<p><strong>inner join coral.cora221 as psa on</strong></p>
<p><strong>pida.buque = psa.buque and</strong></p>
<p><strong>pida.pedido = psa.pedido</strong></p>
<p><strong>inner join coral.cora201 as mfci on</strong></p>
<p><strong>psa.buque = mfci.buque and</strong></p>
<p><strong>psa.pedido = mfci.pedido and</strong></p>
<p><strong>psa.nseq = mfci.nseq and</strong></p>
<p><strong>mfci.tipagr = 'A'</strong></p>
<p><strong>inner join coral.marca as mf on</strong></p>
<p><strong>mfci.buque = mf.buque and</strong></p>
<p><strong>mfci.marca200 = mf.marcah</strong></p>
<p><strong>left join coral.cora220 as pida1</strong></p>
<p><strong>on pida1.pedido = pida.pedido</strong></p>
<p><strong>and pida1.buque in ('4516', '4517','4518','4519', '4520',
'4521', '4522', '4523', '4524', '4525', '4526', '4527')</strong></p>
<p><strong>where pida.buque = ? and psa.pedirp &lt;&gt;
''</strong></p></td>
</tr>
<tr>
<td><p>-- Actualiza PARENT_CI_NO</p>
<p>UPDATE dbo.TBL_B3_CI_CI_APPLICABLITY_INTERM</p>
<p>SET [PARENT_CI_NO] = (SELECT
DBO.ObtenerCMCBigrama([PARENT_CI_NO],'CI'))</p>
<p>where parent_ci_no &lt;&gt; 'CI89000'</p></td>
</tr>
<tr>
<td><p>-- Extract B3_CI_CI_APPLICABLITY (desde InterfacesDWH)</p>
<p>SELECT F.BUQUE, F.CI_NO, F.FIND_NO, F.PARENT_CI_NO,
F.APPLICABILITY</p>
<p>FROM dbo.TBL_B3_CI_CI_APPLICABLITY_INTERM F</p>
<p>GROUP BY F.BUQUE, F.CI_NO, F.FIND_NO, F.PARENT_CI_NO,
F.APPLICABILITY</p></td>
</tr>
<tr>
<td>Update B3_CI_CI_APPLICABLITY y Delete B3_CI_CI_APPLICABLITY</td>
</tr>
</tbody>
</table>

### TBL_B4_CI_COMPONENT.dtsx

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th><p>Truncate table TBL_B4_CI_COMPONENT_INTERM</p>
<p>Truncate table TBL_B4_CI_COMPONENT</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p>-- Extract B4_CI_COMPONENT ITERMEDIO</p>
<p><strong>select case rtrim(dgmf.marca200) when '' then NULL else
dgmf.marca200 END AS CI_NO,</strong></p>
<p><strong>'0000' AS FIND_NO,</strong></p>
<p><strong>case when coalesce(dgmf.nstock, '') = '' then</strong></p>
<p><strong>CASE RTRIM(dgmf.partfb) WHEN '' THEN NULL ELSE dgmf.partfb
END</strong></p>
<p><strong>else</strong></p>
<p><strong>CASE RTRIM(dgmf.nstock) WHEN '' THEN NULL ELSE dgmf.nstock
END</strong></p>
<p><strong>end AS COMPONENT_ID,</strong></p>
<p><strong>CASE RTRIM(left(dgmf.aplael, 1)) WHEN '' THEN '' ELSE
left(dgmf.aplael, 1) END as COMPONENT_CLASS,</strong></p>
<p><strong>dgmf.cant AS QTY_COMPONENTS,</strong></p>
<p><strong>case when dgmf.codenat = 'MPMI' then dgmf.cant else 0 end AS
QTY_HRM_ITEM,</strong></p>
<p><strong>mf.buque, mf.marcah</strong></p>
<p><strong>from coral.marca mf</strong></p>
<p><strong>left outer join coral.cora200a dgmf on</strong></p>
<p><strong>mf.buque = dgmf.buque and</strong></p>
<p><strong>mf.marcah = dgmf.marca200</strong></p>
<p><strong>where mf.buque = ? and dgmf.codenat in
('MPMI','COMPONENT');</strong></p></td>
</tr>
<tr>
<td><p>-- obtengo CI_NO</p>
<p>update dbo.TBL_B4_CI_COMPONENT_interm</p>
<p>set ci_no = (select dbo.ObtenerB4_CI_NO(ci_no))</p></td>
</tr>
<tr>
<td><p>-- borrar CI_NO vacios</p>
<p>delete TBL_B4_CI_COMPONENT_interm</p>
<p>where CI_NO = ''</p></td>
</tr>
<tr>
<td><p>--­ Extract DWH</p>
<p>select F.buque, f.ci_no, f.find_no, f.component_id,
f.component_class, MAX(TAB.QTY_COMPONENTS) as component,
MAX(TAB.QTY_HRM_ITEM) as hrm</p>
<p>FROM dbo.TBL_B4_CI_COMPONENT_INTERM F</p>
<p>INNER JOIN (</p>
<p>select A.buque, A.ci_no,</p>
<p>sum(QTY_COMPONENTS) as QTY_COMPONENTS, sum(QTY_HRM_ITEM) as
QTY_HRM_ITEM</p>
<p>FROM dbo.TBL_B4_CI_COMPONENT_INTERM A</p>
<p>group by A.buque, A.ci_no) AS TAB</p>
<p>ON TAB.BUQUE = F.BUQUE</p>
<p>AND TAB.CI_NO = F.CI_NO</p>
<p>GROUP BY F.buque, f.ci_no, f.find_no, f.component_id,
f.component_class</p></td>
</tr>
<tr>
<td>Update B4_CI_COMPONENTT y Delete B4_CI_COMPONENT</td>
</tr>
</tbody>
</table>

### TBL_B5_CI_DOCUMENT.dtsx

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th>Truncate table TBL_B5_CI_DOCUMENT</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>--Extract B5_CI_DOCUMENT</p>
<p><strong>select distinct</strong></p>
<p><strong>case rtrim(psa.pedirp) when '' THEN NULL ELSE PSA.PEDIRP END
AS CI_NO,</strong></p>
<p><strong>CASE mfdt.docno WHEN '' THEN NULL ELSE mfdt.docno END AS
FULL_DOCUMENT_NO,</strong></p>
<p><strong>case when n11.revision = '' then ' ' else n11.revision end as
REVISION_DOCUMENT,</strong></p>
<p><strong>psa.pedido, psa.nseq, pida.buque</strong></p>
<p><strong>from coral.cora220 as pida</strong></p>
<p><strong>inner join coral.cora221 as psa on</strong></p>
<p><strong>pida.buque = psa.buque and</strong></p>
<p><strong>pida.pedido = psa.pedido</strong></p>
<p><strong>inner join coral.cora201 as mfci on</strong></p>
<p><strong>psa.buque = mfci.buque and</strong></p>
<p><strong>psa.pedido = mfci.pedido and</strong></p>
<p><strong>psa.nseq = mfci.nseq</strong></p>
<p><strong>inner join coral.cora210 as mfdt on</strong></p>
<p><strong>mfci.buque = mfdt.buque and</strong></p>
<p><strong>mfci.marca200 = mfdt.marca200 and</strong></p>
<p><strong>mfci.tipagr = 'A'</strong></p>
<p><strong>inner join nec.nc10sq n10 on</strong></p>
<p><strong>n10.plano = mfdt.docno</strong></p>
<p><strong>inner join</strong></p>
<p><strong>(</strong></p>
<p><strong>select establ, codobra, plano, max(revision) as revision from
nec.nc11sq</strong></p>
<p><strong>where establ=? and codobra=? and sitoftec in ('V', 'E', 'S',
'L')</strong></p>
<p><strong>group by establ, codobra, plano</strong></p>
<p><strong>) as n11 on</strong></p>
<p><strong>n10.establ = n11.establ and</strong></p>
<p><strong>n10.codobra = n11.codobra and</strong></p>
<p><strong>n10.plano = n11.plano</strong></p>
<p><strong>where pida.buque = ? and n10.establ = ? and n10.codobra =
?</strong></p>
<p><strong>and n10.tipopla in ('C', 'H', 'K', 'N', 'R', 'S',
'T')</strong></p>
<p><strong>and psa.pedirp &lt;&gt; '';</strong></p></td>
</tr>
<tr>
<td>Update B5_CI_DOCUMENT y Delete B5_CI_DOCUMENT</td>
</tr>
</tbody>
</table>

### TBL_B6_CI_SA_SCHEDULED_AT.dtsx

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th>Truncate table TBL_B6_CI_SA_SCHEDULED_AT</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>-- Extract B6_CI_SA_SCHEDULED_AT (Excel Source)</p>
<p>--User::V_B6_SQL</p>
<p><strong>select '' as BUQUE</strong></p>
<p><strong>,LTRIM(RTRIM([F1])) AS SCHEDULED_AT</strong></p>
<p><strong>,'0000' AS FIND_NO</strong></p>
<p><strong>,LTRIM(RTRIM([F3])) AS STANDARD_ACT</strong></p>
<p><strong>,LTRIM(RTRIM([F4])) AS REVISION_SA</strong></p>
<p><strong>,LTRIM(RTRIM([F5])) AS APPLICABILITY</strong></p>
<p><strong>,[F6] AS JOB_PRIORI</strong></p>
<p><strong>,LTRIM(RTRIM([F7])) AS WORK_CENTRE</strong></p>
<p><strong>,LTRIM(RTRIM([F8])) AS TRIGGER</strong></p>
<p><strong>FROM [Table B6$]</strong></p>
<p><strong>where [F5] not like 'APPLICA%'</strong></p>
<p><strong>or [F1] not like '%SCHED%'</strong></p>
<p><strong>OR [F8] NOT LIKE '%TRIGG%'</strong></p></td>
</tr>
<tr>
<td>Update B6_CI_SA_SCHEDULED_AT y Deleted B6_CI_SA_SCHEDULED_AT</td>
</tr>
</tbody>
</table>

### TBL_B7_CI_COURSE.dtsx

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th>Truncate table TBL_B7_CI_COURSE</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>--Extract B7_CI_COURSE</p>
<p><strong>select</strong></p>
<p><strong>CASE RTRIM(PSA.PEDIRP) WHEN '' THEN NULL ELSE PSA.PEDIRP END
AS CI_NO,</strong></p>
<p><strong>CASE mfdt.docno WHEN '' THEN NULL ELSE mfdt.docno END AS
COURSE_NO,</strong></p>
<p><strong>case when n11.revision = '' then '0' else n11.revision end as
REVISION_COURSE,</strong></p>
<p><strong>psa.buque, psa.pedido, psa.nseq</strong></p>
<p><strong>from coral.cora220 as pida</strong></p>
<p><strong>inner join coral.cora221 as psa on</strong></p>
<p><strong>pida.buque = psa.buque and</strong></p>
<p><strong>pida.pedido = psa.pedido</strong></p>
<p><strong>inner join coral.cora201 as mfci on</strong></p>
<p><strong>psa.buque = mfci.buque and</strong></p>
<p><strong>psa.pedido = mfci.pedido and</strong></p>
<p><strong>psa.nseq = mfci.nseq</strong></p>
<p><strong>inner join coral.cora210 as mfdt on</strong></p>
<p><strong>mfci.buque = mfdt.buque and</strong></p>
<p><strong>mfci.marca200 = mfdt.marca200 and</strong></p>
<p><strong>mfci.tipagr = 'A'</strong></p>
<p><strong>inner join nec.nc10sq n10 on</strong></p>
<p><strong>n10.plano = mfdt.docno</strong></p>
<p><strong>inner join</strong></p>
<p><strong>(</strong></p>
<p><strong>select establ, codobra, plano, max(revision) as revision from
nec.nc11sq</strong></p>
<p><strong>where establ= ? and codobra= ? and sitoftec in ('V', 'E',
'S', 'L')</strong></p>
<p><strong>group by establ, codobra, plano</strong></p>
<p><strong>) as n11 on</strong></p>
<p><strong>n10.establ = n11.establ and</strong></p>
<p><strong>n10.codobra = n11.codobra and</strong></p>
<p><strong>n10.plano = n11.plano</strong></p>
<p><strong>where pida.buque = ? and n10.establ = ? and n10.codobra =
?</strong></p>
<p><strong>and n10.tipopla = 'X' and psa.pedirp &lt;&gt;
''</strong></p></td>
</tr>
<tr>
<td>Update B7_CI_COURSE y Delete B7_CI_COURSE</td>
</tr>
</tbody>
</table>

### TBL_B8_CI_OCCURRENCE.dtsx

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th>TRUNCATE TABLE dbo.TBL_B8_CI_OCCURRENCE</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>--EXTRACT B8</p>
<p>--User::V_SQL</p>
<p><strong>select case rtrim(psa.pedirp) when '' then NULL else
psa.pedirp END AS CI_NO, '0000' AS FIND_NO, ROW_NUMBER() over(partition
by psa.pedirp order by mfci.marca200) AS OCC_NO, case rtrim(mf.repere)
when '' then 'NK' ELSE mf.repere END as OCC_CMC,</strong></p>
<p><strong>CASE LENGth(ltrim(rtrim(mf.repere))) when 1 then 'CI89000'
else case rtrim(psa.pedirp) when '' then NULL else psa.pedirp END end AS
PARENT_CI_NO, CASE coalesce(mfci.marca200,'') WHEN '' THEN 'NK' ELSE
mfci.marca200 END AS PARENT_OCC_CMC,</strong></p>
<p><strong>mf.titulo AS OCC_DESCRIPTION, CASE RTRIM(dgmf.local) WHEN ''
THEN NULL ELSE dgmf.local END AS COMPARTMENT_CODE, left (mfci.marca200,
3) AS TSC, dgmf.sernfb AS SERIAL_NO, dlmf.obsmel AS BARCODE, dgmf.codlog
AS HRI,</strong></p>
<p><strong>'' AS SPECIAL_PLANT, PSA.PEDIDO, PSA.NSEQ, PSA.BUQUE from
coral.cora220 as pida inner join coral.cora221 as psa on pida.buque =
psa.buque and pida.pedido = psa.pedido inner join (select buque, pedido,
nseq, marca200 as marca200 from coral.cora201 where tipagr = 'A') as
mfci on</strong></p>
<p><strong>psa.buque = mfci.buque and psa.pedido = mfci.pedido and
psa.nseq = mfci.nseq inner join coral.marca as mf on mfci.buque =
mf.buque and mfci.marca200 = mf.marcah inner join coral.cora200a as dgmf
on mfci.buque = dgmf.buque and mfci.marca200 =
dgmf.marca200</strong></p>
<p><strong>left join coral.cora200l as dlmf on mfci.buque = dlmf.buque
and mfci.marca200 = dlmf.marca200 where pida.buque &gt;= '4516' and
pida.buque &lt;= '4527' and psa.pedirp &lt;&gt; '' WITH
UR</strong></p></td>
</tr>
<tr>
<td><p>ACTUALIZA CAMPOS TBL_B8_CI</p>
<p>select ci_no, OCC_CMC from dbo.TBL_B8_CI_OCCURRENCE</p>
<p>where occ_cmc &lt;&gt; 'NK' -&gt; y lo deja en
User::CI_NO_OBJ</p></td>
</tr>
<tr>
<td>Bucle RECORRE CI_NO usando User::CI_no y User::OCC_CMC desde
User::CI_NO_OBJ y ejecuta User::UPD</td>
</tr>
<tr>
<td>Update B8_CI_OCCURRENSE y Delete B8_CI_OCCURRENSE</td>
</tr>
</tbody>
</table>

### TBL_B11_SERIAL_NO_DOCUMENT.dtsx

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th>Truncate table TBL_B11_CI_SERIAL_NO_DOCUMENT</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>--Extract B11_CI_SERIAL_NO_DOCUMENT</p>
<p><strong>select distinct</strong></p>
<p><strong>case rtrim(dgmf.sernfb) when '' then NULL ELSE dgmf.sernfb
END AS SERIAL_NO,</strong></p>
<p><strong>CASE RTRIM(dgmf.fscm) WHEN '' THEN NULL ELSE dgmf.fscm END AS
CAGE,</strong></p>
<p><strong>CASE RTRIM(mfdt.docno) WHEN '' THEN NULL ELSE mfdt.docno END
AS FULL_DOCUMENT_NO,</strong></p>
<p><strong>n11.revision as REVISION_DOCUMENT,</strong></p>
<p><strong>pida.buque</strong></p>
<p><strong>from coral.cora220 as pida</strong></p>
<p><strong>inner join coral.cora221 as psa on</strong></p>
<p><strong>pida.buque = psa.buque and</strong></p>
<p><strong>pida.pedido = psa.pedido</strong></p>
<p><strong>inner join coral.cora201 as mfci on</strong></p>
<p><strong>psa.buque = mfci.buque and</strong></p>
<p><strong>psa.pedido = mfci.pedido and</strong></p>
<p><strong>psa.nseq = mfci.nseq</strong></p>
<p><strong>inner join coral.marca as mf on</strong></p>
<p><strong>mfci.buque = mf.buque and</strong></p>
<p><strong>mfci.marca200 = mf.marcah</strong></p>
<p><strong>inner join coral.cora200a as dgmf on</strong></p>
<p><strong>mfci.buque = dgmf.buque and</strong></p>
<p><strong>mfci.marca200 = dgmf.marca200</strong></p>
<p><strong>inner join coral.cora210 as mfdt on</strong></p>
<p><strong>mfci.buque = mfdt.buque and</strong></p>
<p><strong>mfci.marca200 = mfdt.marca200 and</strong></p>
<p><strong>mfci.tipagr = 'A'</strong></p>
<p><strong>inner join nec.nc10sq n10 on</strong></p>
<p><strong>n10.plano = mfdt.docno</strong></p>
<p><strong>inner join</strong></p>
<p><strong>(</strong></p>
<p><strong>select establ, codobra, plano, max(revision) as revision from
nec.nc11sq</strong></p>
<p><strong>where establ= ? and codobra between '0516' and '0527' and
sitoftec in ('V', 'E', 'S', 'L')</strong></p>
<p><strong>group by establ, codobra, plano</strong></p>
<p><strong>) as n11 on</strong></p>
<p><strong>n10.establ = n11.establ and</strong></p>
<p><strong>n10.codobra = n11.codobra and</strong></p>
<p><strong>n10.plano = n11.plano</strong></p>
<p><strong>where pida.buque = ? and pida.pedido &gt;=
'89000'</strong></p>
<p><strong>and n10.establ = ? and n10.codobra between '0516' and
'0527'</strong></p>
<p><strong>and dgmf.sernfb &lt;&gt; '';</strong></p></td>
</tr>
<tr>
<td>Update B11_SERIAL_NO_DOCUMENT y Delete B11_SERIAL_NO_DOCUMENT</td>
</tr>
</tbody>
</table>

### TBL_C1_COMPONENT.dtsx

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th>Truncate table TBL_C1_COMPONENT</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>--Extract C1_COMPONENT</p>
<p><strong>select</strong></p>
<p><strong>case when coalesce(dgmf.nstock, '') = '' then</strong></p>
<p><strong>CASE RTRIM(dgmf.partfb) WHEN '' THEN NULL ELSE dgmf.partfb
END</strong></p>
<p><strong>else</strong></p>
<p><strong>CASE RTRIM(dgmf.nstock) WHEN '' THEN NULL ELSE dgmf.nstock
END</strong></p>
<p><strong>end AS COMPONENT_ID,</strong></p>
<p><strong>CASE RTRIM(left(dgmf.aplael, 1)) WHEN '' THEN NULL ELSE
left(dgmf.aplael, 1) END as COMPONENT_CLASS,</strong></p>
<p><strong>max(case when dgmf.codenat = 'MPMI' and
ltrim(coalesce(mf.repere, '')) &lt;&gt; '' then substr (mf.repere, 6,
1)</strong></p>
<p><strong>else 'N' end) AS COMPONENT_TYPE,</strong></p>
<p><strong>max(mf.titulo) AS DESCRIPTION_COMPONENT,</strong></p>
<p><strong>'' AS SHELF_LIFE,</strong></p>
<p><strong>'' AS HMC, '' AS SPEC_PROMPT, '' AS SPEC_DATA,</strong></p>
<p><strong>0 AS UNIT_PRICE,</strong></p>
<p><strong>max(CASE RTRIM(dgmf.fscm) WHEN '' THEN NULL ELSE dgmf.fscm
END) AS CAGE, MAX(MF.BUQUE) AS BUQUE</strong></p>
<p><strong>from coral.marca mf</strong></p>
<p><strong>left outer join coral.cora200a dgmf on</strong></p>
<p><strong>mf.buque = dgmf.buque and</strong></p>
<p><strong>mf.marcah = dgmf.marca200</strong></p>
<p><strong>where mf.buque = ? and dgmf.codenat in
('MPMI','COMPONENT')</strong></p>
<p><strong>group by case when coalesce(dgmf.nstock, '') = ''
then</strong></p>
<p><strong>CASE RTRIM(dgmf.partfb) WHEN '' THEN NULL ELSE dgmf.partfb
END</strong></p>
<p><strong>else</strong></p>
<p><strong>CASE RTRIM(dgmf.nstock) WHEN '' THEN NULL ELSE dgmf.nstock
END</strong></p>
<p><strong>end,</strong></p>
<p><strong>CASE RTRIM(left(dgmf.aplael, 1)) WHEN '' THEN NULL ELSE
left(dgmf.aplael, 1) END</strong></p></td>
</tr>
<tr>
<td>Update C1_COMPONENT y Delete C1_COMPONENT</td>
</tr>
</tbody>
</table>

### TBL_C4_PART_NUMBER.dtsx

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th>Truncate table TBL_C4_PART_NUMBER</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>--Extract C4_PART_NUMBER</p>
<p><strong>select distinct</strong></p>
<p><strong>CASE RTRIM(dgmf.partfb) WHEN '' THEN NULL ELSE dgmf.partfb
END AS PART_NO,</strong></p>
<p><strong>CASE RTRIM(dgmf.fscm) WHEN '' THEN NULL ELSE dgmf.fscm END AS
CAGE,</strong></p>
<p><strong>max(mf.titulo) AS DESCRIPTION_COMPONENT,</strong></p>
<p><strong>max(dgmf.modefb) AS CONFIG_STATE_ID,</strong></p>
<p><strong>MAX(mf.buque) AS BUQUE</strong></p>
<p><strong>from coral.marca mf</strong></p>
<p><strong>left outer join coral.cora200a dgmf on</strong></p>
<p><strong>mf.buque = dgmf.buque and</strong></p>
<p><strong>mf.marcah = dgmf.marca200</strong></p>
<p><strong>where mf.buque = ? and dgmf.codenat in
('MPMI','COMPONENT')</strong></p>
<p><strong>group by CASE RTRIM(dgmf.partfb) WHEN '' THEN NULL ELSE
dgmf.partfb END,</strong></p>
<p><strong>CASE RTRIM(dgmf.fscm) WHEN '' THEN NULL ELSE dgmf.fscm
END</strong></p></td>
</tr>
<tr>
<td>Update C4_PART_NUMBER y Delete C4_PART_NUMBER</td>
</tr>
</tbody>
</table>

### TBL_C5_COMPONENT_PART_NUMBER.dtsx

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th>Truncate table TBL_C5_COMPONENT_PART_NUMBER</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>--Extract C5_COMPONENT_PART_NUMBER</p>
<p><strong>select distinct case when coalesce(dgmf.nstock, '') = ''
then</strong></p>
<p><strong>case rtrim(dgmf.partfb) when '' then null else dgmf.partfb
end</strong></p>
<p><strong>else</strong></p>
<p><strong>case rtrim(dgmf.nstock) when '' then null else dgmf.nstock
end</strong></p>
<p><strong>end AS COMPONENT_ID,</strong></p>
<p><strong>case rtrim(left(dgmf.aplael, 1)) when '' then null else
left(dgmf.aplael, 1) end as COMPONENT_CLASS,</strong></p>
<p><strong>case rtrim(dgmf.partfb) when '' then null else dgmf.partfb
end AS PART_NO,</strong></p>
<p><strong>case rtrim(dgmf.fscm) when '' then null else dgmf.fscm end AS
CAGE,</strong></p>
<p><strong>mf.buque</strong></p>
<p><strong>from coral.marca mf</strong></p>
<p><strong>left outer join coral.cora200a dgmf on</strong></p>
<p><strong>mf.buque = dgmf.buque and</strong></p>
<p><strong>mf.marcah = dgmf.marca200</strong></p>
<p><strong>where mf.buque = ? and dgmf.codenat in
('MPMI','COMPONENT');</strong></p></td>
</tr>
<tr>
<td>Update C5_COMPONENT_PART_NUMBER y Delete
C5_COMPONENT_PART_NUMBER</td>
</tr>
</tbody>
</table>

### TBL_C8_HRMI_TD.dtsx

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th>Truncate table TBL_C8_HRMI_TD</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>--Extract C8_HRMI_TD</p>
<p><strong>select</strong></p>
<p><strong>case rtrim(mf.repere) when '' then null else mf.repere end AS
UNIQUE_ITEM_ID,</strong></p>
<p><strong>CASE coalesce(RTRIM(dgmf.sernfb),'') WHEN '' THEN 'NK' ELSE
dgmf.sernfb END AS SERIAL_NO,</strong></p>
<p><strong>CASE RTRIM(dlmf.ffabri) WHEN '' THEN NULL ELSE dlmf.ffabri
END AS DATE_OF_MANUFACTURE,</strong></p>
<p><strong>CASE RTRIM(dlmf.finsta) WHEN '' THEN NULL ELSE dlmf.finsta
END AS TEST_DATE,</strong></p>
<p><strong>CASE coalesce(RTRIM(mfdt.doctec),'') WHEN '' THEN 'NK' ELSE
mfdt.doctec END AS TEST_CERTIFICATE_NO,</strong></p>
<p><strong>'LHDSPO' AS TEST_CERTIFICATE_LOCATION,</strong></p>
<p><strong>CASE coalesce(RTRIM(dlmf.aal),'') WHEN '' THEN 'NK' ELSE
dlmf.aal END AS TAGGED,</strong></p>
<p><strong>'' AS RIGGING_WARRANT,</strong></p>
<p><strong>'' AS SPECIAL_PLANT,</strong></p>
<p><strong>dgmf.codlog AS HRI,</strong></p>
<p><strong>mf.buque, mf.marcah</strong></p>
<p><strong>from coral.marca mf</strong></p>
<p><strong>left outer join coral.cora200a dgmf on</strong></p>
<p><strong>mf.buque = dgmf.buque and</strong></p>
<p><strong>mf.marcah = dgmf.marca200</strong></p>
<p><strong>left outer join coral.cora200l dlmf on</strong></p>
<p><strong>mf.buque = dlmf.buque and</strong></p>
<p><strong>mf.marcah = dlmf.marca200</strong></p>
<p><strong>left outer join (select distinct mfdt.buque, mfdt.marca200,
max(mfdt.docno) as doctec</strong></p>
<p><strong>from coral.cora210 as mfdt</strong></p>
<p><strong>inner join nec.nc10sq n10 on</strong></p>
<p><strong>n10.plano = mfdt.docno</strong></p>
<p><strong>where mfdt.buque = ? and n10.establ = ? and n10.codobra =
?</strong></p>
<p><strong>and n10.tipopla = '8'</strong></p>
<p><strong>group by mfdt.buque, mfdt.marca200</strong></p>
<p><strong>) as mfdt on</strong></p>
<p><strong>mf.buque = mfdt.buque and</strong></p>
<p><strong>mf.marcah = mfdt.marca200</strong></p>
<p><strong>where mf.buque = ? and dgmf.codenat = 'MPMI' and mf.repere
&lt;&gt; ''</strong></p></td>
</tr>
<tr>
<td>Update C8_HRMI_TD Y Delete C8_HRMI_TD</td>
</tr>
</tbody>
</table>

### TBL_C9_HRMI_OCCURRENCE_CBD.dtsx

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th><p>Truncate table TBL_C9_HRMI_OCCURRENCE_CBD</p>
<p>Truncate table TBL_C9_HRMI_OCCURRENCE_CBD_INTERM</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p>--Extract C9_HRMI_OCCURRENCE_CBD</p>
<p>--User::V_SQL</p>
<p><strong>select distinct case rtrim(mf.marcah) when '' then NULL else
mf.marcah END AS CI_NO, '0000' AS FIND_NO, case when
coalesce(dgmf.nstock, '') = '' then case rtrim(dgmf.partfb) when '' then
null else dgmf.partfb end else case rtrim(dgmf.nstock) when '' then null
else dgmf.nstock end</strong></p>
<p><strong>end AS COMPONENT_ID, case rtrim(left(dgmf.aplael, 1)) when ''
then null else left(dgmf.aplael, 1) end as COMPONENT_CLASS, CASE
RTRIM(mf.repere) WHEN '' THEN NULL ELSE mf.repere END AS UNIQUE_ITEM_ID,
case coalesce(rtrim(concat(concat(concat(concat(ntl.nt1, ' '), ntl.nt2),
' '), ntl.nt3)),'') when '' then 'NK' else
concat(concat(concat(concat(ntl.nt1, ' '), ntl.nt2), ' '), ntl.nt3) end
AS UNIQUE_ITEM_DESCRIPTION, CASE RTRIM(ntg.NT1) WHEN '' THEN NULL ELSE
rtrim(ntg.NT1) END AS COMPONENT_SUB_TYPE,</strong></p>
<p><strong>CASE coalesce(RTRIM(dlmf.obsmel),'') WHEN '' THEN 'NK' ELSE
dlmf.obsmel END AS BARCODE, case coalesce(rtrim(mf.marcah),'') when ''
then 'NK' else mf.marcah end AS SBR_NUMBER, CASE
coalesce(RTRIM(dtmf.poten),'') WHEN '' THEN 'NK' ELSE dtmf.poten END AS
TEST_PARAMETER, dtmf.amper AS WORKING_PARAMETER, CASE RTRIM(dgmf.local)
WHEN '' THEN NULL ELSE dgmf.local END AS COMPARTMENT_CODE, case when
dgmf.plano &lt;&gt; '' then concat(concat(dgmf.plano, '/'), dgmf.linea)
else '' end AS LOCATION_DRAWING, dgmf.itemdt AS PRID, case
coalesce(rtrim(mf.repere),'') when '' then 'NK' else mf.repere end as
PARENT_OCC_CMC, mf.buque, mf.marcah from coral.marca mf left outer join
coral.cora200a dgmf on mf.buque = dgmf.buque and mf.marcah =
dgmf.marca200 left outer join coral.cora200l dlmf on</strong></p>
<p><strong>mf.buque = dlmf.buque and mf.marcah = dlmf.marca200 left
outer join coral.cora200t dtmf on mf.buque = dtmf.buque and mf.marcah =
dtmf.marca200 left outer join coral.cora200n ntg on mf.buque = ntg.buque
and mf.marcah = ntg.marca200 and ntg.organ='BG' left outer join
coral.cora200n ntl on mf.buque = ntl.buque and mf.marcah = ntl.marca200
and ntl.organ='BL' where mf.buque in ('4516', '4517', '4518', '4519',
'4520', '4521', '4522', '4523', '4524', '4525', '4526', '4527') and
dgmf.codenat = 'MPMI';</strong></p></td>
</tr>
<tr>
<td><p>--obtengo CI_NO</p>
<p>update TBL_C9_HRMI_OCCURRENCE_CBD_INTERM</p>
<p>set ci_no = (select dbo.ObtenerB4_CI_NO(ci_no))</p></td>
</tr>
<tr>
<td><p>--borrar CI_NO vacios</p>
<p>delete TBL_C9_HRMI_OCCURRENCE_CBD_INTERM</p>
<p>where CI_NO = ''</p></td>
</tr>
<tr>
<td><p>--Extract C9 (en Interfaces DWH)</p>
<p>SELECT A.*, I.CONT</p>
<p>FROM TBL_C9_HRMI_OCCURRENCE_CBD_INTERM A</p>
<p>INNER JOIN</p>
<p>(SELECT C.BUQUE, C.CI_NO, C.FIND_NO, C.COMPONENT_ID,
C.COMPONENT_CLASS, C.UNIQUE_ITEM_ID , COUNT(*) AS CONT</p>
<p>FROM TBL_C9_HRMI_OCCURRENCE_CBD_INTERM C</p>
<p>GROUP BY C.BUQUE, C.CI_NO, C.FIND_NO, C.COMPONENT_ID,
C.COMPONENT_CLASS, C.UNIQUE_ITEM_ID) AS I</p>
<p>ON ISNULL(A.BUQUE, '') = ISNULL(I.BUQUE,'')</p>
<p>AND ISNULL(A.CI_NO, '') = ISNULL(I.CI_NO,'')</p>
<p>AND ISNULL(A.FIND_NO, '') = ISNULL(I.FIND_NO, '')</p>
<p>AND ISNULL(A.COMPONENT_ID, '') = ISNULL(I.COMPONENT_ID, '')</p>
<p>AND ISNULL(A.COMPONENT_CLASS, '') = ISNULL(I.COMPONENT_CLASS, '')</p>
<p>AND ISNULL(A.UNIQUE_ITEM_ID, '') = ISNULL(I.UNIQUE_ITEM_ID,
'')</p></td>
</tr>
<tr>
<td><p>--­BORRADO DE LOS NO MPMI</p>
<p>DELETE FROM [TBL_C9_HRMI_OCCURRENCE_CBD]</p>
<p>WHERE isnull(UNIQUE_ITEM_ID,'') = ''</p></td>
</tr>
<tr>
<td><p>ACTUALIZA CAMPOS TBL_B9 y lo guarda en User::CI_NO_OBJ para usar
en el bucle</p>
<p>SELECT CI_NO,SBR_NUMBER,PARENT_OCC_CMC FROM
dbo.TBL_C9_HRMI_OCCURRENCE_CBD</p></td>
</tr>
<tr>
<td>Bucel RECORRE CI_NO, usando User::CI_NO, User::V_SBR_NUMBER y
User::V_PARENT_OCC_CMC y ejecuta consulta en User::UPD</td>
</tr>
<tr>
<td>Update C9_HRMI_OCCURRENCE_CBD y Delete C9_HRMI_OCCURRENCE_CBD</td>
</tr>
</tbody>
</table>

### TBL_D1_DOCUMENT.dtsx

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th>Truncate table TBL_D1_DOCUMENT</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>-- Extract D1_DOCUMENT</p>
<p><strong>select</strong></p>
<p><strong>case rtrim(n10.plano) when '' then null else n10.plano end as
FULL_DOCUMENT_NO,</strong></p>
<p><strong>case when n11.revision = '' then ' ' else n11.revision end as
REVISION_DOCUMENT,</strong></p>
<p><strong>case rtrim(n10.tipopla) when '' then null else</strong></p>
<p><strong>case when n10.tipopla = 'B' then 'B'</strong></p>
<p><strong>when n10.tipopla = 'C' then 'C'</strong></p>
<p><strong>when n10.tipopla = 'K' then 'D'</strong></p>
<p><strong>when n10.tipopla = 'D' then 'D'</strong></p>
<p><strong>when n10.tipopla = 'N' then 'D'</strong></p>
<p><strong>when n10.tipopla = 'S' then 'D'</strong></p>
<p><strong>when n10.tipopla = 'P' then 'D'</strong></p>
<p><strong>when n10.tipopla = 'N' then 'D'</strong></p>
<p><strong>when n10.tipopla = 'F' then 'F'</strong></p>
<p><strong>when n10.tipopla = 'V' then 'H'</strong></p>
<p><strong>when n10.tipopla = 'Y' then 'I'</strong></p>
<p><strong>when n10.tipopla = 'L' then 'L'</strong></p>
<p><strong>when n10.tipopla = 'U' then 'P'</strong></p>
<p><strong>when n10.tipopla = 'R' then 'R'</strong></p>
<p><strong>when n10.tipopla = 'T' then 'S'</strong></p>
<p><strong>when n10.tipopla = 'H' then 'S'</strong></p>
<p><strong>when n10.tipopla = 'I' then 'X'</strong></p>
<p><strong>else n10.tipopla end</strong></p>
<p><strong>end as DOCUMENT_TYPE,</strong></p>
<p><strong>' ' as DOCUMENT_FUNCTION,</strong></p>
<p><strong>case</strong></p>
<p><strong>coalesce(rtrim(BZNC.NCUDF06('NC06FV','NC10SQ'
,n10.SECUE06,'DESPLAL','INGLES')),'') when '' then 'NK'</strong></p>
<p><strong>else BZNC.NCUDF06('NC06FV ','NC10SQ'
,n10.SECUE06,'DESPLAL','INGLES') end as
DESCRIPTION_DOCUMENT,</strong></p>
<p><strong>'' as SPONSOR,</strong></p>
<p><strong>case coalesce(rtrim(ip.ipval),'') when '' then 'NK' else
ip.ipval end as IP,</strong></p>
<p><strong>case n10.clasifi when '60' then 'R' when '70' then 'C' when
'90' then 'S' else 'U' end as SECURITY,</strong></p>
<p><strong>'NO' as CERTIFICATION_BASIS_RECORD,</strong></p>
<p><strong>'NO' as SHIP_SELECTED_RECORD,</strong></p>
<p><strong>n11.doccli as SECONDARY_DOCUMENT_NO,</strong></p>
<p><strong>'' as LMS_ID, '' as START_DOC, 'E' as
MEDIA_TYPE,</strong></p>
<p><strong>CASE RTRIM(' ') WHEN '' THEN NULL ELSE '' END as
SOURCE_ORG,</strong></p>
<p><strong>n10.establ, n10.codobra, n10.plano, n10.tipopla, n11.doccli,
n10.tarea, n10.seccion, n10.cencost</strong></p>
<p><strong>from nec.nc10sq n10</strong></p>
<p><strong>inner join nec.nc11sq n11</strong></p>
<p><strong>on n10.establ = n11.establ</strong></p>
<p><strong>and n10.codobra = n11.codobra</strong></p>
<p><strong>and n10.plano = n11.plano</strong></p>
<p><strong>left join</strong></p>
<p><strong>(select establ, codobra, plano, min(indref) as
ipval</strong></p>
<p><strong>from nec.nc13sq where establ= ? and codobra= ?</strong></p>
<p><strong>and tiporef = 'I' and tipind = 'EB' group by establ, codobra,
plano</strong></p>
<p><strong>) as IP</strong></p>
<p><strong>on n10.establ = IP.establ</strong></p>
<p><strong>and n10.codobra = IP.codobra</strong></p>
<p><strong>and n10.plano = IP.plano</strong></p>
<p><strong>where n10.establ = ? and n10.codobra = ? and n10.tipopla in
('C', 'H', 'K', 'N', 'R', 'S', 'T')</strong></p>
<p><strong>and n11.sitoftec in ('V', 'E', 'S', 'L');</strong></p></td>
</tr>
<tr>
<td>Update D1_DOCUMENT y Delete D1_DOCUMENT</td>
</tr>
</tbody>
</table>

### TBL_D2_DOCUMENT_IMAGES.dtsx

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th>Truncate table TBL_D2_DOCUMENT_IMAGES</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>-- Extract D2_DOCUMENT_IMAGES</p>
<p><strong>select</strong></p>
<p><strong>CASE RTRIM(plmf.docno) WHEN '' THEN NULL ELSE plmf.docno END
as FULL_DOCUMENT_NO,</strong></p>
<p><strong>case when n11.revision = '' then ' ' else n11.revision end as
REVISION_DOCUMENT,</strong></p>
<p><strong>0 as ITEM_NO,</strong></p>
<p><strong>'' as ITEM_REVISION_NO,</strong></p>
<p><strong>'' as FILENAME,</strong></p>
<p><strong>N10.ESTABL, N10.CODOBRA, N10.PLANO</strong></p>
<p><strong>from</strong></p>
<p><strong>(select distinct docno from coral.cora210</strong></p>
<p><strong>where buque = ?</strong></p>
<p><strong>) as plmf</strong></p>
<p><strong>inner join nec.nc10sq n10</strong></p>
<p><strong>on n10.plano = plmf.docno</strong></p>
<p><strong>inner join nec.nc11sq n11</strong></p>
<p><strong>on n10.establ = n11.establ</strong></p>
<p><strong>and n10.codobra = n11.codobra</strong></p>
<p><strong>and n10.plano = n11.plano</strong></p>
<p><strong>where n10.establ = ? and n10.codobra = ? and n10.tipopla in
('C', 'H', 'K', 'N', 'R', 'S', 'T')</strong></p>
<p><strong>and n11.sitoftec in ('V', 'E', 'S', 'L');</strong></p></td>
</tr>
<tr>
<td>Update D2_DOCUMENT_IMAGES y Delete D2_DOCUMENT_IMAGES</td>
</tr>
</tbody>
</table>

### TBL_D3_TBL_DOCUMENT_APPLICABLITY.dtsx

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th>Truncate table TBL_D3_DOCUMENT_APPLICABLITY</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>-- Extract D3_DOCUMENT_APPLICABLITY</p>
<p><strong>select</strong></p>
<p><strong>CASE RTRIM(plmf.docno) WHEN '' THEN NULL ELSE plmf.docno END
as FULL_DOCUMENT_NO,</strong></p>
<p><strong>n11.revision as REVISION_DOCUMENT,</strong></p>
<p><strong>case rtrim(n10.tipopla) when '' then null else</strong></p>
<p><strong>case when n10.tipopla = 'B' then 'B'</strong></p>
<p><strong>when n10.tipopla = 'C' then 'C'</strong></p>
<p><strong>when n10.tipopla = 'K' then 'D'</strong></p>
<p><strong>when n10.tipopla = 'D' then 'D'</strong></p>
<p><strong>when n10.tipopla = 'N' then 'D'</strong></p>
<p><strong>when n10.tipopla = 'S' then 'D'</strong></p>
<p><strong>when n10.tipopla = 'P' then 'D'</strong></p>
<p><strong>when n10.tipopla = 'N' then 'D'</strong></p>
<p><strong>when n10.tipopla = 'F' then 'F'</strong></p>
<p><strong>when n10.tipopla = 'V' then 'H'</strong></p>
<p><strong>when n10.tipopla = 'Y' then 'I'</strong></p>
<p><strong>when n10.tipopla = 'L' then 'L'</strong></p>
<p><strong>when n10.tipopla = 'U' then 'P'</strong></p>
<p><strong>when n10.tipopla = 'R' then 'R'</strong></p>
<p><strong>when n10.tipopla = 'T' then 'S'</strong></p>
<p><strong>when n10.tipopla = 'H' then 'S'</strong></p>
<p><strong>when n10.tipopla = 'I' then 'X'</strong></p>
<p><strong>else n10.tipopla end</strong></p>
<p><strong>end as DOCUMENT_TYPE,</strong></p>
<p><strong>CASE RTRIM(plmf.buq) WHEN '' THEN NULL ELSE plmf.buq END as
APPLICABILITY,</strong></p>
<p><strong>plmf.buque, n10.establ, n10.codobra, n10.plano</strong></p>
<p><strong>from</strong></p>
<p><strong>(select distinct a.buque, a.docno, b.buque as
buq</strong></p>
<p><strong>from coral.cora210 a</strong></p>
<p><strong>left join coral.cora210 b</strong></p>
<p><strong>on a.marca200 = b.marca200</strong></p>
<p><strong>and a.tipo = b.tipo</strong></p>
<p><strong>and a.docno = b.docno</strong></p>
<p><strong>and b.buque in ('4516', '4517', '4518', '4519', '4520',
'4521', '4522', '4523', '4524', '4525', '4526', '4527')</strong></p>
<p><strong>where a.buque = ?</strong></p>
<p><strong>) as plmf</strong></p>
<p><strong>inner join nec.nc10sq n10</strong></p>
<p><strong>on n10.plano = plmf.docno</strong></p>
<p><strong>inner join nec.nc11sq n11</strong></p>
<p><strong>on n10.establ = n11.establ</strong></p>
<p><strong>and n10.codobra = n11.codobra</strong></p>
<p><strong>and n10.plano = n11.plano</strong></p>
<p><strong>where n10.establ = ? and n10.codobra = ? and n10.tipopla in
('C', 'H', 'K', 'N', 'R', 'S', 'T')</strong></p>
<p><strong>and n11.sitoftec in ('V', 'E', 'S', 'L');</strong></p></td>
</tr>
<tr>
<td>Update D3_DOCUMENT_APPLICABLITY y Delete
D3_DOCUMENT_APPLICABLITY</td>
</tr>
</tbody>
</table>

### TBL_E1_STANDARD_ACTIVITY.dtsx

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th>TRUNCATE TABLE TBL_E1_STANDARD_ACTIVITY</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>-- Extract E1_STANDARD_ACTIVITY (Excel Source
//Fesrv053/interfaces_logs$/ALCM/CBS-Data-Packet.xls)</p>
<p>--User::V_E1_SQL</p>
<p>select '' AS BUQUE</p>
<p>,LTRIM(RTRIM([F1])) AS STANDARD_ACT</p>
<p>,LTRIM(RTRIM([F2])) AS REVISION_SA</p>
<p>,LTRIM(RTRIM([F3])) AS DESCRIPTION_SA</p>
<p>,LTRIM(RTRIM([F4])) AS PRODUCT_SYSTEM</p>
<p>,LTRIM(RTRIM([F5])) AS ACTIVITY_TYPE</p>
<p>,LTRIM(RTRIM([F6])) AS ACTIVITY_CAUSE</p>
<p>,LTRIM(RTRIM([F7])) AS MRC</p>
<p>,LTRIM(RTRIM([F8])) AS MAINTENANCE_LEVEL</p>
<p>,LEFT(LTRIM(RTRIM([F9])),5) AS ELAPSED_HRS</p>
<p>,LTRIM(RTRIM([F10])) AS SOURCE_ORG</p>
<p>,LTRIM(RTRIM([F11])) AS SPONSOR</p>
<p>FROM [Table E1$]</p>
<p>WHERE [F7] NOT LIKE '%MRC%' AND [F1] NOT LIKE '%STANDARD%'</p></td>
</tr>
<tr>
<td>Update E1_STANDARD_ACTIVITY y Delete E1_STANDARD_ACTIVITY</td>
</tr>
</tbody>
</table>

### TBL_E10_SA_INSTRUCTIONS.dtsx

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th>TRUNCATE TABLE TBL_E10_SA_INSTRUCTIONS</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>--EXTRACT TBL_E10_SA_INSTRUCTIONS (Excel source
//FESRV053/interfaces_logs$/ALCM/CBS-Data-Packet.xls)</p>
<p>--User::V_E1_SQL</p>
<p>select '' as BUQUE</p>
<p>,LTRIM(RTRIM([F1])) AS STANDARD_ACT</p>
<p>,LTRIM(RTRIM([F2])) AS REVISION_SA</p>
<p>,LTRIM(RTRIM([F3])) AS INSTRUCT</p>
<p>from [Table E10$]</p>
<p>WHERE [F2] NOT LIKE '%REVD%' AND [F1] NOT LIKE '%INST%'</p></td>
</tr>
<tr>
<td>UPDATE TBL_E10_SA_INSTRUCTIONS y DELETE TBL_E10_SA_INSTRUCTIONS</td>
</tr>
</tbody>
</table>

### TBL_E2_SA_APPLICABLITY.dtsx

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th>TRUNCATE TABLE TBL_E2_SA_APPLICABLITY</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>--EXTRACT E2_SA_APPLICABLITY (Excel Source
//FESRV053/interfaces_logs$/ALCM/CBS-Data-Packet.xls)</p>
<p>select '' as BUQUE</p>
<p>,RTRIM(LTRIM([F1])) AS STANDARD_ACT</p>
<p>,RTRIM(LTRIM([F2])) AS REVISION_SA</p>
<p>,RTRIM(LTRIM([F3])) AS APPLICABILITY</p>
<p>from [Table E2$]</p>
<p>WHERE ([F3] NOT LIKE '%APPLIC%' ) AND [F1] NOT LIKE '%TBL_%'</p></td>
</tr>
<tr>
<td><p>--Limpieza Con E1</p>
<p>DELETE TBL_E2_SA_APPLICABLITY</p>
<p>from dbo.TBL_E2_SA_APPLICABLITY A</p>
<p>where not exists</p>
<p>(select * from dbo.TBL_E1_STANDARD_ACTIVITY B</p>
<p>where A.BUQUE = B.BUQUE</p>
<p>AND A.STANDARD_ACTIVITY_NO = B.STANDARD_ACTIVITY_NO</p>
<p>AND A.REVISION_SA = B.REVISION_SA)</p></td>
</tr>
<tr>
<td>UPDATE E2_SA_APLLICABLITY y DELETE E2_SA_APLLICABLITY</td>
</tr>
</tbody>
</table>

### TBL_E3_SA_SA.dtsx

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th>TRUNCATE TABLE TBL_E3_SA_SA</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>--­EXTRACT E3_SA_SA (Excel SOurce
//FESRV053/interfaces_logs$/ALCM/CBS-Data-Packet.xls)</p>
<p>--User::V_E3_SQL</p>
<p>select '' as BUQUE</p>
<p>,LTRIM(RTRIM([F1])) AS STANDARD_ACT</p>
<p>,LTRIM(RTRIM([F2])) AS REVISION_SA</p>
<p>,LTRIM(RTRIM([F3])) AS RELATED_SA</p>
<p>,LTRIM(RTRIM([F4])) AS RELATED_REVISION</p>
<p>from [Table E3$]</p>
<p>WHERE [F2] NOT LIKE '%REV%' AND [F1] NOT LIKE '%SA_SA%'</p></td>
</tr>
<tr>
<td>UPDATE E3_SA_SA y DELETE E3_SA_SA</td>
</tr>
</tbody>
</table>

### TBL_E4_SA_CI_AFFECTED.dtsx

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th>TRUNCATE TABLE TBL_E4_SA_CI_AFFECTED</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>--Extract E4_SA_CI_AFFECTED (Excel SOurce
//FESRV053/interfaces_logs$/ALCM/CBS-Data-Packet.xls)</p>
<p>--User::V_E4_SQL</p>
<p>SELECT '' AS BUQUE</p>
<p>,RTRIM(LTRIM([F1])) AS STANDARD_ACT</p>
<p>,RTRIM(LTRIM([F2])) AS REVISION_SA</p>
<p>,RTRIM(LTRIM([F3])) AS AFFECTED</p>
<p>FROM [Table E4$]</p>
<p>WHERE [F2] NOT LIKE '%REV%' AND [F1] NOT LIKE '%AFFEC%'</p></td>
</tr>
<tr>
<td><p>--­Limpieza Con E1</p>
<p>DELETE dbo.TBL_E4_SA_CI_AFFECTED</p>
<p>from dbo.TBL_E4_SA_CI_AFFECTED A</p>
<p>where not exists</p>
<p>(select * from dbo.TBL_E1_STANDARD_ACTIVITY B</p>
<p>where A.BUQUE = B.BUQUE</p>
<p>AND A.STANDARD_ACTIVITY_NO = B.STANDARD_ACTIVITY_NO</p>
<p>AND A.REVISION_SA = B.REVISION_SA)</p></td>
</tr>
<tr>
<td>Update E4_SA_CI_AFFECTED y Delete E4_SA_CI_AFFECTED</td>
</tr>
</tbody>
</table>

### TBL_E5_SA_COMPONENT.dtsx

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th>TRUNCATE TABLE TBL_E5_SA_COMPONENT</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>--EXTRACT E5_SA_COMPONENT (Excel SOurce
//FESRV053/interfaces_logs$/ALCM/CBS-Data-Packet.xls)</p>
<p>--User::V_E5_SQL</p>
<p>SELECT '' as BUQUE</p>
<p>,LTRIM(RTRIM([F1])) AS STANDARD_ACT</p>
<p>,LTRIM(RTRIM([F2])) AS REVISION_SA</p>
<p>,LTRIM(RTRIM([F3])) AS COMPONENT_ID</p>
<p>,LTRIM(RTRIM([F4])) AS COMPONENT_CLASS</p>
<p>,LTRIM(RTRIM([F5])) AS UNIT_OF_USAGE</p>
<p>,0 AS QTY_USAGE</p>
<p>,LTRIM(RTRIM([F6])) AS ITEM</p>
<p>FROM [Table E5$]</p>
<p>where [F2] not like '%REV%' AND [F1] NOT LIKE '%COMP%'</p></td>
</tr>
<tr>
<td><p>--Limpieza Con E1</p>
<p>DELETE dbo.TBL_E5_SA_COMPONENT</p>
<p>from dbo.TBL_E5_SA_COMPONENT A</p>
<p>where not exists</p>
<p>(select * from dbo.TBL_E1_STANDARD_ACTIVITY B</p>
<p>where A.BUQUE = B.BUQUE</p>
<p>AND A.STANDARD_ACTIVITY_NO = B.STANDARD_ACTIVITY_NO</p>
<p>AND A.REVISION_SA = B.REVISION_SA)</p></td>
</tr>
<tr>
<td>UPDATED E5_SA_COMPONENT y DELETED E5_SA_COMPONENT</td>
</tr>
</tbody>
</table>

### TBL_E6_SA_REFERENCE_DOCUMENT.dtsx

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th>TRUNCATE TABLE TBL_E6_SA_REFERENCE_DOCUMENT</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>--EXTRACT E6_SA_REFERENCE_DOCUMENT (Excel Source
//Fesrv053/interfaces_logs$/ALCM/CBS-Data-Packet.xls)</p>
<p>--User::V_E6_SQL</p>
<p>SELECT '' AS BUQUE</p>
<p>,RTRIM(LTRIM([F1])) AS STANDAD_ACT</p>
<p>,RTRIM(LTRIM([F2])) AS REVISION_SA</p>
<p>,RTRIM(LTRIM([F3])) AS FULL_DOCUMENT</p>
<p>,RTRIM(LTRIM([F4])) AS REVISION_DOC</p>
<p>FROM [Table E6$]</p>
<p>where [F2] not like '%REV%' AND [F1] NOT LIKE '%REFER%'</p></td>
</tr>
<tr>
<td>UPDATED E6_SA_REFERENCE_DOCUMENT y DELETED
E6_SA_REFERENCE_DOCUMENT</td>
</tr>
</tbody>
</table>

### TBL_E7_SA_CHECKLIST_STATEMENT.dtsx

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th>TRUNCATE TABLE TBL_E7_SA_CHECKLIST_STATEMENT</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>--EXTRACT E7_SA (Excel Source
//Fesrv053/interfaces_logs$/ALCM/CBS-Data-Packet.xls)</p>
<p>--User::V_E7_SQL</p>
<p>select '' as BUQUE</p>
<p>,LTRIM(RTRIM([F1])) AS STANDARD_ACT</p>
<p>,LTRIM(RTRIM([F2])) AS REVISION_SA</p>
<p>,LTRIM(RTRIM([F3])) AS CHECKLIST_STAT</p>
<p>,LTRIM(RTRIM([F4])) AS CHECKLIST_MAND</p>
<p>from [Table E7$]</p>
<p>WHERE [F2] NOT LIKE '%REV%' AND [F1] NOT LIKE '%CHECK%'</p></td>
</tr>
<tr>
<td>UPDATE E7_SA y DELETE E7_SA</td>
</tr>
</tbody>
</table>

### TBL_E8_SCHEDULED_MAINTENANCE_TRIGGERS.dtsx

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th>TRUNCATE TABLE TBL_E8_SCHEDULED_MAINTENANCE_TRIGGERS</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>--EXTRACT E8_SCHEDULED_MAINTENANCE_TRIGGERS (Excel Source
//Fesrv053/interfaces_logs$/ALCM/CBS-Data-Packet.xls)</p>
<p>--User::V_E8_SQL</p>
<p>select '' as BUQUE</p>
<p>,LTRIM(RTRIM([F1])) AS SCHEDULE_AT</p>
<p>,LTRIM(RTRIM([F2])) AS FIND_NO</p>
<p>,LTRIM(RTRIM([F3])) AS STANDARD_ACT</p>
<p>,LTRIM(RTRIM([F4])) AS REVISION_SA</p>
<p>,LTRIM(RTRIM([F5])) AS TRIGGER_COD</p>
<p>,LTRIM(RTRIM([F6])) AS INTERVALL</p>
<p>,LEFT(LTRIM(RTRIM([F7])),1) AS PRIMARY_TRIGG</p>
<p>from [Table E8$]</p>
<p>WHERE [F4] NOT LIKE '%REV%' AND [F1] NOT LIKE '%SCHED%'</p></td>
</tr>
<tr>
<td>UPDATE E8_SCHEDULED_MAINTENANCE_TRIGGERS y DELETE
E8_SCHEDULED_MAINTENANCE_TRIGGERS</td>
</tr>
</tbody>
</table>

### TBL_E9_SCHEDULED_MAINTENANCE_APPLICABLITY.dtsx

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th>TRUNCATE TABLE TBL_E9_SCHEDULED_MAINTENANCE_APPLICABLITY</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>--EXTRACT E9_SCHEDULED_MAINTENANCE_APPLICABLITY (Excel Source
//Fesrv053/interfaces_logs$/ALCM/CBS-Data-Packet.xls)</p>
<p>--User::V_E9_SQL</p>
<p>select '' as BUQUE</p>
<p>,LTRIM(RTRIM([F1])) AS SCHEDULE_AT</p>
<p>,LTRIM(RTRIM([F2])) AS FIND_NO</p>
<p>,LTRIM(RTRIM([F3])) AS STANDARD_ACT</p>
<p>,LTRIM(RTRIM([F4])) AS APPLICAB</p>
<p>from [Table E9$]</p>
<p>WHERE [F3] NOT LIKE '%STAND%' AND [F1] NOT LIKE '%SCHED%'</p></td>
</tr>
<tr>
<td>UPDATE E9_SCHEDULED_MAINTENANCE_APPLICABLITY y DELETE
E9_SCHEDULED_MAINTENANCE_APPLICABLITY</td>
</tr>
</tbody>
</table>

### TBL_F1_COURSE.dtsx

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th>Truncate table TBL_F1_COURSE</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>--Extract F1_COURSE (DB2P)</p>
<p><strong>select</strong></p>
<p><strong>CASE RTRIM(n10.plano) WHEN '' THEN NULL ELSE n10.plano END as
COURSE_NO,</strong></p>
<p><strong>case when n11.revision = '' then '0' else n11.revision end as
REVISION_COURSE,</strong></p>
<p><strong>CASE coalesce(RTRIM(BZNC.NCUDF06('NC06FV ','NC10SQ'
,n10.SECUE06,'DESPLAL','INGLES')),'') WHEN '' THEN 'NK' ELSE
BZNC.NCUDF06('NC06FV ','NC10SQ' ,n10.SECUE06,'DESPLAL','INGLES')
END</strong></p>
<p><strong>as DESCRIPTION_COURSE,</strong></p>
<p><strong>'-' as LMS_ID, '' as EDP_NO, '' as SPONSOR,</strong></p>
<p><strong>n10.establ, n10.codobra, n10.plano</strong></p>
<p><strong>from nec.nc10sq n10</strong></p>
<p><strong>inner join nec.nc11sq n11</strong></p>
<p><strong>on n10.establ = n11.establ</strong></p>
<p><strong>and n10.codobra = n11.codobra</strong></p>
<p><strong>and n10.plano = n11.plano</strong></p>
<p><strong>where n10.establ = ? and n10.codobra = ? and n10.tipopla in
('X')</strong></p>
<p><strong>and n11.sitoftec in ('V', 'E', 'S', 'L');</strong></p></td>
</tr>
<tr>
<td>Update F1_COURSE y Delete F1_COURSE</td>
</tr>
</tbody>
</table>

### TBL_F2_COURSE_COMPONENT.dtsx

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th>Truncate table TBL_F2_COURSE_COMPONENT</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>--Extract F2_COURSE_COMPONENT (DB2P)</p>
<p><strong>select</strong></p>
<p><strong>CASE RTRIM(n10.plano) WHEN '' THEN NULL ELSE n10.plano END as
COURSE_NO,</strong></p>
<p><strong>CASE when n11.revision = '' then '0' else n11.revision end as
REVISION_COURSE,</strong></p>
<p><strong>case when coalesce(dgmf.nstock, '') = '' then</strong></p>
<p><strong>CASE RTRIM(dgmf.partfb) WHEN '' THEN NULL ELSE dgmf.partfb
END</strong></p>
<p><strong>else</strong></p>
<p><strong>CASE RTRIM(dgmf.nstock) WHEN '' THEN NULL ELSE dgmf.nstock
END</strong></p>
<p><strong>end AS COMPONENT_ID,</strong></p>
<p><strong>CASE RTRIM(left(dgmf.aplael, 1)) WHEN '' THEN NULL ELSE
left(dgmf.aplael, 1) END as COMPONENT_CLASS,</strong></p>
<p><strong>case when n12.unidcon = 'NO' then 'EA'</strong></p>
<p><strong>when n12.unidcon= 'M' THEN 'M'</strong></p>
<p><strong>when n12.unidcon= 'CM' THEN 'CMS'</strong></p>
<p><strong>when n12.unidcon= 'G' THEN 'GR'</strong></p>
<p><strong>when n12.unidcon= 'KG' THEN 'KG'</strong></p>
<p><strong>when n12.unidcon= 'L' THEN 'L'</strong></p>
<p><strong>when n12.unidcon= 'HR' THEN 'HR'</strong></p>
<p><strong>else n12.unidcon end as UNIT_OF_USAGE,</strong></p>
<p><strong>n12.cancont AS QTY_USAGE,</strong></p>
<p><strong>n10.establ, n10.codobra, n10.plano</strong></p>
<p><strong>from nec.nc10sq n10</strong></p>
<p><strong>inner join</strong></p>
<p><strong>(</strong></p>
<p><strong>select establ, codobra, plano, max(revision) as revision from
nec.nc11sq</strong></p>
<p><strong>where establ = ? and codobra = ? and sitoftec in ('V', 'E',
'S', 'L')</strong></p>
<p><strong>group by establ, codobra, plano</strong></p>
<p><strong>) as n11 on</strong></p>
<p><strong>n10.establ = n11.establ</strong></p>
<p><strong>and n10.codobra = n11.codobra</strong></p>
<p><strong>and n10.plano = n11.plano</strong></p>
<p><strong>inner join nec.nc12sq n12 on</strong></p>
<p><strong>n10.establ = n12.establ</strong></p>
<p><strong>and n10.codobra = n12.codobra</strong></p>
<p><strong>and n10.plano = n12.plano</strong></p>
<p><strong>and n12.tipoaco = 'X'</strong></p>
<p><strong>inner join nec.nc16sq n16 on</strong></p>
<p><strong>n12.establ = n16.establ</strong></p>
<p><strong>and n12.codobra = n16.codobra</strong></p>
<p><strong>and n12.plano = n16.plano</strong></p>
<p><strong>and n12.linea = n16.linea</strong></p>
<p><strong>and n16.tipodes = 'MF'</strong></p>
<p><strong>left outer join coral.cora200a dgmf on</strong></p>
<p><strong>dgmf.buque = ?</strong></p>
<p><strong>and dgmf.marca200 = n16.elemen</strong></p>
<p><strong>where n10.establ = ? and n10.codobra = ? and n10.tipopla in
('X') ;</strong></p></td>
</tr>
<tr>
<td>Update F2_COURSE_COMPONENT y Delete F2_COURSE_COMPONENT</td>
</tr>
</tbody>
</table>

### TBL_F3_COURSE_DOCUMENT.dtsx

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th>Truncate table TBL_F3_COURSE_DOCUMENT</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>--Extract F3_COURSE_DOCUMENT</p>
<p><strong>select</strong></p>
<p><strong>CASE RTRIM(n10.plano) WHEN '' THEN NULL ELSE n10.plano END as
COURSE_NO,</strong></p>
<p><strong>case when n11.revision = '' then '0' else n11.revision end as
REVISION_COURSE,</strong></p>
<p><strong>CASE RTRIM(n12.planoo) WHEN '' THEN NULL ELSE n12.planoo END
as FULL_DOCUMENT_NO,</strong></p>
<p><strong>case when n11Doc.revision = '' then '0' else n11Doc.revision
end as REVISION_DOCUMENT,</strong></p>
<p><strong>case when n12.unidcon = 'NO' then 'EA'</strong></p>
<p><strong>when n12.unidcon= 'M' THEN 'M'</strong></p>
<p><strong>when n12.unidcon= 'CM' THEN 'CMS'</strong></p>
<p><strong>when n12.unidcon= 'G' THEN 'GR'</strong></p>
<p><strong>when n12.unidcon= 'KG' THEN 'KG'</strong></p>
<p><strong>when n12.unidcon= 'L' THEN 'L'</strong></p>
<p><strong>when n12.unidcon= 'HR' THEN 'HR'</strong></p>
<p><strong>else n12.unidcon end as UNIT_OF_USAGE,</strong></p>
<p><strong>n12.cancont as QTY_USAGE,</strong></p>
<p><strong>N10.ESTABL, N10.CODOBRA, N10.PLANO</strong></p>
<p><strong>from nec.nc10sq n10</strong></p>
<p><strong>inner join</strong></p>
<p><strong>(</strong></p>
<p><strong>select establ, codobra, plano, max(revision) as revision from
nec.nc11sq</strong></p>
<p><strong>where establ =? and codobra =? and sitoftec in ('V', 'E',
'S', 'L')</strong></p>
<p><strong>group by establ, codobra, plano</strong></p>
<p><strong>) as n11 on</strong></p>
<p><strong>n10.establ = n11.establ</strong></p>
<p><strong>and n10.codobra = n11.codobra</strong></p>
<p><strong>and n10.plano = n11.plano</strong></p>
<p><strong>inner join nec.nc12sq n12 on</strong></p>
<p><strong>n10.establ = n12.establ</strong></p>
<p><strong>and n10.codobra = n12.codobra</strong></p>
<p><strong>and n10.plano = n12.plano</strong></p>
<p><strong>and n12.tipoaco = 'D'</strong></p>
<p><strong>inner join</strong></p>
<p><strong>(</strong></p>
<p><strong>select establ, codobra, plano, max(revision) as revision from
nec.nc11sq</strong></p>
<p><strong>where establ =? and codobra =? and sitoftec in ('V', 'E',
'S', 'L')</strong></p>
<p><strong>group by establ, codobra, plano</strong></p>
<p><strong>) as n11Doc on</strong></p>
<p><strong>n12.establ = n11Doc.establ</strong></p>
<p><strong>and n12.codobra = n11Doc.codobra</strong></p>
<p><strong>and n12.planoo = n11Doc.plano</strong></p>
<p><strong>where n10.establ = ? and n10.codobra =? and n10.tipopla in
('X') ;</strong></p></td>
</tr>
<tr>
<td>Update F3_COURSE_DOCUMENT y Delete F3_COURSE_DOCUMENT</td>
</tr>
</tbody>
</table>

## T_DB

### T_BD_CABADD

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">truncate table T_BD_CABADD</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>--Extract T_BD_CABADD (en EEA5)</p>
<p>select isnull(NUM_CABLE, 0) as NUM_CABLE ,NOMBRE_CABLE
,ltrim(isnull(PLANO, '')) as PLANO ,FECHA</p>
<p>,ltrim(isnull(REV, '')) as REV</p>
<p>, ltrim(isnull(DEFINITIVE,'')) as DEFINITIVE</p>
<p>from T_BD_CABADD</p>
<p>where fvolcado = ?</p></td>
</tr>
<tr>
<td style="text-align: left;">Update T_BD_CABADD</td>
</tr>
</tbody>
</table>

### T_BD_CABBORR

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Truncate table T_BD_CABBORR</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>--Extract T_BD_CABBORR</p>
<p>select isnull(NUM_CABLE, 0) as NUM_CABLE ,NOMBRE_CABLE
,ltrim(isnull(PLANO, '')) as PLANO ,FECHA</p>
<p>,ltrim(isnull(REV, '')) as REV , ltrim(isnull(DEFINITIVE, '')) as
DEFINITIVE</p>
<p>from t_bd_cabborr</p>
<p>where fvolcado = ?</p></td>
</tr>
<tr>
<td style="text-align: left;">--Update T_BD_CABBORR</td>
</tr>
</tbody>
</table>

### T_BD_CABLES

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">truncate table T_BD_CABLES</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>--Extract T_BD_CABLES</p>
<p>select NUM_CABLE ,NOMBRE_CABLE ,LONGITUD_CABLE ,NUMERO_CIRCUITOS
,PROCEDENCIA ,DESTINO ,CLASE ,MARGEN_1 ,MARGEN_2 ,TIPO_CABLE ,TACO
,PRENSA ,CONECTOR_A ,TIPO_CONECTOR_A ,TIPO_BACKSHELL_A</p>
<p>,CONECTOR_B ,TIPO_CONECTOR_B ,TIPO_BACKSHELL_B ,ltrim(isnull(PLANO,
'')) as PLANO</p>
<p>,FECHA ,ltrim(isnull(REV, '')) as REV ,ltrim(isnull(DEFINITIVE, ''))
as DEFINITIVE</p>
<p>From T_bd_cables</p>
<p>WHERE FVOLCADO = ?</p></td>
</tr>
<tr>
<td style="text-align: left;">Update T_BD_CABLES</td>
</tr>
</tbody>
</table>

### T_BD_CONEXIONADO

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">truncate table T_BD_CONEXIONADO</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>--Extract T_BD_CONEXIONADO</p>
<p>select</p>
<p>isnull(NUM_CABLE,0) as NUM_CABLE ,ltrim(isnull(NUM_CONDUCT, '')) as
NUM_CONDUCT</p>
<p>,TERM_A ,TERM_B ,OBSERVACIONES ,MARCA_1 ,MARCA_2 ,ltrim(isnull(PLANO,
'')) as PLANO</p>
<p>,FECHA ,ltrim(isnull(REV, '')) as REV, ltrim(isnull(DEFINITIVE, ''))
as DEFINITIVE</p>
<p>from T_BD_CONEXIONADO</p>
<p>WHERE FVOLCADO = ?</p></td>
</tr>
<tr>
<td style="text-align: left;">Update T_BD_CONEXIONADO</td>
</tr>
</tbody>
</table>

### T_BD_EQUIPOS

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Truncate table T_BD_EQUIPOS</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>--Extract T_BD_EQUIPOS</p>
<p>select</p>
<p>ltrim(isnull(CODIGO_LME, '')) as CODIGO_LME ,DESCRIPCION_LME
,DESCRIPCION_CAT</p>
<p>,OBSERV_DESCR ,TYPE_DESIGN ,LEVEL_CODE</p>
<p>,COPIC ,NUM_LOCAL ,DENOMINACION ,BLOQUE</p>
<p>,ZONA ,MARCA ,PLANO_RETIRADA_ALMACEN</p>
<p>,PLANO_DISPOSICION ,T_MASA ,M_MASA ,PESO</p>
<p>,PLANO_POLIN ,PLANTILLA ,ltrim(isnull(PLANO, '')) as PLANO ,FECHA</p>
<p>,ltrim(isnull(REV, '')) as REV ,ltrim(isnull(DEFINITIVE, '')) as
DEFINITIVE</p>
<p>from T_BD_EQUIPOS</p>
<p>WHERE FVOLCADO = ?</p></td>
</tr>
<tr>
<td style="text-align: left;">Updated T_BD_EQUIPOS</td>
</tr>
</tbody>
</table>

### T_BD_INDICCAB

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Truncate table T_BD_INDICCAB</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>-- Extract T_BD_INDICCAB</p>
<p>select isnull(NUM_CABLE, 0) as NUM_CABLE ,NOMBRE_CABLE
,INDICADOR_CABLE</p>
<p>,ltrim(isnull(PLANO, '')) as PLANO ,FECHA ,ltrim(isnull(REV, '')) as
REV</p>
<p>,ltrim(isnull(DEFINITIVE, '')) as DEFINITIVE</p>
<p>from T_BD_INDICCAB</p>
<p>WHERE FVOLCADO = ?</p></td>
</tr>
<tr>
<td style="text-align: left;">Updated T_BD_INDICCAB</td>
</tr>
</tbody>
</table>

### T_BD_NOTAS_CONEX

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Truncate table T_BD_NOTAS_CONEX</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>Extract T_BD_NOTAS_CONEX</p>
<p>SELECT isnull(NUM_CABLE, 0) as NUM_CABLE ,ltrim(isnull(NOTE_NUMBER,
'')) as NOTE_NUMBER</p>
<p>,ltrim(isnull(LINE_NUMBER, '')) as LINE_NUMBER ,NOTE_TEXT
,ltrim(isnull(PLANO, '')) as PLANO</p>
<p>,FECHA ,ltrim(isnull(REV, '')) as REV ,ltrim(isnull(DEFINITIVE, ''))
as DEFINITIVE</p>
<p>FROM T_BD_NOTAS_CONEX</p>
<p>WHERE FVOLCADO = ?</p></td>
</tr>
<tr>
<td style="text-align: left;">Update T_BD_NOTAS_CONEX</td>
</tr>
</tbody>
</table>

### T_BD_PCONTROL

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Truncate table T_BD_PCONTROL</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>Extract T_BD_PCONTROL</p>
<p>SELECT ltrim(isnull(PCONTROL, 0)) as PCONTROL ,BLOQUE_1 ,BLOQUE_2
,ZONA</p>
<p>,COORD_X ,COORD_Y ,COORD_Z</p>
<p>,PLANO_PCONTROL ,LOCALIZACION ,EMC</p>
<p>,ltrim(isnull(PLANO, '')) as PLANO ,FECHA ,ltrim(isnull(REV, '')) as
REV</p>
<p>, ltrim(isnull(DEFINITIVE, '')) as DEFINITIVE</p>
<p>FROM T_BD_PCONTROL</p>
<p>WHERE FVOLCADO = ?</p></td>
</tr>
<tr>
<td style="text-align: left;">Update T_BD_PCONTROL</td>
</tr>
</tbody>
</table>

### T_BD_RUTA

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Truncate table T_BD_RUTA</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>Extract T_BD_RUTA</p>
<p>SELECT isnull(NUM_CABLE, 0) as NUM_CABLE</p>
<p>,isnull(NUM_SECUENCIA_PT, 0) as NUM_SECUENCIA_PT</p>
<p>,NUMERO_ORDEN ,BLOQUE_PROC ,BLOQUE_DEST</p>
<p>,ltrim(isnull(PLANO, '')) as PLANO ,FECHA</p>
<p>,ltrim(isnull(REV, '')) as REV ,ltrim(isnull(DEFINITIVE, '')) as
DEFINITIVE</p>
<p>FROM T_BD_RUTA</p>
<p>WHERE FVOLCADO = ?</p></td>
</tr>
<tr>
<td style="text-align: left;">Update T_BD_RUTA</td>
</tr>
</tbody>
</table>

### T_BD_RUTBLOQ

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Truncate Table T_BD_RUTBLOQ</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>-- Extract T_BD_RUTBLOQ</p>
<p>SELECT isnull(NUM_CABLE, 0) as NUM_CABLE ,NOMBRE_CABLE
,NUM_TRAMOS</p>
<p>,isnull(ORDEN_TRAMO, 0) as ORDEN_TRAMO ,BLOQUE ,LONGITUD</p>
<p>,ltrim(isnull(PLANO, '')) as PLANO ,FECHA</p>
<p>,ltrim(isnull(REV, '')) as REV ,ltrim(isnull(DEFINITIVE, '')) as
DEFINITIVE</p>
<p>FROM T_BD_RUTBLOQ</p>
<p>WHERE FVOLCADO = ?</p></td>
</tr>
<tr>
<td style="text-align: left;">Update T_BD_RUTBLOQ</td>
</tr>
</tbody>
</table>

### T_DB_C_E_CabAdd

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">truncate table T_DB_C_E_CabAdd</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>Extract T_DB_C_E_CabAdd</p>
<p>SELECT CIRCUIT_NUMBER</p>
<p>,ISNULL(NUM_CABLE, 0 ) AS NUM_CABLE</p>
<p>,CABLE_TYPE</p>
<p>,LTRIM(ISNULL(DRAWING_NUMBER, '')) AS DRAWING_NUMBER</p>
<p>,LTRIM(ISNULL(DRAWING_REV, '')) AS DRAWING_REV</p>
<p>,LTRIM(ISNULL(DEFINITIVE, '')) AS DEFINITIVE</p>
<p>,CHECK_DATE</p>
<p>FROM [dbo].[T_DB_C_E_CABADD]</p>
<p>WHERE [FVOLCADO] = ?</p></td>
</tr>
<tr>
<td style="text-align: left;">Updated T_DB_C_E_CabAdd</td>
</tr>
</tbody>
</table>

### T_DB_C_E_CabDel

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">TRUNCATE TABLE T_DB_C_E_CabDel</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>Extract T_DB_C_E_CabDel</p>
<p>SELECT circuit_number</p>
<p>,ISNULL([NUM_CABLE], 0) AS NUM_CABLE</p>
<p>,[cable_type]</p>
<p>,[drawing_descrip]</p>
<p>,LTRIM(isnull(drawing_number, '')) as drawing_number</p>
<p>,LTRIM(isnull(drawing_rev, '' )) as drawing_rev</p>
<p>,LTRIM(isnull(definitive,'')) as definitive</p>
<p>,[check_date]</p>
<p>FROM [dbo].[T_DB_C_E_CabDel]</p>
<p>where FVOLCADO = ?</p></td>
</tr>
<tr>
<td style="text-align: left;">Update T_DB_C_E_CabDel</td>
</tr>
</tbody>
</table>

### T_DB_C_E_Cables

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">TRUNCATE TABLE T_DB_C_E_CABLES</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>Extract T_DB_C_E_CABLES</p>
<p>SELECT circuit_number</p>
<p>,ISNULL([num_cable], 0) AS num_cable</p>
<p>,[cable_type]</p>
<p>,[unit_a]</p>
<p>,[unit_b]</p>
<p>,[cables_in_parallel]</p>
<p>,[connector_type_a]</p>
<p>,[connector_type_b]</p>
<p>,[conn_rev]</p>
<p>,[sheet]</p>
<p>,[drawing_descrip]</p>
<p>,ltrim(isnull(drawing_number, '' )) as drawing_number</p>
<p>,ltrim(isnull([drawing_rev],'')) as drawing_rev</p>
<p>,ltrim(isnull([definitive], '')) as definitive</p>
<p>,[check_date]</p>
<p>FROM [dbo].[T_DB_C_E_Cables]</p>
<p>WHERE FVOLCADO = ?</p></td>
</tr>
<tr>
<td style="text-align: left;">Update T_DB_C_E_CABLES</td>
</tr>
</tbody>
</table>

### T_DB_C_E_Connections

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Truncate table T_DB_C_E_Connections</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>Extract T_DB_C_E_Connections</p>
<p>SELECT [circuit_number]</p>
<p>,ISNULL([NUM_CABLE], 0) AS NUM_CABLE</p>
<p>,ltrim(ISNULL([conductor],'')) AS conductor</p>
<p>,[CONDUCTOR_REV]</p>
<p>,[term_unit_a]</p>
<p>,[term_unit_b]</p>
<p>,[mark]</p>
<p>,[remarks]</p>
<p>,isnull([line_number], ' ') as line_number</p>
<p>,ltrim(ISNULL([drawing_number],'')) AS drawing_number</p>
<p>,ltrim(ISNULL([drawing_rev],'')) AS drawing_rev</p>
<p>,ltrim(ISNULL([definitive], '')) AS definitive</p>
<p>,[check_date]</p>
<p>FROM [dbo].[T_DB_C_E_Connections]</p>
<p>where fvolcado = ?</p></td>
</tr>
<tr>
<td style="text-align: left;">Update T_DB_C_E_Connectios</td>
</tr>
</tbody>
</table>

### T_DB_C_E_Equipment

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Truncate table T_DB_C_E_Equipment</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>Extract T_DB_C_E_Equipment</p>
<p>SELECT ltrim(ISNULL([mel_code],'')) AS mel_code</p>
<p>,[mel_description]</p>
<p>,[room_number]</p>
<p>,[room_description]</p>
<p>,ltrim(ISNULL([drawing_number],'')) AS drawing_number</p>
<p>,ltrim(ISNULL([drawing_rev],'')) AS drawing_rev</p>
<p>,ltrim(ISNULL([definitive],'')) AS definitive</p>
<p>,[check_date]</p>
<p>FROM [T_DB_C_E_Equipment]</p>
<p>WHERE FVOLCADO = ?</p></td>
</tr>
<tr>
<td style="text-align: left;">Update T_DB_C_E_Equipment</td>
</tr>
</tbody>
</table>

### T_DB_C_E_Notes

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">truncate table t_db_c_e_notes</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>Extract T_DB_C_E_Notes</p>
<p>SELECT [circuit_number]</p>
<p>,isnull([NUM_CABLE], 0) AS NUM_CABLE</p>
<p>,ltrim(ISNULL([note_number],'')) AS note_number</p>
<p>,[note_text]</p>
<p>,ltrim(ISNULL([drawing_number],'')) AS drawing_number</p>
<p>,ltrim(ISNULL([drawing_rev],'')) AS drawing_rev</p>
<p>,ltrim(ISNULL([definitive],'')) AS definitive</p>
<p>,[check_date]</p>
<p>FROM [dbo].[T_DB_C_E_Notes]</p>
<p>WHERE FVOLCADO = ?</p></td>
</tr>
<tr>
<td style="text-align: left;">Update T_DB_C_E_Notes</td>
</tr>
</tbody>
</table>

### T_DB_C_SC_CabAdd

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Truncate table T_DB_C_SC_CabAdd</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>Extract T_DB_C_SC_CabAdd</p>
<p>SELECT [CIRCUIT_NUMBER]</p>
<p>,ISNULL([NUM_CABLE], 0) AS NUM_CABLE</p>
<p>,[CABLE_NUMBER]</p>
<p>,[CABLE_TYPE]</p>
<p>,ltrim(ISNULL([DRAWING_NUMBER],'')) AS DRAWING_NUMBER</p>
<p>,ltrim(ISNULL([DRAWING_REV],'')) AS DRAWING_REV</p>
<p>,ltrim(ISNULL([DEFINITIVE],'')) AS DEFINITIVE</p>
<p>,[CHECK_DATE]</p>
<p>FROM [dbo].[T_DB_C_SC_CABADD]</p>
<p>where fvolcado = ?</p></td>
</tr>
<tr>
<td style="text-align: left;">Update T_DB_C_SC_CabAdd</td>
</tr>
</tbody>
</table>

### T_DB_C_SC_CabDel

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">truncate table T_DB_C_SC_CabDel</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>Extract T_DB_C_SC_CabDel</p>
<p>SELECT [CIRCUIT_NUMBER]</p>
<p>,ISNULL([NUM_CABLE], 0) AS NUM_CABLE</p>
<p>,[CABLE_NUMBER]</p>
<p>,[CABLE_TYPE]</p>
<p>,[DRAWING_DESCRIP]</p>
<p>,ltrim(ISNULL([DRAWING_NUMBER],'')) AS DRAWING_NUMBER</p>
<p>,ltrim(ISNULL([DRAWING_REV],'')) AS DRAWING_REV</p>
<p>,ltrim(ISNULL([DEFINITIVE],'')) AS DEFINITIVE</p>
<p>,[CHECK_DATE]</p>
<p>FROM [dbo].[T_DB_C_SC_CABDEL]</p>
<p>where fvolcado = ?</p></td>
</tr>
<tr>
<td style="text-align: left;">Update T_DB_C_SC_CabDel</td>
</tr>
</tbody>
</table>

### T_DB_C_SC_Cables

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">truncate table T_DB_C_SC_Cables</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>Extract T_DB_C_SC_CABLES</p>
<p>SELECT [CIRCUIT_NUMBER]</p>
<p>,[CABLE_NUMBER]</p>
<p>,[CABLE_TYPE]</p>
<p>,[UNIT_A]</p>
<p>,[UNIT_B]</p>
<p>,[CONNECT_UNIT_A]</p>
<p>,[CONNECT_UNIT_A_EXC]</p>
<p>,[CONNECT_UNIT_A_QTY]</p>
<p>,[CONNECT_TYPE_A]</p>
<p>,[CONNECT_UNIT_B]</p>
<p>,[CONNECT_UNIT_B_EXC]</p>
<p>,[CONNECT_UNIT_B_QTY]</p>
<p>,[CONNECT_TYPE_B]</p>
<p>,[BACKSHELL_UNIT_A]</p>
<p>,[BACKSHELL_UNIT_A_EXC]</p>
<p>,[BACKSHELL_UNIT_A_QTY]</p>
<p>,[BACKSHELL_UNIT_B]</p>
<p>,[BACKSHELL_UNIT_B_EXC]</p>
<p>,[BACKSHELL_UNIT_B_QTY]</p>
<p>,[INCIDENTIAL_EQ_A_1]</p>
<p>,[INCIDENTIAL_EQ_A_1_EXC]</p>
<p>,[INCIDENTIAL_EQ_A_1_QTY]</p>
<p>,[INCIDENTIAL_EQ_A_2]</p>
<p>,[INCIDENTIAL_EQ_A_2_EXC]</p>
<p>,[INCIDENTIAL_EQ_A_2_QTY]</p>
<p>,[INCIDENTIAL_EQ_A_3]</p>
<p>,[INCIDENTIAL_EQ_A_3_EXC]</p>
<p>,[INCIDENTIAL_EQ_A_3_QTY]</p>
<p>,[INCIDENTIAL_EQ_A_4]</p>
<p>,[INCIDENTIAL_EQ_A_4_EXC]</p>
<p>,[INCIDENTIAL_EQ_A_4_QTY]</p>
<p>,[INCIDENTIAL_EQ_B_1]</p>
<p>,[INCIDENTIAL_EQ_B_1_EXC]</p>
<p>,[INCIDENTIAL_EQ_B_1_QTY]</p>
<p>,[INCIDENTIAL_EQ_B_2]</p>
<p>,[INCIDENTIAL_EQ_B_2_EXC]</p>
<p>,[INCIDENTIAL_EQ_B_2_QTY]</p>
<p>,[INCIDENTIAL_EQ_B_3]</p>
<p>,[INCIDENTIAL_EQ_B_3_EXC]</p>
<p>,[INCIDENTIAL_EQ_B_3_QTY]</p>
<p>,[INCIDENTIAL_EQ_B_4]</p>
<p>,[INCIDENTIAL_EQ_B_4_EXC]</p>
<p>,[INCIDENTIAL_EQ_B_4_QTY]</p>
<p>,[INCIDENTIAL_EQ_X_1]</p>
<p>,[INCIDENTIAL_EQ_X_1_EXC]</p>
<p>,[INCIDENTIAL_EQ_X_1_QTY]</p>
<p>,[INCIDENTIAL_EQ_X_2]</p>
<p>,[INCIDENTIAL_EQ_X_2_EXC]</p>
<p>,[INCIDENTIAL_EQ_X_2_QTY]</p>
<p>,[INCIDENTIAL_EQ_X_3]</p>
<p>,[INCIDENTIAL_EQ_X_3_EXC]</p>
<p>,[INCIDENTIAL_EQ_X_3_QTY]</p>
<p>,[INCIDENTIAL_EQ_X_4]</p>
<p>,[INCIDENTIAL_EQ_X_4_EXC]</p>
<p>,[INCIDENTIAL_EQ_X_4_QTY]</p>
<p>,[INCIDENTIAL_EQ_X_5]</p>
<p>,[INCIDENTIAL_EQ_X_5_EXC]</p>
<p>,[INCIDENTIAL_EQ_X_5_QTY]</p>
<p>,[INCIDENTIAL_EQ_X_6]</p>
<p>,[INCIDENTIAL_EQ_X_6_EXC]</p>
<p>,[INCIDENTIAL_EQ_X_6_QTY]</p>
<p>,[ACTIVE_WIRES]</p>
<p>,[SHEET]</p>
<p>,[DRAWING_DESCRIP]</p>
<p>,ltrim(ISNULL([DRAWING_NUMBER],'')) AS DRAWING_NUMBER</p>
<p>,ltrim(ISNULL([DRAWING_REV],'')) AS DRAWING_REV</p>
<p>,ltrim(ISNULL([DEFINITIVE],'')) AS DEFINITIVE</p>
<p>,[CHECK_DATE]</p>
<p>,ISNULL([NUM_CABLE], 0) AS NUM_CABLE</p>
<p>FROM [dbo].[T_DB_C_SC_CABLES]</p>
<p>where fvolcado = ?</p></td>
</tr>
<tr>
<td style="text-align: left;">Update T_DB_C_SC_Cables</td>
</tr>
</tbody>
</table>

### T_DB_C_SC_Connections

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Truncate table T_DB_C_SC_Connections</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>Extract T_DB_C_SC_Connections</p>
<p>SELECT [circuit_number]</p>
<p>,ISNULL([NUM_CABLE], 0) AS NUM_CABLE</p>
<p>,[cable_number]</p>
<p>,[cond_group]</p>
<p>,[colour_cond]</p>
<p>,[line_number]</p>
<p>,[line_rev]</p>
<p>,[term_unit_a]</p>
<p>,[term_unit_b]</p>
<p>,[mark_unit_a]</p>
<p>,[mark_unit_b]</p>
<p>,[function]</p>
<p>,ltrim(ISNULL([drawing_number],'')) AS drawing_number</p>
<p>,ltrim(ISNULL([drawing_rev],'')) AS drawing_rev</p>
<p>,ltrim(ISNULL([definitive],'')) AS definitive</p>
<p>,[check_date]</p>
<p>FROM [dbo].[T_DB_C_SC_Connections]</p>
<p>WHERE FVOLCADO = ?</p></td>
</tr>
<tr>
<td style="text-align: left;">Update T_DB_C_SC_Connections</td>
</tr>
</tbody>
</table>

### T_DB_C_SC_Equipment

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Truncate table T_DB_C_SC_Equipment</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>Extract T_DB_C_SC_Equipment</p>
<p>SELECT ltrim(ISNULL([MEL_CODE],'')) AS MEL_CODE</p>
<p>,[MEL_DESCRIPTION]</p>
<p>,[TYPE_DESIGN]</p>
<p>,[LEVEL_CODE]</p>
<p>,[ROOM_NUMBER]</p>
<p>,[ROOM_DESCRIPTION]</p>
<p>,ltrim(ISNULL([DRAWING_NUMBER],'')) AS DRAWING_NUMBER</p>
<p>,ltrim(ISNULL([DRAWING_REV],'')) AS DRAWING_REV</p>
<p>,ltrim(ISNULL([DEFINITIVE],'')) AS DEFINITIVE</p>
<p>,[CHECK_DATE]</p>
<p>FROM [dbo].[T_DB_C_SC_EQUIPMENT]</p>
<p>WHERE FVOLCADO = ?</p></td>
</tr>
<tr>
<td style="text-align: left;">Update T_DB_C_SC_Equipment</td>
</tr>
</tbody>
</table>

### T_DB_C_SC_Notes

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Truncate table T_DB_C_SC_Notes</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>Extract T_DB_C_SC_Notes</p>
<p>SELECT [CIRCUIT_NUMBER]</p>
<p>,ISNULL([NUM_CABLE], 0) AS NUM_CABLE</p>
<p>,[CABLE_NUMBER]</p>
<p>,ltrim(ISNULL([NOTE_NUMBER],'')) AS NOTE_NUMBER</p>
<p>,ltrim(ISNULL([LINE_NUMBER],'')) AS LINE_NUMBER</p>
<p>,[NOTE_TEXT]</p>
<p>,ltrim(ISNULL([DRAWING_NUMBER],'')) AS DRAWING_NUMBER</p>
<p>,ltrim(ISNULL([DRAWING_REV],'')) AS DRAWING_REV</p>
<p>,ltrim(ISNULL([DEFINITIVE],'')) AS DEFINITIVE</p>
<p>,[CHECK_DATE]</p>
<p>FROM [dbo].[T_DB_C_SC_NOTES]</p>
<p>WHERE FVOLCADO = ?</p></td>
</tr>
<tr>
<td style="text-align: left;">Update T_DB_C_SC_Notes</td>
</tr>
</tbody>
</table>

### T_DB_R_E_CabAdd

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Truncate table T_DB_R_E_CabAdd</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>Extract T_DB_R_E_CabAdd</p>
<p>SELECT [circuit_number]</p>
<p>,ISNULL([NUM_CABLE], 0) AS NUM_CABLE</p>
<p>,[cable_type]</p>
<p>,ltrim(ISNULL([drawing_number],'')) AS drawing_number</p>
<p>,ltrim(ISNULL([drawing_rev],'')) AS drawing_rev</p>
<p>,ltrim(ISNULL([definitive],'')) AS definitive</p>
<p>,[check_date]</p>
<p>FROM [dbo].[T_DB_R_E_CabAdd]</p>
<p>Where fvolcado = ?</p></td>
</tr>
<tr>
<td style="text-align: left;">Update T_DB_R_E_CabAdd</td>
</tr>
</tbody>
</table>

### T_DB_R_E_CabDel

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Truncate table T_DB_R_E_CabDel</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>Extract T_DB_R_E_CabDel</p>
<p>SELECT [circuit_number]</p>
<p>,ISNULL([num_cable],0) AS NUM_CABLE</p>
<p>,[cable_type]</p>
<p>,[drawing_descrip]</p>
<p>,ltrim(ISNULL([drawing_number],'')) AS drawing_number</p>
<p>,ltrim(ISNULL([drawing_rev],'')) AS drawing_rev</p>
<p>,ltrim(ISNULL([definitive],'')) AS definitive</p>
<p>,[check_date]</p>
<p>FROM [dbo].[T_DB_R_E_CabDel]</p>
<p>where fvolcado = ?</p></td>
</tr>
<tr>
<td style="text-align: left;">Update T_DB_R_E_CabDel</td>
</tr>
</tbody>
</table>

### T_DB_R_E_Cables

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">truncate table T_DB_R_E_Cables</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>Extract T_DB_R_E_Cables</p>
<p>SELECT [circuit_number]</p>
<p>,ISNULL([num_cable], 0) AS num_cable</p>
<p>,[circuit_rev]</p>
<p>,[from_]</p>
<p>,[to_]</p>
<p>,[cable_length]</p>
<p>,[estim_calc_length]</p>
<p>,[init_length]</p>
<p>,[end_length]</p>
<p>,[cables_in_parallel]</p>
<p>,[acquisition]</p>
<p>,[seg_class]</p>
<p>,[confirmed_cable]</p>
<p>,[cable_type]</p>
<p>,[copic]</p>
<p>,[diameter]</p>
<p>,[mct_block]</p>
<p>,[normal_gland]</p>
<p>,[steel_gland]</p>
<p>,[wazu_gland]</p>
<p>,[screen_gland]</p>
<p>,[stdr_block]</p>
<p>,[emc_block]</p>
<p>,[drawing_descrip]</p>
<p>,ltrim(ISNULL([drawing_number],'')) AS drawing_number</p>
<p>,ltrim(ISNULL([drawing_rev],'')) AS drawing_rev</p>
<p>,ltrim(ISNULL([definitive],'')) AS definitive</p>
<p>,[check_date]</p>
<p>FROM [dbo].[T_DB_R_E_Cables]</p>
<p>where fvolcado = ?</p></td>
</tr>
<tr>
<td style="text-align: left;">Update T_DB_R_E_Cables</td>
</tr>
</tbody>
</table>

### T_DB_R_E_Equipment

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Truncate table T_DB_R_E_Equipment</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>Extract T_DB_R_E_Equipment</p>
<p>SELECT ltrim(ISNULL([mel_code],'')) AS mel_code</p>
<p>,[mel_description]</p>
<p>,[room_number]</p>
<p>,[room_description]</p>
<p>,ltrim(ISNULL([drawing_number],'')) AS drawing_number</p>
<p>,ltrim(ISNULL([drawing_rev],'')) AS drawing_rev</p>
<p>,ltrim(ISNULL([definitive],'')) AS definitive</p>
<p>,[check_date]</p>
<p>FROM [dbo].[T_DB_R_E_Equipment]</p>
<p>where fvolcado = ?</p></td>
</tr>
<tr>
<td style="text-align: left;">Update T_DB_R_E_Equipment</td>
</tr>
</tbody>
</table>

### T_DB_R_E_Route

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Truncate table T_DB_R_E_Route</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>Extract T_DB_R_E_Route</p>
<p>SELECT [circuit_number]</p>
<p>,ISNULL([NUM_CABLE], 0) AS NUM_CABLE</p>
<p>,ISNULL([sequence_num],0) AS sequence_num</p>
<p>,[check_point]</p>
<p>,[deck]</p>
<p>,[zone]</p>
<p>,[block_1]</p>
<p>,[block_2]</p>
<p>,ltrim(ISNULL([drawing_number],'')) AS drawing_number</p>
<p>,ltrim(ISNULL([drawing_rev],'')) AS drawing_rev</p>
<p>,ltrim(ISNULL([definitive],'')) AS definitive</p>
<p>,[check_date]</p>
<p>FROM [dbo].[T_DB_R_E_Route]</p>
<p>where fvolcado = ?</p></td>
</tr>
<tr>
<td style="text-align: left;">Update T_DB_R_E_Route</td>
</tr>
</tbody>
</table>

### T_DB_R_E_ROUTEBLOCK

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">truncate table T_DB_R_E_ROUTEBLOCK</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>EXTRACT T_DB_R_E_ROUTEBLOCK</p>
<p>SELECT [circuit_number]</p>
<p>,isnull([num_cable], 0) as num_cable</p>
<p>,[fragment_block]</p>
<p>,isnull([fragment_number], 0) as fragment_number</p>
<p>,[block]</p>
<p>,[cable_fragment_length]</p>
<p>,ltrim(ISNULL([drawing_number],'')) AS drawing_number</p>
<p>,ltrim(ISNULL([drawing_rev],'')) AS drawing_rev</p>
<p>,ltrim(ISNULL([definitive],'')) AS definitive</p>
<p>,[check_date]</p>
<p>,[fvolcado]</p>
<p>FROM [dbo].[T_DB_R_E_ROUTEBLOCK]</p>
<p>where fvolcado = ?</p></td>
</tr>
<tr>
<td style="text-align: left;">UPDATE T_DB_R_E_ROUTEBLOCK</td>
</tr>
</tbody>
</table>

### T_DB_R_SC_CabAdd

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Truncate table T_DB_R_SC_CabAdd</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>Extract T_DB_R_SC_CabAdd</p>
<p>SELECT [circuit_number]</p>
<p>,ISNULL([NUM_CABLE], 0) AS NUM_CABLE</p>
<p>,ltrim(ISNULL([cable_type],'')) AS cable_type</p>
<p>,ltrim(ISNULL([drawing_number],'')) AS drawing_number</p>
<p>,ltrim(ISNULL([drawing_rev],'')) AS drawing_rev</p>
<p>,ltrim(ISNULL([definitive],'')) AS definitive</p>
<p>,[check_date]</p>
<p>FROM [dbo].[T_DB_R_SC_CabAdd]</p>
<p>WHERE FVOLCADO = ?</p></td>
</tr>
<tr>
<td style="text-align: left;">Update T_DB_R_SC_CabAdd</td>
</tr>
</tbody>
</table>

### T_DB_R_SC_CabDel

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Truncate table T_DB_R_SC_CabDel</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>Extract T_DB_R_SC_CabDel</p>
<p>SELECT [circuit_number]</p>
<p>,ISNULL([NUM_CABLE], 0) AS NUM_CABLE</p>
<p>,[cable_type]</p>
<p>,[drawing_descrip]</p>
<p>,ltrim(ISNULL([drawing_number],'')) AS drawing_number</p>
<p>,ltrim(ISNULL([drawing_rev],'')) AS drawing_rev</p>
<p>,ltrim(ISNULL([definitive],'')) AS definitive</p>
<p>,[check_date]</p>
<p>FROM [dbo].[T_DB_R_SC_CabDel]</p>
<p>where fvolcado = ?</p></td>
</tr>
<tr>
<td style="text-align: left;">Updatet T_DB_R_SC_CabDel</td>
</tr>
</tbody>
</table>

### T_DB_R_SC_Cables

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Truncate table T_DB_R_SC_Cables</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>extract T_DB_R_SC_Cables</p>
<p>SELECT [circuit_number]</p>
<p>,isnull([num_cable], 0) as num_cable</p>
<p>,[cable_number]</p>
<p>,[circuit_rev]</p>
<p>,[from_]</p>
<p>,[to_]</p>
<p>,[cable_length]</p>
<p>,[estim_calc_length]</p>
<p>,[init_length]</p>
<p>,[end_length]</p>
<p>,[acquisition]</p>
<p>,[seg_class]</p>
<p>,[cable_indicator]</p>
<p>,[cable_type]</p>
<p>,[copic]</p>
<p>,[diameter]</p>
<p>,[mct_block]</p>
<p>,[nylon_gland]</p>
<p>,[steel_gland]</p>
<p>,[wazu_gland]</p>
<p>,[screen_gland]</p>
<p>,[stdr_block]</p>
<p>,[emc_block]</p>
<p>,[drawing_descrip]</p>
<p>,ltrim(ISNULL([drawing_number],'')) AS drawing_number</p>
<p>,ltrim(ISNULL([drawing_rev],'')) AS drawing_rev</p>
<p>,ltrim(ISNULL([definitive],'')) AS definitive</p>
<p>,[check_date]</p>
<p>FROM [dbo].[T_DB_R_SC_Cables]</p>
<p>where fvolcado = ?</p></td>
</tr>
<tr>
<td style="text-align: left;">Update T_DB_R_SC_Cables</td>
</tr>
</tbody>
</table>

### T_DB_R_SC_Equipment

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Truncate table T_DB_R_SC_Equipment</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>Extract T_DB_R_SC_Equipment</p>
<p>SELECT ltrim(ISNULL([mel_code],'')) AS mel_code</p>
<p>,[mel_description]</p>
<p>,[type_design]</p>
<p>,[level_code]</p>
<p>,[room_number]</p>
<p>,[room_description]</p>
<p>,ltrim(ISNULL([drawing_number],'')) AS drawing_number</p>
<p>,ltrim(ISNULL([drawing_rev],'')) AS drawing_rev</p>
<p>,ltrim(ISNULL([definitive],'')) AS definitive</p>
<p>,[check_date]</p>
<p>FROM [dbo].[T_DB_R_SC_Equipment]</p>
<p>where fvolcado = ?</p></td>
</tr>
<tr>
<td style="text-align: left;">Update T_DB_R_SC_Equipment</td>
</tr>
</tbody>
</table>

### T_DB_R_SC_Route

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Truncate table T_DB_R_SC_Route</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>Extract T_DB_R_SC_Route</p>
<p>SELECT [circuit_number]</p>
<p>,ISNULL([NUM_CABLE], 0) AS NUM_CABLE</p>
<p>,ISNULL([sequence_num],0) AS sequence_num</p>
<p>,[check_point]</p>
<p>,[deck]</p>
<p>,[zone]</p>
<p>,[block_1]</p>
<p>,[block_2]</p>
<p>,ltrim(ISNULL([drawing_number],'')) AS drawing_number</p>
<p>,ltrim(ISNULL([drawing_rev],'')) AS drawing_rev</p>
<p>,ltrim(ISNULL([definitive],'')) AS definitive</p>
<p>,[check_date]</p>
<p>FROM [dbo].[T_DB_R_SC_Route]</p>
<p>where fvolcado = ?</p></td>
</tr>
<tr>
<td style="text-align: left;">Update T_DB_R_SC_Route</td>
</tr>
</tbody>
</table>

### T_DB_R_SC_ROUTEBLOCK

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">truncate table T_DB_R_SC_ROUTEBLOCK</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>EXTRACT T_DB_R_SC_ROUTEBLOCK</p>
<p>SELECT [circuit_number]</p>
<p>,isnull([num_cable], 0) as num_cable</p>
<p>,[fragment_block]</p>
<p>,isnull([fragment_number], 0) as fragment_number</p>
<p>,[block]</p>
<p>,[cable_fragment_length]</p>
<p>,ltrim(ISNULL([drawing_number],'')) AS drawing_number</p>
<p>,ltrim(ISNULL([drawing_rev],'')) AS drawing_rev</p>
<p>,ltrim(ISNULL([definitive],'')) AS definitive</p>
<p>,[check_date]</p>
<p>,[fvolcado]</p>
<p>FROM [dbo].[T_DB_R_SC_ROUTEBLOCK]</p>
<p>where fvolcado = ?</p></td>
</tr>
<tr>
<td style="text-align: left;">UPDATE T_DB_R_SC_ROUTEBLOCK</td>
</tr>
</tbody>
</table>

### T_DBCatal

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Truncate table T_DBCatal</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>Extract T_DBCatal</p>
<p>SELECT [marca]</p>
<p>,ltrim(ISNULL([codigo],'')) AS codigo</p>
<p>,[unidad]</p>
<p>,[descripcion]</p>
<p>,[peso]</p>
<p>,[plantilla]</p>
<p>,[observ_descr]</p>
<p>,[description]</p>
<p>FROM [T_DBCatal]</p>
<p>where fvolcado = ?</p></td>
</tr>
<tr>
<td style="text-align: left;">Update T_DBCatal</td>
</tr>
</tbody>
</table>

### T_DBDesign

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Truncate table T_DBDesign</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>Extract T_DBDesign</p>
<p>SELECT ltrim(ISNULL([design_name],'')) AS design_name</p>
<p>,[plano]</p>
<p>,[descripcion]</p>
<p>FROM [dbo].[T_DBDesign]</p>
<p>where fvolcado = ?</p></td>
</tr>
<tr>
<td style="text-align: left;">Update T_DBDesign</td>
</tr>
</tbody>
</table>

### T_DBLme

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Truncate table T_DBLme</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>Extract T_DBLme</p>
<p>SELECT distinct ltrim(ISNULL([codigo_lme],'')) AS codigo_lme</p>
<p>,[descripcion]</p>
<p>,[num_local]</p>
<p>,[bloque]</p>
<p>,[plano_compra]</p>
<p>,[plano_disposicion]</p>
<p>,[copic]</p>
<p>,[gdc]</p>
<p>,[T_masa]</p>
<p>,[m_masa]</p>
<p>,[num_T_masa]</p>
<p>,[Plano_T_masa]</p>
<p>,ltrim(isnull([plano_retirada_almacen], '')) as
plano_retirada_almacen</p>
<p>,[zona]</p>
<p>FROM [T_DBLme]</p>
<p>where fvolcado = ?</p></td>
</tr>
<tr>
<td style="text-align: left;">Update T_DBLme</td>
</tr>
</tbody>
</table>

### T_DBLocal

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Truncate table T_DBLocal</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>Extract T_DBLocal</p>
<p>SELECT ltrim(ISNULL([num_local],'')) AS num_local</p>
<p>,[denominacion]</p>
<p>FROM [dbo].[T_DBLocal]</p>
<p>where fvolcado = ?</p></td>
</tr>
<tr>
<td style="text-align: left;">Update T_DBLocal</td>
</tr>
</tbody>
</table>

### T_DBPcontrol

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Truncate table T_DBPcontrol</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>Extract T_DBPcontrol</p>
<p>SELECT [buque]</p>
<p>,[cubierta]</p>
<p>,[zona]</p>
<p>,[numero_orden]</p>
<p>,[coord_x]</p>
<p>,[coord_y]</p>
<p>,[coord_z]</p>
<p>,[estanco]</p>
<p>,[tipo_estanq]</p>
<p>,[bastidor]</p>
<p>,[saturacion]</p>
<p>,[long_bandeja]</p>
<p>,[mm_disponibles]</p>
<p>,[subida_bajada]</p>
<p>,[localizacion]</p>
<p>,[principal]</p>
<p>,[Bloque_1]</p>
<p>,[bloque_2]</p>
<p>,[mslink]</p>
<p>,[superf_area_prensa]</p>
<p>,[emc]</p>
<p>FROM [dbo].[T_DBPcontrol]</p>
<p>where fvolcado = ?</p></td>
</tr>
<tr>
<td style="text-align: left;">Update T_DBPcontrol</td>
</tr>
</tbody>
</table>
