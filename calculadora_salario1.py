imposto = 27.5
while imposto > 0:
    salario = int(input("Qual e o seu salario? Digite aqui: "))
    imposto =  input("Qual o valor do imposto que voce paga? Digite aqui: ")

    imposto = 27.5 if not imposto else float(imposto)

    valor_real = salario - salario * (imposto/100)
    print(f"O seu valor de ganho real e de: {valor_real}")