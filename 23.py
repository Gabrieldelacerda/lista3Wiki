def verificar_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

def encontrar_primos(N):
    primos = []
    divisoes = 0
    for i in range(2, N + 1):
        if verificar_primo(i):
            primos.append(i)
            divisoes += i - 1
    return primos, divisoes

N = int(input("Digite um número inteiro N: "))

primos, divisoes = encontrar_primos(N)

print("Números primos até", N, "são:", primos)

print("Número total de divisões realizadas:", divisoes)
