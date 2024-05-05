numero_aluno_mais_alto = 0
numero_aluno_mais_baixo = 0
altura_aluno_mais_alto = 0
altura_aluno_mais_baixo = float('inf')

for i in range(1, 11):
    numero_aluno = int(input(f"Digite o número do {i} aluno: "))
    altura_aluno = float(input(f"Digite a altura do {i} aluno em cm: "))

    if altura_aluno > altura_aluno_mais_alto:
        numero_aluno_mais_alto = numero_aluno
        altura_aluno_mais_alto = altura_aluno

    if altura_aluno < altura_aluno_mais_baixo:
        numero_aluno_mais_baixo = numero_aluno
        altura_aluno_mais_baixo = altura_aluno

print("Número do aluno mais alto:", numero_aluno_mais_alto)
print("Altura do aluno mais alto:", altura_aluno_mais_alto)
print("Número do aluno mais baixo:", numero_aluno_mais_baixo)
print("Altura do aluno mais baixo:", altura_aluno_mais_baixo)