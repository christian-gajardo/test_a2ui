# Gemini Chatbot & A2UI Foundation

Este proyecto constituye una base modular para el desarrollo de chatbots integrados con la API de Google Gemini y el sistema de componentes dinámicos A2UI.

## Características

- **Integración con IA**: Conexión con el modelo Gemini (gemini-3-flash-preview).
- **Arquitectura Modular**: Estructura organizada para facilitar el escalamiento y mantenimiento.
- **Generador de Formularios A2UI**: Componente capaz de renderizar formularios HTML a partir de definiciones JSON generadas por la IA.
- **Interfaz Profesional**: Diseño basado en una estética de alto nivel, con enfoque en la usabilidad y un entorno visual sobrio.
- **Backend Flask**: Implementación de servidor eficiente con gestión de variables de entorno.

## Estructura del Proyecto

```text
.
├── chatbot/                # Módulo principal
│   ├── controllers/        # Controladores y lógica de rutas
│   ├── models/             # Gestión de lógica de negocio y cliente Gemini
│   ├── static/             # Recursos estáticos
│   │   └── src/
│   │       ├── js/
│   │       │   ├── a2ui/   # Librería de componentes A2UI
│   │       │   └── chatbot.js
│   │       └── css/
│   └── views/templates/    # Plantillas de la interfaz de usuario
├── .env                    # Configuración de variables críticas
├── run.py                  # Punto de entrada de la aplicación
└── README.md               # Documentación general
```

## Instalación y Uso

### 1. Requisitos
- Python 3.10 o superior.
- API Key de Google Gemini.

### 2. Configuración
Defina su clave en el archivo `.env` en el directorio raíz:
```env
GEMINI_API_KEY=SU_API_KEY_AQUI
```

### 3. Instalación de Dependencias
```bash
pip install -r requirements.txt
```

### 4. Ejecución
Inicie el proceso del servidor:
```bash
python run.py
```
Acceda a la aplicación en `http://127.0.0.1:5000`.

## Funcionamiento de A2UI

El sistema permite la generación de componentes interactivos mediante el procesamiento de respuestas estructuradas de la IA.

- **Procedimiento**: Al solicitar un formulario a través del chat, la IA generará un bloque JSON.
- **Procesamiento**: El motor de renderizado detecta el bloque y construye el componente HTML correspondiente de forma dinámica en la interfaz.

## 🛠️ Guía de Extensión: Añadir Componentes A2UI

Para expandir la librería de componentes A2UI y permitir que la IA los genere, siga estos pasos:

### 1. Definir el Componente Frontend
Cree un nuevo archivo JavaScript en `chatbot/static/src/js/a2ui/`.
- Use una clase con un método estático `render`.
- Asegúrese de que devuelva un elemento del DOM.
- Ejemplo: `chatbot/static/src/js/a2ui/nuevo_componente.js`.

### 2. Actualizar las Instrucciones del Sistema (Backend)
Modifique el archivo `chatbot/models/gemini_client.py`.
- Actualice la variable `system_instruction`.
- Defina la estructura JSON que la IA debe generar para su nuevo componente.
- Ejemplo: ```json:mi_componente { "dato": "valor" } ```.

### 3. Integrar en el Procesador de Mensajes
Modifique `chatbot/static/src/js/chatbot.js`.
- Importe su nuevo componente al inicio del archivo.
- Añada una expresión regular y lógica de detección en la función `addMessage` para capturar el nuevo bloque JSON (ej. `json:mi_componente`).
- Instancie y añada el componente al contenedor de mensajes.

### 4. Estilos Visuales
Añada las reglas CSS necesarias en `chatbot/static/src/css/style.css`.
- Asegúrese de mantener la coherencia con las variables de color globales (`--primary`, `--bg-chat`, etc.).
- Use clases específicas para evitar colisiones de estilo.

### 5. Documentar y Probar
- Actualice el `README.md` con el nuevo componente.
- Reinicie el servidor y solicite a la IA que genere el componente para validar la integración.
