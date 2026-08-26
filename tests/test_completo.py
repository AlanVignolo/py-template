import pytest
from py_template.predictor import run_prediction
from py_template.validacion import parsear_valor
from py_template.excepciones import DatosInvalidosError

@pytest.mark.parametrize("entrada, esperando", [
    ("0.1", 0.1),
    (3.14, 3.14),
    ("1e-10", 1e-10),
])
def test_parsear_approx(entrada, esperando):
    assert parsear_valor(entrada) == pytest.approx(esperando)
    
def test_parsear_invalido():
    with pytest.raises(DatosInvalidosError):
        parsear_valor("no es un numero")
        
def test_escribe_archivo(tmp_path):
    archivo = tmp_path / "salida.txt"
    archivo.write_text("Hola mundo")
    assert archivo.read_text() == "Hola mundo"

def test_variable_entorno(monkeypatch):
    monkeypatch.setenv("APP_BATCH_SIZE", "128")
    import os
    assert os.environ["APP_BATCH_SIZE"] == "128"

def test_linear_con_fixture(linear_model):
    assert run_prediction(linear_model, 5.0) == pytest.approx(10.0)