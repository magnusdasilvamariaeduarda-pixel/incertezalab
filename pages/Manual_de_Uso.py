import streamlit as st

st.set_page_config(
    page_title="Manual de Uso",
    page_icon="📖",
    layout="wide"
)

st.title("Manual de Uso - MMG IncertezaLab")

st.markdown("""

# Objetivo

O MMG IncertezaLab foi desenvolvido para auxiliar no cálculo da incerteza de medição de forma rápida e automática.

---

# Grandeza

Selecione a característica que está sendo medida.

Exemplos:

- Temperatura
- Pressão
- Comprimento
- Massa
- Tensão Elétrica

Finalidade: identificar corretamente o tipo de medição.

---

# Unidade

Informe a unidade utilizada.

Exemplos:

- °C
- mm
- cm
- kg
- V

Finalidade: apresentar os resultados com a unidade correta.

---

# Nível de Confiança

Define o nível de confiança estatística utilizado no cálculo.

Opções:

- 90%
- 95%
- 99%

Quanto maior o nível de confiança, maior será a incerteza expandida.

---

# Medições

Digite uma medição por linha.

Exemplo:

97

85

102

94

88

Esses valores serão utilizados para calcular:

- Média
- Desvio padrão
- Incerteza Tipo A

---

# Certificado

Representa a incerteza associada ao certificado de calibração.

---

# Resolução

Representa a menor divisão do instrumento.

---

# Deriva

Representa possíveis alterações do instrumento ao longo do tempo.

---

# Resultados

O sistema calcula:

- Valor Médio
- Desvio Padrão
- Incerteza Tipo A
- Incerteza Tipo B
- Incerteza Combinada
- Incerteza Expandida

---

# Gráfico

O gráfico apresenta a contribuição percentual de cada fonte de incerteza para o resultado final.

---

MMG IncertezaLab
Versão 1.0

""")
