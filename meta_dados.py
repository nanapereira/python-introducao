import os
import sys

def main(caminho):
    for meta_data_file in os.listdir(caminho):
        table_name = meta_data_file.split('.')[0]
        print(table_name)
if __name__ == "__main__":
    caminho = sys.argv[1]
    main(caminho)
