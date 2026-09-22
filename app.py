import streamlit as st
import numpy as np

st.set_page_config(
    page_title="IncertezaLab",
    page_icon="📊",
    layout="wide"
)

# ==========================
# CABEÇALHO
# ==========================

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
            "Tensão Elétrica"
        ]
    )

with col2:
    unidade = st.text_input(
        "Unidade",
        "°C"
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
    placeholder="Digite uma medição por linha\n\n72.4\n72.5\n72.3\n72.4"
)

# ==========================
# FONTES TIPO B
# ==========================

st.subheader("Fontes de Incerteza Tipo B")

col4, col5, col6 = st.columns(3)

with col4:
    u_certificado = st.number_input(
        "Certificado",
        min_value=0.0,
        value=0.25,
        step=0.01
    )

with col5:
    u_resolucao = st.number_input(
        "Resolução",
        min_value=0.0,
        value=0.03,
        step=0.01
    )

with col6:
    u_deriva = st.number_input(
        "Deriva",
        min_value=0.0,
        value=0.00,
        step=0.01
    )

st.divider()

# ==========================
# BOTÃO
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

            c1, c2, c3, c4 = st.columns(4)

            with c1:
                st.metric(
                    "Valor Médio",
                    f"{media:.4f}"
                )

            with c2:
                st.metric(
                    "Desvio Padrão",
                    f"{desvio:.4f}"
                )

            with c3:
                st.metric(
                    "Tipo A",
                    f"{u_a:.4f}"
                )

            with c4:
                st.metric(
                    "Tipo B",
                    f"{u_b:.4f}"
                )

            c5, c6, c7 = st.columns(3)

            with c5:
                st.metric(
                    "Incerteza Combinada",
                    f"{uc:.4f}"
                )

            with c6:
                st.metric(
                    "k",
                    f"{k:.3f}"
                )

            with c7:
                st.metric(
                    "Incerteza Expandida",
                    f"{U:.4f}"
                )

            st.divider()

            st.subheader("Resultado Final")

            st.success(
                f"{media:.4f} ± {U:.4f} {unidade}"
            )

st.subheader("Contribuição das Fontes")

total = (
    u_a**2 +
    u_certificado**2 +
    u_resolucao**2 +
    u_deriva**2
)

tipo_a_pct = (u_a**2 / total) * 100
cert_pct = (u_certificado**2 / total) * 100
res_pct = (u_resolucao**2 / total) * 100
deriva_pct = (u_deriva**2 / total) * 100

    except ValueError:

        st.error(
            "Verifique os valores informados."
        )

st.divider()

st.caption(
    "IncertezaLab • Versão 1.0"
)
