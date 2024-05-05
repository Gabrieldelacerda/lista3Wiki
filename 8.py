numeros = []

for i in range(5):
    numero = float(input(f'Digite o {i+1} número: '))
    numeros.append(numero)

soma = sum(numeros)

media = soma / len(numeros)

print(f'A soma dos números é: {soma}')
print(f'A media dos números é: {media}')