# Mini-Proyecto Chatbot Gemini (Arquitectura Odoo-like)

Este proyecto está estructurado siguiendo los patrones de un módulo de Odoo para facilitar su escalabilidad y futura integración.

## Estructura de Archivos

```text
.
├── addon_chatbot/              # Carpeta del módulo principal
│   ├── __init__.py             # Inicializador del módulo
│   ├── __manifest__.py        # Metadatos del módulo (estilo Odoo)
│   ├── controllers/            # Controladores de Flask (Rutas)
│   │   └── main.py
│   ├── models/                 # Lógica de negocio y clientes API
│   │   └── gemini_client.py
│   ├── static/                 # Archivos estáticos
│   │   └── src/
│   │       ├── js/
│   │       │   ├── a2ui/       # <-- AQUÍ añadir componentes de A2UI
│   │       │   └── chatbot.js
│   │       └── css/
│   │           └── style.css
│   └── views/
│       └── templates/          # Plantillas HTML
│           └── index.html
├── requirements.txt            # Dependencias de Python
├── run.py                      # Punto de entrada de la aplicación
└── README.md                   # Esta documentación
```

## Instalación y Uso

1. Instalar requerimientos:
   ```bash
   pip install -r requirements.txt
   ```

2. Ejecutar la aplicación:
   ```bash
   python run.py
   ```

## Integración con A2UI
Los componentes de **A2UI** deben añadirse en `addon_chatbot/static/src/js/a2ui/`. Desde allí se pueden escalar los widgets y la interfaz del chatbot de forma modular.
