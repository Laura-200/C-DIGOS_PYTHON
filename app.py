print("-" * 50)
print("Olá! Este é um programa simples para coletar informações pessoais.📊")
print("\n")
print("Bem-vindo ao nosso sistema de cadastro!✔️")
print("-" * 50)

nome = input("Digite seu nome: ") # Solicita ao usuário que insira seu nome e armazena na variável 'nome'
email = input("Digite seu email: ") # Solicita ao usuário que insira seu email e armazena na variável 'email'
cidade = input("Digite sua cidade: ") # Solicita ao usuário que insira sua cidade e armazena na variável 'cidade'
estado = input("Digite seu estado: ") # Solicita ao usuário que insira seu estado e armazena na variável 'estado' 
pais = input("Digite seu país: ") # Solicita ao usuário que insira seu país e armazena na variável 'pais'
estado_civil = input("Digite seu estado civil: ") # Solicita ao usuário que insira seu estado civil e armazena na variável 'estado_civil'  
ano_nascimento = input("Digite seu ano de nascimento: ") # Solicita ao usuário que insira seu ano de nascimento e armazena na variável 'ano_nascimento'
ano_atual = 2026# Define o ano atual como 2026
idade = input("Digite sua idade: ") # Solicita ao usuário que insira sua idade e armazena na variável 'idade'
idade = ano_atual - int(ano_nascimento) # Calcula a idade do usuário
idadeFutura = int(idade) + 1 # Calcula a idade futura adicionando 10 anos à idade atual e armazena na variável 'idadeFutura'
print("-" * 50)

print(f"Olá, {nome}!")
print("\n")
print(f"Seu email é: {email}")
print("\n")
print(f"Você mora em {cidade}, {estado}, {pais}.")
print("\n")
print(f"Seu estado civil é: {estado_civil}.")
print("\n")
print(f"Você tem {idade} anos.")
print("\n")
print(f"Em um ano, você terá {idadeFutura} anos.")
print("-" * 50)
print("Obrigado por fornecer suas informações!👌")