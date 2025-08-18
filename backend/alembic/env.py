from logging.config import fileConfig
from sqlalchemy import engine_from_config, create_engine
from sqlalchemy import pool
from alembic import context
import os
import sys

# Ensure src is importable
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SRC_DIR = os.path.abspath(os.path.join(BASE_DIR, "src"))
if SRC_DIR not in sys.path:
    sys.path.insert(0, SRC_DIR)

config = context.config
# Guard against None filename in some contexts
if config.config_file_name:
    fileConfig(config.config_file_name)

from db import Base  # type: ignore

target_metadata = Base.metadata

def run_migrations_offline():
    url = os.getenv("DATABASE_URL") or config.get_main_option("sqlalchemy.url")
    context.configure(url=url, target_metadata=target_metadata, literal_binds=True, compare_type=True)
    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    section = config.get_section(config.config_ini_section) or {}
    # Allow overriding URL via environment variable (e.g., when running in Docker)
    env_url = os.getenv("DATABASE_URL")
    if env_url:
        section["sqlalchemy.url"] = env_url
    connectable = engine_from_config(
        section,
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata, compare_type=True)
        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()

