lista1 = input().split(' ')
codigo1 = int(lista1[0])
numero_de_pecas1 = int(lista1[1])
valor_unitario1 = float(lista1[2])

lista2 = input().split(' ')
codigo2 = int(lista2[0])
numero_de_pecas2 = int(lista2[1])
valor_unitario2 = float(lista2[2])

valor_a_pagar = (numero_de_pecas1 * valor_unitario1) + (numero_de_pecas2 * valor_unitario2)

print("VALOR A PAGAR: R$ {:.2f}" .format(valor_a_pagar))
