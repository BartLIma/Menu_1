import streamlit as st

# Título principal na área central
st.title("📂 Menu Principal - App's")
st.write("Selecione na barra lateral o aplicativo que deseja abrir:")

# Barra lateral
st.sidebar.title("📂 Menu Principal - App's")
st.sidebar.write("Escolha abaixo:")

# Menu lateral com botões
if st.sidebar.button("🔍 Equipamentos Médico-Hospitalares (Lista Renem.)"):
    st.header("🔍 Equipamentos Médico-Hospitalares (Lista Renem.)")
    st.write("Abrindo módulo de equipamentos...")

if st.sidebar.button("📊 Transferências Discricionárias e Legais (convênios)"):
    st.header("📊 Transferências Discricionárias e Legais (convênios)")
    st.write("Abrindo módulo de transferências...")

if st.sidebar.button("📑 Cadastro de Secretarias de Saúde-Fundos de Saúde"):
    st.header("📑 Cadastro de Secretarias de Saúde-Fundos de Saúde")
    st.write("Abrindo módulo de cadastro...")
