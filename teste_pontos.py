import unittest

def remove_pontos(palavra):
    resultado = palavra.split('.')
    return "".join(resultado)

def adiciona_pontos(palavra):
    resultado = list(palavra)
    return ".".join(resultado)

class RemovePontosTest(unittest.TestCase):
    def test_com_pontos(self):
        esperado = "teste"
        resultado = remove_pontos("t.e.s.t.e")
        self.assertEqual(esperado, resultado)

    def test_com_outros_pontos(self):
        esperado = "virginia"
        resultado = remove_pontos("v.i.r.g.i.n.i.a")
        self.assertEqual(esperado, resultado)

    def test_sem_pontos(self):
        esperado = "nana"
        resultado = remove_pontos("nana")
        self.assertEqual(esperado, resultado)

class AdicionaPontosTest(unittest.TestCase):
    def test_com_pontos(self):
        esperado = "t.e.s.t.e"
        resultado = adiciona_pontos("teste")
        self.assertEqual(esperado, resultado)

    def test_com_outros_pontos(self):
        esperado = "d.o.u.g.l.a.s"
        resultado = adiciona_pontos("douglas")
        self.assertEqual(esperado, resultado)

if __name__ == '__main__':
    unittest.main()