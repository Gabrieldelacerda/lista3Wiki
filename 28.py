quantidade_cds = int(input("Digite a quantidade de CDs na coleção: "))

valor_total = 0

for i in range(quantidade_cds):
    valor_cd = float(input(f"Digite o valor do CD {i+1}: "))
    valor_total += valor_cd

if quantidade_cds > 0:
    valor_medio_por_cd = valor_total / quantidade_cds
    print(f"O valor total investido na coleção de {quantidade_cds} é: R${valor_total:.2f}")
    print(f"O valor médio gasto em cada CD é: R${valor_medio_por_cd:.2f}")
else:
    print("Nenhum CD.")