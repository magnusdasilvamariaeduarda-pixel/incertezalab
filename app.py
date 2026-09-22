import streamlit as st

st.title("📊 IncertezaLab")

grandeza = st.selectbox(
    "Grandeza",
    ["Temperatura", "Pressão"]
)

st.write("Grandeza selecionada:", grandeza)
