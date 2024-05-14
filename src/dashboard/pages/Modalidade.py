import streamlit as st
import pandas as pd
import collections
import plotly.express as px

from data.carregar_dados import dados_descricao_modalidade

# Configuração inicial 
st.set_page_config(
    page_title="Analise exploratória",
    page_icon="🧊",
    layout="centered",
    initial_sidebar_state="expanded",
    # menu_items={
    #     'Get Help': 'https://www.extremelycoolapp.com/help',
    #     'Report a bug': "https://www.extremelycoolapp.com/bug",
    #     'About': "# This is a header. This is an *extremely* cool app!"
    # }
)

# Título da página
st.title("Contratos Governo Ceará", anchor="top")
st.divider()

# Sidebar
st.sidebar.header("Modalidade de contrato")
options = ["Todos"]
options.extend([x for x in range(2024, 2013, -1)])
year = st.sidebar.selectbox(
    label="Ano",
    options=options,
    placeholder="Escolha um ano"

)

# Body
st.header("Modalidade de contrato")
df2 = dados_descricao_modalidade(year=year)
grafico2 = px.bar(
    df2,
    x= "descricao_modalidade",
    y= "sum_milhao",
    title= f"Despesa por modalidade de contrato ({year})",
    labels= {"descricao_modalidade": "Modalidade", "sum_milhao": "Milões de R$"},
    color_discrete_sequence = px.colors.sequential.Aggrnyl
)
grafico2

