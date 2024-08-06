from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Alembic Config object
config = context.config

# Set up logging configuration
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Import your Base and metadata
from app.models import Base  # Adjust the import to your actual models module

# Set target_metadata for autogenerate support
target_metadata = Base.metadata

# Function to get database URL
def get_url():
    return (
        f"postgresql://{os.getenv('DB_USER', 'fastapi_test_james')}:"
        f"{os.getenv('DB_PASSWORD')}@"
        f"{os.getenv('EMPLOYEES_HOST', '10.120.1.3')}:"
        f"{os.getenv('EMPLOYEES_PORT', '5432')}/"
        f"{os.getenv('DB_NAME', 'example')}"
    )

# Set SQLAlchemy URL
config.set_main_option('sqlalchemy.url', get_url())

# Debug logging
print("Database connection details:")
print(f"DB_USER: {os.getenv('DB_USER', 'fastapi_test_james')}")
print(f"DB_PASSWORD: {'*' * len(os.getenv('DB_PASSWORD', ''))}")
print(f"DB_HOST: {os.getenv('EMPLOYEES_HOST', '10.120.1.3')}")
print(f"DB_PORT: {os.getenv('EMPLOYEES_PORT', '5432')}")
print(f"DB_NAME: {os.getenv('DB_NAME', 'example')}")
print(f"Full URL: {get_url()}")

def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )
    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online() -> None:
    """Run migrations in 'online' mode."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )
    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata
        )
        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()