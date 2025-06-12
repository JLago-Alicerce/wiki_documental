---
source: tmp_full.md
created: 2025-06-12T13:03:21.397965
---
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

