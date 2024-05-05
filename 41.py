def calcular_parcela(valor_divida, juros, parcelas):
    valor_juros = valor_divida * (juros / 100)
    valor_total = valor_divida + valor_juros
    valor_parcela = valor_total / parcelas
    return valor_total, valor_juros,valor_parcela

tabela_parcelas_juros = {
    1: 0,
    3: 10,
    6: 15,
    9: 20,
    12: 25
}

valor_divida = float(input("Digite o valor da dívida: R$ "))

print("\nValor da Dívida | Valor dos Juros | Quantidade de Parcelas | Valor da Parcela")
print("-" * 82)

for parcelas, juros in tabela_parcelas_juros.items():
    valor_total, valor_juros, valor_parcela = calcular_parcela(valor_divida, juros, parcelas)
    print(f"R$ {valor_total:12.2f} | R$ {valor_juros:15.2f} | R${parcelas:23} | R${valor_parcela:14.2f}")