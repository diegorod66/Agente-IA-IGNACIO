
import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generar_recomendacion(df):
    productos = df.head(5).to_dict(orient='records')
    prompt = f"Actuá como un asesor de negocios. Analizá estos productos:\n{productos}\n¿Qué me recomendás revender por rentabilidad y demanda?"
    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error al consultar la IA: {str(e)}"
