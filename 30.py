preco_pao = float(input("Digite o preço do pão: R$: "))

print("Panificadora Pão de Ontem - Tabela de Preços")

for quantidade in range(1, 51):
    preco_total = quantidade * preco_pao
    print(f"{quantidade} - R${preco_total:.2f}")