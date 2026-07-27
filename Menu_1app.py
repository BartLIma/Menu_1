import streamlit as st

# Título principal na área central
st.title("📂 Menu Principal - App's")
st.write("Selecione na barra lateral o aplicativo que deseja abrir:")

# Barra lateral
st.sidebar.title("📂 Menu Principal - App's")
st.sidebar.write("Escolha abaixo:")

# Botões com links externos
st.sidebar.markdown(
    """
    <a href="https://consequip-yg7w8sxbuqujhvu7spyntb.streamlit.app/"_blank">
        <button style="width:100%; padding:10px; margin-bottom:10px;">
            🔍 Equipamentos Médico-Hospitalares (Lista Renem.)
        </button>
    </a>
    <a href="https://conrepass-frhucxskkdgmt2hxuq4kju.streamlit.app/" target="_blank">
        <button style="width:100%; padding:10px; margin-bottom:10px;">
            📊 Transferências Discricionárias e Legais (convênios)
        </button>
    </a>
    <a href="https://seu-link-cadastro.com" target="_blank">
        <button style="width:100%; padding:10px; margin-bottom:10px;">
            📑 Cadastro de Secretarias de Saúde-Fundos de Saúde
        </button>
    </a>
    """,
    unsafe_allow_html=True
)
