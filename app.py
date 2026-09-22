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
    placeholder="72.4\n72.5\n72.3\n72.4"
)

st.subheader("Fontes de Incerteza Tipo B")

u_certificado = st.number_input(
    "Incerteza padrão do certificado",
    min_value=0.0,
    value=0.25,
    step=0.01
)

u_resolucao = st.number_input(
    "Incerteza da resolução",
    min_value=0.0,
    value=0.03,
    step=0.01
)

u_deriva = st.number_input(
    "Incerteza da deriva",
    min_value=0.0,
    value=0.00,
    step=0.01
)

if st.button("🧮 Calcular"):

    try:

        medicoes = [
            float(x)
            for x in medicoes_texto.splitlines()
            if x.strip()
        ]

        if len(medicoes) < 2:

            st.error(
                "Informe pelo menos duas medições."
            )

        else:

            media = np.mean(medicoes)

            desvio = np.std(
                medicoes,
                ddof=1
            )

            u_a = desvio / np.sqrt(
                len(medicoes)
            )

            uc = np.sqrt(
                u_a**2 +
                u_certificado**2 +
                u_resolucao**2 +
                u_deriva**2
            )

            k = 2

            U = k * uc

            st.success(
                "Cálculo realizado com sucesso!"
            )

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

            st.subheader("Resultado Final")

            col4, col5 = st.columns(2)

            with col4:
                st.metric(
                    "Incerteza Combinada (uc)",
                    f"{uc:.4f}"
                )

            with col5:
                st.metric(
                    "Incerteza Expandida (U)",
                    f"{U:.4f}"
                )

    except ValueError:

        st.error(
            "Verifique as medições informadas."
        )
st.success(
    f"Resultado: {media:.4f} ± {U:.4f} {unidade}"
)
