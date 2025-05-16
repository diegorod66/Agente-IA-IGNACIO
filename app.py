import streamlit as st
import pandas as pd
from scraper import buscar_productos
from db import guardar_en_db, crear_tabla_si_no_existe, obtener_datos
from recomendador_ia import generar_recomendacion
from graficos import generar_grafico

st.set_page_config(page_title="Agente IGNACIO", layout="wide")
st.title("🤖 Agente IGNACIO - Dashboard de Análisis de Mercado Libre")

crear_tabla_si_no_existe()

query = st.text_input("🔍 Ingresá producto, marca o categoría", value="tecnología")

if st.button("Buscar"):
    with st.spinner("Buscando productos..."):
        df = buscar_productos(query)
        guardar_en_db(df)
        st.success(f"{len(df)} productos encontrados.")
        st.dataframe(df)

        csv = df.to_csv(index=False).encode("utf-8")
        st.download_button("📥 Descargar Excel", csv, "productos.csv", "text/csv")

        st.subheader("📈 Gráfico de Precios")
        st.plotly_chart(generar_grafico(df), use_container_width=True)

        st.subheader("💡 Recomendación de IA")
        recomendacion = generar_recomendacion(df)
        st.info(recomendacion)

st.divider()
st.subheader("📊 Historial Reciente")
st.dataframe(obtener_datos())
