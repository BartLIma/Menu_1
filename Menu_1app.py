import streamlit as st

# CSS para ajustar barra de senha e mensagens
st.markdown(
    """
    <style>
    input[type="password"] {
        width: 150px !important;
    }
    .stAlert {
        font-size: 13px;
        padding: 0.4rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Senha fixa
senha_correta = "Ditre123"
senha = st.text_input("Digite a senha para acessar:", type="password")

if senha == senha_correta:
    st.markdown(
        "<p style='color:green; font-size:14px; font-weight:bold;'>Acesso liberado ✅</p>",
        unsafe_allow_html=True
    )

    st.title("📂 Menu Principal - Programas")
    st.write("Selecione abaixo o programa que deseja abrir:")

    # Botões que redirecionam na mesma aba
    st.markdown(
        "<a href='https://consequip-yg7w8sxbuqujhvu7spyntb.streamlit.app/' target='_self'>🔍 Consultar Equipamentos</a>",
        unsafe_allow_html=True
    )
    st.markdown(
        "<a href='https://conrepass-frhucxskkdgmt2hxuq4kju.streamlit.app/' target='_self'>📊 Consultar Transferências (convênios ou contratos de repasse)</a>",
        unsafe_allow_html=True
    )
    st.markdown(
        "<a href='https://semuspb-z2u4ydkkdznpwuchwyau6f.streamlit.app/' target='_self'>📑 Consultar Cadastro de Secretarias de Saúde</a>",
        unsafe_allow_html=True
    )
else:
    st.warning("Digite a senha correta para acessar o sistema.")

# Rodapé discreto
st.markdown(
    "<p style='text-align:right; font-size:12px; color:green;'>Bartolomeu Lima - Corecon-ES 1541</p>",
    unsafe_allow_html=True
)
