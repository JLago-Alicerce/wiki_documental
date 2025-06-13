---
source: DTI-MIGRACION-HOST-R03.md
doc_source: DTI-MIGRACION-HOST-R03.docx
created: 2025-06-13T05:51:57.513386
---
# Estrategia migración de datos

## Planteamiento

Se plantea la creación de un esquema de tablas en SQL Server idéntico al
existente actualmente en Necora. El volcado de datos se hará de la forma
más directa posible y con el menor número de transformaciones. Solo se
realizarán los cambios necesarios para poder almacenar la información
existente en los ficheros VSAM y Secuenciales.

Se asume que la calidad de la información en Necora es la adecuada para
que los datos puedan ser gestionados sin complicaciones por las
aplicaciones Necor@PRYC y Necora@NET. No se considera necesario abordar
ningún tipo de tarea encaminada a corregir o completar la información
existente.

Los grupos de entidades que se han considerado para la migración son:

- Tablas maestras -/> Necor@NET

- Avisos de revisión -/> Necor@NET

- Ingeniería -/> Necor@NET

- Peticiones de oferta -/> Necor@PRYC

- Almacén -/> Necor@PRYC

- Vales y bandejas -/> Necor@PRYC

- Aprovisionamiento (demandas y pedidos) -/> Necor@PRYC

- Producción -/> Necor@PRYC

- Coral -/> Necor@PRYC

Asimismo se integrarán en esta base de datos las entidades ya
descargadas en su día a Sql Server en el marco del proyecto de
eliminación del host.

En el caso de Coral se debe tener en cuenta que las tablas y sus
registros deben ser movidos a diferentes bases de datos SQL Server según
su contenido logístico. Se incluye un Excel con la identificación de las
tablas afectadas y el criterio a seguir para la extracción de los datos.

En la migración se deben considerar igualmente las tablas históricas PH
(Pedidos), BH (Órdenes) y NH (Ingeniería) de las últimas obras (5 años).
No es una información que se considere prioritaria ni necesariamente
accesible desde Necor@. Se mantienen los datos en SQL Server por si se
requiere su consulta en el futuro.

Por cada tabla a migrar se plantea el desarrollo de dos programas:

- Una descarga directamente desde las utilidades del DB2 en el HOST para
  realizar el volcado de datos a fichero plano.

- Un programa SSIS para la carga de datos en SQL Server desde fichero.

## Identificación de tablas y ficheros

En este apartado se incluye una relación exhaustiva de todas las tablas
existentes en Necora, indicando si estas deben ser consideradas para la
migración y si los datos deben ser accesibles a través de las
aplicaciones Necor@.

- **M <sub>(1)</sub> :** Indica si los datos contenidos en la tabla
  deben ser **<u>M</u>**igrados al nuevo entorno SQL Server.

- **P <sub>(2)</sub> :** Indica si se dispone de un **<u>P</u>**roceso
  de exportación/importación desde HOST a Necor@PRYC/NET.

- **F <sub>(3)</sub> :** Indica si se dispone de la
  **<u>F</u>**uncionalidad necesaria para consultar la información desde
  Necor@PRYC/NET.

Se han detectado un total de 285 tablas cuyo creador es NEC. El número
de VSAM es de 8. A continuación mostramos un cuadro resumen del volumen
de tablas candidatas a ser migradas a SQL Server tras el estudio
realizado.

| Área de información | Nº | M <sub>(1)</sub> | P <sub>(2)</sub> | F <sub>(3)</sub> | Observaciones |
|----|----|----|----|----|----|
| TOTAL | 479 | 191 | 70 | 70 |  |
| Almacén | 29 | 21 | 0 | 0 |  |
| Demandas | 16 | 12 | 0 | 0 |  |
| Ingeniería | 56 | 32 | 29 | 29 |  |
| Maestros | 22 | 17 | 17 | 17 |  |
| Órdenes | 48 | 31 | 20 | 20 |  |
| Otras | 58 | 2 | 0 | 0 |  |
| Pedidos | 55 | 29 | 0 | 0 |  |
| Textos (VSAM + DB2) | 9 | 5 | 4 | 4 |  |
| Coral | 186 | 42 | 0 | 0 | Solo consultas desde Necor@ |

Se puede consultar la relación completa de tablas consideradas para la
migración en la hoja Excel “DTI-MIGRACION-HOST-R00_AnexoTablas.xls”.

