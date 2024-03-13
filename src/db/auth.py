import hashlib

from fastapi import HTTPException, Security
from fastapi.security import APIKeyHeader
from sqlalchemy import select

from src.db import async_session
from src.db.models import ApiKeys, User

api_key_header = APIKeyHeader(name="X-API-Key")


async def check_user(api_key: str = Security(api_key_header)) -> bool:
    async with async_session() as session:
        result = await session.execute(
            select(User)
            .join(ApiKeys)
            .where(ApiKeys.key == hashlib.sha256(api_key.encode()).hexdigest())
        )

        user = result.fetchone()

        if user is None:
            raise HTTPException(status_code=400, detail="X-API-Key header invalid")
        else:
            return user.is_active
