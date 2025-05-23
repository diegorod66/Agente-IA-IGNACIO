# Versión: app.py v3.5.1
# Fecha: 2025-05-24
# Descripción: App con scraping robusto, gráfica, IA y exportación Excel

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from core.scraper import obtener_productos
from data.db import guardar_busqueda, obtener_comparacion
from core.recomendador_ia import generar_recomendacion
from components.graficos import mostrar_grafico
from utils.helpers import formatear_precios
import pandas as pd

st.set_page_config(page_title="Agente IGNACIO", layout="wide")
st.title("Agente IGNACIO v3.5.1")

termino = st.text_input("🔍 Ingresá el término de búsqueda", value="tecnología")
cantidad = st.number_input("📦 Cantidad de productos a obtener", min_value=1, max_value=200, value=20)

if st.button("Analizar productos"):
    with st.spinner("Obteniendo resultados desde Mercado Libre..."):
        df = obtener_productos(termino, cantidad)
        if df.empty:
            st.warning("No se encontraron productos. Verificá el término ingresado.")
        else:
            df = formatear_precios(df)
            guardar_busqueda(termino, df)

            with st.container():
                st.subheader("📋 Resultados del scraping")
                st.dataframe(df)

            with st.container():
                st.download_button("📥 Exportar a Excel", data=df.to_csv(index=False), file_name="productos.csv")

            with st.container():
                mostrar_grafico(df)

            with st.container():
                st.subheader("🤖 Recomendación del Agente IA")
                st.info(generar_recomendacion(df))

            with st.container():
                st.subheader("📈 Comparación con búsquedas anteriores")
                st.write(obtener_comparacion(termino, df))