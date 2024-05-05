def e_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False, i
    return True, None

numero = int(input('Digite um número: '))

e_primo, divisor = e_primo(numero)

if e_primo:
    print(f"{numero} é primo.")
else:
    print("Não é primo.")