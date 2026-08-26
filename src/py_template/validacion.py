import logging

from py_template.excepciones import DatosInvalidosError

log = logging.getLogger(__name__)


def parsear_valor(raw: str) -> float:
    try:
        return float(raw)
    except ValueError as e:
        log.exception("Error al parsear valor: %r", raw)
        raise DatosInvalidosError(
            f"El valor proporcionado no es un numero valido: {raw}"
        ) from e


def validar_rango(valor: float) -> float:
    if valor < 0:
        raise DatosInvalidosError(f"El valor debe ser mayor o igual a cero: {valor}")
    return valor
