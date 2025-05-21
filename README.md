
# Agente IGNACIO

**Versión actual:** `v3.2`  
**Descripción:** Asistente IA para análisis inteligente de productos más vendidos en Mercado Libre Argentina. Diseñado para detectar oportunidades de reventa, realizar comparaciones históricas y generar recomendaciones automáticas basadas en IA (GPT-4).

---

## 📦 Estructura del proyecto

```
agente_ignacio_v3_2/
├── app/               ← Lógica principal Streamlit
├── components/        ← Gráficos, tablas, visualización
├── core/              ← Motor IA y análisis inteligente
├── data/              ← Conexión a base de datos (SQLite)
├── utils/             ← Funciones auxiliares
├── requirements.txt   ← Dependencias
├── README.md          ← Este archivo
```

---

## 🔁 Historial de versiones

| Versión | Fecha     | Cambios principales |
|---------|-----------|---------------------|
| v3.0    | 2024-05   | Motor IA funcional, scraping real, exportación Excel |
| v3.1    | 2024-05   | Gráficos, GPT-4, clave segura, base SQLite inicial |
| v3.2    | 2024-05   | Comparación de precios entre fechas + estructura profesional |

---

## ⚙️ Instrucciones de despliegue (Streamlit Cloud)

1. Crear un repositorio en GitHub (ej. `Agente-IA-IGNACIO`)
2. Subir todos los archivos extraídos de este proyecto
3. Ir a [https://streamlit.io/cloud](https://streamlit.io/cloud) e iniciar sesión
4. Hacer clic en "New app" y seleccionar:
   - Repositorio: `Agente-IA-IGNACIO`
   - Archivo principal: `app/app.py`
5. En "Secrets" agregar:
```
OPENAI_API_KEY = "sk-proj-tu-clave"
```
6. Hacer clic en `Deploy` y ¡listo!

---

## 🧠 Requisitos técnicos

- Python 3.10+
- Bibliotecas: streamlit, pandas, openai, sqlite3, plotly, requests

---

## 📌 Próximos hitos (v3.3+)

- Integración con WhatsApp
- Alertas automáticas
- Dashboard de configuración por usuario
- Comparativa visual entre productos y fechas
- Exportación a PDF

---

Desarrollado por Diego R. y asistido por IA ✨
