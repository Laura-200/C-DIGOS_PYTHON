import streamlit as st

st.title("DIPADRE pizzaria 🍕")
st.subheader("---------------------------------------------------------------------------") #75
st.subheader("Conheça nossas Delicias! 😋")
st.divider()

st.write("Calabresa, Marguerita, Portuguesa, Quatro Queijos")

nome = st.text_input("Digite o seu nome: ")
cidade = st.text_input("Informe sua cidade")
bairro = st.text_input("Informe seu bairro")
saborEscolhido = st.selectbox("Cursos disponiveis", ["Calabresa", "Marguerita", "Portuguesa", "Quatro Queijos"])
confirme = st.checkbox("Ao clicar aqui, você ira confirmar seu pedido")

if st.button("FOMEEEEEEE"):
    if nome and cidade and bairro and bairro and saborEscolhido and confirme:
        st.success(f"Olá {nome} você mora em {cidade}, o sabor escolhido foi {saborEscolhido} aproveite sua delicia!🍕, CADASTRO CONCLUIDO!")
        st.balloons()
else:
    st.error("Alguma informação está inválida")