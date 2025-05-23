
# Agente IGNACIO

**Versión actual:** `v3.4.1`  
**Descripción:** Asistente IA con scraping real, recomendaciones, exportación y análisis de productos más vendidos de Mercado Libre Argentina.

---

## 📦 Estructura del proyecto

```
agente_ignacio_v3_4_1/
├── app/               ← Lógica principal Streamlit
├── components/        ← Gráficos, tablas, visualización
├── core/              ← Motor IA + Scraper real
├── data/              ← Base SQLite
├── utils/             ← Limpieza y helpers
├── requirements.txt   ← Dependencias
├── README.md          ← Este archivo
```

---

## 🔁 Historial de versiones

| Versión | Fecha       | Cambios principales |
|---------|-------------|---------------------|
| v3.0    | 2024-05     | IA, scraping simulado, exportación Excel |
| v3.1    | 2024-05     | Gráficos, GPT-4, SQLite, clave segura |
| v3.2    | 2024-05     | Comparación de fechas, estructura profesional |
| v3.3    | 2025-05-22  | Manejo visual con `st.empty()` |
| v3.4    | 2025-05-22  | Scraping real, entrada dinámica, exportación |
| v3.4.1  | 2025-05-22  | Corrección de importaciones (`__init__.py`) y estructura de paquetes |

---

## 🧠 Requisitos

- Python 3.10+
- streamlit, pandas, openai, requests, plotly, beautifulsoup4, sqlite3

---

## 🛠️ Despliegue (Streamlit Cloud)

1. Subir todo a GitHub
2. Crear nueva app en [https://streamlit.io/cloud](https://streamlit.io/cloud)
3. Archivo principal: `app/app.py`
4. Secrets:
```
OPENAI_API_KEY = "sk-proj-..."
```
5. Deploy!

---

Desarrollado por Diego R. y asistido por IA
