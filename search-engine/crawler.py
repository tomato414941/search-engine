from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup


class Crawler:
    def __init__(self):
        self.pages = {}

    def crawl(self, start_url, max_pages=10):
        print(f"Crawling {start_url}...")
        self._crawl_recursive(start_url, max_pages)
        print(f"Crawled {len(self.pages)} pages.")
        return self.pages

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
