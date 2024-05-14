import os
import streamlit as st
import pandas as pd
import collections
import plotly.express as px

from st_pages import show_pages_from_config, add_page_title

add_page_title(
    page_title="Home",
    page_icon=":bar_chart:",
    layout="wide",
    initial_sidebar_state="expanded",


    )
show_pages_from_config()



with open("/home/kandarpa/Github/Z103_trabalho_final/README.md", "r", encoding="utf-8") as f:
    readme = f.read()

    # Gráfico 01
    st.markdown(readme)


col1, col2, col3 = st.columns(3)
col1.metric(label="Temperature", value="70 °F", delta="-1.2 °F")
col2.metric(label="Temperature", value="70 °F", delta="1.2 °F")
col3.metric(label="Temperature", value="70 °F", delta="1.2 °F")