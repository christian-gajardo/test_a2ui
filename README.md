# Mini-Proyecto Chatbot Gemini (A2UI Foundation)

Aplicación de chat moderna y funcional construida con **Flask**, **JavaScript** y la **API de Gemini**.

## Estructura del Proyecto

```text
.
├── chatbot/                    # Módulo de la aplicación
│   ├── controllers/            # Rutas (Flask Blueprints)
│   ├── models/                 # Lógica de GeminiClient
│   ├── static/                 # CSS y JS premium
│   └── views/templates/        # Interfaz de usuario (HTML)
├── .env                        # Configuración de variables de entorno
├── run.py                      # Servidor principal
└── requirements.txt            # Dependencias
```

## Configuración

1. Crea un archivo `.env` en la raíz (si no existe) y añade tu API Key de Gemini:
   ```env
   GEMINI_API_KEY=tu_api_key_aqui
   ```

2. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

## Ejecución

Inicia el servidor:
```bash
python run.py
```
Abre tu navegador en `http://127.0.0.1:5000`.

## Escalabilidad con A2UI
La arquitectura modular permite añadir nuevos componentes en `chatbot/static/src/js/a2ui/`. El frontend ya utiliza variables CSS y una estructura limpia preparada para componentes reutilizables.

