
import plotly.express as px
import streamlit as st

def mostrar_grafico(df):
    if "Precio_num" not in df.columns:
        st.warning("No hay columna de precios numéricos para graficar.")
        return
    fig = px.bar(df, x="Producto", y="Precio_num", title="Precios de productos")
    st.plotly_chart(fig)
