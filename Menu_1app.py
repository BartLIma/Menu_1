import streamlit as st

st.title("📂 Menu Principal - Programas")
st.write("Selecione abaixo o programa que deseja abrir:")

# CSS para estilizar os botões com fundo escuro e texto azul claro
st.markdown(
    """
    <style>
    .menu-button {
        display: inline-block;
        padding: 10px 18px;
        margin: 6px 0;
        font-size: 15px;
        font-weight: bold;
        text-decoration: none;
        border-radius: 6px;
        color: #cce5ff; /* azul claro para contraste */
    }
    .green { background-color: #155724; }  /* verde escuro */
    .blue { background-color: #004085; }   /* azul escuro */
    .gray { background-color: #343a40; }   /* cinza escuro */
    .menu-button:hover {
        opacity: 0.85;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Botões coloridos abrindo em nova guia
st.markdown(
    "<a class='menu-button green' href='https://consequip-yg7w8sxbuqujhvu7spyntb.streamlit.app/' target='_blank'>🔍 Consultar Equipamentos</a>",
    unsafe_allow_html=True
)
st.markdown(
    "<a class='menu-button blue' href='https://conrepass-frhucxskkdgmt2hxuq4kju.streamlit.app/' target='_blank'>📊 Consultar Transferências (convênios ou contratos de repasse)</a>",
    unsafe_allow_html=True
)
st.markdown(
    "<a class='menu-button gray' href='https://semuspb-z2u4ydkkdznpwuchwyau6f.streamlit.app/' target='_blank'>📑 Consultar Cadastro de Secretarias de Saúde</a>",
    unsafe_allow_html=True
)

# Rodapé discreto
st.markdown(
    "<p style='text-align:right; font-size:12px; color:green;'>Bartolomeu Lima - Corecon-ES 1541</p>",
    unsafe_allow_html=True
)
