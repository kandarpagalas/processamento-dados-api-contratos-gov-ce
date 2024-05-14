import streamlit as st
import pandas as pd

### Geral
@st.cache_data(ttl="1h")
def importa_dados_parquet(filename="/home/kandarpa/Github/Z103_trabalho_final/painel/data/dataset.parquet"):
    df = pd.read_parquet(filename)

    df["year"] = df['data_assinatura'].dt.year
    df["year-month"] = df['data_assinatura'].dt.strftime('%Y-%m')
    return df

@st.cache_data
def lista_anos():
    df = importa_dados_parquet()
    df = df.sort_values(by="year", ascending=False)
    years = list(df["year"].unique())
    return years


## Modalidade
@st.cache_data
def dados_grafico_descricao_modalidade(year = "Todos"):
    df = importa_dados_parquet()

    if year != "Todos":
        df = df[df["year"] == year]

    df = df.groupby("descricao_modalidade", observed=True)["calculated_valor_pago"]\
    .agg(["mean", "sum"]).reset_index()\
    .sort_values(by="sum", ascending=False)

    df["sum_milhao"] = round(df["sum"] / 10**6, 2)
    return df

## Situação
@st.cache_data
def dados_grafico_descricao_situacao(year = "Todos"):
    df = importa_dados_parquet()

    if year != "Todos":
        df = df[df["year"] == year]

    df = df.groupby("descricao_situacao", observed=True)["calculated_valor_pago"]\
    .agg(["mean", "sum"]).reset_index()\
    .sort_values(by="sum", ascending=False)

    df["sum_milhao"] = round(df["sum"] / 10**6, 2)
    return df


# Assinaturas
@st.cache_data
def dados_grafico_linha_assinatura(year = "Todos", nivel_detalhe = "Ano"):
    df = importa_dados_parquet()

    if year != "Todos":
        df = df[df["year"] == year]

    if nivel_detalhe == "Ano":
        df = df.groupby("year", observed=True)["calculated_valor_pago"]\
        .agg(["mean", "sum"]).reset_index()\
        .sort_values(by="year", ascending=True)

        df["interval"] = df["year"]
        return df
    
    if nivel_detalhe == "Mês":
        df = df.groupby("year-month", observed=True)["calculated_valor_pago"]\
        .agg(["mean", "sum"]).reset_index()\
        .sort_values(by="year-month", ascending=True)

        df["interval"] = df["year-month"]
        return df

    
