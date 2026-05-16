from agno.agent import Agent 
from agno.models.openai import OpenAIChat 
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.tavily import TavilyTools
from agno.db.sqlite import SqliteDb
from dotenv import load_dotenv


#carregar a chave de API 
load_dotenv()

bancDados = SqliteDb(db_file="temp/registros.db")

agente = Agent(
    #Essa linha define o modelo do meu agente 
    model = OpenAIChat(id = "gpt-4o-mini"),
    description="Você agora é uma princesa encantada, e possui todos os conhecimentos imaginaveis e inimaginaveis, e reponde com muita doçura e segurança",
    add_history_to_context=True,
    db=bancDados,
    num_history_runs=3,
    tools=[DuckDuckGoTools(), TavilyTools],
    markdown = True
)

while True:
    pergunta = input("Digite a sua pergunta: ")
    if pergunta.lower() in ["exit", "sair", "quit"]:
        print("Encerrando o agente... \nFique á vontade quando tiver mais duvidas")
        break
    else:
        agente.print_response(pergunta)