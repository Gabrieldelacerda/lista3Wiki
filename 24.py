n = int(input("Digite o número de notas: "))

soma_notas = 0

for i in range(n):
    nota = float(input(f"Digite a nota {i+1} nota: "))
    soma_notas += nota

media = soma_notas / n

print("A média aritmética das", n, "notas é", media)
