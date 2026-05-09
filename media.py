print("Bem vindo ao nosso sistema de cadastro!✔️")
print("-" * 50) 

n1 = float(input("Digite a primeira nota: ")) # Solicita ao usuário que insira a primeira nota e armazena na variável 'n1'
n2 = float(input("Digite a segunda nota: ")) 
n3 = float(input("Digite a terceira nota: ")) 
n4 = float(input("Digite a quarta nota: ")) 
qtd = [n1, n2, n3, n4] # Armazena as notas em uma lista chamada 'qtd'
print("-" * 50)
print("\n")

media = sum(qtd) / len(qtd) # Calcula a média das notas somando os valores da lista 'qtd' e dividindo pelo número de elementos na lista usando a função 'len()'
print(f"A média de notas do aluno é: {media}") # Exibe a média
print("\n")

print("-" * 50) 
if media >= 6: # Verifica se a média é maior ou igual a 6
    print("Parabéns! Você foi aprovado!🎉") 
else: # Caso contrário
    print("Infelizmente, você foi reprovado.😞") 
