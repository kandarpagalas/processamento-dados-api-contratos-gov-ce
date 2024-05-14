import streamlit as st
import pandas as pd
import collections
import plotly.express as px

from data.dataset_contratos import dados_grafico_linha_assinatura, lista_anos

from st_pages import show_pages_from_config, add_page_title

add_page_title(
    page_title="Exploratória",
    page_icon=":bar_chart:",
    layout="wide",
    initial_sidebar_state="expanded",

    add_icon = True
    )
show_pages_from_config()


st.divider()

# Carrega anos disponíveis no dataset
anos_disponiveis = lista_anos()

# Divide o espaço em colunas
col1, col2 = st.columns([1, 3])
year = "Todos"
with col1:
    nivel_detalhe = st.selectbox(
        label="Nível de detalhe",
        options=["Ano", "Mês"],
        placeholder="Escolha um ano",
    )
    if nivel_detalhe == "Mês":
        # Adiciona a opção "Todos"
        options = ["Todos"]
        options.extend(anos_disponiveis)
        year = st.selectbox(
            label="Filtrar por Ano",
            options=options,
            placeholder="Escolha um ano",
        )


# Carrega dados filtrados
df = dados_grafico_linha_assinatura(year=year, nivel_detalhe = nivel_detalhe)
if year == "Todos":
    leg_year = f"{min(anos_disponiveis)} - {max(anos_disponiveis)}"
else:
    leg_year = year

with col2:

    grafico = px.line(
        df,
        x= "interval",
        y= "sum",
        title= f"Despesa por Período ({leg_year})",
        labels= {"interval": "Período", "sum": "R$"},
        color_discrete_sequence = px.colors.sequential.Aggrnyl
    )
    grafico

with st.expander("Dataframe", expanded=False):
    st.dataframe(df, use_container_width=True)
