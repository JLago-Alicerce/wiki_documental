---
source: DTI-MIGRACION-HOST-R03.md
doc_source: DTI-MIGRACION-HOST-R03.docx
created: 2025-06-13T05:51:57.525125
---
# Optimización de las aplicaciones

Necor@PRYC fue diseñado en su día para la gestión de los proyectos en
curso atendiendo un volumen de información limitado. Sin embargo en el
nuevo escenario propuesto, el número de registros que tanto Necor@PRYC
como Necor@NET deben poder gestionar es muy superior al actual.

Es necesario por tanto llevar a cabo un plan de pruebas exhaustivo que
garantice el acceso óptimo a la información, así como una fluida
comunicación e intercambio de datos entre las aplicaciones Necor@PRYC y
Necor@NET. La ejecución de este plan de pruebas derivará en tareas de
ajuste que será necesario realizar en la capa de acceso a datos.

De cara a la mejora de los tiempos de respuesta se plantea además la
migración del gestor de base de datos SQL Server 2014 versión estándar,
que actualmente soporta a ambas aplicaciones, a una versión superior
2016 en la que ya soporta de serie el particionamiento de tablas e
índices. Consideramos que esta característica es imprescindible para
manejar correctamente el volumen de datos esperado.

