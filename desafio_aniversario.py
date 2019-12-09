#!/usr/bin/env python3
import unittest


def main(nome):
    arquivo = open('aniversarios.txt','r')
    aniversario = dict()
    for i in arquivo:

        valores = i.split('|')
        aniversario[valores[0]] = valores[1][:-1]
    return aniversario.get(nome)



class AniversariosTest(unittest.TestCase):
    def test_aniversario_vinicius(self):
        aniversario = "24/09/1993"
        resposta = main("Vinicius Melo")
        self.assertEqual(aniversario, resposta)

    def test_aniversario_douglas(self):
        aniversario = "02/01/1990"
        resposta = main("Douglas Rosa")
        self.assertEqual(aniversario, resposta)

    def test_aniversario_inajara(self):
        aniversario = "23/07/1986"
        resposta = main("Inajara Pereira")
        self.assertEqual(aniversario, resposta)

    def test_aniversario_virginia(self):
        aniversario = "26/04/1985"
        resposta = main("Virginia Santos")
        self.assertEqual(aniversario, resposta)


if __name__ == '__main__':
    pass