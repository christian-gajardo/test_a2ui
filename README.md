# A2UI Vanilla Base (Camino a Odoo 19)

Este proyecto es una base minimalista que utiliza **Python (FastAPI)** y **JavaScript Vanilla** para demostrar una arquitectura alineada con los patrones modernos de **Odoo 19**.

## Inicio Rápido

1. **Instalar dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Ejecutar el Backend**:
   ```bash
   python backend/main.py
   ```

3. **Ejecutar el Frontend**:
   Simplemente abre `frontend/index.html` en tu navegador.

## Estructura del Proyecto

- `backend/models/`: Lógica de negocio y modelos de datos (imita `models.Model`).
- `backend/controllers/`: Endpoints JSON-RPC (imita controladores de Odoo).
- `frontend/static/js/component.js`: Clase base para componentes (imita **Owl Component**).
- `frontend/static/js/rpc.js`: Utilidad para llamadas al servidor (imita `web.rpc`).

## ¿Por qué esta estructura?

Esta base te permite desarrollar aplicaciones independientes pero con una "mentalidad Odoo". Cuando decidas migrar a Odoo 19:
- Tus modelos en Python se convertirán en modelos de Odoo casi directamente.
- Tus componentes de JS ya tendrán la estructura necesaria para ser convertidos a componentes Owl oficiales.
- La comunicación ya utiliza el estándar JSON-RPC que Odoo requiere.

## Requisitos
- Python 3.9+
- Un navegador moderno.
