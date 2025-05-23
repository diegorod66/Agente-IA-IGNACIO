
# Versión: scraper.py v3.4.1
# Fecha: 2025-05-22
# Descripción: Scraping real desde Mercado Libre con categoría y cantidad configurables (v3.4.1)

import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

def obtener_productos(categoria: str, cantidad: int = 20):
    productos = []
    url_base = "https://listado.mercadolibre.com.ar/"
    categoria = categoria.replace(" ", "-")
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }

    for offset in range(0, cantidad, 48):
        url = f"{url_base}{categoria}_Desde_{offset + 1}_NoIndex_True"
        response = requests.get(url, headers=headers)

        if response.status_code != 200:
            break

        soup = BeautifulSoup(response.text, "html.parser")
        items = soup.select("li.ui-search-layout__item")

        for item in items:
            if len(productos) >= cantidad:
                break

            try:
                nombre = item.select_one("h2.ui-search-item__title").get_text(strip=True)
                precio = item.select_one("span.price-tag-fraction").get_text(strip=True)
                link = item.select_one("a.ui-search-link")["href"]
                vendidos = item.select_one("span.ui-search-item__group__element.ui-search-item__variations-text")
                marca = item.select_one("span.ui-search-item__brand-discoverability__label")
                productos.append({
                    "Producto": nombre,
                    "Precio": f"${precio}",
                    "Vendidos": vendidos.get_text(strip=True) if vendidos else "No informado",
                    "Marca": marca.get_text(strip=True) if marca else "No informado",
                    "Link": link
                })
            except Exception:
                continue

        time.sleep(1.5)

    return pd.DataFrame(productos)
