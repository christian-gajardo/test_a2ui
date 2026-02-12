from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from controllers.main_controller import router as main_router
import uvicorn

app = FastAPI(title="A2UI Vanilla Backend (Español)")

# Habilitar CORS para desarrollo del frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(main_router)

if __name__ == "__main__":
    print("Iniciando Backend A2UI Vanilla en http://localhost:8000")
    uvicorn.run(app, host="0.0.0.0", port=8000)
