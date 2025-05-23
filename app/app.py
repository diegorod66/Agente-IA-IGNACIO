
# Versión: app.py v3.4
# Fecha: 2025-05-22
# Descripción: Integración de scraping real con selección dinámica de categoría y cantidad

import streamlit as st
from core.scraper import obtener_productos
from data.db import guardar_busqueda, obtener_comparacion
from core.recomendador_ia import generar_recomendacion
from components.graficos import mostrar_grafico
from utils.helpers import formatear_precios
import pandas as pd

st.set_page_config(page_title="Agente IGNACIO", layout="wide")
st.title("Agente IGNACIO v3.4")

categoria = st.text_input("🔍 Ingresá la categoría de productos", value="tecnología")
cantidad = st.number_input("📦 Cantidad de productos a obtener", min_value=1, max_value=200, value=20)

if st.button("Analizar productos"):
    with st.spinner("Obteniendo resultados desde Mercado Libre..."):
        df = obtener_productos(categoria, cantidad)
        if df.empty:
            st.warning("No se encontraron productos. Verificá la categoría ingresada.")
        else:
            df = formatear_precios(df)
            guardar_busqueda(categoria, df)

            st.subheader("📋 Resultados del scraping")
            st.dataframe(df)

            st.download_button("📥 Exportar a Excel", data=df.to_csv(index=False), file_name="productos.csv")

            mostrar_grafico(df)

            st.subheader("🤖 Recomendación del Agente IA")
            st.info(generar_recomendacion(df))

            st.subheader("📈 Comparación con búsquedas anteriores")
            st.write(obtener_comparacion(categoria, df))
