---
source: DTI-MIGRACION-HOST-R03.md
doc_source:
  - 20221130_SeguimientoTraspasoConocimientos.docx
  - DTI-MIGRACION-HOST-R03.docx
created: 2025-06-13 05:51:56.765761
---
# Interfaces con clientes externos

Actualmente existen varios procesos SSIS que transfieren la información
desde Necora a los clientes australianos. Concretamente para los
programas AWD y ALHD. Tras el apagado del HOST es imprescindible
mantener en funcionamiento los interfaces del programa AWD, ya que
existe el compromiso de envío de información por parte de Navantia hasta
el año 2021.

No es necesario sin embargo considerar los procesos de extracción del
programa ALHD, ni la F105, ni las órdenes de trabajo de la Zona 8.

Actualmente los interfaces AWD funcionan con un SQL Server 2008. El
principal problema es que esta versión tiene fecha de fin de soporte
para dentro de 2 meses (09/07/2019). Por lo tanto, debería plantearse
una migración de las bases de datos de interfaces y aplicación como
mínimo a un SQL Server 2014.

<img src="assets/media/) | 47 |
| Análisis, diseño y construcción de los procesos de extracción DB2/VSAM | 134 |
| Análisis, diseño y construcción de los packages SSIS para la carga de datos | 1.084 |
| Formación a usuarios y transferencia técnica | 43 |
| **TOTAL** | **1.401** |

**Recursos necesarios**

| Perfil               | Horas | Dedicación |
|----------------------|-------|------------|
| Jefe de Proyecto     | 79    | 5%         |
| Analista Programador | 425   | 40%        |
| Programador          | 897   | 100%       |

### Accesibilidad de la información

| Actividad                                                    | Horas     |
|--------------------------------------------------------------|-----------|
| Análisis y diseño de las funcionalidades a implementar       | 55        |
| Construcción de las pantallas y migración del acceso a datos | 936       |
| Formación a usuarios y transferencia técnica                 | 44        |
| **TOTAL**                                                    | **1.035** |

**Recursos necesarios**

| Perfil               | Horas | Dedicación |
|----------------------|-------|------------|
| Jefe de Proyecto     | 61    | 5%         |
| Analista Programador | 316   | 30%        |
| Programador          | 658   | 100%       |

### Interfaces con clientes externos

| Actividad                                    | Horas   |
|----------------------------------------------|---------|
| Adaptaciones interfaces AWD                  | 266     |
| Formación a usuarios y transferencia técnica | 62      |
| **TOTAL**                                    | **328** |

**Recursos necesarios**

| Perfil               | Horas | Dedicación |
|----------------------|-------|------------|
| Jefe de Proyecto     | 19    | 5%         |
| Analista Programador | 92    | 30%        |
| Programador          | 217   | 100%       |

### Optimización de las aplicaciones

| Actividad | Horas |
|----|----|
| Pruebas unitarias, integración y aceptación | 160 |
| Análisis, diseño y desarrollo de los ajustes necesarios a nivel de base de datos, acceso y aplicación | 80 |
| **TOTAL** | **240** |

**Recursos necesarios**

| Perfil               | Horas | Dedicación |
|----------------------|-------|------------|
| Jefe de Proyecto     | 12    | 5%         |
| Analista Programador | 228   | 100%       |

### Soporte y mantenimiento

| Actividad                                        | Horas   |
|--------------------------------------------------|---------|
| Soporte y mantenimiento correctivo durante 1 año | **320** |

**Recursos necesarios**

| Perfil               | Horas | Dedicación |
|----------------------|-------|------------|
| Jefe de Proyecto     | 16    | 5%         |
| Analista Programador | 304   | 20%        |

## Duración de los trabajos y planificación

El plazo de ejecución de este proyecto es de **8 meses**. A continuación
incluimos un diagrama de Gantt con la planificación prevista, asumiendo
como fecha hipotética de inicio de los trabajos el 1 de septiembre de
2019.

<img src="assets/media/