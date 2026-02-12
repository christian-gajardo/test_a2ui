import { FormRenderer } from './a2ui/form_renderer.js';

/**
 * Lógica principal del Chatbot.
 * Gestiona la interfaz de usuario, la comunicación asíncrona con el servidor
 * y el renderizado de componentes A2UI.
 */
document.addEventListener('DOMContentLoaded', () => {
    const chatMessages = document.getElementById('chat-messages');
    const userInput = document.getElementById('user-input');
    const sendBtn = document.getElementById('send-btn');

    /**
     * Añade un mensaje al contenedor del chat.
     * Detecta si la respuesta incluye un componente de formulario A2UI.
     * @param {string} text - Contenido del mensaje.
     * @param {string} sender - 'user' o 'bot'.
     */
    const addMessage = (text, sender) => {
        const msgDiv = document.createElement('div');
        msgDiv.className = `message ${sender}`;

        // Expresión regular para encontrar el bloque JSON del formulario
        const formRegex = /```json:form\s*([\s\S]*?)```/;
        const match = text.match(formRegex);

        if (match && match[1]) {
            try {
                // Parsea la definición del formulario enviada por la IA
                const formData = JSON.parse(match[1]);
                const cleanText = text.replace(formRegex, '').trim();

                // Si hay texto acompañando al formulario, se añade primero
                if (cleanText) {
                    msgDiv.innerHTML = `<div class="message-content">${cleanText}</div>`;
                }

                // Renderiza el componente de formulario A2UI
                const formElement = FormRenderer.render(formData);
                msgDiv.appendChild(formElement);
            } catch (e) {
                console.error('Error al procesar el JSON del formulario:', e);
                msgDiv.innerHTML = `<div class="message-content">${text}</div>`;
            }
        } else {
            // Mensaje de texto estándar
            msgDiv.innerHTML = `<div class="message-content">${text}</div>`;
        }

        chatMessages.appendChild(msgDiv);
        // Desplazamiento automático al final del chat
        chatMessages.scrollTop = chatMessages.scrollHeight;
    };

    /**
     * Gestiona el envío de mensajes al servidor Flask.
     */
    const sendMessage = async () => {
        const text = userInput.value.trim();
        if (!text) return;

        // Muestra el mensaje del usuario inmediatamente
        addMessage(text, 'user');
        userInput.value = '';

        // Indicador visual de carga (estado "escribiendo")
        const loadingDiv = document.createElement('div');
        loadingDiv.className = 'message bot loading';
        loadingDiv.innerHTML = '<div class="message-content">Escribiendo...</div>';
        chatMessages.appendChild(loadingDiv);
        chatMessages.scrollTop = chatMessages.scrollHeight;

        try {
            // Petición POST al endpoint del controlador
            const response = await fetch('/chat', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ message: text })
            });

            const data = await response.json();
            // Elimina el indicador de carga antes de mostrar la respuesta
            chatMessages.removeChild(loadingDiv);

            if (data.response) {
                addMessage(data.response, 'bot');
            } else {
                addMessage('Error: ' + (data.error || 'Ocurrió algo inesperado'), 'bot');
            }
        } catch (error) {
            chatMessages.removeChild(loadingDiv);
            addMessage('Error de conexión con el servidor.', 'bot');
        }
    };

    // Eventos de interacción
    sendBtn.addEventListener('click', sendMessage);
    userInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') sendMessage();
    });
});
