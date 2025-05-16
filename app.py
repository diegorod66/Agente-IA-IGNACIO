import streamlit as st
import pandas as pd
from scraper import obtener_productos
from db import guardar_en_db, crear_tabla_si_no_existe, obtener_datos
from recomendador_ia import generar_recomendacion
from graficos import generar_grafico

st.set_page_config(page_title="Agente IGNACIO", layout="wide")
st.title("🤖 Agente IGNACIO - Análisis de Mercado Libre Argentina")

crear_tabla_si_no_existe()

categoria = st.text_input("🔍 Ingresá una categoría (ej: tecnología)", value="tecnología")

if st.button("Analizar"):
    with st.spinner("Obteniendo productos..."):
        df = obtener_productos(categoria)
        guardar_en_db(df, categoria)
        st.success(f"{len(df)} productos analizados.")
        st.dataframe(df)

        csv = df.to_csv(index=False).encode("utf-8")
        st.download_button("📥 Descargar Excel", csv, "productos.csv", "text/csv")

        st.subheader("📈 Evolución de Precios")
        fig = generar_grafico(df)
        st.plotly_chart(fig, use_container_width=True)

        st.subheader("💡 Recomendación del Agente IA")
        respuesta = generar_recomendacion(df)
        st.info(respuesta)

st.divider()
st.subheader("📊 Historial Guardado")
historico = obtener_datos()
st.dataframe(historico)
