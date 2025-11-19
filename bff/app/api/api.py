from app.core.http_client import HTTPXClient
from app.services.habr_adapter.api import get_article_from_habr
from app.services.habr_adapter.schemas import SArticleParseRequest
from app.services.llm_service.api import send_article_to_queue
from config import settings
from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/api", tags=["bff"])


@router.post("/articles/process")
async def process_article(body: SArticleParseRequest):
    article = await get_article_from_habr(body.url)
    if not article or not article.text:
        raise HTTPException(
            status_code=400, detail="Не удалось получить текст статьи"
        )

    task = await send_article_to_queue(article)
    return task


@router.get("/articles/result/{task_id}")
async def get_article_result(task_id: str):
    """Получить результат обработки статьи по task_id."""

    async with HTTPXClient() as client:
        resp = await client.request(
            "GET",
            f"{settings.LLM_SERVICE_BASE_URL}/api/gemini/tasks/{task_id}",
        )

        if resp.status_code == 404:
            raise HTTPException(status_code=404, detail="Результат не найден")

        resp.raise_for_status()
        return resp.json()
