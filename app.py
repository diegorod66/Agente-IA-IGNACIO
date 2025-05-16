
import streamlit as st
import pandas as pd
from scraper import obtener_productos
from recomendador_ia import generar_recomendacion

st.set_page_config(page_title="Agente IGNACIO", layout="wide")
st.title("🤖 Agente IGNACIO - Análisis de Mercado Libre Argentina")

categoria = st.text_input("🔍 Ingresá una categoría de productos (ej: tecnología, electrodomésticos)", value="tecnología")

if st.button("Analizar"):
    with st.spinner("Obteniendo productos más vendidos..."):
        df = obtener_productos(categoria)
        st.success(f"Se encontraron {len(df)} productos.")
        st.dataframe(df)

        # Exportar a Excel
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button("📥 Descargar Excel", csv, "productos.csv", "text/csv")

        # Clave OpenAI
        st.subheader("💡 Recomendación del Agente IA")
        api_key = st.text_input("🔑 Ingresá tu clave OpenAI (no se guarda)", type="password")
        if api_key:
            respuesta = generar_recomendacion(df, api_key)
            st.info(respuesta)
