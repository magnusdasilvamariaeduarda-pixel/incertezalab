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

        st.success("Cálculo realizado!")

        st.metric(
            "Valor Médio",
            f"{media:.4f} {unidade}"
        )

    except:

        st.error(
            "Verifique as medições informadas."
        )
