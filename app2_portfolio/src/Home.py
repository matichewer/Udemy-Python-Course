import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Matias's Portfolio",
    page_icon="🧾",
    layout="wide",
    # initial_sidebar_state="auto",
)

col1, col2 = st.columns(2)

with col1:
    st.image(
        "https://avatars.githubusercontent.com/u/48109018?s=400&u=4f8d102cc44fd5494fcf43aa088d31520f2d8d3d&v=4",
        width=400,
    )

with col2:
    st.title("Matias David Schwerdt")
    content_description_profile = """
    Hi, I am Matias David Schwerdt, a software engineer student at the National University of the South.
    This is a portfolio of my projects.
    """
    st.info(content_description_profile)


content_introduce_apps = """
Below you can find some apps I have made.
"""
st.write(content_introduce_apps)


col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5]) # ancho de las columnas

df = pd.read_csv("db/data.csv", sep=";")
df_to_show = df[df["show"] == True]
mid_rows = len(df_to_show) // 2 # division entera
#print(f"Division entera: {mid_rows}")

with col3:
    for index, row in df_to_show[:mid_rows].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"], width=300)
        url = row["url"]
        st.write(f"[Source Code]({ row['url'] })")

with col4:
    for index, row in df_to_show[mid_rows:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"], width=300)
        st.write(f"[Source Code]({ row['url'] })")
