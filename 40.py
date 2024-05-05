maior_indice_acidentes = float('-inf')
menor_indice_acidentes = float('inf')
cidade_maior_indice = ''
cidade_menor_indice = ''
total_veiculos = 0
total_acidentes_cidades_menos_2000_veiculos = 0
total_cidades_menos_2000_veiculos = 0

for i in range(1, 6):
    print(f"\nDados da cidade {i}:")
    codigo_cidade = int(input("Código da cidade: "))
    veiculos = int(input("Número de veículos de passeio em 1999: "))
    acidentes = int(input("Número de acidentes de trânsito com vítimas em 1999: "))

    if acidentes > maior_indice_acidentes:
        maior_indice_acidentes = acidentes
        cidade_maior_indice = codigo_cidade
    if acidentes < menor_indice_acidentes:
        menor_indice_acidentes = acidentes
        cidade_menor_indice = codigo_cidade

    total_veiculos += veiculos

    if veiculos < 2000:
        total_acidentes_cidades_menos_2000_veiculos += acidentes
        total_cidades_menos_2000_veiculos += 1

media_veiculos = total_veiculos / 5

if total_cidades_menos_2000_veiculos > 0:
    media_acidentes_menos_2000_veiculos = total_acidentes_cidades_menos_2000_veiculos
else:
    media_acidentes_menos_2000_veiculos = 0

print("\nResultados:")
print(f"Maior índice de acidentes de trânsito: {maior_indice_acidentes} na cidade {cidade_maior_indice}")
print(f"Menor índice de acidentes de trânsito: {menor_indice_acidentes} na cidade {cidade_menor_indice}")
print(f"Média de veículos nas cinco cidades juntas: {media_veiculos}")
print(f"Média de acidentes de trânsito nas cidades com menos de 2000 veículos: {media_acidentes_menos_2000_veiculos}")