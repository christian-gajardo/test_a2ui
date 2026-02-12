from typing import Any, Dict, List

class Model:
    """
    Clase de modelo base que imita a models.Model de Odoo.
    En una aplicación real, esto se conectaría con una base de datos (SQLAlchemy, Tortoise, etc.).
    """
    _name: str = "base.model"
    _description: str = "Modelo Base"

    def __init__(self, data: Dict[str, Any] = None):
        self._data = data or {}

    @classmethod
    def search(cls, domain: List[Any] = None) -> List['Model']:
        """Imita el método search de Odoo."""
        print(f"Buscando {cls._name} con dominio: {domain}")
        return []

    def write(self, values: Dict[str, Any]) -> bool:
        """Imita el método write de Odoo."""
        self._data.update(values)
        return True

    def browse(self, ids: List[int]) -> List['Model']:
        """Imita el método browse de Odoo."""
        return [self] # Retorno simplificado de sí mismo
