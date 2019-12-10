impostos = ['MEI','SIMPLES','LTDA']
for i in impostos:
    if i.startswith('M'):
        continue
    print(i)
    