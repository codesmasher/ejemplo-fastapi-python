from fastapi import FastAPI

# Configurar el depurador de Python
import debugpy
if not debugpy.is_client_connected():
    try:
        debugpy.listen(("0.0.0.0", 5678))
        print("🐍 [DEBUGGER] Escuchando en 0.0.0.0:5678 - Listo para adjuntar VS Code")
    except RuntimeError:
        # El puerto ya está en uso por el proceso padre de Uvicorn, continuamos de forma segura
        pass

app = FastAPI(title="Nombre del sistema")

# Declaración del documento raíz
@app.get("/")
async def root():
    return {"message": "Hello World"}
