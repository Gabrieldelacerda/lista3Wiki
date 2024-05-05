while True:
    nome = input("Digite o nome (maior que 3 caracteres): ")
    if len(nome) > 3:
        break
    else:
        print("Erro: O nome deve ter mais de 3 caracteres. Por favor, tente novamente!")

while True:
    idade = int(input("Digite a idade (entre 0 e 150): "))
    if 0 <= idade <= 150:
        break
    else:
        print("Erro: A idade deve estar entre 0 e 150. Por favor, tente novamente.")

while True:
    salario = float(input("Digite o salario (maior que zero): "))
    if salario > 0:
        break
    else:
        print("Erro: O salário deve ser maior que 0. Por favor, tente novamente.")

while True:
    sexo = input("Digite o sexo, f para feminino, m para masculino").lower()
    if sexo in ['f', 'm']:
        break
    else:
        print("Erro: O sexo deve ser 'f' ou 'm'. Por favor tente novamente.")

while True:
    estado_civil = input("Digite o estado civil, s para solteiro, c para casado, v para viúvo, d para divorciado.").lower()
    if estado_civil in ['s', 'c', 'v', 'd']:
        break
    else:
        print("Erro: O estado civil não é válido.")

print("Informações válidas:")
print("Nome:", nome)
print("Sexo:", sexo)
print("Civil:", estado_civil)
print("Idade:", idade)
print("Salário:", salario)