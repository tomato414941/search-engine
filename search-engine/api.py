from fastapi import APIRouter, HTTPException, Request
from pydantic import BaseModel

router = APIRouter()


class SearchQuery(BaseModel):
    query: str


@router.post("/api/crawl")
async def crawl(request: Request, url: str, max_pages: int = 10):
    search_engine = request.app.state.search_engine
    search_engine.crawl_and_index(url, max_pages)
    return {"message": "Crawling and indexing completed"}


@router.post("/api/search")
async def search(request: Request, search_query: SearchQuery):
    search_engine = request.app.state.search_engine
    try:
        results = search_engine.search(search_query.query)
        return {"results": results}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
