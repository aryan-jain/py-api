from typing import Optional

from pydantic import BaseModel, Field

from src import version


class HealthData(BaseModel):
    version: str = Field(default=version, description="Version of the service")
    uptime: int = Field(description="Uptime in seconds")


class APIResponse(BaseModel):
    status: int = Field(description="Status code")
    message: Optional[str] = Field(default=None, description="Message")
    data: Optional[HealthData] = Field(default=None, description="Data")
