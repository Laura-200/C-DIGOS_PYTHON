import streamlit as st

st.title("Secretaria SENAI Americana ⭕")
st.subheader("---------------------------------------------------------------------------") #75
st.subheader("Conheça os nossos cursos")

st.write("I.A. Generativa, Power BI, Empilhadeira, Excel, Eletricista Instalador")
st.divider()
st.markdown("**ATENÇÃO** : Verifique se existem vagas disponiveis.")

nome = st.text_input("digite o seu nome: ")
idade = st.number_input("Digite a sua idade", min_value=16, max_value=99)
cursoEscolhido = st.selectbox("Cursos disponiveis", ["I.A. Generativa", "Power BI", "Empilhadeira", "Excel", "Eletricista Instalador"])
aceitaTermos = st.checkbox("Ao clicar aqui, você aceita os termos e condições")

if st.button("Enviar resposta"):
    if nome and idade and cursoEscolhido and aceitaTermos:
        st.success(f"Olá {nome} você tem {idade} anos, o cursoescolhido foi {cursoEscolhido} e os termos foram aceitados. CADASTRO CONCLUIDO!")
        st.balloons()
else:
    st.error("Alguma informação está inválida")