def calcular_fatorial(numero):
    fatorial = 1
    for i in range(1, numero + 1):
        fatorial *= i
    return fatorial

numero = int(input("Digite um número inteiro: "))

if numero < 0:
    print("Não é possível calcular o fatorial de números negativos.")
else:
    resultado = calcular_fatorial(numero)
    print(f"{numero}! = {resultado}")