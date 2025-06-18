<!--
---
source: EstadoActualPlataformaBBD_V27_3_42.md
doc_source: EstadoActualPlataformaBBD_V27_3_42.docx
inserted: 2025-06-18T23:14:04.894857
---
-->

<div class="fragment-meta">source: EstadoActualPlataformaBBD_V27_3_42.md | doc: EstadoActualPlataformaBBD_V27_3_42.docx | inserted: 2025-06-18T23:14:04.894857</div>

# Cambios recientes:

- Optimización de vistas y reestructuración de Interfaces PEC
  (junio–julio 2020).

- Implantación de auditoría interna mediante tabla log /_Audit_Changes.

- Normalización de estructuras para compatibilidad internacional.

  1.  <span id="_Toc199209694" class="anchor"></span>Contexto y
      dependencias

Esta instancia se emplea principalmente para la gestión y explotación
funcional dentro del entorno Necor@AWD, cubriendo diversos ámbitos:
gestión documental (NecoraDocAWD), procesamiento de flujos técnicos
(InterfacesAWD_PEC, NAI_InterfacesAWD) y explotación de datos
(Necor@AWD).

Además, aloja el servidor de informes REPORTSERVERSNECORANET, que
facilita la publicación de dashboards y consultas externas. También
integra el objeto PDB, que centraliza y consolida información de
múltiples fuentes para su distribución a instancias internacionales.

El modelo operativo se basa en una dualidad entre la gestión interna de
datos y la preparación de flujos estructurados hacia entornos remotos
(SQLTURK y SQLNORWAY), a través del objeto PDB que actúa como puente
lógico. Este diseño asegura la coherencia estructural y minimiza el
acoplamiento entre esquemas, facilitando la interoperabilidad con
clientes internacionales.

En 2020 se llevó a cabo un proceso de optimización orientado a mejorar
el rendimiento, reorganizando vistas y creando sinónimos funcionales.
Asimismo, se implementó un sistema de auditoría a nivel de registros
para reforzar la trazabilidad.

