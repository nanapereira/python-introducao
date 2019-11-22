def divisores():
    try:
        numero = int(input())
        lista = []
        for i in range(2, numero):
            if numero % i == 0:
                lista.append(i)
        print(lista)

    except (TypeError, ValueError):
        print("Digite um numero inteiro")

if __name__ == "__main__":
    divisores()
    