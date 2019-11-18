nome_vendedor = input()
salario_fixo = float(input())
total_em_vendas = float(input())

total_a_receber = salario_fixo + (total_em_vendas * 0.15)

print("TOTAL = R$ {:.2f}".format(total_a_receber))
