import streamlit as st

# Senha fixa
senha_correta = "ditre123"
senha = st.text_input("Digite a senha para acessar:", type="password")

if senha == senha_correta:
    st.success("Acesso liberado ✅")
    st.title("📂 Menu Principal - Programas")

    st.write("Selecione abaixo o programa que deseja abrir:")

    st.markdown("[🔍 ConsEquip](https://consequip-yg7w8sxbuqujhvu7spyntb.streamlit.app/)")
    st.markdown("[📊 Conrepass](https://conrepass-frhucxskkdgmt2hxuq4kju.streamlit.app/)")
    st.markdown("[📑 Semuspb](https://semuspb-z2u4ydkkdznpwuchwyau6f.streamlit.app/)")
else:
    st.warning("Digite a senha correta para acessar o sistema.")

# Rodapé discreto
st.markdown(
    "<p style='text-align:right; font-size:12px; color:green;'>Bartolomeu Lima</p>",
    unsafe_allow_html=True
)
