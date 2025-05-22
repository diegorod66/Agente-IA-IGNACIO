
# Versión: app.py v3.3
# Fecha: 2025-05-22
# Descripción: Manejo de bloques dinámicos con st.empty() para evitar errores de render

import streamlit as st
from data.db import guardar_busqueda, obtener_comparacion
from core.recomendador_ia import generar_recomendacion
from components.graficos import mostrar_grafico
from utils.helpers import formatear_precios
import pandas as pd

st.set_page_config(page_title="Agente IGNACIO", layout="wide")
st.title("Agente IGNACIO v3.3")

categoria = st.text_input("Ingresá una categoría", value="tecnología")

if st.button("Analizar"):
    with st.spinner("Cargando análisis..."):

        # Simulación de scraping real
        productos = [
            {"Producto": "Notebook Lenovo", "Precio": "$450.000", "Vendidos": 530, "Marca": "Lenovo"},
            {"Producto": "Auriculares JBL", "Precio": "$18.999", "Vendidos": 1200, "Marca": "JBL"},
            {"Producto": "TV Samsung 50''", "Precio": "$305.999", "Vendidos": 800, "Marca": "Samsung"},
        ]
        df = pd.DataFrame(productos)
        df = formatear_precios(df)

        guardar_busqueda(categoria, df)

        tabla_container = st.empty()
        tabla_container.dataframe(df)

        grafico_container = st.empty()
        with grafico_container:
            mostrar_grafico(df)

        ia_container = st.empty()
        with ia_container:
            recomendacion = generar_recomendacion(df)
            st.info(recomendacion)

        comparacion_container = st.empty()
        with comparacion_container:
            comparacion = obtener_comparacion(categoria, df)
            st.subheader("Comparación de precios con búsquedas anteriores")
            st.write(comparacion)
