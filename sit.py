import streamlit as st

st.title("SUPER CLÍNICA 🏥")
st.subheader("---------------------------------------------------------------------------") #75
st.subheader("Conheça nossos especialistas ")

st.write("Dra. Clara Nutri 🍳 ")
st.write("Coach Bruno Força 💪🏻 ")
st.write("Ana Serenidade 🧠 ")
st.divider()

st.subheader("Insira seus dados pessoais para o agendamento de consultas! ")

nome = st.text_input("Digite o seu nome: ")
cpf = st.text_input("Informe seu C.P.F")
st.divider()

EspecialidadeEscolhida = st.selectbox("Especialidades da nossa Clinica: ", ["Especialista em alimentação saudável, sugere receitas e refeições equilibradas", "Especialista em exercícios físicos, monta treinos e dá dicas de musculação e cardio", "Especialista em bem-estar mental, dá dicas de gerenciamento de estresse e ansiedade", ])
confirme = st.checkbox("Ao clicar aqui, você ira confirmar sua consulta")

if st.button("agendamento"):
    if nome and cpf  and EspecialidadeEscolhida and confirme:
        st.success(f"Olá {nome} sua consulta foi agendada com SUCESSO! ")
        st.balloons()
else:
    st.error("Alguma informação está inválida")