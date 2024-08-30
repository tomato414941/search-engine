from collections import defaultdict
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup


class SearchEngine:
    def __init__(self):
        self.pages = {}
        self.index = defaultdict(list)

    def crawl(self, start_url, max_pages=10):
        print(f"Crawling {start_url}...")
        self._crawl_recursive(start_url, max_pages)
        print(f"Crawled {len(self.pages)} pages.")

    def _crawl_recursive(self, url, max_pages):
        if len(self.pages) >= max_pages or url in self.pages:
            return

        try:
            response = requests.get(url)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, "html.parser")
                self.pages[url] = {
                    "title": soup.title.string if soup.title else "",
                    "content": soup.get_text(),
                }

                print(f"Crawled {url}")

                for link in soup.find_all("a"):
                    next_url = urljoin(url, link.get("href"))
                    self._crawl_recursive(next_url, max_pages)

        except Exception as e:
            print(f"Error crawling {url}: {e}")

    def create_index(self):
        print("Creating index...")
        for url, page_data in self.pages.items():
            words = page_data["content"].lower().split()
            for word in words:
                if url not in self.index[word]:
                    self.index[word].append(url)
        print("Index created.")

    def search(self, query):
        words = query.lower().split()
        if not words:
            return []
        results = set(self.index[words[0]])
        for word in words[1:]:
            results.intersection_update(set(self.index[word]))
        return list(results)


def main():
    engine = SearchEngine()

    # Crawl a website
    start_url = "http://example.com"
    engine.crawl(start_url, max_pages=10)

    # Create an index
    engine.create_index()

    # Search loop
    while True:
        query = input("Enter your search query (or 'quit' to exit): ").strip()

        if query.lower() == "quit":
            print("Thank you for using Simple Search Engine. Goodbye!")
            break

        if not query:
            print("Please enter a valid search query.")
            continue

        print(f"\nSearching for: '{query}'")
        results = engine.search(query)

        if results:
            print("\nSearch Results:")
            for i, url in enumerate(results, 1):
                print(f"{i}. {url}")
        else:
            print("No results found.")

        print()  # Empty line for readability


if __name__ == "__main__":
    main()
