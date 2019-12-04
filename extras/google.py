import webbrowser
import sys

def main(frase_de_busca):
    google = 'http://www.google.com/search?q={}'
    site = google.format(frase_de_busca)
    webbrowser.open(site)

if __name__ == "__main__":
    if len(sys.argv) == 1:
        raise ValueError('Parametro de busca nao enviado')
    else:
        frase = "." .join(sys.argv[1:])
        main(frase)
        