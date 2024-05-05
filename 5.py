def obter_dados():
    try:
        populacao_a = float(input("Informe a população inicial do país A: "))
        taxa_crescimento_a = float(input("Informe a taxa de crescimento anual do país A (em decimal): "))
        populacao_b = float(input("Informe a população inicial do país B: "))
        taxa_crescimento_b = float(input("Informe a taxa de crescimento anual do país B (em decimal): "))
        if populacao_a <= 0 or populacao_b <= 0 or taxa_crescimento_a < 0 or taxa_crescimento_b < 0:
            print("Por favor, insira valores válidos maiores que zero e taxas de crescimento não negativas.")
            return obter_dados()
        return populacao_a, taxa_crescimento_a, populacao_b, taxa_crescimento_b
    except ValueError:
        print("Por favor, insira valores numéricos válidos.")
        return obter_dados()

def calcular_anos(populacao_a, taxa_crescimento_a, populacao_b, taxa_crescimento_b):
    anos = 0
    while populacao_a < populacao_b:
        populacao_a += populacao_a * taxa_crescimento_a
        populacao_b += populacao_b * taxa_crescimento_b
        anos += 1
    return anos

def main():
    while True:
        populacao_a, taxa_crescimento_a, populacao_b, taxa_crescimento_b = obter_dados()
        anos_necessarios = calcular_anos(populacao_a, taxa_crescimento_a, populacao_b, taxa_crescimento_b)
        print(f"Serão necessários {anos_necessarios} anos para que a população do país A ultrapasse a população do país B.")
        continuar = input("Deseja continuar? (s/n): ").lower()
        if continuar != 's':
            break

if __name__ == "__main__":
    main()
