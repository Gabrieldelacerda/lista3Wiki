numeros_pares = 0
numeros_impares = 0

for _ in range(10):
    numero = int(input('Digite um número inteiro: '))
    if numero % 2 == 0:
        numeros_pares += 1
    else:
        numeros_impares += 1

print(f"Quantidade de números pares: {numeros_pares}")
print(f"Quantidade de números ímpares: {numeros_impares}")