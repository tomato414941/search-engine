from collections import defaultdict


class Indexer:
    def __init__(self):
        self.index = defaultdict(list)

    def create_index(self, pages):
        print("Creating index...")
        for url, page_data in pages.items():
            words = page_data["content"].lower().split()
            for word in words:
                if url not in self.index[word]:
                    self.index[word].append(url)
        print("Index created.")
        return self.index
