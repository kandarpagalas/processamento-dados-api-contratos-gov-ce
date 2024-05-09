import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

df = pd.read_csv("contratos_2020.csv", low_memory=False)

df = df.fillna(0)


# pd.to_datetime('2018-10-26 12:00:00.0000000011',
#                format='%Y-%m-%dT%H:%M:%S.%f')

# '2018-10-26 12:00:00.0000000011'
# "2018-03-28T10:27:38.707-03:00"

df["data_assinatura"] = pd.to_datetime(df["data_assinatura"])
df["data_processamento"] = pd.to_datetime(df["data_processamento"])
df["data_termino"] = pd.to_datetime(df["data_termino"])
df["data_publicacao_doe"] = pd.to_datetime(df["data_publicacao_doe"], format="ISO8601", errors = 'coerce')
df["data_auditoria"] = pd.to_datetime(df["data_auditoria"], format="%Y-%m-%d", errors = 'coerce')
df["data_termino_original"] = pd.to_datetime(df["data_termino_original"], errors = 'coerce')
df["data_inicio"] = pd.to_datetime(df["data_inicio"], errors = 'coerce')

df["data_rescisao"] = pd.to_datetime(df["data_rescisao"], utc=False,  errors = 'coerce')
# df["data_finalizacao_prestacao_contas"] = pd.to_datetime(df["data_finalizacao_prestacao_contas"], errors = 'coerce')


for d in df["data_rescisao"].unique():
    print(d)
# print(df["data_publicacao_doe"].unique())


datas = [
    'data_assinatura', 
    'data_processamento', 
    'data_termino', 
    'data_publicacao_portal', 
    'data_publicacao_doe', 
    'data_auditoria', 
    'data_termino_original', 
    'data_inicio', 
    'data_rescisao', 
    'data_finalizacao_prestacao_contas'
    ]


# print(df[datas].sample(10))

