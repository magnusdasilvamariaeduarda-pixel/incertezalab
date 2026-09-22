import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="IncertezaLab",
    page_icon="📊",
    layout="wide"
)

st.title("📊 IncertezaLab")
st.caption(
    "Sistema para cálculo automático de incerteza de medição"
)

st.divider()

# ==========================
# DADOS DA MEDIÇÃO
# ==========================

col1, col2, col3 = st.columns(3)

with col1:
    grandeza = st.selectbox(
        "Grandeza",
        [
            "Temperatura",
            "Pressão",
            "Comprimento",
            "Massa",
            "Tensão Elétrica",
            "Outro"
        ]
    )

with col2:
    unidade = st.text_input(
        "Unidade",
        ""
    )

with col3:
    confianca = st.selectbox(
        "Nível de confiança",
        ["90%", "95%", "99%"],
        index=1
    )

st.subheader("Medições")

medicoes_texto = st.text_area(
    "",
    height=180,
    placeholder="Digite uma medição por linha\n\n97\n85\n102\n94\n88"
)

# ==========================
# FONTES TIPO B
# ==========================

st.subheader("Fontes de Incerteza Tipo B")

c1, c2, c3 = st.columns(3)

with c1:
    u_certificado = st.number_input(
        "Certificado",
        min_value=0.0,
        value=0.25,
        step=0.01
    )

with c2:
    u_resolucao = st.number_input(
        "Resolução",
        min_value=0.0,
        value=0.03,
        step=0.01
    )

with c3:
    u_deriva = st.number_input(
        "Deriva",
        min_value=0.0,
        value=0.00,
        step=0.01
    )

st.divider()

# ==========================
# CÁLCULO
# ==========================

if st.button("🧮 Calcular Incerteza", use_container_width=True):

    try:

        medicoes = [
            float(x.replace(",", "."))
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

            u_b = np.sqrt(
                u_certificado**2 +
                u_resolucao**2 +
                u_deriva**2
            )

            uc = np.sqrt(
                u_a**2 +
                u_b**2
            )

            if confianca == "90%":
                k = 1.645
            elif confianca == "95%":
                k = 2.0
            else:
                k = 2.576

            U = k * uc

            st.success(
                "Cálculo realizado com sucesso!"
            )

            st.subheader("Resultados")

            r1, r2, r3, r4 = st.columns(4)

            with r1:
                st.metric(
                    "Valor Médio",
                    f"{media:.6f}"
                )

            with r2:
                st.metric(
                    "Desvio Padrão",
                    f"{desvio:.6f}"
                )

            with r3:
                st.metric(
                    "Tipo A",
                    f"{u_a:.6f}"
                )

            with r4:
                st.metric(
                    "Tipo B",
                    f"{u_b:.6f}"
                )

            r5, r6, r7 = st.columns(3)

            with r5:
                st.metric(
                    "Incerteza Combinada",
                    f"{uc:.6f}"
                )

            with r6:
                st.metric(
                    "k",
                    f"{k:.3f}"
                )

            with r7:
                st.metric(
                    "Incerteza Expandida",
                    f"{U:.6f}"
                )

            st.divider()

            st.subheader("Resultado Final")

            st.success(
                f"{media:.6f} ± {U:.6f} {unidade}"
            )

            st.divider()

            st.subheader("Contribuição das Fontes")

            total = (
                u_a**2 +
                u_certificado**2 +
                u_resolucao**2 +
                u_deriva**2
            )

            dados = pd.DataFrame(
                {
                    "Fonte": [
                        "Tipo A",
                        "Certificado",
                        "Resolução",
                        "Deriva"
                    ],
                    "Percentual": [
                        (u_a**2 / total) * 100,
                        (u_certificado**2 / total) * 100,
                        (u_resolucao**2 / total) * 100,
                        (u_deriva**2 / total) * 100
                    ]
                }
            )

            fig = px.pie(
                dados,
                names="Fonte",
                values="Percentual",
                hole=0.35,
                title="Participação das fontes na incerteza total"
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

    except ValueError:

        st.error(
            "Verifique os valores informados."
        )

st.divider()

st.caption(
    "IncertezaLab • Versão 1.0"
)
