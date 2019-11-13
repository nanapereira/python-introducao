def main():
    contador = 0
    espaco = 7
    while contador < 7:
        contador += 1
        espaco -=1
        print((" " * espaco),("#" * contador),("#" * contador))

if __name__ == "__main__":
    main()
