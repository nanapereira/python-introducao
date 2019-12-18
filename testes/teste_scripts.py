import unittest
from collections import Counter

def contador_frase(frase):
    resultado = Counter(frase)
    return resultado

def contador_caracteres(frase):
    contador = 0
    letra_atual = frase[0]
    resultado = ''
    for indice, letra in enumerate(frase):
        if letra != letra_atual or indice == (len(frase) -1):
            if indice == (len(frase) -1):
                contador += 1
            resultado += str(contador) + letra_atual
            letra_atual = letra
            contador = 1
        else:
            contador += 1
    return resultado

class ContagemCaracteresTest(unittest.TestCase):
    def teste_frase(self):
        frase = "teste jcavi treinamentos"
        esperado = {'t':4, 'e':4, 's':2, ' ':2, 'j':1, 'c':1, 'a':2, 'v':1, 'i':2,
         'r':1, 'n':2, 'm':1, 'o':1}
        resultado =  contador_frase(frase)
        self.assertEqual(esperado, resultado)

    def teste_caractere(self):
        frase = "aaaaabbbbccccccaaaaaaa"
        esperado = '5a4b6c7a'
        resultado = contador_caracteres(frase)
        self.assertEqual(esperado, resultado)

if __name__ == '__main__':
    unittest.main()