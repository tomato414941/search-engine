from fastapi import APIRouter, Query, Request
from fastapi.responses import HTMLResponse

router = APIRouter()


@router.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return request.app.state.templates.TemplateResponse(
        "index.html", {"request": request}
    )


@router.get("/search", response_class=HTMLResponse)
async def search(request: Request, query: str = Query(None)):
    if not query:
        return request.app.state.templates.TemplateResponse(
            "index.html", {"request": request}
        )

    search_engine = request.app.state.search_engine
    try:
        results = search_engine.search(query)
        return request.app.state.templates.TemplateResponse(
            "results.html", {"request": request, "query": query, "results": results}
        )
    except Exception as e:
        return request.app.state.templates.TemplateResponse(
            "index.html", {"request": request, "error": str(e)}
        )
