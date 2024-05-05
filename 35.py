def e_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

limite_superior = int(input("Digite um número inteiro: "))

numeros_primos = [numero for numero in range(2, limite_superior + 1) if e_primo(numero)]

print("Números primos entre 1 e", limite_superior, ": ", numeros_primos)