{
    'name': 'Chatbot Gemini A2UI',
    'version': '1.0',
    'category': 'Tools',
    'summary': 'Mini-proyecto de chatbot vinculado con la API de Gemini y A2UI',
    'description': """
        Estructura base para un chatbot escalable utilizando Flask y JS.
        Sigue la arquitectura de un módulo de Odoo.
    """,
    'author': 'Antigravity',
    'depends': ['base'],
    'data': [
        'views/templates/index.html',
    ],
    'qweb': [],
    'installable': True,
    'application': True,
}
