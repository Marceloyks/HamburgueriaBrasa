import streamlit as st 

st.set_page_config(page_title="Brasa & Pão - Painel SQL", layout="wide")
st.image('banner.jpg', width="stretch")

st.navigation([
    st.Page("paginas/inicio.py", title="Início", default=True),
    st.Page("paginas/nivel1_.py", title="Nível 1 - Aquecimento"),
    st.Page("paginas/nivel2_.py", title="Nível 2 - Join"),
    st.Page("paginas/nivel3_.py", title="Nível 3 - Desafio")

]).run()
