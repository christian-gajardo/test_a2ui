# -*- coding: utf-8 -*-
import google.generativeai as genai
import os

class GeminiClient:
    """
    Clase para gestionar la comunicación con la API de Gemini.
    """
    def __init__(self, api_key=None):
        self.api_key = api_key or os.getenv("GEMINI_API_KEY")
        if self.api_key:
            genai.configure(api_key=self.api_key)
            self.model = genai.GenerativeModel('gemini-3-flash-preview')
        else:
            self.model = None

    def send_message(self, message):
        if not self.model:
            return "Error: GEMINI_API_KEY no configurada."
        
        try:
            response = self.model.generate_content(message)
            return response.text
        except Exception as e:
            return f"Error al comunicarse con Gemini: {str(e)}"

