#salario = 1000.00

#aumento_percentual = 1.5 / 100

#for ano in range(1996, 2023):
    #salario += salario * aumento_percentual
    #aumento_percentual *= 2

#print("O salário atual do funcionário em 2023 é R$", round(salario, 2))

# Solicitação do salário inicial do funcionário
salario_inicial = float(input("Digite o salário inicial do funcionário: "))

# Salário inicial
salario = salario_inicial

# Aumento inicial em 1996
aumento_percentual = 1.5

# Loop para calcular os aumentos salariais a partir de 1997
for ano in range(1996, 2023):
    salario += salario * aumento_percentual  # Aumento do salário
    aumento_percentual *= 2  # Dobro do percentual do ano anterior

# Exibição do salário atual
print("O salário atual do funcionário em 2023 é R$", round(salario, 2))
