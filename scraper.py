import pandas as pd

def obtener_productos(categoria):
    # Simulación de scraping real
    productos = [
        {"Producto": "Auriculares Bluetooth", "Precio": 18999, "Vendidos": 1200, "Marca": "JBL", "Link": "https://mercadolibre.com.ar/item1"},
        {"Producto": "Notebook Lenovo i5", "Precio": 459999, "Vendidos": 540, "Marca": "Lenovo", "Link": "https://mercadolibre.com.ar/item2"},
        {"Producto": "Smart TV 50'' 4K", "Precio": 309999, "Vendidos": 820, "Marca": "Samsung", "Link": "https://mercadolibre.com.ar/item3"},
    ]
    return pd.DataFrame(productos)
