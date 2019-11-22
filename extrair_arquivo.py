import os
import zipfile
import sys

def main(path):
    """if not os.path.exists(path):
        print("Arquivo {} nao existe".format(path))
        sys.exit(-1)
    elif not str(path).endswith('.zip'):
        print(f"Arquivo {path} nao e.zip")
        sys.exit(-1)
    else:"""
    try:
        zfile = zipfile.ZipFile(path)
        zfile.extractall()
        print("Arquivos extraidos")
    except FileNotFoundError:
        print("Arquivo inexistente")
    except PermissionError as pme:
        print("Erro de permissao")
    """except Exception:
        print("Erro inesperado")"""

if __name__ == "__main__":
    if len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        print('Voce nao digitou nenhum arquivo para ser extraido')
        