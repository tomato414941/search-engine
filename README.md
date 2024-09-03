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
    ├── preprocessor.py     # Text preprocessing functionality
    ├── download_nltk_data.py # Script to download required NLTK data
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
5. Download required NLTK data: `python search-engine/download_nltk_data.py`


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
- Indexing of crawled pages with advanced text preprocessing
- Search functionality based on the created index
- Web interface for easy searching
- API endpoints for crawling and searching
- Basic snippet generation for search results
- Display of title, URL, snippet, and last crawled date in search results
- Text preprocessing including tokenization, stop word removal, and stemming


## Future Plans

1. Search Functionality Improvements:
   - Implement a more sophisticated ranking algorithm (e.g., TF-IDF, PageRank)
   - Add support for phrase searches and boolean operators (AND, OR, NOT)
   - Implement fuzzy matching for typo tolerance
   - Add support for wildcards in search queries
   - Implement semantic search capabilities

2. Crawler Enhancements:
   - Add support for different content types (e.g., PDFs, DOCs)
   - Implement a distributed crawling system for better scalability
   - Add support for sitemaps to improve crawling efficiency
   - Implement adaptive crawling frequencies based on page update patterns

3. User Interface and Experience:
   - Implement pagination for search results
   - Develop a more advanced snippet generation algorithm
   - Add filters for search results (e.g., by date, content type)
   - Implement an auto-suggest feature for search queries
   - Create a more visually appealing and responsive web interface

4. Data Management and Persistence:
   - Add data persistence to store crawled pages and index
   - Implement a caching system for frequently accessed pages or search results
   - Develop a system for incremental updates to the index

5. Performance Optimization:
   - Optimize the indexing process for faster updates
   - Implement query result caching
   - Optimize memory usage for large-scale indexing

6. Analytics and Monitoring:
   - Implement logging and monitoring for crawler and search performance
   - Add analytics for popular search terms and user behavior

7. Advanced Features:
   - Implement image search capabilities
   - Add support for multiple languages
   - Develop a simple recommendation system based on search history

8. API and Integration:
   - Expand the API to allow for more customized searches
   - Develop plugins for popular platforms to integrate your search engine

9. Security and Privacy:
   - Implement secure searching (HTTPS)
   - Add user authentication for personalized results
   - Develop privacy controls for indexed content

We welcome contributions and suggestions for additional features!

## Contributing

[TODO: Add contribution guidelines]

## License

[TODO: Add license information]
