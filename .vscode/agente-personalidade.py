from dotenv import load_dotenv
from agno.agent import Agent 
from agno.models.openai import OpenAIChat 

#todos os agentes nescessitam da chave de API, e a função LOAD_DONTEV faz a leitura do arquivo no .env
load_dotenv()

agente = Agent(
    #Essa linha define o modelo do meu agente 
    model = OpenAIChat(id = "gpt-4o-mini"),
    description="Você agora é uma princesa encantada, e possui todos os conhecimentos imaginaveis e inimaginaveis, e reponde com muita doçura e segurança",
    markdown = True
)

while True:
    pergunta = input("Digite a sua pergunta")
    if pergunta.lower() in ["exit", "sair", "quit"]:
        print("Encerrando o agente... \nFique á vontade quando tiver mais duvidas")
        break
    else:
        agente.print_response(pergunta)