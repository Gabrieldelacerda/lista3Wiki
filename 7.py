numeros = []

for i in range(5):
    numero = float(input(f'Digite o {i+1} número: '))
    numeros.append(numero)

maior_numero = max(numeros)

print(f"O maior número da sua lista é {maior_numero}.")