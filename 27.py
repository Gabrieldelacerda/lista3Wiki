quantidade_turmas = int(input("Digite a quantidade de turmas: "))

total_alunos = 0
num_turmas_validas = 0

for i in range(quantidade_turmas):
    num_alunos = int(input(f"Digite a quantidade de alunos para a turma {i + 1}: "))

    if num_alunos <= 40:
        total_alunos += num_alunos
        num_turmas_validas += 1
    else:
        print("Não pode passar de 40!")

if num_turmas_validas > 0:
    media_alunos_por_turma = total_alunos / num_turmas_validas
    print(f"A média de alunos por turma é: {media_alunos_por_turma:.2f}")
else:
    print("Não há turmas válidas para calcular a média.")
