# Search Engine Project

This project implements a basic search engine using Python with FastAPI for the backend and a simple web interface.

## Project Structure

```
search-engine/
│
├── .venv/                  # Virtual environment (not tracked by git)
├── .gitignore              # Specifies intentionally untracked files to ignore
├── README.md               # This file
├── requirements.txt        # Project dependencies
│
└── search-engine/          # Source code for the search engine
    ├── __init__.py
    ├── main.py             # Entry point for the application
    ├── api.py              # API routes
    ├── web.py              # Web UI routes
    ├── crawler.py          # Web crawler implementation
    ├── indexer.py          # Indexing functionality
    ├── searcher.py         # Search functionality
    │
    └── templates/          # HTML templates
        ├── index.html      # Search page
        └── results.html    # Search results page

```

## Setup

1. Clone the repository
2. Create a virtual environment: `python -m venv .venv`
3. Activate the virtual environment:
- On Windows: `.venv\Scripts\activate`
- On macOS and Linux: `source .venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`

## Usage

1. Ensure you're in the root directory of the project.
2. Run the FastAPI server:
```
uvicorn search-engine.main:app --reload
```
3. Open a web browser and navigate to `http://localhost:8000` to access the web interface.
4. To use the API directly:
- Crawl a website: Send a POST request to `http://localhost:8000/api/crawl?url=<website_url>&max_pages=<number>`
- Perform a search: Send a POST request to `http://localhost:8000/api/search` with a JSON body `{"query": "your search term"}`

## Features

- Web crawling with basic HTML parsing
- Simple indexing of crawled pages
- Search functionality based on the created index
- Web interface for easy searching
- API endpoints for crawling and searching
- Basic snippet generation for search results
- Display of title, URL, snippet, and last crawled date in search results


## Future Plans

- Implement respect for robots.txt files in the crawler
- Add support for different content types (e.g., PDFs)
- Enhance the indexing process with text preprocessing (stemming or lemmatization)
- Implement a more sophisticated ranking algorithm
- Add support for phrase searches and boolean operators
- Implement pagination for search results
- Develop a more advanced snippet generation algorithm
- Add data persistence to store crawled pages and index

We welcome contributions and suggestions for additional features!

## Contributing

[TODO: Add contribution guidelines]

## License

[TODO: Add license information]
