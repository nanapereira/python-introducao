lista = input().split()
a = int(lista[0])
b = int(lista[1])
c = int(lista[2])

maior_ab = (a+b+abs(a-b))/2
maior = int((maior_ab+c+abs(maior_ab-c))/2)

print("{} eh o maior" .format(maior))
