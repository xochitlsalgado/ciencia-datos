import streamlit as st
import pandas as pd 
st.title("Actividad")
st.write("Xochitl Salgado")
dataframe = pd.read_csv("https://raw.githubusercontent.com/adsoftsito/ciencia-datos/refs/heads/main/titanic.csv")
st.dataframe(dataframe)
