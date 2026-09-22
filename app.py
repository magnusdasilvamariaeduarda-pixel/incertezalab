import streamlit as st
import numpy as np

st.set_page_config(
    page_title="IncertezaLab",
    page_icon="📊"
)

st.title("📊 IncertezaLab")

grandeza = st.selectbox(
    "Grandeza",
    [
        "Temperatura",
        "Pressão",
        "Comprimento",
        "Massa",
        "Tensão"
    ]
)

unidade = st.text_input(
    "Unidade",
    "°C"
)

medicoes_texto = st.text_area(
    "Medições (uma por linha)",
    placeholder="72.4\n72.5\n72.3"
)

if st.button("🧮 Calcular"):

    try:

        medicoes = [
            float(x)
            for x in medicoes_texto.splitlines()
            if x.strip()
        ]

media = np.mean(medicoes)

desvio = np.std(
    medicoes,
    ddof=1
)

u_a = desvio / np.sqrt(
    len(medicoes)
)

st.success("Cálculo realizado!")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Valor Médio",
        f"{media:.4f} {unidade}"
    )

with col2:
    st.metric(
        "Desvio Padrão",
        f"{desvio:.4f}"
    )

with col3:
    st.metric(
        "Incerteza Tipo A",
        f"{u_a:.4f}"
    )
        )

    except:

        st.error(
            "Verifique as medições informadas."
        )
