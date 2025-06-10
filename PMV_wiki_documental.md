# 🚀 PMV – Producto Mínimo Viable para `wiki_documental`

Este documento define el estado actual del proyecto `wiki_documental`, los requisitos mínimos para una primera entrega sólida y funcional, y las tareas necesarias para completarla mediante Codex.

---

## 🎯 1. Resumen Ejecutivo

`wiki_documental` es una solución para:

- Centralizar la documentación de un proyecto con 16 años de historia.
- Consumir archivos `.docx` y `.pdf`, convertirlos a Markdown, limpiarlos y organizarlos.
- Permitir una navegación tipo wiki a través de un `index.html` alimentado por Docsify.
- Soportar ingesta incremental, integración temática y metadatos para búsquedas.

---

## 🧱 2. PMV – Alcance Funcional Mínimo

| Requisito PMV                              | Descripción                   | Estado actual | Gap                              |
| ------------------------------------------ | ----------------------------- | ------------- | -------------------------------- |
| Conversión `.docx` a `.md`                 | `pandoc` CLI integrado        | ✅            | –                                |
| Extracción de encabezados                  | `generar_mapa_encabezados.py` | ✅            | –                                |
| Generación de `index.yaml` y `_sidebar.md` | Estructura funcional          | ✅            | –                                |
| Ingesta incremental por carpeta            | Parcialmente funcional        | ⚠️            | Mejora lógica de control         |
| Fusión temática de contenidos              | No implementado               | ❌            | Requiere lógica por slug o alias |
| Soporte para `.pdf`                        | No funcional aún              | ⚠️            | Añadir extracción OCR o texto    |
| Normalización de `.docx`                   | No integrada aún              | ❌            | Ver `TASK-DOCX001`               |
| Metadatos enriquecidos                     | Parcial                       | ⚠️            | Ampliar esquema                  |
| Estética adaptable a Altia                 | CSS básico presente           | ⚠️            | Integrar diseño de @PRC          |

---

## 📋 3. Tareas Codex para completar PMV

### Funcionalidad base

- `TASK-PMV001` – Procesador de carpeta `_originales/` para detectar nuevos `.docx/.pdf`.
- `TASK-PMV002` – Integración de contenido en `.md` existente por encabezado o tema.
- `TASK-PMV003` – Soporte básico para `.pdf` mediante OCR o conversión a texto.

### Calidad de entrada

- `TASK-DOCX001` – Script `normalizar_estilos_docx.py` para estandarizar encabezados.
- `TASK-PMV004` – Integración del normalizador en `wiki_cli.py`.

### Metadatos y trazabilidad

- `TASK-PMV005` – Inyección automática de metadatos en `.md`.
- `TASK-PMV006` – Generación y mantenimiento de `metadata.yaml` indexado.

### Presentación

- `TASK-FRONT001` – Refactor de `custom.css` con estética Altia.
- `TASK-FRONT002` – Etiquetas de estado visuales en cada documento (`Publicado`, `Borrador`, etc.).

---

## 📈 4. Recomendaciones para futuro escalado

| Área                 | Propuesta                                              |
| -------------------- | ------------------------------------------------------ |
| Refactor estructural | Separar `core/`, `scripts/`, `ui/`, `config/`, `docs/` |
| IA contextual        | Agrupación y sugerencias semánticas                    |
| Multicliente         | Configuración dinámica por proyecto                    |
| Publicación          | GitHub Pages, intranet o export web controlada         |
| Buscador             | Indexación semántica con Lunr.js o ElasticLite         |

---

## ✅ 5. Criterios de aceptación

1. `wiki_cli.py full archivo.docx` genera un `.md` estructurado con metadatos.
2. Sidebar y `index.yaml` reflejan correctamente las secciones procesadas.
3. Nuevos documentos son detectados sin duplicación.
4. Si hay coincidencia de tema, se integran en el `.md` correspondiente.
5. El `.css` aplicado cumple con los criterios visuales de Altia.
6. La wiki es navegable desde `index.html`.

---
