# py-template
[![CI](https://github.com/AlanVignolo/py-template/actions/workflows/ci.yml/badge.svg)](https://github.com/AlanVignolo/py-template/actions/workflows/ci.yml)

Template de proyecto Python con buenas prácticas: tipado estático, tests, CI y configuración segura.

## Uso

1. Usá este repo como template en GitHub
2. Cloná tu nuevo repo
3. `uv sync`

## Estructura

\```
src/py_template/   # código fuente
tests/             # tests
.env.example       # variables de entorno requeridas
\```

## Limitaciones

- Es una plantilla de demostración, no un paquete publicado en PyPI
- Las dependencias (numpy, pandas, opencv) son de ejemplo, no forman parte de la funcionalidad
- No tiene autenticación ni manejo de secretos en producción

## Decisiones de diseño

| Decisión | Alternativa descartada | Por qué |
|---|---|---|
| `uv` | `pip` | uv es significativamente más rápido y maneja el entorno virtual y las dependencias en un solo comando |
| layout `src/` | flat (código en la raíz) | evita que el paquete local sea importable sin estar instalado, lo que hace que los tests reflejen el comportamiento real |
| `pydantic-settings` | `os.environ` pelado | agrega tipado, validación y jerarquía de fuentes (env var > .env > default) sin código extra |
| `uv_build` (hatchling) | `setuptools` | es el backend por defecto de uv, más simple y sin configuración adicional para proyectos nuevos |
