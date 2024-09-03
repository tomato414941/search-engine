from collections import defaultdict

from .preprocessor import preprocessor


class Indexer:
    def __init__(self):
        self.index = defaultdict(list)
        self.page_data = {}

    def create_index(self, pages):
        print("Creating index...")
        for url, page_info in pages.items():
            if "content" in page_info:
                words = preprocessor.preprocess(page_info["content"])
                for word in words:
                    if url not in self.index[word]:
                        self.index[word].append(url)
                self.page_data[url] = {
                    "title": page_info.get("title", ""),
                    "snippet": page_info.get("snippet", ""),
                    "last_crawled": page_info.get("last_crawled", ""),
                    "robots_info": page_info.get("robots_info", {}),
                }
            else:
                print(f"Skipping indexing for {url} (no content available)")
        print("Index created.")
        return self.index, self.page_data
