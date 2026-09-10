from fastapi import FastAPI

app = FastAPI()

# Declaración del documento raíz
@app.get("/")
async def root():
    return {"message": "Hello World"}
