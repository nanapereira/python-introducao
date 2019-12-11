from calculadora import soma, multiplicacao

def test_soma_positivos():
    resultado = soma(10, 20)
    esperado = 30
    assert resultado == esperado

def test_soma_negativos():
    resultado = soma(-10, -20)
    esperado = -30
    assert resultado == esperado

def test_multiplicacao_positivos():
    resultado = multiplicacao(10, 20)
    esperado = 200
    assert resultado == esperado

def test_multiplicacao_negativos():
    resultado = multiplicacao(-10, 20)
    esperado = -200
    assert resultado == esperado
    