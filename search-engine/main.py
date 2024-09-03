from fastapi import FastAPI
from fastapi.templating import Jinja2Templates

from . import api, web
from .crawler import Crawler
from .download_nltk_data import download_nltk_data
from .indexer import Indexer
from .searcher import Searcher


class SearchEngine:
    def __init__(self):
        self.crawler = Crawler(
            use_robots_parser=True, default_delay=1, user_agent="search-engine"
        )
        self.indexer = Indexer()
        self.searcher = None

    def crawl_and_index(self, start_url, max_pages=10):
        pages = self.crawler.crawl(start_url, max_pages)
        index, idf, page_data = self.indexer.create_index(pages)
        self.searcher = Searcher(index, idf, page_data)

    def search(self, query):
        if self.searcher is None:
            raise Exception("Search engine hasn't crawled any pages yet.")
        return self.searcher.search(query)


def create_app():
    # Ensure NLTK data is downloaded
    download_nltk_data()

    app = FastAPI(title="Search Engine")

    # Create SearchEngine instance
    search_engine = SearchEngine()

    # Setup Jinja2 templates
    templates = Jinja2Templates(directory="search-engine/templates")

    # Include API and web routes
    app.include_router(api.router)
    app.include_router(web.router)

    # Add SearchEngine and templates to app state
    app.state.search_engine = search_engine
    app.state.templates = templates

    # Crawl and index initial data
    search_engine.crawl_and_index("https://en.wikipedia.org/wiki/Main_Page", 10)

    return app


app = create_app()
