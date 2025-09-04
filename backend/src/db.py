import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Default to Docker/K8s service name "db" instead of localhost
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql+psycopg://sovren:securepass@db:5432/sovren_ai"
)

# 🟢 Production-ready engine with connection pooling
engine = create_engine(
    DATABASE_URL,
    pool_size=10,           # max number of persistent connections
    max_overflow=20,        # extra connections allowed beyond pool_size
    pool_timeout=30,        # wait time before giving up on a connection
    pool_pre_ping=True,     # keep connections alive, auto-reconnect
    future=True
)

# 🟢 Session factory
SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
    future=True
)

# 🟢 Declarative base for ORM models
Base = declarative_base()
