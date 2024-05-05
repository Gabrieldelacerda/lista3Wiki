def calcular_min_max_soma(valores):
    if not valores:
        return None, None, 0

    menor = maior = valores[0]
    soma = 0

    for valor in valores:
        if valor < menor:
            menor = valor
        if valor > maior:
            maior = valor
        soma += valor

    return menor, maior, soma

N = int(input("Quantos números você deseja inserir? "))
numeros = []

for i in range(N):
    numero = float(input(f"Digite o {i+1} número: "))
    numeros.append(numero)

menor, maior, soma = calcular_min_max_soma(numeros)

print(f"Menor valor: {menor}")
print(f"Maior valor: {maior}")
print(f"Soma: {soma}")