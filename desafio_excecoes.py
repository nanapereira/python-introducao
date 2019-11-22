numero_1 = input()
numero_2 = input()

def dividir(numero_1, numero_2):
    try:
        resultado = int(numero_1) / int(numero_2)
        print(resultado)
    except (ZeroDivisionError, ValueError):
        print("Erro na divisao")
        
if __name__ == "__main__":
    dividir(numero_1, numero_2)
