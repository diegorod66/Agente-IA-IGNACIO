# Agente IGNACIO

**Versión actual:** `v3.4.4`  
**Descripción:** Asistente IA con scraping real, recomendaciones, exportación y estructura escalable. Esta versión corrige imports desde subcarpetas.

---

## 🔁 Historial de versiones

| Versión | Fecha       | Cambios principales |
|---------|-------------|---------------------|
| v3.0    | 2024-05     | IA, scraping simulado, exportación Excel |
| v3.1    | 2024-05     | Gráficos, GPT-4, SQLite, clave segura |
| v3.2    | 2024-05     | Comparación de fechas, estructura profesional |
| v3.3    | 2025-05-22  | Manejo visual con `st.empty()` |
| v3.4    | 2025-05-22  | Scraping real, entrada dinámica, exportación |
| v3.4.1  | 2025-05-22  | Fix de imports y estructura de paquetes |
| v3.4.2  | 2025-05-22  | Fix visual con `st.container()` |
| v3.4.3  | 2025-05-23  | Fix en requirements.txt (sqlite3 eliminado) |
| v3.4.4  | 2025-05-23  | Fix de importación de módulos (sys.path) |

---

## 🛠️ Despliegue

1. Archivo principal: `app/app.py`
2. Repositorio: GitHub (estructura escalable)
3. Secrets:
```
OPENAI_API_KEY = "tu-clave"
```