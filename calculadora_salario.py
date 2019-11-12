salario = float(input("Qual e o seu salario? Digite aqui: "))
imposto = input("Qual o valor de imposto que voce paga? Digite aqui: ")

if imposto == "":
    imposto = 27.5
else:
    imposto = float(imposto)

valor_real = salario - salario * (imposto/100)
print(f"O seu valor de ganho real e de: {valor_real}")
