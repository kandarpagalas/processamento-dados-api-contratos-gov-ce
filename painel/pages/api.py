import os
import streamlit as st
import pandas as pd


from st_pages import show_pages_from_config, add_page_title

add_page_title(
    page_title="API",
    page_icon=":bar_chart:",
    layout="wide",
    initial_sidebar_state="expanded",


    )
show_pages_from_config()


mkd = """
Dados abertos do Governo do Estado do Ceará

### Descrição
API disponibilizada pelo Goverdo do Estado do Ceará, com o objetivo de dar transparência.
Permite consulta a contratos firmado pelo Estado a partir de 2007.

### Endpoint: 
"https://api-dados-abertos.cearatransparente.ce.gov.br/transparencia/contratos/contratos"

"""


st.markdown(mkd)