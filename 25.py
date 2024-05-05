n_pessoas = int(input('Quantas pessoas na turma? '))

soma_idades = 0
contador_pessoas = 0

for i in range(n_pessoas):
    idade = int(input(f"Digite a idade da pessoa {i+1}: "))
    soma_idades += idade
    contador_pessoas += 1

media_idades = soma_idades / contador_pessoas

if 0 <= media_idades <= 25:
    print("Turma jovem.")

elif 26 <= media_idades <= 60:
    print("Turma adulta.")
else:
    print("Turma idosa.")