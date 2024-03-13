import tomllib

from fastapi import APIRouter

from src.api.v1 import router as v1_router

info = tomllib.load(open("pyproject.toml", "rb"))
version = info["tool"]["poetry"]["version"]

router = APIRouter(prefix="/api")
router.include_router(v1_router)
