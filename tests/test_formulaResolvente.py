import pytest
from functions.formulaResolvente import formulaResolvente

def test_duas_raizes_distintas():
    # x^2 - 5x + 6 = 0  →  x1=3, x2=2
    resultado = formulaResolvente(1, -5, 6)
    assert resultado == (3.0, 2.0)

def test_raiz_dupla():
    # x^2 - 2x + 1 = 0  →  x1=x2=1
    resultado = formulaResolvente(1, -2, 1)
    assert resultado == (1.0, 1.0)

def test_sem_raizes_reais():
    # x^2 + 1 = 0  →  delta negativo
    resultado = formulaResolvente(1, 0, 1)
    assert resultado is None

def test_coeficiente_a_zero():
    # a=0 não é equação de segundo grau
    with pytest.raises(ValueError):
        formulaResolvente(0, 1, 1)

def test_raizes_negativas():
    # x^2 + 5x + 6 = 0  →  x1=-2, x2=-3
    resultado = formulaResolvente(1, 5, 6)
    assert resultado == (-2.0, -3.0)