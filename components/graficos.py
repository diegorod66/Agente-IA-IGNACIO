# Versión: graficos.py v3.5.1
# Fecha: 2025-05-24
# Descripción: Visualización de precios con Plotly

import plotly.express as px
import streamlit as st

def mostrar_grafico(df):
    if "Precio_num" not in df.columns:
        st.warning("No hay columna de precios numéricos para graficar.")
        return
    fig = px.bar(df, x="Producto", y="Precio_num", title="Precios de productos")
    st.plotly_chart(fig)