import pytest
from py_template.excepciones import DatosInvalidosError
from py_template.validacion import parsear_valor, validar_rango

def test_parsear_valor_valido():
    assert parsear_valor("3.14") == 3.14

def test_parsear_valor_invalido():
    with pytest.raises(DatosInvalidosError):
        parsear_valor("abc")

def test_validar_rango_valido():
    assert validar_rango(5.0) == 5.0

def test_validar_rango_invalido():
    with pytest.raises(DatosInvalidosError):
        validar_rango(-1.0)