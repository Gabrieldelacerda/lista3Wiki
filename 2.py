while True:
    usuario = input("Digite o nome do usuário: ")
    senha = input("Digite a senha: ")

    if senha != usuario:
        print("Usuário e senha cadastrados com sucesso!")
        break
    else:
        print("ERRO: A senha não pode ser igual ao nome de usuário.")