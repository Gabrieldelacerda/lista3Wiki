menor_temperatura = float('inf')
maior_temperatura = float('-inf')
soma_temperaturas = 0
quantidade_de_temperaturas = 0

while True:
    temperatura = input("Digite a temperatura (ou 'fim' para encerrar): ")

    if temperatura.lower() == 'fim':
        break

    temperatura = float(temperatura)

    if temperatura < menor_temperatura:
        menor_temperatura = temperatura
    if temperatura > maior_temperatura:
        maior_temperatura = temperatura

    soma_temperaturas += temperatura
    quantidade_de_temperaturas += 1

media_temperaturas = soma_temperaturas / quantidade_de_temperaturas

print(f"A menor temperatura foi: {menor_temperatura:.2f}")
print(f"A maior temperatura foi: {maior_temperatura:.2f}")
print(f"A média das temperaturas foi: {media_temperaturas:.2f}")