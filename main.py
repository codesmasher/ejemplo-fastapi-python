from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

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

# 1. Montar directorio para archivos estáticos (CSS, JS, imágenes)
app.mount("/static", StaticFiles(directory="views/static"), name="static")

# 2. Configurar el motor de plantillas HTML
templates = Jinja2Templates(directory="views/templates")

# Declaración del documento raíz
@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse(
        request,
        "main.html"
    )
