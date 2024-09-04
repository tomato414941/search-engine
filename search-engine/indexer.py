import math
from collections import defaultdict

from .pagerank import calculate_pagerank
from .preprocessor import preprocessor


class Indexer:
    def __init__(self):
        self.index = defaultdict(dict)
        self.idf = {}
        self.page_data = {}
        self.document_count = 0
        self.pagerank_scores = {}

    def create_index(self, pages, links):
        print("Creating index...")
        self.document_count = len(pages)

        self.pagerank_scores = calculate_pagerank(links)

        for url, page_info in pages.items():
            if "content" in page_info:
                words = preprocessor.preprocess(page_info["content"])
                word_count = len(words)
                word_freq = defaultdict(int)
                for word in words:
                    word_freq[word] += 1

                for word, freq in word_freq.items():
                    self.index[word][url] = freq / word_count  # Term frequency

                self.page_data[url] = {
                    "title": page_info.get("title", ""),
                    "snippet": page_info.get("snippet", ""),
                    "last_crawled": page_info.get("last_crawled", ""),
                    "robots_info": page_info.get("robots_info", {}),
                    "pagerank": self.pagerank_scores.get(url, 0),
                }
            else:
                print(f"Skipping indexing for {url} (no content available)")

        self.calculate_idf()
        print("Index created.")
        return self.index, self.idf, self.page_data

    def calculate_idf(self):
        for word in self.index:
            self.idf[word] = math.log(self.document_count / len(self.index[word]))
