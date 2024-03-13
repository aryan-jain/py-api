from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from src import config

engine = create_async_engine(
    f"postgresql+asyncpg://{config['db']['user']}:{config['db']['password']}@{config['db']['host']}:{config['db']['port']}/{config['db']['database']}"
)

async_session = async_sessionmaker(engine, expire_on_commit=False)
