import pandas as pd
from datetime import datetime

def obtener_productos(categoria):
    productos = [
        {"Producto": "Auriculares Bluetooth", "Precio": 18999, "Vendidos": 1200, "Marca": "JBL", "Link": "https://ml.com/item1"},
        {"Producto": "Notebook Lenovo i5", "Precio": 459999, "Vendidos": 540, "Marca": "Lenovo", "Link": "https://ml.com/item2"},
        {"Producto": "Smart TV 50'' 4K", "Precio": 309999, "Vendidos": 820, "Marca": "Samsung", "Link": "https://ml.com/item3"},
    ]
    df = pd.DataFrame(productos)
    df["Fecha"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    df["Categoría"] = categoria
    return df
