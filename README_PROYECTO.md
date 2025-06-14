# Uso del proyecto

Para ejecutar el pipeline completo sin detenerse ante diferencias entre `map.yaml` e `index.yaml`, utiliza:

```bash
poetry run wiki full --skip-verify
```

Para limpiar los formatos de .docx

```bash
poetry run python tools/clean_docx_format.py --source inputs/_originals/borrador --dest inputs/_originals/listos_para_procesar  --errors inputs/_originals/errores --template templates/plantilla_base.docx
```
