# Versión: db.py v3.5.0
# Fecha: 2025-05-24
# Descripción: Módulo de base de datos SQLite para guardar y comparar productos

import sqlite3
import pandas as pd
from datetime import datetime

def conectar():
    return sqlite3.connect("productos.db", check_same_thread=False)

def guardar_busqueda(termino, df):
    conn = conectar()
    fecha = datetime.now().isoformat()
    df["fecha"] = fecha
    df["termino"] = termino
    df.to_sql("productos", conn, if_exists="append", index=False)
    conn.close()

def obtener_comparacion(termino, df_actual):
    conn = conectar()
    try:
        df_hist = pd.read_sql(f"SELECT * FROM productos WHERE termino = '{termino}'", conn)
        conn.close()
        if df_hist.empty:
            return "No hay datos históricos para comparar."
        df_actual = df_actual.set_index("Producto")
        df_hist = df_hist.set_index("Producto")
        comparacion = df_actual.join(df_hist, lsuffix='_actual', rsuffix='_hist', how='inner')
        return comparacion[["Precio_num_actual", "Precio_num_hist"]]
    except Exception as e:
        return f"Error en comparación: {str(e)}"