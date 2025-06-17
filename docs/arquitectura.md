# 🧱 Estructura funcional – wiki_documental

Este documento describe la arquitectura actual del sistema `wiki_documental` a nivel de módulos Python.  
Se actualiza tras cada cambio relevante mediante tareas formales.

---

## 📁 src/wiki_documental/processing

| Módulo | Función principal | Usado en `wiki full` | Se limpia en `reset` |
|--------|-------------------|----------------------|-----------------------|
| `docx_to_md.py` | Convierte `.docx` a `.md` con Pandoc | ✅ | ✅ (borra `.md`) |
| `headings_map.py` | Extrae encabezados y genera `map.yaml` | ✅ | ✅ |
| `index_builder.py` | Genera `index.yaml` jerárquico | ✅ | ✅ |
| `ingest.py` | Fragmenta `.md` en secciones wiki | ✅ | ✅ |
| `md_post.py` | Limpia puntos y corrige saltos | ✅ (post-ingestión) | N/A |
| `normalize_docx.py` | Aplica estilos estructurados | ✅ | ❌ |
| `reclassify.py` | Redistribuye contenido `unclassified` | ❌ (manual) | ✅ |
| `sidebar.py` | Genera `_sidebar.md` desde `index.yaml` | ✅ | ✅ |
| `style_map.py` | Reglas de estilo de headings | ✅ (desde `normalize_docx`) | ❌ |
| `verify_pre_ingest.py` | Verifica coherencia `map` ↔ `index` | ✅ | ❌ |

---

## 📁 Otras herramientas

| Módulo | Función | CLI disponible | Tiene test |
|--------|---------|----------------|------------|
| `cli.py` | Entrada principal del sistema | ✅ (`wiki ...`) | ✅ |
| `config.py` | Carga de rutas y opciones (`cfg`) | ✅ (interno) | ✅ |
| `reset` | Limpia entorno de trabajo | ✅ | ✅ |
| `reclassify.py` | CLI: `wiki reclassify` | ✅ | ✅ |
| `check_sidebar_links.py` | Verifica enlaces en CI | ❌ (solo script) | ✅ |

---

### 🦾 Convenciones

- Los archivos `.md` generados siempre se ubican en `wiki/`.
- Las imágenes deben estar en `wiki/assets/media/`.
- El contenido no clasificado va a `99_unclassified.md`.
- Los metadatos se insertan como YAML front‑matter.

