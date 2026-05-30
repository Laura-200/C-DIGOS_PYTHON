import streamlit as st

st.title("Bem Vindo ao Cadastro do RH Já!✔️ ")
st.subheader("Gerenciado por: Laura")
st.subheader("---------------------------------------------------------------------------") #75

nome = st.text_input("Digite o seu nome: ")
email = st.text_input("Digite o seu E-mail: ")

if st.button("cadastrar"):
    if nome and email:
       st.success(f"Bem Vindo {nome}")
       st.success("E-mail valido!")
       st.balloons()
    else:
       st.error("Você precisa preencher com seus dados pessoais para prosseguir! ")
