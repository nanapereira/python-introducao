import pytest
from lista_ao_quadrado import lista_ao_quadrado

@pytest.fixture
def lista():
    return [1,2,3,4,5,6,7,8]

@pytest.fixture
def lista_2():
    return list(range(10, 20, 3))

def test_lista_1(lista):
    esperado = [1,4,9,16,25,36,49,64]
    resultado = lista_ao_quadrado(lista)
    assert esperado == resultado

def test_lista_2(lista_2):
    esperado = [100, 169, 256, 361]
    resultado = lista_ao_quadrado(lista_2)
    assert esperado == resultado
    