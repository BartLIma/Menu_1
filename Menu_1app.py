import streamlit as st

# Senha fixa
senha_correta = "dit"
senha = st.text_input("Digite a senha para acessar:", type="password")

if senha == senha_correta:
    # Mensagem de acesso liberado mais discreta
    st.markdown(
        "<p style='color:green; font-size:14px; font-weight:bold;'>Acesso liberado ✅</p>",
        unsafe_allow_html=True
    )

    st.title("📂 Menu Principal - Programas")

    st.write("Selecione abaixo o programa que deseja abrir:")

    # Links com descrições personalizadas
    st.markdown("[🔍 Consultar Equipamentos](https://consequip-yg7w8sxbuqujhvu7spyntb.streamlit.app/)")
    st.markdown("[📊 Consultar Transferências (convênios ou contratos de repasse)](https://conrepass-frhucxskkdgmt2hxuq4kju.streamlit.app/)")
    st.markdown("[📑 Consultar Cadastro de Secretarias de Saúde](https://semuspb-z2u4ydkkdznpwuchwyau6f.streamlit.app/)")
else:
    st.warning("Digite a senha correta para acessar o sistema.")

# Rodapé discreto
st.markdown(
    "<p style='text-align:right; font-size:12px; color:green;'>Bartolomeu Lima - Corecon-ES 1541</p>",
    unsafe_allow_html=True
)
