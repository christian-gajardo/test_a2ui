from flask import Flask
from chatbot.controllers.main import chatbot_web
from dotenv import load_dotenv
import os

# Cargar variables de entorno desde .env
load_dotenv()

app = Flask(__name__, 
            static_folder='chatbot/static',
            template_folder='chatbot/views/templates')

# Registrar el blueprint del módulo
app.register_blueprint(chatbot_web)

if __name__ == '__main__':
    app.run(debug=True, port=5000)

