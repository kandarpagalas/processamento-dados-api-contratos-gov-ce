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
    st.markdown(readme)
