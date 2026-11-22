import os
from sqlalchemy import create_engine

def get_database_url() -> str:
    url = os.getenv("DATABASE_URL")
    if not url:
        raise RuntimeError(
            "A variável de ambiente DATABASE_URL não está configurada."
        )

    if url.startswith("postgres://"):
        url = url.replace("postgres://", "postgresql://", 1)

    return url


database_url = get_database_url()

connect_args = {}
if "localhost" not in database_url and "127.0.0.1" not in database_url:
    if "sslmode=" not in database_url:
        connect_args["sslmode"] = "require"

engine = create_engine(
    database_url,
    connect_args=connect_args,
    pool_pre_ping=True,  
)