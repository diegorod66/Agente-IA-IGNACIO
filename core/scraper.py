# core/scraper.py v3.5.3 — Scraping robusto + logging para depuración
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import unicodedata
import streamlit as st

def normalizar_termino(termino):
    nfkd = unicodedata.normalize('NFKD', termino)
    sin_tildes = "".join([c for c in nfkd if not unicodedata.combining(c)])
    return sin_tildes.lower().replace(" ", "-")

def obtener_productos(termino: str, cantidad: int = 20):
    productos = []
    url_base = "https://listado.mercadolibre.com.ar/"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    term_norm = normalizar_termino(termino)

    # 1er intento: URL tradicional
    for offset in range(0, cantidad, 48):
        url = f"{url_base}{term_norm}_Desde_{offset+1}_NoIndex_True"
        st.write(f"Intentando URL: {url}")
        response = requests.get(url, headers=headers)
        st.write(f"Código de estado: {response.status_code}")
        if response.status_code != 200:
            break

        soup = BeautifulSoup(response.text, "html.parser")
        items = soup.select("li.ui-search-layout__item")
        st.write(f"Productos encontrados en esta página: {len(items)}")
        for item in items:
            if len(productos) >= cantidad:
                break
            try:
                # Nombre
                nombre = item.select_one("h2.ui-search-item__title")
                if not nombre:
                    continue
                nombre = nombre.get_text(strip=True)

                # Precio
                precio = item.select_one("span.price-tag-fraction")
                if not precio:
                    continue
                precio = precio.get_text(strip=True)

                # Link
                link_tag = item.select_one("a.ui-search-link")
                if not link_tag:
                    continue
                link = link_tag["href"]

                # Vendidos y Marca (opcionales)
                vendidos = item.select_one("span.ui-search-item__group__element.ui-search-item__variations-text")
                marca = item.select_one("span.ui-search-item__brand-discoverability__label")

                productos.append({
                    "Producto": nombre,
                    "Precio": f"${precio}",
                    "Vendidos": vendidos.get_text(strip=True) if vendidos else "No informado",
                    "Marca": marca.get_text(strip=True) if marca else "No informado",
                    "Link": link
                })
            except Exception as e:
                st.write(f"Error inesperado al parsear item: {e}")
                continue
        if productos:
            break
        time.sleep(1.2)

    # 2do intento: búsqueda general (misma lógica)
    if not productos:
        url2 = f"https://www.mercadolibre.com.ar/jm/search?as_word={termino.replace(' ', '+')}"
        st.write(f"Intentando URL alternativa: {url2}")
        response = requests.get(url2, headers=headers)
        st.write(f"Código de estado alternativo: {response.status_code}")
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            items = soup.select("li.ui-search-layout__item")
            st.write(f"Productos encontrados en alternativa: {len(items)}")
            for item in items:
                if len(productos) >= cantidad:
                    break
                try:
                    nombre = item.select_one("h2.ui-search-item__title")
                    if not nombre:
                        continue
                    nombre = nombre.get_text(strip=True)

                    precio = item.select_one("span.price-tag-fraction")
                    if not precio:
                        continue
                    precio = precio.get_text(strip=True)

                    link_tag = item.select_one("a.ui-search-link")
                    if not link_tag:
                        continue
                    link = link_tag["href"]

                    vendidos = item.select_one("span.ui-search-item__group__element.ui-search-item__variations-text")
                    marca = item.select_one("span.ui-search-item__brand-discoverability__label")

                    productos.append({
                        "Producto": nombre,
                        "Precio": f"${precio}",
                        "Vendidos": vendidos.get_text(strip=True) if vendidos else "No informado",
                        "Marca": marca.get_text(strip=True) if marca else "No informado",
                        "Link": link
                    })
                except Exception as e:
                    st.write(f"Error inesperado al parsear item alternativa: {e}")
                    continue
            time.sleep(1.2)
    st.write(f"Total de productos obtenidos: {len(productos)}")
    return pd.DataFrame(productos)

