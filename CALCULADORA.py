# Desafio 3: Calculadora

# Enunciado:
# Vamos criar uma mini-calculadora de soma. Siga estes passos:
# Peça para o usuário digitar o primeiro número e guarde em uma variável.
# Peça para o usuário digitar o segundo número e guarde em uma variável.
# Crie uma variável que receba a soma das duas variáveis anteriores.
# Imprima o resultado na tela.

bemVindo = (f"Bem-vindo à Calculadora de Soma!➕")
print("-" * 50)
print(bemVindo)
print("\n")

num1 = float(input("Digite o primeiro número: ")) # Solicita ao usuário que insira o primeiro número e armazena na variável
num2 = float(input("Digite o segundo número: ")) 
soma = num1 + num2 # Calcula a soma dos dois números e armazena na variável 'soma'
print("-" * 50)

print(f"A soma de {num1} e {num2} é: {soma}") # Exibe o resultado da soma

