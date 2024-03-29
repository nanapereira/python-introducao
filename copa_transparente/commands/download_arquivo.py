import io
import sys
import urllib.request as request

BUFF_SIZE = 1024

def download_lenght(response, output, lenght):
    times = lenght // BUFF_SIZE
    if lenght % BUFF_SIZE > 0:
        times += 1
    for time in range(times):
        output.write(response.read(BUFF_SIZE))
        print(f"Download {(time * BUFF_SIZE/lenght)*100}")

def download(response, output):
    total_downloaded = 0
    while True:
        data = response.read(BUFF_SIZE)
        total_downloaded += len(data)
        if not data:
            break
    output.write(data)
    print('Download {bytes}'.format(bytes=total_downloaded))

def main():
    response = request.urlopen(sys.argv[1])
    out_file = io.FileIO("saida.zip", mode="w")

    content_lenght = response.getheader('Content-Length')
    try:
        if content_lenght:
            lenght = int(content_lenght)
            download_lenght(response, out_file, lenght)
        else:
            download(response, out_file)
    except Exception an e:
        print("Erro durante o dowload")
        raise e
    finally:
        out_file.close()
        response.close()
        print("Fim")

if __name__ == "__main__":
    main()
    