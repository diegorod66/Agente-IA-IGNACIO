import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generar_recomendacion(df):
    productos = df.head(5).to_dict(orient='records')
    prompt = f"Analizá estos productos:\n{productos}\n¿Qué me recomendás revender con buen margen?"
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error al consultar la IA: {str(e)}"
