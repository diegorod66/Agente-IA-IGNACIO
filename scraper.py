import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

def buscar_productos(query):
    headers = {"User-Agent": "Mozilla/5.0"}
    url = f"https://listado.mercadolibre.com.ar/{query.replace(' ', '-')}"
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    resultados = []
    items = soup.select("li.ui-search-layout__item")

    for item in items[:10]:
        try:
            titulo = item.select_one("h2.ui-search-item__title").text.strip()
            precio_elem = item.select_one("span.price-tag-fraction")
            precio = f"$ {int(precio_elem.text.replace('.', '')):,}".replace(",", ".")

            link = item.select_one("a.ui-search-link")["href"]
            link_html = f"[Abrir]({link})"

            vendidos = "-"
            vendido_elem = item.select_one("span.ui-search-item__group__element.ui-search-item__variations-text")
            if vendido_elem:
                vendidos = vendido_elem.text.strip()

            resultados.append({
                "Producto": titulo,
                "Precio": precio,
                "Vendidos": vendidos,
                "Link": link_html,
                "Fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "Categoría": query
            })
        except Exception:
            continue

    return pd.DataFrame(resultados)
