from contextlib import asynccontextmanager
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

# Importar variables de entorno del sistema
from config.settings import settings
# Importar conexión a PostgreSQL
from config.database import db
# Importacion de Controllers
from controllers import user_controller

# Lifecycle Handler para la conexión asincrona
@asynccontextmanager
async def lifespan(app: FastAPI):
    # 1. Startup: Abrimos el pool de PostgreSQL al iniciar el contenedor
    await db.connect()
    yield
    # 2. Shutdown: Cerramos el pool de forma limpia al apagar
    await db.disconnect()

# Configurar el depurador de Python
import debugpy
if not debugpy.is_client_connected():
    try:
        debugpy.listen(("0.0.0.0", 5678))
        print("🐍 [DEBUGGER] Escuchando en 0.0.0.0:5678 - Listo para adjuntar VS Code")
    except RuntimeError:
        # El puerto ya está en uso por el proceso padre de Uvicorn, continuamos de forma segura
        pass

app = FastAPI(
    title=settings.APP_NAME,
    debug=settings.APP_DEBUG,
    lifespan=lifespan
)

# 1. Montar directorio para archivos estáticos (CSS, JS, imágenes)
app.mount("/static", StaticFiles(directory="views/static"), name="static")
# 2. Agregar rutas del controlador
app.include_router(user_controller.router)
# 3. Configurar el motor de plantillas HTML
templates = Jinja2Templates(directory="views/templates")

# Declaración del documento raíz
@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse(
        request,
        "main.html"
    )

# Ruta provcional para revisar los valores de las variables de entorno
@app.get("/api/v1/envs")
def get_envs():
    return {
        "sistema": settings.APP_NAME,
        "entorno": settings.APP_ENV
    }
