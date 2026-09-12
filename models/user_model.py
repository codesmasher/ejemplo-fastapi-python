from config.database import db

class UserModel:
    def __init__(self, id_user: int, username: str, email: str, password_hash: str):
        self.id_user = id_user,
        self.username = username,
        self.email = email,
        self.password_hash = password_hash
    #
    @classmethod
    async def search_for_username(cls, username: str):
        """
        Consulta asíncrona directa a la tabla 'users' en PostgreSQL usando asyncpg
        """
        sql = """
            SELECT tid AS id_user, username, email, password_hash
            FROM users
            WHERE username = $1 OR email = $1
            LIMIT 1
        """

        if db.pool is None:
            return None
        # Adquirimos una conexión del pool
        async with db.pool.acquire() as conn:
            # fetchrow ejecuta la sentencia preparada y devuelve una fila en formato Dict
            row = await conn.fetchrow(sql, username)

            if row:
                return cls(
                    id_user=row["id_user"],
                    username=row["username"],
                    email=row["email"],
                    password_hash=row["password_hash"]
                )
            return None
