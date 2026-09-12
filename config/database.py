import asyncpg
import logging
from typing import Optional
from config.settings import settings

# Configuración básica de logs
logger = logging.getLogger("uvicorn")
print(settings.DATABASE_URL)

class Database:
    """
    Gestor del Pool de Conexiones a PostgreSQL utilizando asyncpg.
    Sigue el patrón Singleton para mantener un único pool activo en la aplicación.
    """
    pool: Optional[asyncpg.Pool] = None

    @classmethod
    async def connect(cls):
        """Inicializa el pool de conexiones al arrancar FastAPI"""
        if cls.pool is None:
            try:
                logger.info("🔌 Conectando al pool de PostgreSQL (asyncpg)...")
                cls.pool = await asyncpg.create_pool(
                    dsn=settings.DATABASE_URL,
                    min_size=5,         # Mínimo de conexiones en espera en el pool
                    max_size=20,        # Máximo de conexiones simultaneas
                    max_queries=5000,   # Límite de consultas por conexión antes de reciclarla
                    timeout=30.0
                )
                logger.info("✅ Pool de conexiones a PostgreSQL establecido exitosamente.")
            except Exception as e:
                logger.error(f"❌ Error al conectar a la base de datos PostgreSQL: {e}")
                raise e

    @classmethod
    async def disconnect(cls):
        """Cierra el pool de conexiones al apagar FastAPI"""
        if cls.pool is not None:
            logger.info("🔌 Cerrando el pool de conexiones a PostgreSQL...")
            await cls.pool.close()
            cls.pool = None
            logger.info("✅ Pool de conexiones cerrado")

    @classmethod
    async def get_connection(cls):
        """
        Generador/Context Manager para adquirir una conexión del pool
        Se usa en los modelos para ejecutar consultas SQL puras.
        """
        if cls.pool is None:
            raise RuntimeError("El pool de la base de datos no está inicializado.")

        async with cls.pool.acquire() as connection:
            yield connection

# Instancia única para usar en el ciclo de vida de la aplicación
db = Database()
