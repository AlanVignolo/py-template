from py_template import saludo


def test_saludar():
    assert saludo.saludar("Alberto") == "Hola, Alberto!"
    assert saludo.saludar("Mundo") == "Hola, Mundo!"
