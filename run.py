from flask import Flask
from chatbot.controllers.main import chatbot_web
from dotenv import load_dotenv
import os

# Carga las variables de entorno definidas en el archivo .env (como GEMINI_API_KEY)
load_dotenv()

# Inicialización de la aplicación Flask
# Se configuran las carpetas de estáticos y plantillas dentro del módulo 'chatbot'
app = Flask(__name__, 
            static_folder='chatbot/static',
            template_folder='chatbot/views/templates')

# Registro del Blueprint del controlador del chatbot
app.register_blueprint(chatbot_web)

if __name__ == '__main__':
    # Ejecución del servidor de desarrollo con modo debug activado en el puerto 5000
    app.run(debug=True, port=5000)


