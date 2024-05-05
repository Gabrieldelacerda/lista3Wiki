intervalo_0_25 = 0
intervalo_26_50 = 0
intervalo_51_75 = 0
intervalo_76_100 = 0

while True:
    numero = int(input("Digite um número positivo (ou negativo para sair): "))

    if numero < 0:
        break

    if numero >= 0 and numero <= 25:
        intervalo_0_25 += 1
    elif numero >= 26 and numero <= 50:
        intervalo_26_50 += 1
    elif numero >= 51 and numero <= 75:
        intervalo_51_75 += 1
    elif numero >= 76 and numero <= 100:
        intervalo_76_100 += 1

print("Quantidade de  números no intervalo [0-25]:", intervalo_0_25)
print("Quantidade de números no intervalo [26-50]:", intervalo_26_50)
print("Quantidade de números no intervalo [51-75]:", intervalo_51_75)
print("Quantidade de números no intervalo [76-100]:", intervalo_76_100)