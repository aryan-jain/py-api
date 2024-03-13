from fastapi import APIRouter

from src.schema import ImageQuery, ImageResponse

router = APIRouter(prefix="/image")


@router.post("/query")
async def describe_image(req: ImageQuery) -> ImageResponse:
    return ImageResponse(text=req.text)
