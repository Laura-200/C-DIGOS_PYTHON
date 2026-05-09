nomeUsuario = input("Digite seu nome de usuário: ")
senhaUsuario = input("Digite sua senha: ")
print("-" * 50)
print("\n")

if nomeUsuario == "Laura" and senhaUsuario == "1234":
    print("Login bem-sucedido! Bem-vindo, Laura!🎉") 
else:
    print("Login falhou! Verifique seu nome de usuário e senha.😞")