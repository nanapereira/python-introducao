entrada = input()
contador = []
for string_qualquer in entrada:
    if string_qualquer == '(':
        contador.append('(')
    elif string_qualquer == ')':
        if len(contador) > 0:
            contador.pop()
    else:
        if string_qualquer == ')':
            string_qualquer.append(')')
            break
if len(contador) == 0:
    print('Balanceado')
else:
    print('Desbalanceado')
    