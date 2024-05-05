inicio = int(input('Digite o primeiro número: '))
fim = int(input('Digite o segundo número: '))

print("Números no intervalo entre,", inicio, "e", fim, ":")

if inicio > fim:
    inicio, fim = fim, inicio

for numero in range(inicio + 1, fim):
    print(numero, end=" ")