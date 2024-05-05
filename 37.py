codigos = []
alturas = []
pesos = []

while True:
    codigo = input("Digite o código do cliente (ou 0 para encerrar): ")

    if codigo == '0':
        break

    altura = float(input("Digite a altura do cliente (em metros): "))
    peso = float(input("Digite o peso do cliente (em quilogramas): "))

    codigos.append(codigo)
    alturas.append(altura)
    pesos.append(peso)

if len(codigos) > 0:
    indice_mais_alto = alturas.index(max(alturas))
    indice_mais_baixo = alturas.index(min(alturas))
    indice_mais_gordo = pesos.index(max(pesos))
    indice_mais_magro = pesos.index(min(pesos))

    media_alturas = sum(alturas) / len(alturas)
    media_pesos = sum(pesos) / len(pesos)

    print("\nResultados:")
    print("Código do cliente mais alto:", codigos[indice_mais_alto])
    print("Código do cliente mais baixo:", codigos[indice_mais_baixo])
    print("Código do cliente mais gordo:", codigos[indice_mais_gordo])
    print("Código do cliente mais magro:", codigos[indice_mais_magro])
    print("Média de alturas dos clientes:", round(media_alturas, 2), "metros")
    print("Média dos pesos dos clientes:", round(media_pesos, 2), "quilogramas")
else:
    print("Nenhum cliente foi cadastrado.")