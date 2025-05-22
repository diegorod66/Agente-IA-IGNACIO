
# Agente IGNACIO

**Versión actual:** `v3.3`  
**Descripción:** Asistente IA para análisis de productos más vendidos en Mercado Libre. Realiza scraping real, análisis histórico, recomendaciones por IA, comparación de precios y exportación de datos.

---

## 📦 Estructura del proyecto

```
agente_ignacio_v3_3/
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

| Versión | Fecha       | Cambios principales |
|---------|-------------|---------------------|
| v3.0    | 2024-05     | Motor IA, scraping real, exportación Excel |
| v3.1    | 2024-05     | Gráficos, GPT-4, BD SQLite, clave segura |
| v3.2    | 2024-05     | Comparación de precios entre fechas, estructura profesional |
| v3.3    | 2025-05-22  | Manejo de errores visuales, versionado por archivo, estructura validada |

---

## ⚙️ Instrucciones de despliegue (Streamlit Cloud)

1. Crear repositorio en GitHub
2. Subir todos los archivos extraídos
3. Entrar a [https://streamlit.io/cloud](https://streamlit.io/cloud)
4. Crear nueva app:
   - Repositorio: `Agente-IA-IGNACIO`
   - Archivo principal: `app/app.py`
5. En "Secrets" agregar:
```
OPENAI_API_KEY = "sk-proj-tu-clave"
```
6. Hacer clic en `Deploy`

---

## 🧠 Requisitos técnicos

- Python 3.10+
- Bibliotecas: streamlit, pandas, openai, plotly, sqlite3, requests

---

## 🚀 Próximas versiones

- v3.4: Alertas automáticas
- v3.5: Integración con WhatsApp Cloud API
- v4.0: Panel admin + filtros configurables + usuarios

Desarrollado por Diego R. y asistido por IA
