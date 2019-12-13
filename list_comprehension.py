numbers_um = [i for i in range(5)]
numbers_dois = [i + 3 * 2 for i in range(5)]
pares = [i for i in range(20) if i % 2 == 0]
impares = [i for i in range(20) if i % 2 == 1]
nested = [(i, j) for i in range(3) for j in range(3)]

print(numbers_um)
print(numbers_dois)
print(pares)
print(impares)
print(nested)
