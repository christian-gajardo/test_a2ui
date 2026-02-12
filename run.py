from flask import Flask
from addon_chatbot.controllers.main import chatbot_web

app = Flask(__name__)

# Registrar el blueprint del módulo
app.register_blueprint(chatbot_web)

@app.route('/')
def index():
    return "Base de Chatbot Gemini lista (Arquitectura Odoo-like)"

if __name__ == '__main__':
    app.run(debug=True, port=5000)
