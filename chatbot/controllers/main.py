# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, request, jsonify
from chatbot.models.gemini_client import GeminiClient

# Definición del Blueprint para organizar las rutas del chatbot
chatbot_web = Blueprint('chatbot_web', __name__)

# Instancia global del cliente Gemini
gemini = GeminiClient()

@chatbot_web.route('/')
def index():
    """Ruta principal que sirve la interfaz de usuario."""
    return render_template('index.html')

@chatbot_web.route('/chat', methods=['POST'])
def chat():
    """
    Endpoint de la API que procesa los mensajes del usuario.
    Recibe un JSON con el campo 'message' y devuelve la respuesta de la IA.
    """
    data = request.json
    user_message = data.get('message')
    
    if not user_message:
        return jsonify({'error': 'No se proporcionó ningún mensaje'}), 400
        
    # Obtiene la respuesta de la lógica de Gemini
    response = gemini.send_message(user_message)
    
    return jsonify({'response': response})


