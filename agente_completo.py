import streamlit as st 
from agno.models.openai import OpenAIChat
from agno.agent import Agent
from dotenv import load_dotenv
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.wikipedia import WikipediaTools

load_dotenv()

personalidade = st.sidebar.selectbox("Personalidade",
["Professor de Python", 
"Professor de História", 
"Cientista maluco"])

descricao = {
    "Professor de Python":"Voce é um professor de Python que r'esponde com exemplos e contexto",
    "professor de história":"Voce é um professor de historia, que ensina de forma clara, simples e objetiva.",
    "Cienista maluco":"Voce é um cientista maluco que sempre esta em busca de inovacoes e e projetos."
}

agente = Agent( #tupla pois nao mudaremos os parametos do agente
               
    model=OpenAIChat(id="gpt-4o-mini"),
    description=descricao[personalidade],
    tools=[DuckDuckGoTools(),WikipediaTools()],
    markdown=True
)

if "mensagens" not in st.session_state:
    st.session_state.mensagem = []
    
for msg in st.session_state.mensagem:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
        
if st.sidebar.button("limpar conversas"):
    st.session_state.mensagem = []
    st.rerun()
    
st.title("Sistema MultAgentes")
    
pergunta = st.chat_input("Pergunte ao Agente")

if pergunta:
    
    with st.chat_message("user"):
        st.markdown(pergunta)
        
    st.session_state.mensagem.append({"role": "user", "content": pergunta})
        
    with st.chat_message("assistant"):
        resposta = agente.run(pergunta)
        st.markdown(resposta.contnt)
    st.session_state.mensagem.append({"role": "assistant","content":resposta.content})
    
