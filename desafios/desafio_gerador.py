from random import randint

numero_aleatorio = randint(1, 101)
contador = 0

while True:
    contador += 1
    numero_secreto = input("Adivinhe o numero secreto de 1 a 100: ")
    if numero_secreto == "sair":
        print("Sair")
        break
    numero_secreto = int(numero_secreto)
    if numero_secreto > numero_aleatorio:
        print("Numero muito alto")
    elif numero_secreto < numero_aleatorio:
        print("Numero muito baixo")
    else:
        print("Exatamente certo")
        break

print(f"Voce tentou {contador} vezes")
