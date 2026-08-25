# py-template

## Decisiones de diseño

| Decisión | Alternativa descartada | Por qué |
|---|---|---|
| `uv` | `pip` | uv es significativamente más rápido y maneja el entorno virtual y las dependencias en un solo comando |
| layout `src/` | flat (código en la raíz) | evita que el paquete local sea importable sin estar instalado, lo que hace que los tests reflejen el comportamiento real |
| `pydantic-settings` | `os.environ` pelado | agrega tipado, validación y jerarquía de fuentes (env var > .env > default) sin código extra |
| `uv_build` (hatchling) | `setuptools` | es el backend por defecto de uv, más simple y sin configuración adicional para proyectos nuevos |
