
import streamlit as st
from data.db import guardar_busqueda, obtener_comparacion
from core.recomendador_ia import generar_recomendacion
from components.graficos import mostrar_grafico
from utils.helpers import formatear_precios
import pandas as pd

st.title("Agente IGNACIO v3.2")
categoria = st.text_input("Ingresá una categoría", value="tecnología")

if st.button("Analizar"):
    # Simulación de scraping (debería conectarse a scraper real)
    productos = [
        {"Producto": "Notebook Lenovo", "Precio": "$450.000", "Vendidos": 530, "Marca": "Lenovo"},
        {"Producto": "Auriculares JBL", "Precio": "$18.999", "Vendidos": 1200, "Marca": "JBL"},
        {"Producto": "TV Samsung 50''", "Precio": "$305.999", "Vendidos": 800, "Marca": "Samsung"},
    ]
    df = pd.DataFrame(productos)
    df = formatear_precios(df)
    guardar_busqueda(categoria, df)
    st.dataframe(df)
    mostrar_grafico(df)
    recomendacion = generar_recomendacion(df)
    st.info(recomendacion)
    comparacion = obtener_comparacion(categoria, df)
    st.write(comparacion)
