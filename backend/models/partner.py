from models.base_model import Model
from typing import List

class Partner(Model):
    _name = "res.partner"
    _description = "Socio/Contacto"

    @classmethod
    def search_read(cls, domain=None, fields=None) -> List[dict]:
        """
        Imita el search_read de Odoo.
        """
        # Datos de ejemplo
        return [
            {"id": 1, "name": "Azure Interior", "email": "azure@example.com"},
            {"id": 2, "name": "Gemini Corp", "email": "info@gemini.com"},
        ]
