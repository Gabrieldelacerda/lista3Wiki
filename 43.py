def calcular_valor(codigo, quantidade):
    if codigo == 100:
        return 1.20 * quantidade
    elif codigo  == 101:
        return 1.3 * quantidade
    elif codigo == 102:
        return 1.5 * quantidade
    elif codigo == 103:
        return 1.2 * quantidade
    elif codigo == 104:
        return 1.3 * quantidade
    elif codigo == 105:
        return 1 * quantidade
    else:
        return 0.00

total_pedido = 0.0

while True:
    codigo = int(input("Digite o código do item (ou 0 para encerrar o pedido): "))
    if codigo == 0:
        break
    quantidade = int(input("Digite a quantidade desejada: "))
    valor_item = calcular_valor(codigo, quantidade)
    total_pedido += valor_item
    print(f"Valor a ser pago pelo item: R$ {valor_item:.2f}")

print(f"Total do pedido: R$ {total_pedido:.2f}")