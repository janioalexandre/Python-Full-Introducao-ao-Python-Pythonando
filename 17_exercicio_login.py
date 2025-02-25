# Defina um usuário e senha e depois verifique se 
# login do usuário é valido.

USUARIO = "janio"
SENHA = "DeuséFiel"

while True:
    usuario = input("Digite seu nome de usuário: ")
    senha = input("Digite sua senha: ")

    if usuario == USUARIO and senha == SENHA:
        print("Login efetuado com sucesso!")
        break
    else:
        print("Usuário ou senha inválido.")
