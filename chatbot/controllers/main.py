# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, request, jsonify
from chatbot.models.gemini_client import GeminiClient

chatbot_web = Blueprint('chatbot_web', __name__)
gemini = GeminiClient()

@chatbot_web.route('/')
def index():
    return render_template('index.html')

@chatbot_web.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('message')
    
    if not user_message:
        return jsonify({'error': 'No message provided'}), 400
        
    response = gemini.send_message(user_message)
    return jsonify({'response': response})

