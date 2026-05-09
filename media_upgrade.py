listaNotas = [] # Cria uma lista vazia chamada 'notas' para armazenar as notas inseridas pelo usuário

print("-" * 50)
print("Bem vindo a I.A que calcula a média de notas!📊")
print("\n")

while True:
    notas = input("Digite a nota que deseja inserir(ou 'sair' para finalizar): ") # Solicita ao usuário que insira uma nota ou 'sair' para finalizar e armazena na variável 'notas'
    if notas.lower() == "sair":
        break
    else:
        listaNotas.append(float(notas)) # Adiciona a nota convertida para float à lista 'notas'
        
print(listaNotas) # Exibe a lista de notas inseridas
print("\n")

media = sum (listaNotas) / len (listaNotas) # Calcula a média das notas somando os valores da lista 'notas' e dividindo pelo número de elementos na lista usando a função 'len()'
print(f"A média de notas do aluno é: {media}") # Exibe a média