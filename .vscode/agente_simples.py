from dotenv import load_dotenv
from agno.agent import Agent 
from agno.models.openai import OpenAiChat 

#todos os agentes nescessitam da chave de API, e a função LOAD_DONTEV faz a leitura do arquivo no .env
load_dotenv()

agente = Agent(
    #Essa linha define o modelo do meu agente 
    model = OpenAiChat(id = "gpt-4o-mini"),
    markdown = True
)

agente.print_reponse("Me conte uma curiosidade: ")