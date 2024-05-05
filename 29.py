print("Lojas Quase Dois - Tabela de Preços")

for quantidade in range(1, 51):
    preco = quantidade * 1.99
    print(f"{quantidade} - R$ {preco:.2f}")
    