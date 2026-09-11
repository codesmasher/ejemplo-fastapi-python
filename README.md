# ejemplo-fastapi-python
Ejemplo de aplicación hecha con FastAPI de Python 3

## Consideraciones Iniciales
Para el uso de la aplicación de este repositorio es necesario previamente haber previamente realizado la instalación de python y la siguiente lista de dependencias:

1. FastAPI V.0.110.0 o superior
2. UVicorn V.0.28.0 o superior
3. Jinja2 V.3.1.0 o superior
4. PyDantic V.2.0.0 o superior
5. DebugPy V.1.8.0 o superior

### Declaración de Variables de Entorno
Copie o renombre el archivo `.env.example` por `.env` y configure las variables de entorno según sea el caso. 

### Inicilizar la Aplicación
Utilice el siguiente comando para iniciar la operación de la aplicación: 

```
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

Considere utilizar un contenedor Docker para facilitar el mantenimiento del ambiente de desarrollo y/o productivo. Viste el repositorio [ejemplo-docker-compose](https://github.com/codesmasher/ejemplo-docker-compose) donde se encuentra un contenedor con lo necesario para el funcionamiento de esta aplicación 

## Navegar el sitio web
Abrir el navegador y escribir la dirección `localhost:8000`. Para obtener información sobre la _*API REST*_ del sitio utilize la URL `localhost:8000/docs`. 

## Documentación de FastAPI
* Consultar el sitio oficial de [FastAPI](https://fastapi.tiangolo.com/reference/fastapi) para referencia de su uso.
