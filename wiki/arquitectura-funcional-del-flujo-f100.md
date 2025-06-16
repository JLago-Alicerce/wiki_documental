---
source: EstadoActualPlataformaBBD_V0306_10_32.md
doc_source: EstadoActualPlataformaBBD_V0306_10_32.docx
created: 2025-06-15T23:47:26.859159
---
<div class="fragment-meta">source: EstadoActualPlataformaBBD_V0306_10_32.md | doc: EstadoActualPlataformaBBD_V0306_10_32.docx | created: 2025-06-15T23:47:26.859159</div>

# 4. Arquitectura funcional del flujo F100 

<img src="C:/PROYECTOS_GPT/wiki_documental/wiki/assets/media/image5.jpg"
style="width:9.39375in;height:4.075in" />

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
<p>MASQL20142/NECORANET.InterfacesAWD_PEC</p>
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

- MASQL2014/SQLTURK (Turquía)

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

- MA SQL20221/SQLTURK y /SQLNORWAY

Estas instancias están diseñadas para soportar entornos funcionales,
pruebas, publicaciones a clientes externos o acceso desde plataformas
como Power BI.

### 4.4.1. Integración ampliada del modelo funcional – Foran /<-/> Windchill /<-/> SAP

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

<img src="C:/PROYECTOS_GPT/wiki_documental/wiki/assets/media/image4.jpg"
style="width:7.18472in;height:2.86667in" />

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

