from collections import defaultdict


class Indexer:
    def __init__(self):
        self.index = defaultdict(list)
        self.page_data = {}

    def create_index(self, pages):
        print("Creating index...")
        for url, page_info in pages.items():
            words = page_info["content"].lower().split()
            for word in words:
                if url not in self.index[word]:
                    self.index[word].append(url)
            self.page_data[url] = {
                "title": page_info["title"],
                "snippet": page_info["snippet"],
                "last_crawled": page_info["last_crawled"],
            }
        print("Index created.")
        return self.index, self.page_data
