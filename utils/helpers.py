# Versión: helpers.py v3.4.1
# Fecha: 2025-05-22
# Descripción: Formateo de precios para scraping de ML

def formatear_precios(df):
    df["Precio_num"] = (
        df["Precio"]
        .astype(str)
        .str.replace("$", "", regex=False)
        .str.replace(".", "", regex=False)
        .str.replace(",", ".", regex=False)
        .str.replace(" ", "", regex=False)
        .astype(float)
    )
    return df