
import openai

def generar_recomendacion(df, api_key):
    productos = df.head(5).to_dict(orient='records')
    prompt = f"Analizá estos productos para reventa:
{productos}
¿Qué me recomendás comprar para revender con buen margen?"

    openai.api_key = os.getenv("OPENAI_API_KEY")
    try:
        respuesta = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return respuesta.choices[0].message.content
    except Exception as e:
        return f"Error al consultar la IA: {str(e)}"
