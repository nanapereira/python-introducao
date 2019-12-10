import unittest

def main(nome):
    arquivo = open('aniversarios.txt', 'r')
    aniversario = dict()
    for i in arquivo:
        valores = i.split('|')
        aniversario[valores[0]] = valores[1][:-1]
    return aniversario.get(nome)
    