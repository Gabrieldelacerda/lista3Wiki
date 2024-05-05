def calcular_fatorial(numero):
    if numero < 0 or numero >= 16:
        return None
    elif numero == 0:
        return 1
    else:
        fatorial = 1
        for i in range(1, numero + 1):
            fatorial *= i
        return fatorial

while True:
    try:
        numero = int(input("Digite um número inteiro positov menor que 16 para calcular o fatorial: "))
        if numero >= 0 and numero < 16:
            resultado = calcular_fatorial(numero)
            if resultado is not None:
                print(f"O fatorial de {numero} é {resultado}")
            else:
                print("Número inválido. Por favor, insira um número inteiro positivo menor que 16.")
        else:
            print("Número inválido. Por favor, insira um número inteiro positivo menor que 16.")
    except ValueError:
        print("VALOR INVÁLIDO!")

    continuar = input("Deseja calcular o fatorial de outro número? (s/n): ").lower()
    if continuar != "s":
        break