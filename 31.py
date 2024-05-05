print("Lojas Tabajara")
print("Para finalizar a contagem de produtos, insira 0.")

total = 0
quantidade_produtos = 0

while True:
    preco = float(input(f"Produto {quantidade_produtos + 1}: R$ "))
    if preco == 0:
        break
    total += preco
    quantidade_produtos += 1

print(f"Total: R$ {total:.2f}")

dinheiro = float(input("Dinheiro: R$ "))
troco = dinheiro - total

print(f"Troco: R$ {troco:.2f}")