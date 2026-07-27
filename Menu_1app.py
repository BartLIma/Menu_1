import streamlit as st

# Título principal na área central
st.title("📂 Menu Principal - App's")
st.write("Selecione na barra lateral o aplicativo que deseja abrir:")

# Barra lateral
st.sidebar.title("📂 Menu Principal - App's")
st.sidebar.write("Escolha abaixo:")

# Links clicáveis na barra lateral
st.sidebar.markdown(
    """
    🔍 [Equipamentos Médico-Hospitalares (Lista Renem.)](https://seu-link-renem.com)  
    📊 [Transferências Discricionárias e Legais (convênios)](https://seu-link-transferencias.com)  
    📑 [Cadastro de Secretarias de Saúde-Fundos de Saúde](https://seu-link-cadastro.com)  
    """,
    unsafe_allow_html=True
)
