from databases import Database
from fastapi import APIRouter, Depends

from src.dependencies import get_db
from src.quote.models import Quote
from src.models import ListResponse

router = APIRouter()


@router.get("", response_model=ListResponse[Quote])
async def list_quotes(db: Database = Depends(get_db)):
    results = await db.fetch_all(
        "SELECT id, category, source, content FROM quote ORDER BY id"
    )

    return {"results": results}
