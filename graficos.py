import plotly.express as px

def generar_grafico(df):
    fig = px.bar(df, x="Producto", y=df["Precio"].str.replace("$ ", "").str.replace(".", "").astype(float),
                 color="Producto", title="Precios por Producto")
    return fig
