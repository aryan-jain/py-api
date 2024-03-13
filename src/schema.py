from typing import Optional

from pydantic import BaseModel, Field

from src import version


class HealthData(BaseModel):
    version: str = Field(default=version, description="Version of the service")
    uptime: int = Field(description="Uptime in seconds")


class HealthResponse(BaseModel):
    status: int = Field(description="Status code")
    data: HealthData = Field(default=None, description="Data")


class ImageQuery(BaseModel):
    text: str = Field(description="Text describing image")


class ImageResponse(BaseModel):
    text: str = Field(description="Text describing image")
