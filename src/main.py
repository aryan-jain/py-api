import time

import uvicorn
from fastapi import Depends, FastAPI
from fastapi.responses import RedirectResponse

from src import router
from src.db.auth import check_user
from src.schema import HealthData, HealthResponse

app = FastAPI(
    title="FastAPI Example",
    version="0.1.0",
    description="FastAPI example project",
)
app.include_router(router, dependencies=[Depends(check_user)])


@app.get("/", include_in_schema=False)
async def redirect_to_docs():
    return RedirectResponse(url="/docs")


@app.get("/health")
async def health() -> HealthResponse:
    return HealthResponse(
        status=200,
        data=HealthData(
            uptime=int(time.perf_counter() - start),
        ),
    )


if __name__ == "__main__":
    start = time.perf_counter()
    uvicorn.run(app, host="0.0.0.0", port=8000)
