from fastapi import FastAPI
from fastapi.templating import Jinja2Templates

from . import api, web
from .crawler import Crawler
from .indexer import Indexer
from .searcher import Searcher


class SearchEngine:
    def __init__(self):
        self.crawler = Crawler()
        self.indexer = Indexer()
        self.searcher = None

    def crawl_and_index(self, start_url, max_pages=10):
        pages = self.crawler.crawl(start_url, max_pages)
        index = self.indexer.create_index(pages)
        self.searcher = Searcher(index)

    def search(self, query):
        if self.searcher is None:
            raise Exception("Search engine hasn't crawled any pages yet.")
        return self.searcher.search(query)


def create_app():
    app = FastAPI(title="Search Engine")

    # Create SearchEngine instance
    search_engine = SearchEngine()
    search_engine.crawl_and_index("https://fastapi.tiangolo.com/", 10)

    # Setup Jinja2 templates
    templates = Jinja2Templates(directory="search-engine/templates")

    # Include API and web routes
    app.include_router(api.router)
    app.include_router(web.router)

    # Add SearchEngine and templates to app state
    app.state.search_engine = search_engine
    app.state.templates = templates

    return app


app = create_app()
