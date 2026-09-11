from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # Definición de variables con sus valores por defecto
    APP_NAME: str
    APP_ENV: str
    APP_DEBUG: bool = True
    APP_PORT: int = 8000

    # Base de datos PostgreSQL
    DB_HOST: str
    DB_PORT: int = 5432
    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: str

    # JWT
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    # Genera la cadena de conexión DSN para PostgreSQL (útil para asyncpg/SQLAlchemy)
    @property
    def DATABASE_URL(self) -> str:
        return f"postgresql://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    # Configuración de lectura del archivo .env
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )

# Instancia única (Singleton) para reutilizar en toda la aplicación
settings = Settings()
