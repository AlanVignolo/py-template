import numpy as np
import pytest
from py_template.preprocessing import preprocess

H, W, C = 100, 800, 3

@pytest.fixture
def imagen_rgb(): # Fixture to generate a random RGB image
    rng = np.random.default_rng(seed=42)
    return rng.integers(0, 256, size=(H, W, C), dtype=np.uint8)

def test_forma_salida(imagen_rgb):
    resultado = preprocess(imagen_rgb)
    assert resultado.shape == (3, 224, 224)

def test_rango_valores(imagen_rgb):
    resultado = preprocess(imagen_rgb)
    assert resultado.min() >= 0.0 
    assert resultado.max() <= 1.0

def test_imagen_1x1():
    imagen = np.array([[[255, 0, 0]]], dtype=np.uint8) # Shape (1, 1, 3)
    resultado = preprocess(imagen)
    assert resultado.shape == (3, 224, 224)
    assert resultado.min() >= 0.0
    assert resultado.max() <= 1.0

def test_determinista(imagen_rgb):
    assert np.array_equal(preprocess(imagen_rgb), preprocess(imagen_rgb))
    
def test_array_vacio():
    with pytest.raises(Exception):
        preprocess(np.array([]))