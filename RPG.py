# Desafio 1: O Criador de Personagens RPG 
# Objetivo: Lidar com múltiplos inputs sequenciais e estruturar o código.
# Enunciado:
# Você está criando um jogo e precisa montar o personagem do jogador. Peça para o usuário digitar três coisas, uma de cada vez:
# O nome do personagem 
# A classe do personagem (mago, guerreiro, etc)
# O tipo de skin que o personagem irá possuir (grátis, plus ou pro).
# Agora, exiba no console as três informações.

bemVindo = (f"Bem-vindo ao Criador de Personagens RPG!🎮")
print("-" * 50)
print(bemVindo)
print("\n")

nomePersonagem = input("Digite o nome do seu personagem: ") 
classePersonagem = input("Digite a classe do seu personagem (mago, guerreiro, etc): ")
tipoSkin = input("Digite o tipo de skin do seu personagem (grátis, plus ou pro): ") 
print("-" * 50)

print(f"Nome do personagem: {nomePersonagem}") 
print(f"Classe do personagem: {classePersonagem}")
print(f"Tipo de skin do personagem: {tipoSkin}")

print(f"seu nome é  {nomePersonagem} , sua classe é  {classePersonagem}  e seu tipo de skin é  {tipoSkin} !")

