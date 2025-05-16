import sqlite3
import pandas as pd

DB = "productos.db"

def crear_tabla_si_no_existe():
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS productos (
            Producto TEXT,
            Precio TEXT,
            Vendidos TEXT,
            Link TEXT,
            Fecha TEXT,
            Categoría TEXT
        )
    """)
    conn.commit()
    conn.close()

def guardar_en_db(df):
    conn = sqlite3.connect(DB)
    df.to_sql("productos", conn, if_exists="append", index=False)
    conn.close()

def obtener_datos():
    conn = sqlite3.connect(DB)
    df = pd.read_sql("SELECT * FROM productos ORDER BY Fecha DESC LIMIT 100", conn)
    conn.close()
    return df
