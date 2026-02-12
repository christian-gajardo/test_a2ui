/**
 * A2UI Form Renderer
 * Genera formularios dinámicos en el DOM a partir de una estructura JSON.
 * Ideal para integrar componentes generados por IA en interfaces web.
 */
export class FormRenderer {
    /**
     * Crea un elemento de formulario HTML basado en los datos proporcionados.
     * @param {Object} formData - Objeto con 'title', 'fields' y 'submit_label'.
     * @returns {HTMLElement} El formulario renderizado.
     */
    static render(formData) {
        // Creación del contenedor principal del formulario
        const form = document.createElement('form');
        form.className = 'a2ui-form';

        // Añade el título si existe
        if (formData.title) {
            const title = document.createElement('h3');
            title.textContent = formData.title;
            form.appendChild(title);
        }

        // Itera sobre cada campo definido en el JSON
        formData.fields.forEach(field => {
            const fieldWrapper = document.createElement('div');
            fieldWrapper.className = 'form-field';

            // Etiqueta del campo
            const label = document.createElement('label');
            label.textContent = field.label;
            label.setAttribute('for', field.name);
            fieldWrapper.appendChild(label);

            // Generación del tipo de input correspondiente
            let input;
            if (field.type === 'textarea') {
                input = document.createElement('textarea');
            } else if (field.type === 'select') {
                input = document.createElement('select');
                if (field.options) {
                    field.options.forEach(opt => {
                        const option = document.createElement('option');
                        option.value = opt;
                        option.textContent = opt;
                        input.appendChild(option);
                    });
                }
            } else {
                input = document.createElement('input');
                input.type = field.type || 'text';
            }

            // Atributos básicos
            input.id = field.name;
            input.name = field.name;
            input.placeholder = field.label;
            fieldWrapper.appendChild(input);
            form.appendChild(fieldWrapper);
        });

        // Botón de envío personalizado
        const submitBtn = document.createElement('button');
        submitBtn.type = 'submit';
        submitBtn.className = 'form-submit';
        submitBtn.textContent = formData.submit_label || 'Enviar';
        form.appendChild(submitBtn);

        // Gestión del evento de envío
        form.onsubmit = (e) => {
            e.preventDefault();
            const data = new FormData(form);
            // Muestra los datos capturados en la consola para depuración
            console.log('Datos del formulario capturados:', Object.fromEntries(data));
            alert('Formulario enviado con éxito. Revisa la consola para ver los datos.');
        };

        return form;
    }
}
