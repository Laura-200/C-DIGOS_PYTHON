# Desafio 2: Questionário do Detetive 

# Objetivo: Simular um mini-diálogo onde o programa coleta vários dados para montar um relatório.
# Enunciado:
# Crie um programa que simula um interrogatório. Faça 3 perguntas ao usuário:
# Onde ele estava ontem á noite? (Guarde em uma variável)
# O que ele estava fazendo (Guarde em uma variável)
# Quem estava com ele? (Quem estava com ele)
#  No final, imprima o "Relatório Investigativo" juntando todas as respostas para ver se a história faz sentido. 

bemVindo = (f"Bem-vindo ao Questionário do Detetive!🕵️‍♂️")
print("-" * 50)
print(bemVindo)
print("\n")

#em uma noite dois amigos estavam caminhando na rua indo comprar um lanche, quando um crime aconteceu, um deles foi roubado e é preciso encontrar o culpado, para isso, o detetive irá fazer algumas perguntas para a população da região, e no final irá analisar as respostas para descobrir quem é o culpado.

local = input("Onde você estava ontem à noite? ")
atividade = input("O que você estava fazendo? ")
companhia = input("Quem estava com você? ")
print("-" * 50)

# if local == "casa" and atividade == "assistindo filme" and companhia == "amigos":
#     suspeita = "Sua história parece consistente. Você é inocente!✔️"
# else:
#     suspeita = "Sua história tem inconsistências. Você é suspeito!❌"
# print("\n")

# if local == "rua" and atividade == "caminhando" and companhia == "amigo":
#     suspeita = "Sua história parece suspeita. Você é suspeito!❌"
# else:
#     inocente = "Sua história tem consistências. Você é inocente!✔️"
#   


print("Relatório Investigativo: 🔎")

print(f"Local: {local}")
print(f"Atividade: {atividade}")
print(f"Companhia: {companhia}")
print(f"Então, ontem à noite, você estava em {local}, fazendo {atividade} com {companhia}.")

if local == "casa" and atividade == "bolinho" and companhia == "mamãe":
    print( "Sua história parece consistente. Você é inocente!✔️")
else:
    print("Sua história tem inconsistências. Você é suspeito!❌")





