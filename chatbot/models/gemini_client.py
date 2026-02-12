# -*- coding: utf-8 -*-
import google.generativeai as genai
import os

class GeminiClient:
    """
    Cliente para la API de Gemini de Google.
    Esta clase gestiona la configuración del modelo y la generación de contenido,
    incluyendo instrucciones específicas para la creación de componentes A2UI.
    """
    def __init__(self, api_key=None):
        # Obtiene la API Key desde los argumentos o variables de entorno
        self.api_key = api_key or os.getenv("GEMINI_API_KEY")
        
        if self.api_key:
            # Configura la librería de Google Generative AI
            genai.configure(api_key=self.api_key)
            
            # Instrucciones del sistema para guiar el comportamiento de la IA
            system_instruction = """
            Eres un asistente experto en generar interfaces minimalistas y funcionales. 
            Tu objetivo es ayudar al usuario y, cuando sea necesario, generar componentes UI.
            
            REGLA DE FORMULARIOS:
            Si el usuario te pide un formulario, responde con un bloque JSON encerrado en ```json:form ... ```.
            El JSON debe seguir estrictamente esta estructura:
            {
                "title": "Título descriptivo del formulario",
                "fields": [
                    {
                        "name": "id_unico_del_campo", 
                        "label": "Etiqueta visible", 
                        "type": "text|email|number|textarea|select", 
                        "options": ["Opción 1", "Opción 2"] (solo si el tipo es select)
                    }
                ],
                "submit_label": "Texto para el botón de envío"
            }
            Acompaña siempre el componente con una breve explicación de lo que has generado.
            """
            # Inicializa el modelo generativo
            self.model = genai.GenerativeModel('gemini-3-flash-preview', system_instruction=system_instruction)
        else:
            self.model = None

    def send_message(self, message):
        """
        Envía un mensaje al modelo y devuelve la respuesta en texto.
        """
        if not self.model:
            return "Error: La variable de entorno GEMINI_API_KEY no está configurada."
        
        try:
            # Genera contenido basado en el mensaje del usuario
            response = self.model.generate_content(message)
            return response.text
        except Exception as e:
            # Captura y formatea errores de comunicación
            return f"Error al comunicarse con Gemini: {str(e)}"


