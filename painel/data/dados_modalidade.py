import streamlit as st
import pandas as pd

from .dataset_contratos import importa_dados_parket

@st.cache_data(ttl="1h")
def importa_dados(year = None):
    df = importa_dados_parket()
    df["year"] = df['data_assinatura'].dt.year
    df["month"] = df['data_assinatura'].dt.month
    df["year-month"] = df['data_assinatura'].dt.strftime('%Y-%m')

    if year is None:
        return df
    
    df_filtered = df[df["year"] == year]
    return df_filtered

@st.cache_data
def lista_anos():
    df = importa_dados()
    df = df.sort_values(by="year", ascending=False)
    years = list(df["year"].unique())
    return years



@st.cache_data
def dados_grafico_descricao_modalidade(year = "Todos"):
    if year == "Todos":
        df = importa_dados()
    else:
        df = importa_dados(year=year)

    df_modalidade = df.groupby("descricao_modalidade", observed=True)["calculated_valor_pago"]\
    .agg(["mean", "sum"]).reset_index()\
    .sort_values(by="sum", ascending=False)
    df_modalidade["sum_milhao"] = round(df_modalidade["sum"] / 10**6, 2)
    df_modalidade["sum_bilhao"] = round(df_modalidade["sum"] / 10**9, 2)
    return df_modalidade