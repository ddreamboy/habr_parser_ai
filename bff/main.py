from app.api import router as habr_router
from app.core.logging_config import setup_logging
from fastapi import FastAPI

setup_logging()
app = FastAPI(title="BFF")

app.include_router(habr_router)


@app.get("/health")
async def health():
    return {"status": "ok"}
