base = int(input("Qual a base? "))
expoente = int(input("Digite o expoente: "))

resultado = 1

for _ in range(expoente):
    resultado *= base

print(f"{base} elevado a {expoente} é igual a {resultado}.")