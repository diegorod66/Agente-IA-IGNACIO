import plotly.express as px

def generar_grafico(df):
    fig = px.bar(df, x="Producto", y="Precio", color="Marca", title="Precios por Producto")
    return fig
