from fastapi import APIRouter, Request
from typing import Any, Dict

router = APIRouter()

@router.post("/jsonrpc")
async def jsonrpc_handler(request: Request):
    """
    Manejador genérico de JSON-RPC que imita el estilo /web/dataset/call_kw de Odoo.
    """
    payload = await request.json()
    params = payload.get("params", {})
    method = payload.get("method", "call")
    
    # En Odoo, esto se dirigiría a los métodos del modelo (search, read, write, etc.)
    model = params.get("model")
    method_name = params.get("method")
    args = params.get("args", [])
    kwargs = params.get("kwargs", {})

    print(f"Ejecutando {model}.{method_name} con args: {args}, kwargs: {kwargs}")

    # Para demostración, manejamos un "ping" simple
    if model == "test.ping":
        return {
            "jsonrpc": "2.0",
            "id": payload.get("id"),
            "result": {"status": "success", "message": "Pong desde A2UI Vanilla"}
        }

    return {
        "jsonrpc": "2.0",
        "id": payload.get("id"),
        "result": {"status": "ok", "processed": True}
    }
