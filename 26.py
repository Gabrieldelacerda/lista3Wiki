total_eleitores = int(input("Digite o número total de eleitores: "))

votos_candidato1 = 0
votos_candidato2 = 0
votos_candidato3 = 0

for i in range(total_eleitores):
    print(f"Eleitor {i+1}, vote em um dos candidatos:")
    print("1 - Zé de Corinto")
    print("2 - Zé Espartano")
    print("3 - Zé Ateniense")
    voto = int(input("Digite o número do candidato em que você deseja votar: "))

    if voto == 1:
        votos_candidato1 += 1
    elif voto == 2:
        votos_candidato2 += 1
    elif voto == 3:
        votos_candidato3 += 1
    else:
        print("Voto invalido")

print(f"Candidato 1: {votos_candidato1}")
print(f"Candidato 2: {votos_candidato2}")
print(f"Candidato 3: {votos_candidato3}")